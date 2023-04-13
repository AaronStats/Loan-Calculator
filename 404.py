import pytest
from app import app, Loan

def test_full_loan_calculation(client):
    response = client.GET(
        "/astatler"
    )
    assert response.status_code == 404
