from bs4 import BeautifulSoup as bs
import requests as rs

search=input("enter the search quarry :> ")
# List_of_pizza_varieties_by_country
re=rs.get(f"https://en.wikipedia.org/wiki/{search}")
soupp=bs(re.text,"html.parser")
res=soupp.find("div",{"id":"toc"})
link=soupp.find("ul")
for links in link:
    if links.find("li",{"class":"toclevel-1 tocsection-10"}) :
        item=links.find("li").text
        print(item)