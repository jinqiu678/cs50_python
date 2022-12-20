import sys
import requests
import json

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
 
def main():
    #try: 
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # print(json.dumps(response.json(), indent=2))
        output = response.json()
        total_amount = output['bpi']['USD']['rate_float'] * float(sys.argv[1])
        print(f"${total_amount:,.4f}")


if __name__ == "__main__":
    main()