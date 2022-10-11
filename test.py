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


def read_folder_files():
    # global user_ch
    title = []
    data = []

    data_folder = os.path.join(os.getcwd(), 'articles')

    for root, folder, files in os.walk(data_folder):
        for file in files:
            path = os.path.join(root, file)
            with open(path, 'r', errors='ignore') as inf:
                title.append(inf.readline())
                data.append(inf.read())
                inf.close()

    return title, data


article_hist = []
articles_keywords = []
common_dicts = []
art_num = 1
max_intersections = 3
most_relevant = {}
article_title, article_str = read_folder_files()


for article in article_str:
    article_hist.append(word_histogram(article))
    articles_keywords.append(max_elements(article_hist[art_num-1],7))
    print(art_num, article_title[art_num - 1])
    art_num += 1


user_selected_method = input('Do you want to test a text ~T~ or read from articles database ~D~ ::: ')

if user_selected_method == 'D' or user_selected_method == 'd':
    user_ch = int(input('Choose article number to read:: ')) - 1
    print(article_title[user_ch], '\n', article_str[user_ch])
    print(article_hist[user_ch])
    selected_article_keywords = articles_keywords[user_ch]
    print(selected_article_keywords)
    print(articles_keywords)hxhgds

elif user_selected_method == 'T' or user_selected_method == 't':
    user_txt = input('Enter the text here ::: ')
    selected_txt_hist = word_histogram(user_txt)
    selected_article_keywords = max_elements(selected_txt_hist, 7)

interSS=[]
for art_kw in articles_keywords:
    interSS.append(len(set(art_kw.keys()) & set(selected_article_keywords.keys())))

print('ENTERRRRRRRRRRRRRR', interSS)
mm = max(interSS)
print(max(interSS))
print(interSS.index(mm))
interSS.remove(mm)
mm = max(interSS)
print(max(interSS))
print(interSS.index(mm))
mm = max(interSS)
print(max(interSS))
print(interSS.index(mm))

'''

for art_kw in articles_keywords:
    if len(set(art_kw.keys()) & set(selected_article_keywords.keys())) >= max_intersections:
        max_intersections = len(set(art_kw.keys()) & set(selected_article_keywords.keys())) > max_intersections
        most_relevant = articles_keywords[articles_keywords.index(art_kw)]
    else:
        print('No Related')
        break

print(most_relevant)

'''
#comment