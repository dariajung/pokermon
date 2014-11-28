import poker


def test_parse_card():
    assert(poker.parse_card("King of Diamonds")) == ("King", "Diamonds")
    print "test parse card passed"


def test_literal_to_int():
    mapping = poker.translate_name_to_value()
    assert(poker.return_card_to_int_tuple("King", "Diamonds", mapping)) == (12, "Diamonds")
    assert(poker.return_card_to_int_tuple("10", "Diamonds", mapping)) == (10, "Diamonds")
    print "test literal to int passed"


if __name__ == "__main__":
    test_parse_card()
    test_literal_to_int()
    print "All tests passed"
