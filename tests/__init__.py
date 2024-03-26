from os.path import dirname, abspath, join


FIXTURES_DIR = join(dirname(abspath(__file__)), 'fixtures')


def get_fixtures_contents(*fixtures_names):
    return (
        get_fixture_content(get_fixture_path(fixture_name))
        for fixture_name in fixtures_names
    )


def get_fixture_content(fixture_path):
    with open(fixture_path) as fixture:
        return fixture.read()


def get_fixture_path(fixture_name):
    return join(FIXTURES_DIR, fixture_name)
