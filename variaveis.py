#  declaração de variáveis
nome = "Suk4shi"   # string (texto)
idade = 25         # int (inteiro)
altura = 1.75      # float (decimal)
ativo = True       # bool (booleano)

# Para verificar o tipo da da variavel
print(type(nome))
print(type(idade))
print(type(altura))
print(type(ativo))
print(type(1 + 2j))

# Função isinstance
a = 10
b = 'sol'

print(isinstance(a, str))

# converter tipos
# int → float
x = 10
x = float(x)
print(x)  # 10.0

# float → int
y = 7.9
y = int(y)
print(y)  # 7

# str → int
idade = int("25")

# int → str
idade_txt = str(25)

# bool → int
ativo = int(True)  # 1
