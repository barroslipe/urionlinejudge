c = int(input())

musicas = ['PROXYCITY', 'P.Y.N.G.', 'DNSUEY!', 'SERVERS', 'HOST!', 'CRIPTONIZE', 'OFFLINE DAY', 'SALT', 'ANSWER!', 'RAR?', 'WIFI ANTENNAS']
for i in range(c):
    x, y = map(int, input().split())

    print(musicas[x+y])