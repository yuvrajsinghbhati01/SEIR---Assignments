'''
Write a python program that takes a URL on the command line, fetches the page, and outputs (one per line)
    Page Title (without any HTML tags)
    Page Body (just the text, without any html tags)
    All the URLs that the page points/links to
'''


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import sys 

# Function to fetch the webpage from the provided url
def fetch_page(url) :
    url = url 
    browsers = {'User-Agent' : 'Mozilla/5.0'}
    soup = BeautifulSoup(urlopen(Request(url, headers= browsers)), features="lxml")
    return soup 

# Function to print the title of the webpage
def print_page_title(soup) :
    title = soup.find("title").get_text()
    if title :
        print("The title of the page is as follows : \n")
        print(f"Title : ", title)
    else : 
        print("Webpage does not contains title.")
    print()

# Function to print the body of the webpage by extracting the text from all the paragraph tags
def print_page_body(soup) :
    allParagraphs = []

    i = 0
    all_paragraph_tags = soup.find_all("p")
    for paragraph_tag in all_paragraph_tags :
        paragraph_text = str(paragraph_tag.get_text())
        allParagraphs.append(paragraph_text)
        print(f"{i}. ", paragraph_text)
        i+=1
    print("Total Paragraphs : ", len(allParagraphs))
    print()

# Function to print the page links where the Url points to 
def print_page_links(soup) :
    allLinks = {}
    i = 0
    all_anchor_tags = soup.find_all("a")
    for anchor_tag in all_anchor_tags :
        link_text = anchor_tag.get_text()
        link = anchor_tag.get('href')
        if link and link_text and link.startswith('http') :
            allLinks[link_text] = link
            print(f"{i}. {link_text} : ", link)
            print()
            i+=1
    print("Total Links : ", len(allLinks.keys()))
    print()


# Main function to perform the operations and extracting important details from Url
def get_page() :
    url = sys.argv[1]
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    print(url)
    soup = fetch_page(url)
    print_page_title(soup)
    print("The body of the webpage is as follows : \n")
    print_page_body(soup)
    print("The links to which the webpage points is as follows : \n")
    print_page_links(soup)

get_page()
