from PyPI_TravisCI_Example.calculate import add


class TestCalculateClass:
    def test_calculate_return_value(self):
        assert add(1, 2) == 3
        assert add(3, 4) == 7
