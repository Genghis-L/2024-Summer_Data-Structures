# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

# Method of sorted() used for conciseness

import re

regex = re.escape(" \\/.,()[]")


def anagram(string1: str, string2: str) -> bool:
    """
    :param string1: String -- the first python string.
    :param string2: String -- the second python string.

    :return: True if string1 is anagram of string2
             False otherwise.
    """

    string1 = re.sub(f"[{regex}]", "", string1).lower()
    string2 = re.sub(f"[{regex}]", "", string2).lower()
    return sorted(string1) == sorted(string2)


"""
note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

"""


# def main():
#     string1 = "william shakespeare"
#     string2 = "i am a weakish speller"
#     print(anagram(string1, string2))

#     string1 = "software"
#     string2 = "swear oft"
#     print(anagram(string1, string2))


# if __name__ == "__main__":
#     main()
