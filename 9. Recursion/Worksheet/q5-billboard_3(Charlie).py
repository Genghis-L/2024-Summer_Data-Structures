def HollywoodBlockBusterGenerator(names, casting_size):
    generateBillboard(names, casting_size, [], 0)


def generateBillboard(names, casting_size, result_list, position):

    # Base Case
    if position >= len(names):
        return
    if len(result_list) == casting_size:
        print(result_list)
        return

    # Include the current name in the combination and proceed
    result_list_new = result_list[:]
    result_list_new.append(names[position])
    generateBillboard(names, casting_size, result_list_new, position + 1)
    # Exclude the current name and proceed
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
