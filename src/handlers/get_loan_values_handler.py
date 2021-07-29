from src.handlers.loan_validations_handler import validate_loan_values


def get_loan_values_from_user() -> dict:
    """
    Get loan values from user input.
    :return: Dict, loan values. e.g.
        {
            'amount': "100000",
            'interest': "5.5",
            'downpayment': "20000",
            'term': "30",
        }
    """
    print("... Hi, You're going to specify the information to generate the loan payment calculations. \n")
    while True:
        loan_values = {
            'amount': "",
            'interest': "",
            'downpayment': "",
            'term': "",
        }

        for key in loan_values.keys():
            loan_values[key] = input(f"{key.title()}: ")

        errors = validate_loan_values(loan_values)
        if errors:
            _show_errors(errors)
            continue
        else:
            break

    return loan_values


def _show_errors(errors):
    print("\n===========")
    print("The loan has some errors: ")
    for error in errors:
        print(f"  -> {error}")
    print("=========== \n")
    print("Please, specify correctly the loan values. \n")
