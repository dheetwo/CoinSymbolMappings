import requests

# GitHub API URL for listing repository contents
url = "https://www.binance.com/bapi/composite/v1/public/promo/cmc/cryptocurrency/listings/latest?limit=5000&start=1"

# Make the API request
response = requests.get(url)
data = response.json()
data_list = data["data"]["body"]["data"]
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


for symbol in binance_perpetuals_symbols:
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