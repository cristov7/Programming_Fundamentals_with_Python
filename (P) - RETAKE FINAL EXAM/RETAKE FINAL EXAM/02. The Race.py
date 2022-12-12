import re
regex = r"([\#|\$|\%|\*|\&]{1})([A-Za-z]{1,})\1\=([\d]{1,})\!!([\S]{1,})"
while True:
    command = input()
    current_command_list = re.findall(regex, command)
    if len(current_command_list) == 0:
        print("Nothing found!")
    else:
        current_tuple = current_command_list[0]
        name_of_racer = current_tuple[1]
        length_of_geohash_code = int(current_tuple[2])
        encrypted_geohash_code = current_tuple[3]
        if length_of_geohash_code == len(encrypted_geohash_code):
            geohash_code = ""
            for char in encrypted_geohash_code:
                ord_char = ord(char)
                new_ord_char = ord_char + length_of_geohash_code
                new_char = chr(new_ord_char)
                geohash_code += new_char
            print(f"Coordinates found! {name_of_racer} -> {geohash_code}")
            break
        else:
            print("Nothing found!")
