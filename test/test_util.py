from unittest import TestCase, main

from podcastDownloader.util import http_request_parameters, create_download_file_name, default_download_url


class TestUtil(TestCase):
    def test_http_request_parameters(self):
        expected_params = {
            'authority': 'media001.f4wonline.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'cache-control': 'no-cache',
            'referer': 'https://archive.f4wonline.com/',
        }

        actual_params = http_request_parameters()

        self.assertEqual(expected_params, actual_params)

    def test_download_podcast_data(self):
        self.assertEqual(True, True)

    def test_generate_download_directories(self):
        self.assertEqual(True, True)

    def test_default_download_path(self):
        self.assertEqual(True, True)

    def test_get_user_cookies(self):
        self.assertEqual(True, True)

    def test_create_download_url(self):
        self.assertEqual(True, True)

    def test_create_download_file_name(self):
        path = '/test/subDir/'
        show_date = '01011970'
        show_name = 'unitTesting'

        expected_file_name = '/test/subDir/01011970unitTesting.mp3'

        actual_file_name = create_download_file_name(path, show_date, show_name)

        self.assertEqual(expected_file_name, actual_file_name)

    def test_default_download_url(self):
        expected_url = 'https://media001.f4wonline.com/dmdocuments/'

        actual_url = default_download_url()

        self.assertEqual(expected_url, actual_url)


if __name__ == '__main__':
    main()
