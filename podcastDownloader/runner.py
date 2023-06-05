import requests
from util import getHTTPParameters, createPodcastURL, createPodcastPath
import sys


def main():
    print('Running Downloader')

    args = sys.argv

    showDate = args[1]
    showName = args[2]

    podcastURL = createPodcastURL(showDate, showName)
    podcastPath = createPodcastPath('', showDate, showName)

    result = requests.get(url=podcastURL, headers=getHTTPParameters())

    print('response: ', result.status_code)

    if result.status_code == 200:
        print('managed to get podcast!')
        with open(podcastPath, 'wb') as f:
            f.write(result.content)


if __name__ == "__main__":
    main()
