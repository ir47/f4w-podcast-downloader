from cookieStore import cookie
import requests


def getHTTPParameters():
    return {
        'authority': 'consent.cookiebot.com',
        'cache-control': 'no-cache',
        'referer': 'https://archive.f4wonline.com/',
        'Cookie': cookie,
    }


def getPodcastData(podcastURL, podcastPath):
    print('Fetching Podcast from F4W Archive')
    result = requests.get(url=podcastURL, headers=getHTTPParameters())

    print('response: ', result.status_code)

    if result.status_code == 200:
        with open(podcastPath, 'wb') as f:
            f.write(result.content)


def baseURL():
    return 'https://media001.f4wonline.com/dmdocuments/'


def createPodcastURL(showDate, showName):
    return baseURL() + showDate + showName + '.mp3'


def createPodcastPath(path, showDate, showName):
    return path + showDate + showName + '.mp3'


def showNameToFileName(showName):
    return ''
