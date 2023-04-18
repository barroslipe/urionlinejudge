n = int(input())
numeros = list(map(int, input().split()))

m_2 = m_3 = m_4 = m_5 = 0

for i in numeros:
    
    if i%2 == 0:
        m_2 += 1
    if i%3 == 0:
        m_3 += 1
    if i%4 == 0:
        m_4 += 1
    if i%5 == 0:
        m_5 += 1

print(f"{m_2} Multiplo(s) de 2")
print(f"{m_3} Multiplo(s) de 3")
print(f"{m_4} Multiplo(s) de 4")
print(f"{m_5} Multiplo(s) de 5")