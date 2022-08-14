# from v8f.
from tcpgecko import TCPGecko
tcp = TCPGecko("192.168.1.")
tcp.pokemem(0x02E9B1B0, 0x7FE4FB78)
tcp.s.close()
print("Armor Hud Enabled!.")
