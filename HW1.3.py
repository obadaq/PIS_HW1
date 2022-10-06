import os


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


def read_folder_files():
    data_folder = os.path.join(os.getcwd(), 'articles')
    data = []
    for root, folder, files in os.walk(data_folder):
        for file in files:
            path = os.path.join(root, file)
            with open(path) as inf:
                data.append(inf.read())

    article_hist = []
    k = 0

    for article in data:
        article_hist.append(word_histogram(data[k]))
        k += 1
    return article_hist


print(read_folder_files())
dict1 = sorted(read_folder_files()[0], key=read_folder_files()[0].get, reverse=True)
print(dict1)
keyWord = input("Enter keywords to search with spaces between them : ")
keyWords = keyWord.split(' ')
print(keyWords, type(keyWords))

bol = keyWords[0] in dict1
print(bol)
if bol:
    print(read_folder_files()[0].get(keyWords[0]))
