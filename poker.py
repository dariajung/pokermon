
# possible hands

# Royal Flush: A K Q J 10 all of the same suit
# Straight Flush: any five card sequence in the same suit
# Four of a kind: any four cards of the same rank
# Full house: Three of a kind combined with a pair
# Flush: Any five cards of same suit
# Straight: Five cards in sequence but different suits
# Three of a kind: three card of same rank
# Two pair: two separate pairs
# Pair: pair of same rank
# High Card: highest ranking single card


# cards = [Ace of Diamonds, Queen of Diamonds, King of Diamonds, 10 of Diamonds, Jack of Diamonds]
# result = your_method(cards)
# assert result == RoyalFlush

def translate_hand(hand):
    mapping = translate_name_to_value()
    parsed_hand = map(parse_card, hand)
    valued_hand = map(lambda (v, s): return_card_to_int_tuple(v, s, mapping), parsed_hand)
    return sorted(valued_hand, reverse=True)


def return_card_to_int_tuple(value, suit, mapping):
    if value in mapping:
        value = mapping[value]
    else:
        value = int(value)

    return (value, suit)


def check_royal_flush(hand):
    royal_flush = False
    first_suit = hand[0][1]
    same_suit = reduce((lambda acc, (val, suit): acc and (first_suit == suit)), hand, True)
    if same_suit:
        # since ordered in descending order
        f = map(lambda (val, suit): val, hand)
        if f == [14, 13, 12, 11, 10]:
            royal_flush = True
    else:
        royal_flush = False

    return royal_flush


# ie: King --> 13
# anything lower than A K Q J can be translated to an Int value
# using int(str)
def translate_name_to_value():
    mapping = {
        "Ace": 14,
        "King": 13,
        "Queen": 12,
        "Jack": 11
    }

    return mapping


def rank_hand(hand):
    pass


def parse_card(string_description_of_card):
    split = string_description_of_card.split()
    return (split[0], split[2])
