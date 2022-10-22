from Functions import word_histogram, max_elements, read_folder_files


article_hist = []
articles_keywords = []
most_relevant = []
art_num = 1
h = 0
article_title, article_str = read_folder_files()

for article in article_str:
    article_hist.append(word_histogram(article))
    articles_keywords.append(max_elements(article_hist[art_num-1], 7))
    print(art_num, article_title[art_num - 1])
    art_num += 1

user_ch = int(input('Choose article number to read:: ')) - 1
print(article_title[user_ch], '\n', article_str[user_ch])
selected_article_keywords = articles_keywords[user_ch]

for art_kw in articles_keywords:
    if len(set(art_kw.keys()) & set(selected_article_keywords.keys())) >= 3:
        if art_kw != selected_article_keywords:
            most_relevant.append(h)
            print('\n', h+1, article_title[h])
    h += 1

if not most_relevant:
    print('\n', 'No related articles found  !!!!!!')
else:
    print('\n', 'Those articles are relevant ^^^ ::', most_relevant)
