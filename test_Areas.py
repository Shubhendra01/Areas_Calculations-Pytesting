import Areas


def test_RectangleArea():
    x = 10
    y = 20
    result = Areas.RectangleArea(x, y)
    assert x * y == result
def test_RectanglePerimeter():
    x = 10
    y = 20
    result = Areas.RectanglePerimeter(x, y)
    assert  2*(x+y) == result
def test_SquareArea():
    x = 10
    result = Areas.SquareArea(x)
    assert x * x == result