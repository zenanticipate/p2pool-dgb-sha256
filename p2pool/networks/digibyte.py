from p2pool.bitcoin import networks

PARENT=networks.nets['digibyte']
SHARE_PERIOD=15
CHAIN_LENGTH=24*60*60//10
REAL_CHAIN_LENGTH=24*60*60//10
TARGET_LOOKBEHIND=50
SPREAD=30
IDENTIFIER='1bfe01c1d4426db3'.decode('hex')
PREFIX='1bfe01c1d4db0434'.decode('hex')
P2P_PORT=5026
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=True
WORKER_PORT=5027
BOOTSTRAP_ADDRS='crypto.office-on-the.net p2p-spb.xyz sha.dgb.crabs.pro'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-dgb-sha256'
VERSION_CHECK=lambda v: True
VERSION_WARNING=lambda v: 'Upgrade DigiByte >=6.14.2!' if v < 70015 else None
