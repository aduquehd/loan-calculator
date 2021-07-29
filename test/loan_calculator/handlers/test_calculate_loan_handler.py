import unittest

from src.handlers.calculate_loan_handler import calculate_loan


class TestCalculateLoanHandler(unittest.TestCase):

    def test_calculate_loan_successfully(self):
        loan_data = calculate_loan(
            interest=0.055,
            principal=80000,
            term=30
        )
        expected_result = {
            'monthly payment': '$454.23',
            'total interest': '$83,523.23',
            'total payment': '$163,523.23',
        }
        assert loan_data == expected_result


if __name__ == '__main__':
    unittest.main()
