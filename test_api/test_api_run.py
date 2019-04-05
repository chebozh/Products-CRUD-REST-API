import json
import os

import requests

url = 'https://products-rest-api.herokuapp.com'


def get_access_token():
    """Method to authorize in order to delete items.
   Authorization need ony for DELETE /item/<name> and /store/<name> endpoints
    """
    auth_data = {
        'username': os.environ.get('products_rest_api_user'),
        'password': os.environ.get('products_rest_api_password')
    }
    r = requests.post(f'{url}/auth', json=auth_data)
    token = r.json().get('access_token')
    return token


def read_file(filename):
    with open(filename, 'r') as data_file:
        json_data = data_file.read()

    data = json.loads(json_data)
    return data


def add_test_data(filename):
    """Method to add some sample data to the database trough the API.
    """

    def post_item(name, data):
        add_item_endpoint = f'{url}/item/{name}'
        r = requests.post(add_item_endpoint, data=data)
        print(r.text)

    data = read_file(filename)
    for item in data:
        name = item.pop('name')
        post_item(name, item)


def delete_test_data(filename, token):
    """Method to delete specified items from the database trough the API.
    Rquires authorization.
    """

    def delete_item(name):
        del_item_endpoint = f'{url}/item/{name}'
        r = requests.delete(del_item_endpoint, headers={'Authorization': f'JWT {token}'})
        print(r.text)

    data = read_file(filename)
    for item in data:
        delete_item(item.get('name'))


if __name__ == '__main__':
    # access_token = get_access_token()

    add_test_data('deichman_nike_air.json')
    # delete_test_data('deichman_nike_air.json', access_token)

    add_test_data('adidas.json')
    # delete_test_data('adidas.json', access_token)
