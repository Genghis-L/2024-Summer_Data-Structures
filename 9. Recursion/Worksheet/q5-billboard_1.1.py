# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu
# Solution 1.1: In-place recursion on position


def HollywoodBlockBusterGenerator(names, casting_size):
    # TODO
    generateBillboard(names, casting_size, [], 0)
    print(f"\nThe total number of casting: {sum}")


def generateBillboard(names, casting_size, result_list, position):
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

    # Include the current name and proceed
    result_list.append(names[position])
    generateBillboard(names, casting_size, result_list, position + 1)
    # Otherwise, we proceed
    result_list.pop()
    generateBillboard(names, casting_size, result_list, position + 1)


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
