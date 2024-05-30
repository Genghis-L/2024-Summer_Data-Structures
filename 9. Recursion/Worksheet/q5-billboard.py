# Not sure about whether we can discard curCast


def HollywoodBlockBusterGenerator(names, casting_size):
    # TODO
    result_list = []
    generateBillboard(names, casting_size, result_list, 0, [])
    print("All the possible casts: ")
    for cast in result_list:
        print(cast)

    print(len(result_list))


def generateBillboard(names, casting_size, result_list, position, curCast):
    # curCast is list; result_list is list of lists
    # TODO
    # Base Case of stopping
    if position >= len(names):
        return

    # Base Case of recording the valid result
    if len(curCast) == casting_size:
        result_list.append(curCast[:])
        curCast = []  # Clear the curCast
        return

    # The case of including the first one
    curCast.append(names[position])
    generateBillboard(names, casting_size, result_list, position + 1, curCast)

    # The case of excluding the first one
    curCast.pop()
    generateBillboard(names, casting_size, result_list, position + 1, curCast)


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
