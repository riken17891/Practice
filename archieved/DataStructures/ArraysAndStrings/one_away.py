
def one_away(s1, s2):

    op = replace
    max_index = len(s1)

    if len(s1) > len(s2):
        op = remove
        max_index = len(s2)
    elif len(s2) > len(s1):
        op = add

    i = 0
    edited = False

    while i < max_index:
        if s1[i] != s2[i]:

            if edited:
                return False

            s1 = op(s1, i, s2[i] if op == replace else s1[i])
            edited = True

        i += 1

    return True

def replace(s, i, c):
    return s[:i] + c + s[i+1:]

def add(s, i, c):
    return s[:i] + c + s[i:]

def remove(s, i, c):
    return s[:i] + s[i+1:]

if __name__ == "__main__":
    print(one_away("pale", "ple"))
    print(one_away("pales", "pale"))
    print(one_away("pale", "bale"))
    print(one_away("pale", "bake"))
    
