from cookieStore import cookie
import requests


def http_request_parameters():
    return {
        'authority': 'consent.cookiebot.com',
        'cache-control': 'no-cache',
        'referer': 'https://archive.f4wonline.com/',
        'Cookie': cookie,
    }


def download_podcast_data(podcast_url, podcast_file_path):
    print('Fetching Podcast from F4W Archive')
    result = requests.get(url=podcast_url, headers=http_request_parameters())

    print('response: ', result.status_code)

    if result.status_code == 200:
        with open(podcast_file_path, 'wb') as f:
            f.write(result.content)


def create_download_url(show_date, show_name, base_download_url=None):
    if base_download_url is None:
        base_download_url = default_download_url()

    return base_download_url + show_date + show_name + '.mp3'


def create_download_file_path(path, show_date, show_name):
    return path + show_date + show_name + '.mp3'


def convert_show_name(show_name):
    show_mappings = show_name_mappings()

    converted_show_name = show_mappings.get(show_name.upper())

    return converted_show_name


def show_name_mappings():
    return {'WRESTLING OBSERVER LIVE': 'wol'}


def default_download_url():
    return 'https://media001.f4wonline.com/dmdocuments/'
