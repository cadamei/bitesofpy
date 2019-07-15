from collections import deque


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    string1 = deque(string)

    for i in range(0, n):
        if i < n:
            result = string1.popleft()
            string1.append(result)
        else:
            break

    return ''.join(string1)


if __name__ == '__main__':
    print(rotate("Johnathan", 3))
