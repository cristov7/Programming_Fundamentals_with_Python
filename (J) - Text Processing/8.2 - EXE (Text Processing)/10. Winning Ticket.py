collection_of_tickets_list = [ticket.strip() for ticket in input().split(", ")]
jackpot_combination = ["@@@@@@@@@@@@@@@@@@@@", "####################", "$$$$$$$$$$$$$$$$$$$$", "^^^^^^^^^^^^^^^^^^^^"]
for ticket in collection_of_tickets_list:
    if ticket in jackpot_combination:
        match_symbol = ticket[0]
        print(f'ticket "{ticket}" - 10{match_symbol} Jackpot!')
    else:
        length = len(ticket)
        if length == 20:
            combination = ["@@@@@@", "######", "$$$$$$", "^^^^^^"]
            first_part = ticket[:10]
            second_part = ticket[10:]
            for symbols in combination:
                if symbols in first_part and symbols in second_part:
                    match_symbol = symbols[0]
                    uninterrupted_match_length = 0
                    if match_symbol * 9 in first_part and match_symbol * 9 in second_part:
                        uninterrupted_match_length = 9
                    elif match_symbol * 8 in first_part and match_symbol * 8 in second_part:
                        uninterrupted_match_length = 8
                    elif match_symbol * 7 in first_part and match_symbol * 7 in second_part:
                        uninterrupted_match_length = 7
                    elif match_symbol * 6 in first_part and match_symbol * 6 in second_part:
                        uninterrupted_match_length = 6
                    print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}')
                    break
                else:
                    continue
            else:
                print(f'ticket "{ticket}" - no match')
        else:
            print("invalid ticket")


# def is_winning_ticket(ticket):
#     if len(ticket) != 20:
#         return "invalid ticket"
#     winning_symbols = ['@', '#', '$', '^']
#     left_part = ticket[:10]
#     right_part = ticket[10:]
#     for match_symbol in winning_symbols:
#         for uninterrupted_match_length in range(10, 5, -1):
#             winning_symbol_repetitions = match_symbol * uninterrupted_match_length
#             if winning_symbol_repetitions in left_part and winning_symbol_repetitions in right_part:
#                 if uninterrupted_match_length == 10:  # We have Jackpot here
#                     return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
#                 return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
#     return f'ticket "{ticket}" - no match'
#
#
# tickets = [ticket.strip() for ticket in input().split(", ")]
# for ticket in tickets:
#     print(is_winning_ticket(ticket))
