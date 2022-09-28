from modelo import *

conta01 = Conta("1234", "Fernando", 1000, 2000.00)
conta02 = Conta("1235", "joao", 800, 3000.00)

print(f"{conta01.numero}")
print(f"{conta01.titular}")

print(f"{conta01}")
print(f"{conta02}")

conta01.transferir(200, conta02)
conta01.sacar(200)
print(f"SALDO: {conta01.saldo}")
print(f"SALDO: {conta02.saldo}")
print(f"SALDO: {conta01.extrato}")
print(f"SALDO: {conta02.extrato}")


todasContas = [conta01, conta02]
contas = ListContas("lista final de semana", todasContas)

for conta in contas:
    print(f"{conta}")

contaPoupanca =  ContaPoupanca("32145", "Joaquim Silveira", 200.00, 1000.00, 4000.00)

print(f"CONTA POUPANCA: {contaPoupanca}")


print(f"CONTA: {Conta.tipo_banco()}")


print(f" ID: {conta01.id}")
print(f" ID: {conta02.id}")
print(f" ID: {Conta.static_total_contas}")