# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

# We assume that there is no comment in the test.c

from queue import Empty


# Use this stack to perform token checking. No need to modify the stack class.
class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop(-1)

    def __repr__(self):
        return str(self._data)


def check_tokens(filename):
    """
    :param filename: String -- the filename string

    Use a stack!

    :return: True if all "(""[""{""}""]"")" are matching.
             False otherwise.
    """
    # TODO
    stack = ArrayStack()
    matching_bracket = {")": "(", "]": "[", "}": "{"}
    opening_brackets = matching_bracket.values()
    closing_brackets = matching_bracket.keys()

    with open(filename, "r") as file:
        content = file.read()

        # Traverse the content
        for char in content:
            # If the char is an opening bracket, push it to the stack
            if char in opening_brackets:
                stack.push(char)
            # If the char is a closing bracket, either the stack is empty or the previous one is not opening will result in False
            elif char in closing_brackets:
                # We still pop the previous element out whether the condition is satisfied or not
                if stack.is_empty() or stack.pop() != matching_bracket[char]:
                    return False

    # If at last the stack is empty, the opening and closing brackets are well-paired
    return stack.is_empty()


##############TEST CODES#################
""" Comment out the test code if you are grading on gradescope."""


def main():
    filename = "test.c"
    print(check_tokens(filename))  ### True

    # You can modify the test.c file to create your own test cases.


if __name__ == "__main__":
    main()
