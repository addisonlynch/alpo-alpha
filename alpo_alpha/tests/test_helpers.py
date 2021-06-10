import pytest

from alpo_alpha.helpers import odds_to_decimal, parse_choice_string


class TestHelpers:

    # odds_to_decimal
    def test_odds_to_decimal_fail(self):
        with pytest.raises(ValueError):
            odds_to_decimal("")

        with pytest.raises(ValueError):
            odds_to_decimal("110")

    def test_odd_to_decimal_plus(self):

        data = odds_to_decimal("+110")
        assert data == 1.1

        data = odds_to_decimal("-200")
        assert data == 0.5

    # parse_choice_string
    def test_parse_choice_string_fail(self):
        with pytest.raises(ValueError):
            parse_choice_string("")

    def test_parse_choice_string(self):

        data = parse_choice_string("Sixers -6.5 (-110)")
        assert data == "-110"
