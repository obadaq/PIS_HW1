from  Functions import word_histogram, max_elements,  read_folder_files


article_hist = []
articles_keywords = []
common_dicts = []
art_num = 1
most_relevant = []
article_title, article_str = read_folder_files()

for article in article_str:
    article_hist.append(word_histogram(article))
    articles_keywords.append(max_elements(article_hist[art_num-1],7))
    print(art_num, article_title[art_num - 1])
    art_num += 1

user_ch = int(input('Choose article number to read:: ')) - 1
print(article_title[user_ch], '\n', article_str[user_ch])
selected_article_keywords = articles_keywords[user_ch]

intersections=[]
h = 0
print('\n','The following articles are relevant')
for art_kw in articles_keywords:

    if len(set(art_kw.keys()) & set(selected_article_keywords.keys())) >= 3 :
        most_relevant.append(h)
        if h != user_ch + 1 :
            print(h,article_title[h])
    h += 1

