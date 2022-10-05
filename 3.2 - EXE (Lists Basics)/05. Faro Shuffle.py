deck_of_cards_as_strings = input()
deck_of_cards_in_list = deck_of_cards_as_strings.split()   # .split(" ")
count_shuffles = int(input())
for shuffle in range(1, count_shuffles + 1):
    final_deck = []
    half_deck = len(deck_of_cards_in_list) // 2   # (x // 2 == int) and (x / 2 == float)
    left_part = deck_of_cards_in_list[0: half_deck]   # [0: half_deck] = [0: half_deck: 1]
    right_part = deck_of_cards_in_list[half_deck::]   # [half_deck::] = [half_deck::1]
    for card_index in range(len(left_part)):   # len(left_part) = len(right_part)
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])
    deck_of_cards_in_list = final_deck
print(deck_of_cards_in_list)
