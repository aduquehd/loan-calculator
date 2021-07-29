from mortgage import Loan


def calculate_loan(interest: float, principal: float, term: int) -> dict:
    """
    Calculate loan payments
    """
    loan = Loan(
        interest=interest,
        principal=principal,
        term=term,
    )
    return {
        'monthly payment': '${:,.2f}'.format(float(loan.monthly_payment)),
        'total interest': '${:,.2f}'.format(float(loan.total_interest)),
        'total payment': '${:,.2f}'.format(float(loan.total_paid)),
    }
