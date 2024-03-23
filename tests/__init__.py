from os.path import dirname, abspath, join


FIXTURE_PATH_START = join(dirname(abspath(__file__)), 'fixtures')


def get_fixture_content(fixture_name):
    fixture_path = join(FIXTURE_PATH_START, fixture_name)
    with open(fixture_path) as fixture:
        return fixture.read()
