from collections import Counter
from typing import Any, Dict, List, Tuple


def aggregate_solutions(
    similar_cases: List[Tuple[Dict[str, Any], float]],
    top_n: int = 5,
) -> List[Dict[str, Any]]:
    """
    Aggregate solutions from similar cases.

    Strategy:
    - Count frequency of (Category, Type) pairs weighted by similarity.
    - Sort by weighted score (frequency * similarity).
    - Return top_n unique solutions.
    """

    scores: Counter[tuple[str, str]] = Counter()

    for case, sim in similar_cases:
        for sol in case.get("Solutions", []):
            key = (sol.get("Category", ""), sol.get("Type", ""))
            scores[key] += sim

    ranked = scores.most_common(top_n)

    recommendations: List[Dict[str, Any]] = []
    for (category, sol_type), score in ranked:
        recommendations.append(
            {"Category": category, "Type": sol_type, "Score": score}
        )

    return recommendations
