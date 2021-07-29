def validate_loan_values(loan_values: dict) -> (bool, dict):
    errors = []

    loan_values = _loan_float_values_validation(errors, loan_values)
    if errors:
        return errors

    _loan_amount_validation(errors, loan_values['amount'], loan_values['downpayment'])
    _loan_term_validation(errors, loan_values['term'])
    _interest_validation(errors, loan_values['interest'])
    return errors


def _loan_float_values_validation(errors: list, loan_values: dict) -> dict:
    """
    Validate that every value could be converted to a float.
    """
    for key in loan_values:
        try:
            loan_values[key] = float(loan_values[key])
        except ValueError:
            errors.append(f"The value for '{key.title()}' should be a decimal or digit.")

    return loan_values


def _loan_amount_validation(errors: list, amount: float, downpayment: float):
    """
    Validate that the loan amount is greater than downpayment.
    """
    if amount <= downpayment:
        errors.append("The Downpayment should be less than the Loan amount.")


def _loan_term_validation(errors: list, term: float):
    if term > 50:
        errors.append("The term should less or equal than 50.")


def _interest_validation(errors: list, interest: float):
    if interest >= 100:
        errors.append("The interest should less than 100%.")
