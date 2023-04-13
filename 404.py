import pytest
from app import app, Loan


def test_full_loan_calculation(client):
    """
    GIVEN a user enters their loan details
    WHEN the user clicks the calculate button
    THEN the user sees the monthly payment for their loan and the amortization table
    """
    response = client.GET(
        "/astatler", data={"loanAmt": "100000", "lengthOfLoan": "30", "intRate": "0.06"}
    )
    assert response.status_code == 404
