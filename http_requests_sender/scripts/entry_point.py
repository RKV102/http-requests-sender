from http_requests_sender import get_files_paths, get_files_contents
from http_requests_sender.http_requests_sender import send_http_requests
from http_requests_sender.cli import parse


def main():
    input_dir, host, first_request_num, second_request_num = parse()
    files_paths = get_files_paths(input_dir)
    contents = get_files_contents(files_paths)
    send_http_requests(contents=contents, host=host,
                       first_request_num=first_request_num,
                       second_request_num=second_request_num)


if __name__ == '__main__':
    main()
