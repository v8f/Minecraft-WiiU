# by v8f.
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.")
tcp.pokemem(0x02F70970, 0x38600001)
tcp.pokemem(0x032283CC, 0x38800000)
tcp.pokemem(0x02F59534, 0x480002E8)
tcp.s.close()
print("Craft whatever you want now.")
