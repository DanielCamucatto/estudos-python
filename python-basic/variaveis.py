# Variáveis são container que armazenam valores de dados
# Python não tem um comando para declarar variável, uma variável é criada no momento em que atribui um valor a ela pela primeira vez
x = 5
y = 'hello word'

print(x, y)

# variavel não precisam ser declaradas com nenhum tipo especifico e podem até mesmo mudar de tipo depois de serem declaradas
x = 4
x = 'verdade'
print(x) # o resultado será verdade

# FUNDIÇÃO
# se for preciso especificar o tipo de dados de uma variável, isso pode ser feito com conversão
x = str(3) # o resultado será '3'
y = int(3) # o resultado sera 3
z = float(3) # o resultado sera 3.0
print(x, y, z)


# TIPO DE DADOS
# Para saber qual o tipo de dado que uma variavel esta trazendo é possível usar um função para isso
x = 'john'
y = 5
print(type(x))
print(type(y))

# ASPAS SIMPLES OU DUPLAS
# variaveis de string podem ser declaradas usando aspas simples ou duplas
x = 'John'
y = "Peter"
# o resultado disso é o mesmo

# MAIÚSCULAS E MINISCULAS
# Os nomes de variaveis diferenciam maiusculas e minisculas
a = 4
A = "John"
# o exemplo acima demontra que são variaveis diferentes

# NOME DE VARIAVEIS
