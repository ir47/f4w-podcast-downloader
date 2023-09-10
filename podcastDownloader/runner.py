import argparse

from util import create_download_url, create_download_file_name, download_podcast_data, generate_download_directories, \
    default_download_path


def main():
    print('Running Downloader')

    parser = argparse.ArgumentParser(description='F4W Podcast Downloader')

    # TODO Update interval argument to allow for days of the week
    parser.add_argument('-n', '--name', required=True, type=str, help='Show name of Podcast to be downloaded')
    parser.add_argument('-s', '--start', required=True, type=str, help='Starting podcast value')
    parser.add_argument('-o', '--output', required=True, type=str, help='Podcast download path')
    parser.add_argument('-e', '--end', required=False, type=str, default=None, help='End value of podcasts to download')
    parser.add_argument('-i', '--increments', required=False, type=int, default=0,
                        help='Interval range between podcast episodes')
    # TODO Make this only one of 2 values possibly prefix true or false
    parser.add_argument('-f', '--format', required=False, type=str, default='prefix',
                        help='Should the episode indicator be before or after the episode name')
    parser.add_argument('-cp', '--configPath', required=False, type=str,
                        default=None,
                        help='Path to config file with podcast information')

    args = vars(parser.parse_args())

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

    if not generate_download_directories(download_path):
        download_path = default_download_path()

    podcast_url = create_download_url(show_name, show_start_date)
    podcast_file_name = create_download_file_name(download_path, show_start_date, show_name)

    download_podcast_data(podcast_url, podcast_file_name)


if __name__ == '__main__':
    main()
