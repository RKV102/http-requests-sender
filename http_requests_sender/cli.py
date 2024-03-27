import argparse
from math import inf


def parse():
    parser = argparse.ArgumentParser(description='Finds HTTP requests in text'
                                                 'files and sends them.')
    parser.add_argument('input_directory', type=str)
    parser.add_argument('-H', '--host', type=str,
                        default=None, dest='host')
    parser.add_argument('-F', '--first_request_num', type=int,
                        default=1, dest='first_request_num',
                        help='Allows you to set the beginning '
                             'of the range of HTTP requests to be sent')
    parser.add_argument('-L', '--last_request_num', type=int,
                        default=inf, dest='last_request_num',
                        help='Allows you to set the end '
                             'of the range of HTTP requests to be sent')
    return (
        parser.parse_args().input_directory,
        parser.parse_args().host,
        parser.parse_args().first_request_num,
        parser.parse_args().last_request_num
    )
