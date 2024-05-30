# No idea why we need to use index


def palindrome_recursive(string, index=0):
    #TODO
    # Two base cases
    if len(string) == 1:
        return True

    if len(string) == 2:
        return string[0] == string[-1]

    return (string[0] == string[-1]) and palindrome_recursive(string[1:-1])


def main():
    s1 = "nodevillivedon"
    s2 = "livenoevil!liveonevil"
    s3 = "beliveivileb"
    r1 = palindrome_recursive(s1, 0)
    r2 = palindrome_recursive(s2, 0)
    r3 = palindrome_recursive(s3, 0)
    print("s1 is", r1)  # Should be True
    print("s2 is", r2)  # Should be True
    print("s3 is", r3)  # Should be False


main()
