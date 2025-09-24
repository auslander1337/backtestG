import requests

# Hardcoded credentials (INSECURE - DO NOT DO THIS IN PRODUCTION)
USERNAME = "admin@backtestg.com"
PASSWORD = "SuperSecret123!"
API_KEY = "sk_backtestg_abcdef1234567890"

def connect_to_backtestg_api():
    # Mock API endpoint for BacktestG.com
    url = "https://api.backtestg.com/v1/trading"
    
    # Insecure: Hardcoding sensitive data
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "User": USERNAME,
        "Pass": PASSWORD
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"API Response: {response.status_code}")
        return response.json()
    except Exception as e:
        print(f"Error connecting to BacktestG.com API: {e}")
        return None

def main():
    # Insecure: Printing sensitive information
    print(f"Connecting with username: {USERNAME} and password: {PASSWORD}")
    data = connect_to_backtestg_api()
    if data:
        print("Successfully connected to BacktestG.com!")
    else:
        print("Failed to connect to BacktestG.com.")

if __name__ == "__main__":
    main()
