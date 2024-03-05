#!/usr/bin/python3
"""
given URL & email as params, display response body utf-8, print error codes
usage: ./3-error_code.py http://0.0.0.0:5000/status_401
"""

if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
