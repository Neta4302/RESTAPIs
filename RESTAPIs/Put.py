import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.post(api_url)
response.json()

todo = {
    "userId": 909,
    "id": 909,
    "title": "IamGod",
    "completed": True
    }

response = requests.put(api_url, json=todo)
print(response.json())
print(response.status_code)