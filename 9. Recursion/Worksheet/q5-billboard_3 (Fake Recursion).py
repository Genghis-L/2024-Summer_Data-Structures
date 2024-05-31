# Solution 3: Recursion on size
# I think this is a also fake recursion because I use the idea of looping in essence


def HollywoodBlockBusterGenerator(names, casting_size):
    result_list = []
    generateBillboard(names, casting_size, 0, result_list)
    print("All the possible casts: ")
    for cast in result_list:
        print(cast)

    print(f"\nThe total number of casting: {len(result_list)}")


def generateBillboard(names, casting_size, position, result_list):
    # Base case: if the casting size is 0, add an empty list to result_list
    if casting_size == 0:
        result_list.append([])
        return

    for i in range(position, len(names)):
        temp_list = []
        # The idea of this recursion:  names[i] + the smaller size of casting in the latter slicing
        generateBillboard(names, casting_size - 1, i + 1, temp_list)
        for combo in temp_list:
            result_list.append([names[i]] + combo)


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
