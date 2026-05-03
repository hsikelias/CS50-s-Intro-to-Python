from plates import is_valid

def test_length():
  assert is_valid("A") == False
  assert is_valid("AWHER89") == False
  assert is_valid("AA") == True
  assert is_valid("AAG34") == True

def test_number_in_end():
  ...
  assert is_valid("AFG89") == True
  assert is_valid("AER98A") == False

def test_start_with_two_letters():
  ...
  assert is_valid("AWWR78") == True
  assert is_valid("A4AWB3") == False
  assert is_valid("ABAAE") == True
  assert is_valid("1ABW23") == False
  assert is_valid("A3BWE3") == False
  assert is_valid("ABC12") == True

def test_punctuation_check():
  ...
  assert is_valid("A ER78") == False
  assert is_valid("HE!68") == False

def test_zero_in_plate():
  assert is_valid("ABWE03") == False