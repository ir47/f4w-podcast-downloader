import argparse

from util import create_download_url, create_download_file_path, download_podcast_data


def main():
    print('Running Downloader')

    parser = argparse.ArgumentParser(description='F4W Podcast Downloader')

    # TODO Update interval argument to allow for days of the week
    parser.add_argument('-n', '--name', required=True, type=str, help='Show name of Podcast to be downloaded')
    parser.add_argument('-s', '--start', required=True, type=str, help='Starting podcast value')
    parser.add_argument('-e', '--end', required=False, type=str, default=None, help='End value of podcasts to download')
    parser.add_argument('-i', '--increments', required=False, type=int, default=0,
                        help='Interval range between podcast episodes')
    # TODO Make this only one of 2 values possibly prefix true or false
    parser.add_argument('-f', '--format', required=False, type=str, default='prefix',
                        help='Should the episode indicator be before or after the episode name')

    args = vars(parser.parse_args())

    if args:
        print('Displaying Output as: % s' % args)

    show_name = args.get("name")
    show_start_date = args.get("start")
    show_end_date = args.get("end")
    show_interval = args.get("interval")

    podcast_url = create_download_url(show_name, show_start_date)
    podcast_path = create_download_file_path('', show_start_date, show_name)

    download_podcast_data(podcast_url, podcast_path)


if __name__ == '__main__':
    main()
