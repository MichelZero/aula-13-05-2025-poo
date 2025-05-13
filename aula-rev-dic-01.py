# autor: michel
# data: 2025/05/13

print("--- 1 ---")
####################  1 ##################
# precipitação de chuvas em mm
# jan fev mar
# 40  50  20 
print("Precipitação de chuva em mm")
print("jan\t fev\t mar\t")
print("40\t 50\t 20\t ")
###########################################

print("--- 2 ---")
####################  2 ##################
# dic = {'chave': valor}
chuvas = { 'jan': 40, 'fev': 50, 'mar': 20}
# mesma coisa
# chuvas = { 'fev': 50, 'mar': 20, 'jan': 40}
print("chuvas = { 'jan': 40, 'fev': 50, 'mar': 20}")
###########################################

print("--- 3 ---")
####################  3 ##################
# iteração 'in' 
for maria in chuvas:
  print(maria)
  print(chuvas[maria])
  
print()
for maria in chuvas:
  print(f"{maria}: {chuvas[maria]}")
  
# print()
# for maria in chuvas:
#   if maria == 'fev':
#     chuvas[maria] = "jun"
    
print()
for maria in chuvas:
  print(f"{maria}: {chuvas[maria]}")
  
print("--- 3.1 ---")
for maria, jose in chuvas.items():
  print(f"{maria}: {jose}")
  
###############################################

print("--- 4 ---")
####################  4 ##################
print(chuvas.keys())
print(type(chuvas.keys()))
##########################################

print("--- 5 ---")
####################  5  ##################
print(chuvas.values())

for elemento in chuvas.values():
  print(elemento)
###########################################

print("--- 6 ---")
####################  6 ##################
# soma
print(f"{sum(chuvas.values())}")
# máximo
print(f"{max(chuvas.values())}")
#mínimo
print(f"{min(chuvas.values())}")
# tamanho
print(f"{len(chuvas)}")