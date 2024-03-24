from os.path import dirname, abspath, join


FIXTURE_PATH_START = join(dirname(abspath(__file__)), 'fixtures')


def get_fixture_path(fixture_name):
    return join(FIXTURE_PATH_START, fixture_name)
