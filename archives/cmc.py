import requests
import pandas

etherscan_tickers = [
    "BNB", "NEAR", "WLD", "INJ", "ARB", "ID", "LINK", "REEF", "ZRX", "PIXEL",
    "FET", "ARPA", "FTM", "SPELL", "CELO", "GMT", "RNDR", "MKR", "UNI", "GRT",
    "APE", "SSV", "MEME", "SAND", "DYDX", "STX", "ARKM", "ENS", "ZIL", "SNX",
    "AXS", "CRV", "THETA", "LDO", "TRB", "UMA", "AI", "ALT", "BIGTIME", "BLUR",
    "POWR", "PEOPLE", "HOT", "MASK", "LPT", "ACH", "MANA", "CHZ", "CAKE",
    "ONDO", "COMP", "STMX", "PORTAL", "IOTX", "LINA", "IMX", "SUSHI", "STORJ",
    "TRX", "LRC", "OCEAN", "OGN", "LEVER", "API3", "SXP", "RDNT", "FXS", "MTL",
    "QNT", "IOST", "ENJ", "CHR", "COTI", "GAS", "1INCH", "WOO", "CTSI", "METIS",
    "MAV", "BOND", "SLP", "PENDLE", "RSR", "RLC", "KNC", "ZETA", "YFI", "DENT",
    "GLM", "LIT", "FRONT", "ORBS", "TLM", "AUCTION", "SFP", "OMG", "ONE",
    "SKL", "ILV", "C98", "ALPHA", "MDT", "ALICE", "STG", "BAND", "T", "ATA",
    "HFT", "DUSK", "CELR", "KEY", "GTC", "AMB", "BAT", "AXL", "BLZ", "NMR",
    "OM", "CVX", "TOKEN", "BNT", "NKN", "LQTY", "BAL", "IDEX", "TRU",
    "AGLD", "USDC", "SNT", "OXT", "COMBO", "ANT"
]

def get_ticker_data(ticker):
    api_key = "a401b699-2392-422b-a44b-d75159bd0004"  # Replace with your own API key
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol={ticker.upper()}&CMC_PRO_API_KEY={api_key}"

    response = requests.get(url)
    data = response.json()

    try:
        ticker_data = data["data"][ticker.upper()]
        print(ticker_data)

        # Extracting the required fields
        token_address = ticker_data.get('platform')['token_address']
        usd_price = data['data'][ticker.upper()]['quote']['USD']['price']

        circulating_supply = ticker_data.get("circulating_supply")
        total_supply = ticker_data.get("total_supply")
        return token_address, usd_price, circulating_supply, total_supply
    except:
        # Return None for all attributes if data["data"] is empty
        return None, None, None, None


token_address, circulating_supply, total_supply = get_ticker_data("WLD")

print(f"Token Address: {token_address}")
# print(f"Price (USD): {usd_price}")
# print(f"Circulating Supply: {circulating_supply}")
# print(f"Max Supply: {max_supply}")

# for ticker in etherscan_tickers:
#     print(ticker)
#     token_address, usd_price, circulating_supply, total_supply = get_ticker_data(ticker)
#     print(ticker, usd_price, circulating_supply, total_supply)
#     print(f"Token Address: {token_address}")