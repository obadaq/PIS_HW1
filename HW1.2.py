import os


# Word Histogram extracting function from a specified text - returns a list od dict
def word_histogram(org_str):
    org_str = org_str.lower()
    irrelevant_word = ["\n", ".", ",", "? ", "! ",
                       "the ", "a ", " for ", "by ",
                       "and ", "to ", "in ", "with ",
                       "is ", "of ", "this ", "was ",
                       "all ", "as", "its", "that",
                       '"', "she", "on", "her", ' s', ' c', ' e']

    for irr_word in irrelevant_word:
        org_str = org_str.replace(irr_word, " ")

    word_list = org_str.split(" ")
    # print(word_list)

    word_hist = {}
    for word in word_list:
        if word not in word_hist.keys():
            word_hist[word] = 1
        else:
            word_hist[word] = word_hist[word] + 1

    word_hist.pop("")
    return word_hist


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


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num


# file handling function to handle .txt files articles and return a histogram for each article
# returns a list of dict
def read_folder_files():
    global user_ch
    global data
    data = []
    f_num = 1
    data_folder = os.path.join(os.getcwd(), 'articles')

    for root, folder, files in os.walk(data_folder):
        for file in files:
            path = os.path.join(root, file)
            with open(path) as inf:
                print(f_num, ' ', inf.readline())
                data.append(inf.read())
                inf.close()
            f_num += 1
    article_hist = []
    k = 0
    user_ch = int(input('Choose article number to read:: ')) - 1
    print(data[user_ch])

    for article in data:
        article_hist.append(word_histogram(data[k]))
        k += 1

    return article_hist


dict_list = read_folder_files()
articles_keywords = []
selected_article_keywords = max_elements(dict_list[user_ch], 5)
deselected = dict_list.remove(dict_list[user_ch])
# print(selected_article_keywords)


for art_dict in dict_list:
    articles_keywords.append(max_elements(art_dict, 5))

ak = 0

common_dicts = []
print(selected_article_keywords,"selecteddddddddddddddd")
for key in selected_article_keywords.keys():

    for dicts in articles_keywords:

        for art_key in dicts.keys():
            if key != art_key:
                continue
            else:
                common_dicts.append(articles_keywords.index(dicts))
                print(dicts, "common")
                break

print(common_dicts)
t = most_frequent(common_dicts)
print(t)
common_dicts.remove(t)
t = most_frequent(common_dicts)
print(t)
common_dicts.remove(t)
t = most_frequent(common_dicts)
print(t)
