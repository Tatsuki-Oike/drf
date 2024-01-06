import requests
import os

API_URL = "http://127.0.0.1:8000/api/task/"
DUE_API_URL = "http://127.0.0.1:8000/api/due/"
TAX_API_URL = "http://127.0.0.1:8000/api/tax/"

DATA = [
    {"content": "Task 1", "status": "todo", "due": "2024-05-01"},
    {"content": "Task 2", "status": "todo", "due": "2024-05-01"},
    {"content": "Task 3", "status": "todo", "due": "2022-05-01"},
    ]

def result(response):
    print(f"url: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {response.json()}\n")
    return response.json()

def main():

    ## Tax
    print("\nPOSTリクエスト")
    response = requests.post(TAX_API_URL, json={"price": 100})
    result(response)

    ## POSTリクエスト
    print("\nPOSTリクエスト")
    # API_URL -----------------------------------
    for task in DATA:
        response = requests.post(API_URL, json=task)
        result(response)

    ## GETリクエスト
    print("\nGETリクエスト")
    response = requests.get(API_URL)
    response_data = result(response)

    ## GETリクエスト
    print("\nGETリクエスト")
    response = requests.get(DUE_API_URL)
    response_data = result(response)

    ## /task_id DELETEリクエスト
    print("\nDELETEリクエスト")
    if response_data:
        for task in response_data:
            TASK_URL = os.path.join(API_URL, str(task["id"]))
            response = requests.delete(TASK_URL, json=task)
            print(f"status code: {response.status_code}")

    ## GETリクエスト
    print("\nGETリクエスト")
    response = requests.get(API_URL)
    result(response)

if __name__ == '__main__':
    main()