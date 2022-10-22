import os


# Word Histogram extracting function from a specified text - returns a list od dict
def word_histogram(org_str):
    org_str = org_str.lower()
    irrelevant_word = ["\n", ".", ",", "? ", "! ",
                       "the ", "a ", " for ", "by ",
                       "and ", "to ", " in ", "with ",
                       "is ", "of ", "this ", "was ",
                       "all ", "as", "its", "that",
                       '"', "she", "on", "her", ' s', ' c', ' e']
    for irr_word in irrelevant_word:
        org_str = org_str.replace(irr_word, " ")

    word_list = org_str.split(" ")

    word_hist = {}
    for word in word_list:
        if word not in word_hist.keys():
            word_hist[word] = 1
        else:
            word_hist[word] = word_hist[word] + 1

    word_hist.pop("")
    return word_hist


def read_folder_files():

    title = data = []
    
    data_folder = os.path.join(os.getcwd(), 'articles')

    for root, folder, files in os.walk(data_folder):
        for file in files:
            path = os.path.join(root, file)
            with open(path, 'r', errors='ignore') as inf:
                title.append(inf.readline())
                data.append(inf.read())
                inf.close()

    return title, data


# Extracting n max elements in a dictionary - returns a dict
def max_elements(dict1, n):

    values_list = list(dict1.values())
    keys_list = list(dict1.keys())
    max_vlist = []
    max_klist = []
    for i in range(0, n):
        max1 = 0
        max2 = 0
        for j in range(len(values_list)):
            if values_list[j] > max1:
                max1 = values_list[j]
                max2 = keys_list[j]
        values_list.remove(max1)
        keys_list.remove(max2)
        max_vlist.append(max1)
        max_klist.append(max2)

    max_dict = {}
    for key in max_klist:
        for value in max_vlist:
            max_dict[key] = value
            max_vlist.remove(value)
            break

    return max_dict