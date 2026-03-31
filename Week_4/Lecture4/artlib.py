import requests

def main():
  print("Search Art Institute of Chicago!")
  artist = input("Artists: ")
  try:
    response = requests.get("https://api.artic.edu/api/v1/artworks/searchi",{"q":artist})
    response.raise_for_status() #sents request and checks if the request worked, if it didnt raises HTTP error. 
    return response
  except requests.HTTPError:
    print("Couldn't complete request!")
    return

content = response.json()
for artwork in content["data"]:
  print(f"*{artwork["title"]}")

main()