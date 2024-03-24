from http_requests_sender import get_files, DESTINATION_IP
from http_requests_sender.http_requests_sender import send_http_requests


def main():
    files = get_files()
    send_http_requests(files, DESTINATION_IP)


if __name__ == '__main__':
    main()
