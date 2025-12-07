from typing import Any, Dict, List, Tuple


# Group weights for similarity combination
GROUP_WEIGHTS: Dict[str, float] = {
    "User_Info": 0.15,
    "Disposal_Behavior": 0.45,
    "Context": 0.30,
    "Solutions": 0.10,
}

# Attribute weights for disposal behavior (Problem)
DISPOSAL_BEHAVIOR_WEIGHTS: Dict[str, float] = {
    "PO-PD": 5,
    "PO-RC": 5,
    "PO-PULPD": 5,
    "NT-DNRO": 3,
    "NT-POT": 3,
    "NG-IRBU": 8,
    "NG-DTPR": 10,
    "NG-LOG": 10,
}

# Attribute weights for context
CONTEXT_WEIGHTS: Dict[str, float] = {
    "PF-LPA": 3,
    "PF-CRG": 4,
    "EF-OTB": 4,
    "EF-SWS": 3,
    "EF-DFTC": 4,
    "EF-INOB": 4,
    "EF-SPB": 2,
}


def _sim_categorical(a: str, b: str) -> float:
    """
    Simple categorical similarity: 1.0 if same, else 0.0.
    """
    return 1.0 if a == b else 0.0


def _sim_weighted_binary_vector(
    v_new: Dict[str, int],
    v_case: Dict[str, int],
    weights: Dict[str, float],
) -> float:
    """
    Weighted Jaccard-like similarity for binary/ordinal attributes.

    score = sum(w * min(a, b)) / sum(w * max(a, b, 1))
    """
    numerator = 0.0
    denominator = 0.0

    for key, w in weights.items():
        a = v_new.get(key, 0)
        b = v_case.get(key, 0)
        numerator += w * min(a, b)
        denominator += w * max(a, b, 1)

    if denominator == 0:
        return 0.0
    return numerator / denominator


def _sim_solutions(
    new_solutions: List[Dict[str, Any]],
    case_solutions: List[Dict[str, Any]],
) -> float:
    """
    Similarity of solution sets (TUX / SUX / BUX).

    Uses Jaccard similarity over (Category, Type) pairs.
    """
    if not new_solutions or not case_solutions:
        return 0.0

    def to_pairs(solutions: List[Dict[str, Any]]) -> set[tuple[str, str]]:
        return {
            (s.get("Category", ""), s.get("Type", ""))
            for s in solutions
        }

    set_new = to_pairs(new_solutions)
    set_case = to_pairs(case_solutions)

    intersection = len(set_new & set_case)
    union = len(set_new | set_case)

    if union == 0:
        return 0.0
    return intersection / union


def similarity_between_cases(
    new_case: Dict[str, Any],
    past_case: Dict[str, Any],
) -> float:
    """
    Compute overall similarity between a new case and a past case.
    """

    # 1) User info
    user_new = new_case.get("User_Basic_Information", {})
    user_past = past_case.get("User_Basic_Information", {})
    user_sim = 0.0

    if user_new and user_past:
        sim_type = _sim_categorical(
            user_new.get("User_Interaction_Type", ""),
            user_past.get("User_Interaction_Type", ""),
        )
        sim_scenario = _sim_categorical(
            user_new.get("Scenario", ""),
            user_past.get("Scenario", ""),
        )
        user_sim = 0.5 * sim_type + 0.5 * sim_scenario

    # 2) Disposal behavior
    disp_new = new_case.get("Problem", {}).get("Disposal_Behavior", {})
    disp_past = past_case.get("Problem", {}).get("Disposal_Behavior", {})
    behavior_sim = _sim_weighted_binary_vector(
        disp_new, disp_past, DISPOSAL_BEHAVIOR_WEIGHTS
    )

    # 3) Context
    ctx_new = new_case.get("Context", {})
    ctx_past = past_case.get("Context", {})
    context_sim = _sim_weighted_binary_vector(
        ctx_new, ctx_past, CONTEXT_WEIGHTS
    )

    # 4) Solutions (optional; usually 0 for new case)
    sol_new = new_case.get("Solutions", [])
    sol_past = past_case.get("Solutions", [])
    solution_sim = _sim_solutions(sol_new, sol_past)

    total_similarity = (
        GROUP_WEIGHTS["User_Info"] * user_sim
        + GROUP_WEIGHTS["Disposal_Behavior"] * behavior_sim
        + GROUP_WEIGHTS["Context"] * context_sim
        + GROUP_WEIGHTS["Solutions"] * solution_sim
    )

    return total_similarity


def find_similar_cases(
    new_case: Dict[str, Any],
    case_base: List[Dict[str, Any]],
    top_k: int = 3,
) -> List[Tuple[Dict[str, Any], float]]:
    """
    Return top_k most similar cases sorted by similarity descending.
    """
    scored: List[Tuple[Dict[str, Any], float]] = []

    for case in case_base:
        sim = similarity_between_cases(new_case, case)
        if sim > 0:
            scored.append((case, sim))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:top_k]
