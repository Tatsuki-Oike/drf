import requests
import os

API_URL = f"http://127.0.0.1:8000/api/task/"
DIY_API_URL = f"http://127.0.0.1:8000/api/diy/"

DATA = [
    {"content": "Task 1", "status": "todo"},
    {"content": "Task 2", "status": "todo"},
    {"content": "Task 3", "status": "todo"},
    ]
PATCH_DATA = {"status": "active"}

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
    # DIY_API_URL -----------------------------------
    # for task in DATA:
    #     response = requests.post(DIY_API_URL, json=task)
    #     print(f"status code: {response.status_code}")


    ## GETリクエスト
    print("\nGETリクエスト")
    # API_URL -----------------------------------
    response = requests.get(API_URL)
    response_data = result(response)
    # DIY_API_URL -----------------------------------
    # response = requests.get(DIY_API_URL)
    # response_data = result(response)


    ## /task_id GETリクエスト
    print("\nGETリクエスト")
    TASK_URL = os.path.join(API_URL, str(response_data[0]["id"]))
    response = requests.get(TASK_URL)
    result(response)

    ## /task_id PATCHリクエスト
    print("PATCHリクエスト")
    TASK_URL = os.path.join(API_URL, str(response_data[0]["id"])) + "/"
    response = requests.patch(TASK_URL, data=PATCH_DATA)
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