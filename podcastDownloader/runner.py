import requests
from util import getHTTPParameters, createPodcastURL, createPodcastPath, getPodcastData
import sys


def main():
    print('Running Downloader')

    args = sys.argv

    showDate = args[1]
    showName = args[2]

    podcastURL = createPodcastURL(showDate, showName)
    podcastPath = createPodcastPath('', showDate, showName)

    getPodcastData(podcastURL, podcastPath)



if __name__ == "__main__":
    main()
