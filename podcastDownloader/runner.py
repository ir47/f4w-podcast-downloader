import argparse
from datetime import datetime, timedelta

from util import create_download_url, create_download_file_name, download_podcast_data, generate_download_directories, \
    default_download_path, get_user_cookies


def main():
    print('Running Downloader')

    parser = argparse.ArgumentParser(description='F4W Podcast Downloader')

    # TODO Update interval argument to allow for days of the week
    parser.add_argument('-n', '--name', required=True, type=str, help='Show name of Podcast to be downloaded')
    parser.add_argument('-s', '--start', required=True, type=str, help='Starting podcast value')
    parser.add_argument('-o', '--output', required=False, type=str, default=None, help='Podcast download path')
    parser.add_argument('-e', '--end', required=False, type=str, default=None, help='End value of podcasts to download')
    parser.add_argument('-i', '--increments', required=False, type=int, default=0,
                        help='Interval range between podcast episodes')
    parser.add_argument('-m', '--monthlyFolder', required=False, type=bool, default=True,
                        help='Create new folder for each month')
    parser.add_argument('-y', '--yearlyFolder', required=False, type=bool, default=True,
                        help='Create new folder for each year')
    # TODO Make this only one of 2 values possibly prefix true or false
    parser.add_argument('-f', '--format', required=False, type=str, default='prefix',
                        help='Should the episode indicator be before or after the episode name')
    parser.add_argument('-cp', '--configPath', required=False, type=str,
                        default=None,
                        help='Path to config file with podcast information')

    args = vars(parser.parse_args())

    user_cookies = get_user_cookies()

    if not user_cookies:
        print('Could not get cookie data please login to F4WOnline in your browser before continuing.')
        return

    if args:
        print('Displaying Output as: % s' % args)

    if args.get('configPath'):
        # TODO get podcast info from config
        print('Feature to be implemented')
        return

    show_name = args.get("name")
    show_start_date = args.get("start")
    download_path = args.get("output")

    show_end_date = args.get("end")
    show_interval = args.get("interval")

    monthly_folder = args.get("monthlyFolder")
    yearly_folder = args.get("yearlyFolder")

    podcast_downloader(show_name, show_start_date, show_end_date, download_path, monthly_folder, yearly_folder,
                       user_cookies)


def podcast_downloader(show_name, show_start_date, show_end_date, download_path, monthly_folder, yearly_folder,
                       user_cookie, date_format='%m%d%y'):
    start_date = datetime.strptime(show_start_date, date_format)
    end_date = datetime.strptime(show_end_date, date_format)

    delta = timedelta(days=1)

    if yearly_folder:
        download_path += start_date.strftime('%Y') + '/'

    if monthly_folder:
        download_path += start_date.strftime('%B') + '/'

    print('Download Path: ', download_path)

    if download_path is None or not generate_download_directories(download_path):
        download_path = default_download_path()

    while start_date <= end_date:
        print('Podcast Date: ', start_date)

        podcast_url = create_download_url(show_name, show_start_date)
        print('Podcast URL: ', podcast_url)
        podcast_file_name = create_download_file_name(download_path, show_start_date, show_name)

        download_podcast_data(podcast_url, podcast_file_name, user_cookie)

        previous_date = start_date

        start_date += delta

        if yearly_folder and previous_date.year != start_date.year:
            new_download_path = download_path.split(previous_date.strftime('%Y'))[0]

            download_path = new_download_path + start_date.strftime('%Y') + '/'

        if monthly_folder and previous_date.month != start_date.month:
            new_download_path = download_path.split(previous_date.strftime('%B'))[0]

            download_path = new_download_path + start_date.strftime('%B') + '/'

        generate_download_directories(download_path)
        show_start_date = start_date.strftime(date_format)


if __name__ == '__main__':
    main()
