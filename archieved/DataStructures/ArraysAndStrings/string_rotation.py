
def is_substring(s1, s2):
    return s2 in s1

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    return is_substring(s1+s1, s2)

if __name__ == "__main__":
    print(is_rotation('riken', 'kenri'))
    print(is_rotation('waterbottle', 'erbottlewat'))
    print(is_rotation('test', 'estte'))
