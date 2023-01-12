import requests
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {
    "userId": 909,
    "id": 909,
    "title": "Nattaphat Sangsunt",
    "completed": False
    }

response = requests.post(api_url, json=todo)
print(response.json())
print(response.status_code)