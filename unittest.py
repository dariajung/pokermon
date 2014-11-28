import poker


def test_parse_card():
    assert(poker.parse_card("King of Diamonds")) == ("King", "Diamonds")
    print "test parse card passed"


def test_literal_to_int():
    mapping = poker.translate_name_to_value()
    assert(poker.return_card_to_int_tuple("King", "Diamonds", mapping)) == (13, "Diamonds")
    assert(poker.return_card_to_int_tuple("10", "Diamonds", mapping)) == (10, "Diamonds")
    print "test literal to int passed"


def test_translate_hand():
    cards = ["Ace of Diamonds", "Queen of Diamonds", "King of Diamonds", "10 of Diamonds", "Jack of Diamonds"]
    assert(poker.translate_hand(cards)) == [(14, "Diamonds"), (13, "Diamonds"), (12, "Diamonds"),
                                            (11, "Diamonds"), (10, "Diamonds")]
    print "test translate_hand passed"


def test_check_royal_flush():
    cards = [(14, "Diamonds"), (13, "Diamonds"), (12, "Diamonds"), (11, "Diamonds"), (10, "Diamonds")]

    assert(poker.check_royal_flush(cards))
    "print test check royal flush passed"

if __name__ == "__main__":
    test_parse_card()
    test_literal_to_int()
    test_translate_hand()
    test_check_royal_flush()
    print "All tests passed"
