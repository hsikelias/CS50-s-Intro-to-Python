from calculator import square


def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-3) == 9
    assert square(-2) == 4
    assert square(0) == 0


"""
# tests calculator.py, it's functionality
from calculator import square

def main():
  test_square()

# testing the square function
def test_square():
  try:
    assert square(2) == 4
  except AssertionError:
    print("2 squared was not 4")

  try:
    assert square(3) == 9
  except AssertionError:
    print("3 squared was not 9")

  try:
    assert square(-2) == 4
  except AssertionError:
    print("-2 squared was not 4")
  try:
    assert square(0) == 0
  except AssertionError:
    print("0 squared was not 0")
  
if __name__ == "__main__":
  main()
"""

# another practice to do is dividing function
# based on possible fails.
