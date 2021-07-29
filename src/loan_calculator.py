import pprint

# Handlers
from src.handlers.get_loan_values_handler import get_loan_values_from_user
from src.handlers.calculate_loan_handler import calculate_loan


def _print_results(loan_data):
    """
    Print the results on the console
    :param loan_data: List, event results.
    """
    print("===========")
    print("This is your loan calculation: \n")
    pprint.pprint(loan_data)
    print("\n ===========")


def main():
    """
    Execute the application.
    """
    loan_values = get_loan_values_from_user()

    loan_data = calculate_loan(
        interest=loan_values['interest'] / 100,
        principal=loan_values['amount'] - loan_values['downpayment'],
        term=int(loan_values['term'])
    )

    _print_results(loan_data)
