songs = {}
count_songs = int(input())
for song in range(1, count_songs + 1):
    current_song = input()
    info = current_song.split("|")
    current_piece = info[0]
    current_composer = info[1]
    current_key = info[2]
    songs[current_piece] = [current_composer, current_key]
while True:
    current_command = input()
    if current_command == "Stop":
        break
    else:
        command_list = current_command.split("|")
        command = command_list[0]
        if command == "Add":
            piece = command_list[1]
            composer = command_list[2]
            key = command_list[3]
            if piece not in songs:
                songs[piece] = [composer, key]
                print(f"{piece} by {composer} in {key} added to the collection!")
            else:
                print(f"{piece} is already in the collection!")
        elif command == "Remove":
            piece = command_list[1]
            if piece in songs:
                del songs[piece]
                print(f"Successfully removed {piece}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")
        elif command == "ChangeKey":
            piece = command_list[1]
            new_key = command_list[2]
            if piece in songs:
                songs[piece][1] = new_key
                print(f"Changed the key of {piece} to {new_key}!")
            else:
                print(f"Invalid operation! {piece} does not exist in the collection.")
# sorted_songs_list = sorted(songs.items(), key=lambda keys: keys[0])
# for piece_info, other_info in sorted_songs_list:
for piece_info, other_info in songs.items():
    composer_info = other_info[0]
    key_info = other_info[1]
    print(f"{piece_info} -> Composer: {composer_info}, Key: {key_info}")
