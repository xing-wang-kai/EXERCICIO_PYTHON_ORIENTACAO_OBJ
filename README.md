# EXERCICIOS PYTHON OO

### SOBRE

Nesse arquivo de estudos foi estudado do básico ao avançado de orientação a objetos.

Para o estudo foi implementando uma class com nome Conta e subclass com o nome ContaPoupanca que herda informações da class mãe Conta.

Além disso foram testado herança da class List para torna uma class um array interavel com comandos For in not in etc. E também a implementação para leitura de tamanho.

Foi testado também os modelos duck Typing com as tipagens __getitem__ para usar a class como uma list e interar com o for no item que é uma list e o metodo __len__ para poder retornar os total de instancias dentro do objeto.

Foi usado o metodo __str__ para sobreescrever o retorno do print da class com uma STRING.

### CONSTRUINDO UMA CLASS

Em python uma class pode ser devida pelo chamado class + nome da class por padrão usamos o type UpperCamelCase para definir o nome da class. ex.:

```python
     class Conta:
        
```

Dentro das class também foram definidos o constructor com o metodo __init__

```python
   class Conta:
        def __init__(self):
```

### ATRIBUTOS

(***Atributos são caracteristas de uma class ou morfologias da mesma***)

Os atributos de uma class em Python são definidos após o construtor para serem instancia do objeto. também foi usado o padrão do python para tornar um metodo privado que pode ser defindo com um underline _ ou dois underline __ ex.:

```python
   class Conta:
        def __init__(self, numero, titular, saldo):
            self.__saldo = saldo
            self.__numero = numero
            self.__titular = titular
```

### METODOS
                  
(___metodos são ações e comportamentos especificas dentro de uma class___)

Foram estudados a forma de definição de METODOS dentro de uma class em python os mesmo são usados como funcões comuns,  ex.: 

```python
   class Conta:
        def __init__(self, numero, titular, saldo):
            self.__saldo = saldo
            self.__numero = numero
            self.__titular = titular
        
        def sacar(self, valor):
            if(self.__saldo < valor):
                print("não é possivel sacar")
            else:
                self.__saldo -= valor
```

#### METODOS GETTER E SETTER

em uma class é comun manipular elementos atravez de Getter e Setter em vez diretamente por meio do atributo. para isso construimos a anostação @property e a anotação @<atributo>.setter (onde <atributo é o valor do atributo>) para definir este metodos e conseguir usa-los sem danificar o projeto.

```python
   class Conta:
        def __init__(self, numero, titular, saldo):
            self.__saldo = saldo
            self.__numero = numero
            self.__titular = titular
        
        @property
        def saldo(self):
            return self.__saldo
        
        @saldo.setter
        def saldo(self, valor):
            self.__saldo = valor
```

### HERANÇA

Uma class pode herdar atributos de outra class ou então comportamentos, e a class filho ter mais atributos especificos. usando o exemplo da conta acima Ex.

```python
    from model import *

   class ContaPoupanca(Conta):
        def __init__(self, numero, titular, saldo, pop_saldo):
            super().__init__(numero, titular, saldo)
            self.pop_saldo = pop_saldo
```

No exemplo acima a ContaPoupanca herda propriedade de Conta e desta forma com o construtor SUPER o mesmo já atribui os metodos que uma CONTA deve ter, todos atributos e metodos que estão em Conta podem ser usados pelos objetos instanciados por ContaPoupanca.

### STATICOS

Alguns metodos e atributos podem ser staticos dentro de uma class, isso significa que eles são instanciados pela formula da class e não pelos objetos que são instanciados pela calss.

ex.:

```python
   class Conta:
        total_contas = 0
        def __init__(self, numero, titular, saldo):
            Conta.total_contas += 1
            
            self.__id = Conta.total_contas
            self.__saldo = saldo
            self.__numero = numero
            self.__titular = titular
```

Para metodos que serão staticos devemos colocar a anotação sobre o metodo para informar este comportamente que seria @staticmethod

```python
   class Conta:
        def __init__(self, numero, titular, saldo):
            self.__saldo = saldo
            self.__numero = numero
            self.__titular = titular

        @staticmethod
        def retonar_nome_banco():
            return "BYTEBANC O BANCO DIGITAL"
```
### SOBREESCRITA DE METODOS DA CLASS

Alguns metodos da class podem ser adiconados para retornos especificos, como no caso em que queremos retonar uma STRING com dados da class em vez do endereço de memória dela. então definimos o metodos __str__

```python
   class Conta:
        def __init__(self, numero, titular, saldo):
            self.__saldo = saldo
            self.__numero = numero
            self.__titular = titular

        def __str__(self):
            return f"[ numero: {self.__numero},\n"\
                   f"  titular: {self.__titular},\n"\
                   f"  saldo: {self.__saldo}\n ]"
```

No exemplo acima o sistema ao chamar a conta vai imprimir uma string com os dados da conta.
Também é possivel construir um objeto com propriedades de Array onde será possivel interar por ele com elementos como For in etc. 

```python
   class ArrayConta(list):
        def __init__(self, nome, Conta):
            super().__init__(Conta)
            self.__nome = nome
```

Ao interar pelo metodo acima será como em um array, porém também é possivel realizar outra performace sem usar a class list, mas escrevendo os atributos. __getitem__ e __len__ etc.

```python
   class ArrayConta():
        def __init__(self, nome, Conta):
            self.__Conta = Conta
            self.__nome = nome
        
        def __str__(self):
            return len(self.__Conta)
        
        def __getitem__(self, item):
            return self.__Conta[item]
```

### ABSTRACÃO

Podemos criar class que não podem ser instanciadas somente herdadas, estão class são chamadas de abstratas e no python para criar este exemplo de class devemos importa de ABS essa informações.

```python
   from abc import ABCMeta, abstractmethod

    class programa(metaclass=ABCMeta)
        @abstractmethod
        def __str__(self):
            pass
```