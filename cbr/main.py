from typing import Any, Dict

# Relative import handling (supports `python -m cbr.main` and `python cbr/main.py`)
try:
    from .case_loader import load_case_base
    from .similarity import find_similar_cases
    from .evaluation import evaluate_behavior
    from .solution_engine import aggregate_solutions
except ImportError:  # pragma: no cover
    from case_loader import load_case_base
    from similarity import find_similar_cases
    from evaluation import evaluate_behavior
    from solution_engine import aggregate_solutions


def _ask_choice(prompt: str, choices: Dict[str, str]) -> str:
    print(prompt)
    for code, desc in choices.items():
        print(f"  {code}: {desc}")
    while True:
        value = input("Enter code: ").strip().upper()
        if value in choices:
            return value
        print("Invalid code, try again.")


def _ask_yes_no(prompt: str) -> int:
    ans = input(f"{prompt} (y/n, default n): ").strip().lower()
    return 1 if ans.startswith("y") else 0


def _get_new_case_interactive() -> Dict[str, Any]:
    """
    Simple CLI to collect a new case.
    """

    print("=== New Case Input ===")

    user_type_choices = {
        "RU": "Recreational Users",
        "SIU": "Special Interest Users",
        "EP": "Event Participants",
        "CEU": "Cultural & Educational Users",
        "OS": "Operational Staff",
        "SS": "Support Services",
    }
    scenario_choices = {
        "ET": "Exploring Trails",
        "EP": "Enjoying Picnics",
        "EIP": "Engaging in Play",
        "PS": "Participating in Sports",
        "AE": "Attending Events",
        "ON": "Observing Nature",
        "RS": "Relaxing in Solitude",
    }

    user_info = {
        "User_Interaction_Type": _ask_choice(
            "Select User Interaction Type:", user_type_choices
        ),
        "Scenario": _ask_choice("Select Scenario:", scenario_choices),
    }

    print("\n=== Disposal Behavior (y/n) ===")
    disposal_behavior = {
        "PO-PD": _ask_yes_no("Proper Disposal (PO-PD)"),
        "PO-RC": _ask_yes_no("Recycling Correctly (PO-RC)"),
        "PO-PULPD": _ask_yes_no("Picking Up Litter for Proper Disposal (PO-PULPD)"),
        "NT-DNRO": _ask_yes_no("Neutral: Disposing Non-recyclables Only (NT-DNRO)"),
        "NT-POT": _ask_yes_no("Neutral: Packing Out Trash (NT-POT)"),
        "NG-IRBU": _ask_yes_no("Negative: Incorrect Recycling Bin Use (NG-IRBU)"),
        "NG-DTPR": _ask_yes_no(
            "Negative: Disposing Trash in Public Restrooms (NG-DTPR)"
        ),
        "NG-LOG": _ask_yes_no("Negative: Littering on the Ground (NG-LOG)"),
    }

    print("\n=== Context (y/n) ===")
    context = {
        "PF-LPA": _ask_yes_no("Lack of Public Awareness (PF-LPA)"),
        "PF-CRG": _ask_yes_no("Confusing Recycling Guidelines (PF-CRG)"),
        "EF-OTB": _ask_yes_no("Overflowing Trash Bin (EF-OTB)"),
        "EF-SWS": _ask_yes_no("Seasonal Waste Spike (EF-SWS)"),
        "EF-DFTC": _ask_yes_no("Difficulty Finding Trash Can (EF-DFTC)"),
        "EF-INOB": _ask_yes_no("Insufficient Number of Bins (EF-INOB)"),
        "EF-SPB": _ask_yes_no("Strategically Placed Bins (EF-SPB)"),
    }

    new_case: Dict[str, Any] = {
        "CaseID": "NEW",
        "User_Basic_Information": user_info,
        "Problem": {"Disposal_Behavior": disposal_behavior},
        "Context": context,
        "Solutions": [],  # new case has no solutions yet
    }

    return new_case


def main() -> None:
    print("Loading case base...")
    case_base = load_case_base()

    print(f"Loaded {len(case_base)} cases.\n")

    new_case = _get_new_case_interactive()

    print("\nEvaluating behavior...")
    evaluation = evaluate_behavior(new_case["Problem"]["Disposal_Behavior"])
    print(f"Evaluation Outcome (A/PA/IA): {evaluation}")

    print("\nFinding similar cases...")
    similar_cases = find_similar_cases(new_case, case_base, top_k=3)

    if not similar_cases:
        print("No similar cases found.")
        return

    print("\nTop similar cases:")
    for case, score in similar_cases:
        print(f"  Case {case.get('CaseID')}  similarity={score:.3f}")

    print("\nAggregating recommended solutions...")
    recommendations = aggregate_solutions(similar_cases, top_n=5)

    if not recommendations:
        print("No solutions found in similar cases.")
        return

    print("\nRecommended UX Solutions (TUX / SUX / BUX):")
    for i, sol in enumerate(recommendations, start=1):
        print(
            f"{i}. {sol['Category']} – {sol['Type']}  "
            f"(score={sol['Score']:.3f})"
        )


if __name__ == "__main__":
    main()
