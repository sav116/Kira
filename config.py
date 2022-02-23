from environs import Env

env = Env()
env.read_env()

KIRA_ADDRESS = env.str("KIRA_ADDRESS")
KIRA_MONIKER = env.str("KIRA_MONIKER")
KIRA_URL = "https://testnet-rpc.kira.network/api/valopers?all=true"

BOT_TOKEN = env.str("BOT_TOKEN")
CHAT_ID = env.str("CHAT_ID")
