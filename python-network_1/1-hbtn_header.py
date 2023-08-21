import requests


def main():

    url = input("Enter a URL: ")

    response = requests.get(url)

    if response.status_code == 200:
        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print("X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id not found in response headers")
    else:
        print("Error: Unable to fetch data from the URL. Status code:",
        response.status_code)


if __name__ == "__main__":
    main()
