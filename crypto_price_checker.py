import requests

def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd,pln"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if crypto_id in data:
            return data[crypto_id]['usd'], data[crypto_id]['pln']
        else:
            print(f"Error: Cryptocurrency ID '{crypto_id}' not found.")
            return None, None
    else:
        print(f"Error: Unable to fetch data for {crypto_id} (status code: {response.status_code})")
        return None, None

def main():
    crypto_id = input("Enter the cryptocurrency ID (e.g., bitcoin, ethereum): ").strip().lower()
    
    if not crypto_id.isalnum():
        print("Error: Invalid cryptocurrency ID. Please enter a valid ID.")
        return
    
    usd_price, pln_price = get_crypto_price(crypto_id)
    
    if usd_price is not None and pln_price is not None:
        print(f"The current price of {crypto_id} is ${usd_price:.2f} ({pln_price:.2f} PLN).")
    else:
        print(f"Failed to retrieve the price for '{crypto_id}'.")

if __name__ == "__main__":
    main()
