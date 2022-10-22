from Functions import word_histogram, max_elements, read_folder_files


article_hist = []
articles_keywords = []
most_relevant = []
art_num = 1

article_title, article_str = read_folder_files()

for article in article_str:
    article_hist.append(word_histogram(article))
    articles_keywords.append(max_elements(article_hist[art_num-1], 7))
    print(art_num, article_title[art_num - 1])
    art_num += 1