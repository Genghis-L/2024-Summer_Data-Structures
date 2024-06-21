# Setting word to be key is better than setting frequency to be key since the latter will cause too many collisions
# For the CHt, in this code we can not always get the first word in count_words.txt with highest frequency since the position is not fixed
# Also, for the CHt, since we use hash() in ChainHashtable.py, the seed is not always fixed for different environment, hence we will see different hash tables (dict2) appear in each run of this file

from DictionaryAsList import DictionaryAsDoubleList
from ChainHashtable import ChainHashtable


def read_file(filename):
    with open(filename, "r") as file:
        text = file.read()
    return text.split()


def most_freq_word(dict):
    maxWord = ""
    maxfreq = 0
    for word, freq in dict.items():
        if freq > maxfreq:
            maxWord = word
            maxfreq = freq
    return maxWord, maxfreq


def main():
    words = read_file("count_words.txt")

    dict1 = DictionaryAsDoubleList()
    dict2 = ChainHashtable(11)

    for word in words:
        if word in dict1:
            dict1.put(word, dict1.get(word) + 1)
        else:
            dict1.put(word, 1)

        if word in dict2:
            dict2.put(word, dict2.get(word) + 1)
        else:
            dict2.put(word, 1)

    print(dict1, "\n")
    print(dict2, "\n")

    word1, freq1 = most_freq_word(dict1)
    word2, freq2 = most_freq_word(dict2)

    print("Test of DADL: ")
    print(f"The most frequent word is: {word1} with frequency {freq1} \n")

    print("Test of CHt: ")
    print(f"The most frequent word is: {word2} with frequency {freq2} \n")


if __name__ == "__main__":
    main()
