def get_index_different_char(chars: list):
    list_len = len(chars)
    i = 0
    for char in chars:
        if str(char).isalnum():
            i += 1

    if i < list_len - i:
        for j, char in enumerate(chars):
            if str(char).isalnum():
                return j
    else:
        for j, char in enumerate(chars):
            if not str(char).isalnum():
                return j


if __name__ == '__main__':
    print(get_index_different_char(['A', 'f', '.', 'Q', 2]))
