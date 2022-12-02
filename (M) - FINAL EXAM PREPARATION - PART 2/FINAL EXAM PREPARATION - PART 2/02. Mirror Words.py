import re
regex = r"(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1"
text = input()
result_list = re.findall(regex, text)
if result_list:
    words_list = [(info[1], info[3]) for info in result_list]
    valid_pairs_count = len(words_list)
    print(f"{valid_pairs_count} word pairs found!")
    mirror_words = [f"{word[0]} <=> {word[1]}" for word in words_list if word[0] == word[1][::-1]]
    if mirror_words:
        print(f"The mirror words are:\n{', '.join(mirror_words)}")
    else:
        print("No mirror words!")
else:
    print("No word pairs found!\nNo mirror words!")
