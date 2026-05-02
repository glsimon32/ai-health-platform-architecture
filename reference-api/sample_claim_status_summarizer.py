"""
Sanitized reference claim status summarizer for an AI Health Platform.

This file is for portfolio demonstration only.
It does not include production source code, PHI, payer data,
EHR data, EDI files, claim adjudication logic, or clinical logic.
"""


def summarize_claim_status(claim):
    status = claim.get("claimStatus", "Unknown")
    billed = claim.get("billedAmount", 0)
    paid = claim.get("payerPaidAmount", 0)
    responsibility = claim.get("patientResponsibility", 0)

    return {
        "claimId": claim.get("claimId"),
        "status": status,
        "summary": (
            f"This synthetic claim is currently marked as {status}. "
            f"The billed amount is {billed}, payer paid amount is {paid}, "
            f"and sample patient responsibility is {responsibility}."
        ),
        "disclaimer": (
            "This is a synthetic explanation for architecture demonstration only. "
            "It is not a payer determination, billing advice, medical advice, or production claim output."
        ),
    }


if __name__ == "__main__":
    sample_claim = {
        "claimId": "sample-claim-001",
        "claimStatus": "Pending Review",
        "billedAmount": 1320.50,
        "payerPaidAmount": 640.00,
        "patientResponsibility": 220.25,
    }

    print(summarize_claim_status(sample_claim))
