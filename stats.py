from symbol import extract_symbol, get_token_data
import requests

api_key = 'freekey'
url_header = 'https://api.binance.com/'
etherscan_binance_perps_symbols = [
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
price_request = 'api/v3/ticker/price?symbol='
daily_volume_request = 'api/v3/ticker/24hr?symbol='
trading_stats_dict = {}

for symbol in etherscan_binance_perps_symbols:
    ticker = f"{symbol}USDT"

    price_url = f"{url_header}{price_request}{ticker}"
    price_response = requests.get(price_url)
    price_data = price_response.json()

    daily_data_url = f"{url_header}{daily_volume_request}{ticker}"
    daily_data_response = requests.get(daily_data_url)
    daily_data = daily_data_response.json()

    # Assuming price_data is your dictionary
    price = price_data.get('price', 'price not found')
    daily_volume = daily_data.get('volume', 'volume not found')

    trading_stats_dict[symbol] = {"price": price, "24hr volume": daily_volume}
