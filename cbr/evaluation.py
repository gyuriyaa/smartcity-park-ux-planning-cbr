from typing import Dict


def evaluate_behavior(disposal_behavior: Dict[str, int]) -> str:
    """
    Rule-based evaluation of disposal behavior.

    Returns:
        "A"  – Appropriate
        "PA" – Partially Appropriate
        "IA" – Inappropriate
    """

    ng_flags = [
        "NG-IRBU",
        "NG-DTPR",
        "NG-LOG",
    ]
    nt_flags = [
        "NT-DNRO",
        "NT-POT",
    ]

    has_negative = any(disposal_behavior.get(k, 0) for k in ng_flags)
    has_neutral_issue = any(disposal_behavior.get(k, 0) for k in nt_flags)
    is_proper = (
        disposal_behavior.get("PO-PD", 0)
        or disposal_behavior.get("PO-RC", 0)
        or disposal_behavior.get("PO-PULPD", 0)
    )

    if has_negative:
        return "IA"
    if is_proper and not has_neutral_issue:
        return "A"
    if is_proper and has_neutral_issue:
        return "PA"
    return "PA"
