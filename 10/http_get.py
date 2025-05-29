import requests

def print_article(article):
    print("=============")
    print("Title: ", article["title"], end=" ")
    print("by user with id:", article["id"])
    print(article["body"])

if __name__ == '__main__':
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    data = response.json()
    print("Article: \n=========================")
    for article in data:
        print_article(article)

