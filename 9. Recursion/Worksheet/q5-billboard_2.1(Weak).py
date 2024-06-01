# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu
# Solution 2: Traverse the names to do in-place recursion on position
# The idea of such recursion is weaker because we use the idea of looping in essence


def HollywoodBlockBusterGenerator(names, casting_size):
    # TODO
    generateBillboard(names, casting_size, [], 0)
    global sum
    print(f"\nThe total number of casting: {sum}")


def generateBillboard(names, casting_size, result_list, position):
    # curCast is list; result_list is list of lists
    # TODO
    # If the current combination is of the desired size, add it to the results
    if len(result_list) == casting_size:
        print(result_list)
        global sum
        sum += 1
        return

    # Base Case
    if position >= len(names):
        return

    for i in range(position, len(names)):
        # Include the i-th term
        result_list.append(names[i])
        generateBillboard(names, casting_size, result_list, i + 1)
        # Exclude the i-th term and move to the next position
        result_list.pop()


sum = 0
casting = [
    "Gal Gadot",
    "Al Pacino",
    "Gong Li",
    "Hu Ge",
    "Denzel Washington",
    "Zhang Ziyi",
    "Brad Pitt",
]
HollywoodBlockBusterGenerator(casting, 2)
