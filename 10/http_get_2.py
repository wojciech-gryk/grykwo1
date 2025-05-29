import requests

post = {
    "userid": 1,
    "id": 100,
    "body": "Test",
    "title": "Test"
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=post)
print(response)

