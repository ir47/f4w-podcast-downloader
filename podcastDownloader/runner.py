import requests
from util import getHTTPParameters

def main():
    print('Running Downloader')

    result = requests.get(url='https://media001.f4wonline.com/dmdocuments/052723wol.mp3', headers=getHTTPParameters())

    print('response: ', result.status_code)

    if result.status_code == 200:
        print('managed to get podcast!')
        with open('podcast.mp3', 'wb') as f:
            f.write(result.content)



if __name__ == "__main__":
    main()
