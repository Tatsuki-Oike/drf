import requests
import os

TASK_API_URL = "http://127.0.0.1:8000/api/task/"
USER_API_URL = "http://127.0.0.1:8000/api/user/"
USER_TASK_API_URL = "http://127.0.0.1:8000/api/user_task/"

USER_DATA = [
    {"username": "user", "password": "userpass"},
    {"username": "user2", "password": "userpass2"}
    ]

TASK_DATA = [
    {"content": "Task 1", "status": "todo", "due": "2024-05-01", "user": ""},
    {"content": "Task 2", "status": "todo", "due": "2024-05-01", "user": ""},
    {"content": "Task 3", "status": "todo", "due": "2024-03-01", "user": ""},
    ]

def result(response):
    print(f"url: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {response.json()}\n")
    return response.json()

def main():

    print("\nUSER POSTリクエスト")
    for user in USER_DATA:
        response = requests.post(USER_API_URL, json=user)
        print(f"status code: {response.status_code}")

    print("\nUSER GETリクエスト")
    response = requests.get(USER_API_URL)
    response_data = result(response)

    print("\nTASK POSTリクエスト")
    for task in TASK_DATA:
        task["user"] = response_data[0]["id"]
        response = requests.post(TASK_API_URL, json=task)
        print(f"status code: {response.status_code}")
    for task in TASK_DATA:
        task["user"] = response_data[1]["id"]
        response = requests.post(TASK_API_URL, json=task)
        print(f"status code: {response.status_code}")

    print("\nTASK GETリクエスト")
    response = requests.get(TASK_API_URL)
    result(response)

    print("USER_TASK GETリクエスト")
    user_task_path = os.path.join(USER_TASK_API_URL, str(response_data[0]["id"]))
    response = requests.get(user_task_path)
    result(response)

    print("USER DELETEリクエスト")
    if response_data:
        for user in response_data:
            TASK_URL = os.path.join(USER_API_URL, str(user["id"]))
            response = requests.delete(TASK_URL, json=user)
            print(f"status code: {response.status_code}")

if __name__ == '__main__':
    main()