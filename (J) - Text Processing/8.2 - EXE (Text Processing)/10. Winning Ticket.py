collection_of_tickets = [info_ticket.strip() for info_ticket in input().split(", ")]
valid_chars = ['@', '#', '$', '^']
match = False
next_ticket = False
for ticket in collection_of_tickets:
    length_of_chars = len(ticket)
    if length_of_chars == 20:
        first_part_chars_of_ticket = ticket[:10]
        second_part_chars_of_ticket = ticket[10:]
        for char in valid_chars:
            if next_ticket:
                break
            else:
                jackpot = 20 * char
                if jackpot == ticket:
                    uninterrupted_match_length = 10
                    match_symbol = char
                    print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!')
                    match = True
                    next_ticket = True
                    break
                else:
                    for count_valid_chars in range(9, 5, -1):
                        combination = char * count_valid_chars
                        if (combination in first_part_chars_of_ticket) and (combination in second_part_chars_of_ticket):
                            uninterrupted_match_length = count_valid_chars
                            match_symbol = char
                            print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}')
                            match = True
                            next_ticket = True
                            break
                        else:
                            continue
        if not match:
            print(f'ticket "{ticket}" - no match')
            next_ticket = False
        else:
            match = False
            next_ticket = False
    else:
        print("invalid ticket")


# collection_of_tickets_list = [ticket.strip() for ticket in input().split(", ")]
# jackpot_combination = ["@@@@@@@@@@@@@@@@@@@@", "####################", "$$$$$$$$$$$$$$$$$$$$", "^^^^^^^^^^^^^^^^^^^^"]
# for ticket in collection_of_tickets_list:
#     if ticket in jackpot_combination:
#         match_symbol = ticket[0]
#         print(f'ticket "{ticket}" - 10{match_symbol} Jackpot!')
#     else:
#         length = len(ticket)
#         if length == 20:
#             combination = ["@@@@@@", "######", "$$$$$$", "^^^^^^"]
#             first_part = ticket[:10]
#             second_part = ticket[10:]
#             for symbols in combination:
#                 if symbols in first_part and symbols in second_part:
#                     match_symbol = symbols[0]
#                     uninterrupted_match_length = 0
#                     if match_symbol * 9 in first_part and match_symbol * 9 in second_part:
#                         uninterrupted_match_length = 9
#                     elif match_symbol * 8 in first_part and match_symbol * 8 in second_part:
#                         uninterrupted_match_length = 8
#                     elif match_symbol * 7 in first_part and match_symbol * 7 in second_part:
#                         uninterrupted_match_length = 7
#                     elif match_symbol * 6 in first_part and match_symbol * 6 in second_part:
#                         uninterrupted_match_length = 6
#                     print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}')
#                     break
#                 else:
#                     continue
#             else:
#                 print(f'ticket "{ticket}" - no match')
#         else:
#             print("invalid ticket")


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
