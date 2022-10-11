def get_characters_string(start, end):
    """
    This function receives two characters and prints all ASCII characters between them
    :param start: a single character from the ASCII table
    :param end: a single character from the ASCII table that appears after the starting character
    :return: a list of ASCII characters
    """
    characters_list = []
    for character in range(ord(start) + 1, ord(end)):
        characters_list.append(chr(character))
    return characters_list


first_character = input()
second_character = input()
print(*get_characters_string(first_character, second_character))