import pytest
from app import demo


class TestAdd:
    def test_add(self):
        assert demo.add(2, 3) == 5

    def test_add_error(self):
        with pytest.raises(demo.MysteryError):
            demo.add(99, 0)

    @pytest.mark.parametrize(
        'a, b, expected', [
            (1, 1, 2),
            (2, 1, 3),
            (3, 1, 4),
            (4, 1, 5),
            (5, 1, 6),
            (6, 1, 7),
            (7, 1, 8),
            (8, 1, 9),
            (9, 1, 10),
            (10, 1, 11)
        ]
    )
    def test_add_multiple_values(self, a, b, expected):
        assert demo.add(a, b) == expected

    # my_fixture comes from conftest.py file
    def test_fixtures(self, my_fixture):
        assert my_fixture == 42

    def test_capsys(self, capsys):  # capturing system logs
        print('hello')
        out, err = capsys.readouterr()
        assert 'hello\n' in out

    def test_monkeypatch(self, monkeypatch):
        def fake_add(a, b):
            return 42
        monkeypatch.setattr(demo, 'add', fake_add)
        assert demo.add(2, 3) == 42

    def test_tmpdir(self, tmpdir):
        some_file = tmpdir.join('something.txt')
        some_file.write('{"hello": "world"}')

        result = demo.read_json(str(some_file))
        assert result['hello'] == 'world'

    def test_fixture_with_fixtures(self, capsys, captured_print):
        print('more')
        out, err = capsys.readouterr()
        assert out == 'hello\nmore\n'