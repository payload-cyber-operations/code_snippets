#!/usr/bin/python3


import requests
import sys
from pprint import pprint


def checking_headers(target_url: str) -> None:
    response = requests.get(url=target_url)
    
    # here you can find different
    # ways to get the information
    # of the target url

    # viewing the url for the request
    # print("URL: ", response.url)

    print("STATUS CODE: ", response.status_code)
    # STATUS CODE: 200 



    # checking information in the headers
    
    headers = response.headers
    for x in headers:
        print(f"{x} => {headers[x]}")
    


def main():
    
    url = sys.argv[1]
    first_interaction(url)




if __name__ == "__main__":
    main()
