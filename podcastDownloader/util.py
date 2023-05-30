from cookieStore import cookie


def getHTTPParameters():
    return {
        'authority': 'consent.cookiebot.com',
        'cache-control': 'no-cache',
        'referer': 'https://archive.f4wonline.com/',
        'Cookie': cookie,
    }


def showNameToFileName(showName):
    return ''


