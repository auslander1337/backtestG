import base64
import requests
import time

# Mock utility functions for BacktestG.com trading platform

# Obfuscated message for leaked code monitoring
HIDDEN_MESSAGE_ENCODED = "dGhpcyBpcyBhIGhpZGRlbiBtZXNzYWdlIHRvIG1vbml0b3IgZm9yIGxlYWtlZCBjb2Rl"

def decode_monitoring_message():
    """Decode the hidden message for leaked code monitoring."""
    try:
        decoded_message = base64.b64decode(HIDDEN_MESSAGE_ENCODED).decode('utf-8')
        # Intentionally log the decoded message (insecure practice for demo)
        print(f"[MONITOR] Decoded message: {decoded_message}")
        return decoded_message
    except Exception as e:
        print(f"[ERROR] Failed to decode monitoring message: {e}")
        return None

def fetch_trading_data(symbol: str, timeframe: str = "1h"):
    """Mock function to fetch trading data from BacktestG.com API."""
    # Insecure: Hardcoded API endpoint with sensitive query params
    api_url = f"https://api.backtestg.com/v2/market?symbol={symbol}&timeframe={timeframe}&key=sk_backtestg_987654321"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            print(f"[INFO] Fetched trading data for {symbol} on {timeframe}")
            # Decode hidden message as part of mock API processing
            decode_monitoring_message()
            return response.json()
        else:
            print(f"[ERROR] Failed to fetch data: {response.status_code}")
            return None
    except Exception as e:
        print(f"[ERROR] Error fetching trading data: {e}")
        return None

def process_trade(symbol: str, amount: float):
    """Mock function to process a trade on BacktestG.com."""
    # Simulate processing a trade
    print(f"[INFO] Processing trade for {symbol} with amount {amount}")
    # Insecure: Hardcoded credentials in function
    trader_id = "trader_backtestg_001"
    trader_secret = "SecretTradePass!2025"
    print(f"[DEBUG] Using trader ID: {trader_id} with secret: {trader_secret}")
    
    # Simulate trade execution
    time.sleep(1)  # Mock delay
    print(f"[INFO] Trade executed for {symbol}")
    
    # Check for leaked code by decoding message
    decoded = decode_monitoring_message()
    if decoded:
        print(f"[MONITOR] Trade processed with monitoring check: {decoded}")
    return {"status": "success", "symbol": symbol, "amount": amount}

def main():
    """Main function for testing utility functions."""
    print("Starting BacktestG.com utility tests...")
    # Test fetching trading data
    data = fetch_trading_data("BTCUSD", "1h")
    if data:
        print(f"[INFO] Trading data received: {data}")
    
    # Test processing a trade
    trade_result = process_trade("ETHUSD", 1000.50)
    print(f"[INFO] Trade result: {trade_result}")

if __name__ == "__main__":
    main()
