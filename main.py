from bs4 import BeautifulSoup as bs
import requests
import html5lib

#this is the url of website we are about to scrap
url = "https://newsummit.edu.np/"

#request is used to load the url html in our program
r = requests.get(url)
html_content = r.content


#to parse the html
soup = bs(html_content, "html.parser")
##this will print content of webpage in organized manner
#

# #to print the title of webpage
# print(soup.title.string)

# #lets see what kinda object is soup
# print(type(soup))

#to get the first element
#this will print the class of first division
element = soup.find("div")["class"]
# print(element)

#to find any specific tag
paragraph = soup.find_all("p")
# print(paragraph)

#to find tag with specific name
spc_element = soup.findAll("p", class_ = "float-right")
# print(spc_element)


#we can get the text of any tag/element in this way👇
#this code will print text of first p tag in html
text = soup.find("p").get_text()
# print(text)


#to get the link of anchor tag
anchor = soup.find_all("a")
#above code will get all anchor tag.
#we need to get link of all tags seperately by iterating through for loop

for link in anchor:
    linkof_anchor = link.get("href")
    #above code will give link of all anchor tag serially
    # print(linkof_anchor)


#difference between .content and .children
#in .content a tag's children are available as a list
#in .children a tag's children are available as generator

#.children are faster   and .content takes more memory space and are a bit slower



data = soup.find("div", class_ = "top-header")
for items in data.stripped_strings:
    # print(items)
    pass

#in this way you can get all the strings of specific tag.
#in above code we get all the strings of children tag of division which has class top-header.


#if we want to get the parent element / tag of any element then we use .parent
data1 = soup.find("a")
# print(data1.parent)

for items in data1.parents:
    print(items.name)
#this will print all the parents tag of a / anchor tag

#there is a difference in .parent  and .parents ||  .parent will give the first parent of the tag whereas .parents will give all the parent tags of a




