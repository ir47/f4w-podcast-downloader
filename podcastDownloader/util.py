from cookieStore import cookie
import requests
from pathlib import Path


def http_request_parameters():
    return {
        'authority': 'media001.f4wonline.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'cache-control': 'no-cache',
        'referer': 'https://archive.f4wonline.com/',
    }


def download_podcast_data(podcast_url, podcast_file_path):
    print('Fetching Podcast from F4W Archive')
    result = requests.get(url=podcast_url, headers=http_request_parameters(), cookies=cookie)

    print('response: ', result.status_code)

    if result.status_code == 200:
        with open(podcast_file_path, 'wb') as f:
            f.write(result.content)


def generate_download_directories(path):
    try:
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        return True

    except OSError:
        print("Could not create directory structor. Defaulting to Downloads folder")
        return False


def default_download_path():
    return str(Path.home() / "Downloads")


def create_download_url(show_name, episode_indicator, prefix_indicator=True, file_format='.mp3',
                        base_download_url=None):
    if base_download_url is None:
        base_download_url = default_download_url()

    if prefix_indicator:
        file_name = episode_indicator + show_name + file_format
    else:
        file_name = show_name + episode_indicator + file_format

    return base_download_url + file_name


def create_download_file_name(path, show_date, show_name):
    return path + show_date + show_name + '.mp3'


def default_download_url():
    return 'https://media001.f4wonline.com/dmdocuments/'
