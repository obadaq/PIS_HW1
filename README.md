***************************************************************
HW1 Repostory on Github :>> https://github.com/obadaq/PIS_HW1 *
***************************************************************

the project consist of 2 .py files

- functions : contains user defined functions listed below
- main : main project file to run the homework in

******************************************************************************************************************************
when running the main file :																    
																				    
the program prints a list of articles titles ( provided in the database 'articles' folder inside the project folder        
then promote the user to enter article number to read 											   
																				  
after printing the whole article the program prints all the articles titles that have more than 2 common keywords           
******************************************************************************************************************************

Functions :

- first function word_histogram(**)
takes a string returns a dectionary with keys : words in the txt , values : frequency of the word

- second function read_folder_files()
takes nothing return title and data of all articles in 'article folder' inside the project folder

- third function def max_elements(**,*):
takes a dictionary of word histograms and number N returns maximum N elements in the dectionary 'most frequent N words'

******************************************************************************************************************************
******************************************************************************************************************************
sequence of the program 

-START
-first thing read the database of articles
-for every article in database create a word histogram
-for every histogram extract 7 keywords "most frequent words"
-print titles and promote the user to select a certain article to read
-for the user selected article extract keywords
-for every article keywords find the length of intersection 
-if the intersection is more than or equal 3 then the article is relevant
-print all relevant articles titles
-END
******************************************************************************************************************************
******************************************************************************************************************************
Note: when testing the program note that not all articles have other relevent articles# PIS_HW1
[HW01.pdf](https://github.com/obadaq/PIS_HW1/files/10472920/HW01.pdf)
