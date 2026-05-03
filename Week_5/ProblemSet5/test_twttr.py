from twttr import shorten

def test_lower():
  assert shorten("twitter") == "twttr"
  assert shorten("apple") == "ppl"

def test_upper():
  assert shorten("Twitter") == "Twttr"
  assert shorten("APPLE") == "PPL"

def test_numbers():
  assert shorten("tw1tt3r") == "tw1tt3r"

def test_punctuation():
  assert shorten("twitter!!") == "twttr!!"
