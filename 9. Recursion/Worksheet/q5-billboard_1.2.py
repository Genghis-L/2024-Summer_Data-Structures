# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu
# Solution 1.2: adding a dynamic curCast to put all casts into result_list as a list of lists


def HollywoodBlockBusterGenerator(names, casting_size):
    # TODO
    result_list = []
    generateBillboard(names, casting_size, result_list, 0, [])
    print("All the possible casts: ")
    for cast in result_list:
        print(cast)

    print(f"\nThe total number of casting: {len(result_list)}")


def generateBillboard(names, casting_size, result_list, position, curCast):
    # curCast is list; result_list is list of lists
    # TODO
    # If the current combination is of the desired size, add it to the results
    if len(curCast) == casting_size:
        result_list.append(curCast[:])
        return

    # Base Case
    if position >= len(names):
        return

    # Include the current name and proceed
    curCast.append(names[position])
    generateBillboard(names, casting_size, result_list, position + 1, curCast)
    # Exclude the current name and proceed
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
