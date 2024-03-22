import requests

# GitHub API URL for listing repository contents
url = "https://www.binance.com/bapi/composite/v1/public/promo/cmc/cryptocurrency/listings/latest?limit=5000&start=1"

# Make the API request
response = requests.get(url)
data = response.json()
data_list = data["data"]["body"]["data"]
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
address_dict = {}

def get_token_address(symbol):
    for item in data_list:
        if item.get('symbol') == symbol:
            platform = item.get('platform')
            if platform is not None:
                return platform.get('token_address')
            else:
                print(f"Platform not found for symbol {symbol}")
                break # Exit the loop if platform is None
    return "Symbol not found"


for symbol in etherscan_binance_perps_symbols:
    address_dict[symbol] = get_token_address(symbol)


# Hard code addresses not found
address_dict['BNB'] = '0xB8c77482e45F1F44dE1745F52C74426C631bDD52'
address_dict['NEAR'] = '0x85F17Cf997934a597031b2E18a9aB6ebD4B9f6a4'
address_dict['REEF'] = '0xFE3E6a25e6b192A42a44ecDDCd13796471735ACf'
address_dict['FET'] = '0xaea46A60368A7bD060eec7DF8CBa43b7EF41Ad85'
address_dict['FTM'] = '0x4E15361FD6b4BB609Fa63C81A2be19d873717870'
address_dict['CELO'] = '0x3294395e62F4eB6aF3f1Fcf89f5602D90Fb3Ef69'
address_dict['STX'] = '0x006BeA43Baa3f7A6f765F14f10A1a1b08334EF45'
address_dict['ZIL'] = '0x05f4a42e251f2d52b8ed15E9FEdAacFcEF1FAD27'
address_dict['THETA'] = '0x0000000DE40dfa9B17854cBC7869D80f9F98D823'
address_dict['IOTX'] = '0x6fB3e0A217407EFFf7Ca062D46c26E5d60a14d69'
address_dict['TRX'] = '0x50327c6c5a14DCaDE707ABad2E27eB517df87AB5'
address_dict['SXP'] = '0x8CE9137d39326AD0cD6491fb5CC0CbA0e089b6A9'
address_dict['IOST'] = '0xFA1a856Cfa3409CFa145Fa4e20Eb270dF3EB21ab'
address_dict['ENJ'] = '0xF629cBd94d3791C9250152BD8dfBDF380E2a3B9c'
address_dict['COTI'] = '0xDDB3422497E61e13543BeA06989C0789117555c5'
address_dict['ONE'] = '0x799a4202c12ca952cB311598a024C80eD371a41e'
address_dict['AMB'] = '0x586ee5df24c5a426e42ed7ea6e3eb0f00a4a2256'
address_dict['NKN'] = '0x5Cf04716BA20127F1E2297AdDCf4B5035000c9eb'
address_dict['INJ'] = '0xe28b3b32b6c345a34ff64674606124dd5aceca30'
address_dict['DYDX'] = '0x92D6C1e31e14520e676a687F0a93788B716BEff5'