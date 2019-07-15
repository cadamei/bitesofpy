from collections import deque


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    string1 = deque(string)
    if n < 0:
        for i in range(n, 0):
            result = string1.pop()
            string1.appendleft(result)
    else:
        for i in range(0, n):
            result = string1.popleft()
            string1.append(result)

    return ''.join(string1)


if __name__ == '__main__':
    print(rotate("Johnathan", 3))
