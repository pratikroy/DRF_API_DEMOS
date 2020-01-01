import requests

def client():
    # credentials = {"username": "pratik", "password": "password@789"}
    # login_url = "http://127.0.0.1:8000/api/rest-auth/login/"
    #
    # login_response = requests.post(login_url, data=credentials)

    token = "Token 1d472de9bbce3177b3302d4f8833e1a0b346a8cb"
    token_header = {"Authorization": token}
    res = requests.get("http://127.0.0.1:8000/api/profiles/",
                        headers=token_header)

    print("Status code: ", res.status_code)
    response_data = res.json()
    print(response_data)


if __name__ == "__main__":
    client()
