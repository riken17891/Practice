
def compress(s):
    result = ""
    i = 1

    current_count = 1
    last_char = s[0]

    original = True

    while i < len(s):
        c = s[i]
        if s[i] == last_char:
            current_count += 1
            original = False
        else:
            result = result + last_char + str(current_count)
            current_count = 1

        last_char = c
        i += 1

    result = result + last_char + str(current_count)

    if original:
        return s

    return result

if __name__ == "__main__":
    print(compress("aabccccaaa"))
    print(compress("avvvpppddddsdeeeeedddd"))
