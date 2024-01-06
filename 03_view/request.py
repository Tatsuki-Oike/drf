import requests
import os

API_URL = "http://127.0.0.1:8000/api/task/"
GENERIC_API_URL = "http://127.0.0.1:8000/api/generic/"
DIY_API_URL = "http://127.0.0.1:8000/api/diy/"
FILTER_API_URL = "http://127.0.0.1:8000/api/filter/"
DUE_API_URL = "http://127.0.0.1:8000/api/due/"

DATA = [
    {"content": "Task 1", "status": "todo", "due": "2024-05-01"},
    {"content": "Task 2", "status": "todo", "due": "2024-05-01"},
    {"content": "Task 3", "status": "todo", "due": "2024-03-01"},
    ]
FILTER = {
    "content": "Task 2"
}
FILTER_DATE = {
    "due__gte": "2024-04-01"
}

def result(response):
    print(f"url: {response.url}")
    print(f"status code: {response.status_code}")
    print(f"content: {response.json()}\n")
    return response.json()

def main():

    ## POSTリクエスト
    print("\nPOSTリクエスト")
    # API_URL -----------------------------------
    for task in DATA:
        response = requests.post(API_URL, json=task)
        print(f"status code: {response.status_code}")


    ## GETリクエスト
    print("\nGETリクエスト")
    response = requests.get(API_URL)
    response_data = result(response)

    ## GETリクエスト
    print("GETリクエスト")
    response = requests.get(GENERIC_API_URL)
    result(response)

    ## GETリクエスト
    print("GETリクエスト")
    response = requests.get(DIY_API_URL)
    result(response)


    ## GETリクエスト
    print("\nGETリクエスト")
    response = requests.get(FILTER_API_URL, params=FILTER)
    result(response)

    ## GETリクエスト
    print("GETリクエスト")
    response = requests.get(DUE_API_URL, params=FILTER_DATE)
    result(response)


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