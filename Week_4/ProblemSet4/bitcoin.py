import requests
import sys

try:
  ''''''
  if len(sys.argv) == 2:
    user_usd = float(sys.argv[1]) 
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=c63730d04bacd28c29f6d9e47f1588e7dc1442712cc78516543eca214256e767")
    response.raise_for_status()
    data = response.json()

    
    bit_usd = float(data['data']['priceUsd'])
    amount = bit_usd * user_usd
    print(f"${amount:,.4f}")
    sys.exit()
  sys.exit(1)

except EOFError:
  sys.exit(1)
  print("System exit!")
except KeyboardInterrupt:
  sys.exit(1)
  print("System exit")
except ValueError:
  sys.exit(1)
  print("enter valid input!")
except IndexError:
  sys.exit(1)
  print("enter valid input")
except KeyError:
  sys.exit(1)
  print("enter valid input")
except requests.HTTPError:
  print("response time out")
