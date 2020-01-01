import requests

def client():
    data = {
        "username": "user02",
        "email": "user02@gmail.com",
        "password1": "password@789",
        "password2": "password@789"
    }

    register_url = "http://127.0.0.1:8000/api/rest-auth/registration/"

    response = requests.post(register_url, data=data)

    print("Status code: ", response.status_code)
    json_data = response.json()
    print(json_data)

if __name__ == "__main__":
    client()
