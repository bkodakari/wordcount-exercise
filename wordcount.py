# open file
# create empty dict
# iterate through lines?
# split lines on spaces to get words?
# loop through words
# add words to dict
# if else to count words
# loop through dict
    # print key value


def word_count(filename):
    with open(filename) as text_file:
        word_dict = {}
        text = text_file.read()
        word_list = text.split()
        # the below commented section works, but the .get() method is cleaner
        # word_list = []
        # for line in text_file:
        #     line.rstrip()
        #     word_list.extend(line.split(" "))
        # for word in word_list:
        #     if word in word_dict:
        #         word_dict[word] += 1
        #     else:
        #         word_dict[word] = 1
        for word in word_list:
            word_dict[word] = word_dict.get(word, 0) + 1

        return word_dict


def print_word_count(word_dict):
    for word, count in word_dict.items():
        print word, count


print_word_count(word_count("test.txt"))
