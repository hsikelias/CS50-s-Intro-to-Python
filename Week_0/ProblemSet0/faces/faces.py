def convert(text):
  new_text = text.replace(":(", "🙁")
  new_text = new_text.replace(":)", "🙂")
  return new_text

def main():
  OgText = input("Enter: ")
  final_text = convert(OgText)
  print(final_text)
main()