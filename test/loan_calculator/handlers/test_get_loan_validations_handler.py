import unittest

from src.handlers.loan_validations_handler import validate_loan_values


class TestLoanValidationsHandler(unittest.TestCase):

    def test_correct_loan_values(self):
        loan_values = {
            'amount': "100000",
            'interest': "5.5",
            'downpayment': "20000",
            'term': "30",
        }

        errors = validate_loan_values(loan_values)
        assert errors == []

    def test_correct_loan_amount_validation(self):
        loan_values = {
            'amount': "10000",
            'interest': "5.5",
            'downpayment': "200000",
            'term': "30",
        }

        errors = validate_loan_values(loan_values)
        assert errors == ["The Downpayment should be less than the Loan amount."]

    def test_correct_float_values_validation(self):
        loan_values = {
            'amount': "SOMESTRING",
            'interest': "5.5",
            'downpayment': "200000",
            'term': "30",
        }

        errors = validate_loan_values(loan_values)
        assert errors == ["The value for 'Amount' should be a decimal or digit."]

    def test_correct_interest_validation(self):
        loan_values = {
            'amount': "100000",
            'interest': "150",
            'downpayment': "20000",
            'term': "30",
        }
        errors = validate_loan_values(loan_values)
        assert errors == ["The interest should less than 100%."]


if __name__ == '__main__':
    unittest.main()
