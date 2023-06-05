from cookieStore import cookie
import requests


def getHTTPParameters():
    return {
        'authority': 'consent.cookiebot.com',
        'cache-control': 'no-cache',
        'referer': 'https://archive.f4wonline.com/',
        'Cookie': cookie,
    }


def getPodcastData(url, headers):
    print('Fetching Podcast from F4W Archive')
    result = requests.get(url=url, headers=headers)

    if result.status_code == 200:
        print('managed to get podcast!')

    return requests


def baseURL():
    return 'https://media001.f4wonline.com/dmdocuments/'


def createPodcastURL(showDate, showName):
    return baseURL() + showDate + showName + '.mp3'


def createPodcastPath(path, showDate, showName):
    return path + showDate + showName + '.mp3'


def showNameToFileName(showName):
    return ''
