# Solution 1: Best work fitting the original idea
# Charlie's work


def HollywoodBlockBusterGenerator(names, casting_size):
    generateBillboard(names, casting_size, [], 0)


def generateBillboard(names, casting_size, result_list, position):
    # TODO
    # Base Case
    if position >= len(names):
        return

    # If the current combination is of the desired size, add it to the results
    if len(result_list) == casting_size:
        print(result_list)
        return

    # Include the current name and proceed
    result_list_include = result_list[:]
    result_list_include.append(names[position])
    generateBillboard(names, casting_size, result_list_include, position + 1)
    # Otherwise, we proceed
    generateBillboard(names, casting_size, result_list, position + 1)


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
