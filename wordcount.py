# f = open("test.txt")

# for line in f:
#     print line

def words_in_file(file):
    our_file = open(file)
    words_list = []
    full_list = []

    for word in our_file:
        words_list = word.split(" ")
        full_list += words_list
    print full_list

    count = 0
    word_dict = {}

    for word in full_list:
        if word in full_list:
            count += 1
        else:
            count += 1
            word_dict[word] = word

    print word_dict
    return word_dict

words_in_file("test.txt")
#  words_in_file()