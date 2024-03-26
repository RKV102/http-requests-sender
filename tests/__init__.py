from os.path import dirname, abspath, join


FIXTURES_DIR = join(dirname(abspath(__file__)), 'fixtures')


def get_fixture_content(fixture_name):
    with open(get_fixture_path(fixture_name)) as fixture:
        return fixture.read()


def get_fixture_path(fixture_name):
    return join(FIXTURES_DIR, fixture_name)
