f1, f2 = map(float, input().split())

flutuacao = 1.0 * (1.0 + f1/100) * (1 + f2/100)

print("%.6f" % ((flutuacao - 1.0)*100))