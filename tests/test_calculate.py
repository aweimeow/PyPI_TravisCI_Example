from PyPI_TravisCI_Example.calculate import add, sub


class TestCalculateClass:
    def test_calculate_return_value(self):
        assert add(1, 2) == 3
        assert add(3, 4) == 7

        assert sub(5, 4) == 1
        assert sub(9, 3) == 6
