import requests
import configuration
import data
import token


def post_new_user():
    return requests.post(configuration.URL + configuration.CREATE_USER_PATH,
                         json=data.user_body,
                         headers=data.headers
                         ).json()["authToken"]


token = post_new_user()


def post_new_client_kit(body):
    auth_token = data.header_auth.copy()
    auth_token["Authorization"] = token
    return requests.post(configuration.URL + configuration.CREATE_KITS_PATH, headers=auth_token,
                         json=body)


response = post_new_client_kit(data.kit_body).json()
print(response)


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body
print(get_kit_body(123))


