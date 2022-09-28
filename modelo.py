class Conta:
    static_total_contas = 0

    def __init__(self, numero, titular, saldo, limite):

        Conta.static_total_contas += 1

        self.__id = Conta.static_total_contas
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__extrato = []

    @property
    def id(self):
        return self.__id

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def extrato(self):
        return self.__extrato

    @id.setter
    def id(self, valor):
        self.__id = valor

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    def add_extrato(self, valor):
        self.__extrato.append(valor)

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Não é possivel sacar valor R${valor} maior que o saldo R${self.saldo}")
            self.add_extrato(f"Tentativa inválida de saque")
        else:
            self.saldo -= valor
            extrato_valor = f"você sacou R${valor}, seu saldo atual é R${self.saldo}"
            self.add_extrato(extrato_valor)

    def depositar(self, valor):
        self.saldo += valor
        self.add_extrato(f"você depositou R${valor}, seu saldo atual é R${self.saldo}")

    def transferir(self, valor, conta):
        self.sacar(valor)
        conta.depositar(valor)
        self.add_extrato(f"transferido para conta {conta.numero} ")
        conta.add_extrato(f"transferencia da conta {self.numero} ")

    def __str__(self):
        return f"\n*********CONTA COMUN********\n" \
               f"****************************\n" \
               f"[ numero: {self.numero},\n" \
               f"  titular: {self.titular},\n" \
               f"  saldo: {self.saldo},\n" \
               f"  limite: {self.limite} ]\n" \
               f"****************************\n"

    @staticmethod
    def tipo_banco():
        return "Bradesco"


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo, limite, saldo_pop):
        super().__init__(numero, titular, saldo, limite)
        self.__saldo_pop = saldo_pop

    def __str__(self):
        return f"\n********CONTA POUPANCA****\n" \
               f"****************************\n" \
               f"[ numero: {self.numero},\n" \
               f"  titular: {self.titular},\n" \
               f"  saldo: {self.saldo},\n" \
               f"  limite: {self.limite}\n" \
               f"  saldo_pop: {self.__saldo_pop}]\n" \
               f"****************************\n"


class ListContas(list):
    def __init__(self, nome, Conta):
        self.nome = nome
        super().__init__(Conta)

    @property
    def __getitem__(self, item):
        return Conta[item]

    def __len__(self):
        return len(self.Conta)
