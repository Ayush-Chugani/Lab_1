from app import square

def test_1():
  assert square(2) == 4

def test_2():
  assert square(-3) == 9

def test_3():
  assert square(0) == 0