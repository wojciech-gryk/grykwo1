import sys
import requests

def print_article(article):
    print("=============")
    print("Title: ", article["title"], end=" ")
    print("by user with id:", article["id"])
    print(article["body"])

if __name__ == '__main__':
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    # if response.status_code != 200:   #sprawdzenie czy strona działa dobrze
    #     print("ERROR", response.status_code)
    #     sys.exit(1) # koniec działania programu

    response.raise_for_status()   # inaczej niż u góry - zwróci wyjątek

    data = response.json()
    print("Article: \n=========================")
    for article in data:
        print_article(article)

    