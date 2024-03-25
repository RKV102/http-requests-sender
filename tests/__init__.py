from os.path import dirname, abspath, join


FIXTURES_DIR = join(dirname(abspath(__file__)), 'fixtures')


def get_fixture_path(fixture_name):
    return join(FIXTURES_DIR, fixture_name)
