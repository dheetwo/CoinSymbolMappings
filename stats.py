import requests

api_key = 'freekey'
url_header = 'https://api.binance.com/'
binance_perpetuals_symbols = [
    "BTC", "ETH", "SOL", "1000PEPE", "XRP", "AVAX", "BNB", "DOGE", "ORDI", "NEAR",
    "1000SHIB", "WLD", "INJ", "HIFI", "GALA", "ARB", "WIF", "1000FLOKI", "ID", "FIL",
    "LTC", "TIA", "ADA", "MATIC", "OP", "LINK", "REEF", "WAVES", "RUNE", "DOT", "ZRX",
    "SEI", "BCH", "PIXEL", "SUI", "FET", "1000SATS", "ETC", "ARPA", "1000BONK", "FTM",
    "SPELL", "CELO", "GMT", "RNDR", "APT", "MKR", "UNI", "MANTA", "ATOM", "GRT", "APE",
    "JUP", "TON", "SSV", "MEME", "SAND", "DYDX", "STRK", "MOVR", "STX", "JOE", "PYTH",
    "EOS", "ALGO", "ARKM", "ENS", "AAVE", "ZIL", "SNX", "AXS", "CRV", "THETA", "1000RATS",
    "MINA", "ICP", "XAI", "YGG", "MYRO", "LDO", "TRB", "UMA", "AI", "ALT", "FLOW", "BAKE",
    "BIGTIME", "EGLD", "BLUR", "POWR", "ANKR", "XLM", "PEOPLE", "HOT", "JASMY", "MASK",
    "1000LUNC", "IOTA", "JTO", "LPT", "DYM", "CFX", "ACH", "HBAR", "MANA", "CHZ", "LOOM",
    "PHB", "ZEN", "CAKE", "ONDO", "COMP", "BELU", "STMX", "PORTAL", "AR", "CKB", "ACE",
    "XEM", "KSM", "IOTX", "XVG", "NFP", "LINA", "IMX", "VET", "SUSHI", "LUNA2", "MAGIC",
    "UNFI", "STORJ", "TRX", "QTUM", "LRC", "OCEAN", "XTZ", "OGN", "LEVER", "NEO", "API3",
    "SXP", "RONIN", "RDNT", "GLMR", "FXS", "MTL", "QNT", "GAL", "IOST", "ENJ", "CHR",
    "COTI", "GAS", "1INCH", "MAVIA", "ROSE", "1000XEC", "WOO", "FLM", "ASTR", "ZEC",
    "KAVA", "AUDIO", "CTSI", "PERP", "USTC", "BSV", "METIS", "BNX", "MAV", "RAD", "GMX",
    "BOND", "SLP", "PENDLE", "RSR", "KAS", "RLC", "CYBER", "EDU", "KNC", "ZETA", "ONT",
    "KLAY", "YFI", "RVN", "DENT", "BEAMX", "GLM", "LIT", "FRONT", "ARK", "ORBS", "ICX",
    "TLM", "NTRN", "AUCTION", "SFP", "OMG", "LSK", "HOOK", "ONE", "SKL", "ILV", "C98",
    "DAR", "XVS", "DASH", "ALPHA", "MDT", "ALICE", "STG", "BAND", "T", "ATA", "STRAX",
    "HFT", "DUSK", "CELR", "POLYX", "KEY", "GTC", "BICO", "AMB", "BAT", "REN", "AXL",
    "BLZ", "NMR", "TWT", "OM", "SUPER", "DODOX", "BADGER", "XMR", "CVX", "TOKEN", "BNT",
    "NKN", "LQTY", "HIGH", "MBL", "RIF", "BAL", "IDEX", "WAXP", "STEEM", "CTK", "TRU",
    "SPTPT", "DGB", "AGLD", "ETHW", "USDC", "SNT", "OXT", "COMBO", "ONG", "ANT", "BTCDOM",
    "DEFI", "FOOTBALL", "BLUEBIRD"
]
price_request = 'api/v3/ticker/price?symbol='
daily_volume_request = 'api/v3/ticker/24hr?symbol='
trading_stats_dict = {}

for symbol in binance_perpetuals_symbols:
    ticker = f"{symbol}USDT"

    price_url = f"{url_header}{price_request}{ticker}"
    price_response = requests.get(price_url)
    price_data = price_response.json()

    daily_data_url = f"{url_header}{daily_volume_request}{ticker}"
    daily_data_response = requests.get(daily_data_url)
    daily_data = daily_data_response.json()

    # print(price_url)
    # print(daily_data_url)

    # Assuming price_data is your dictionary
    price = price_data.get('price', 'price not found')
    daily_volume = daily_data.get('volume', 'volume not found')

    trading_stats_dict[symbol] = {"price": price, "24hr volume": daily_volume}
