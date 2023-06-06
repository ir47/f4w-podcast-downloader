import requests
from util import create_download_url, create_download_file_path, download_podcast_data
import sys


def main():
    print('Running Downloader')

    args = sys.argv

    show_date = args[1]
    show_name = args[2]

    podcast_url = create_download_url(show_date, show_name)
    podcast_path = create_download_file_path('', show_date, show_name)

    download_podcast_data(podcast_url, podcast_path)


if __name__ == "__main__":
    main()
