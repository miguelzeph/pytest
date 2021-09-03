# Pytest 

Primeiramente o pytest é um Framework e não uma biblioteca, é utilizado para realizar testes.

## Why do we test at all?
**Trust:** You checked at least some cases if they work. So others can have more trust in the quality of your work and you can also put more trust in it.<br/>
**Breaking Changes:** For a bigger project, it is sometimes hard to have every part in mind. By writing tests, you make it easier to change something and see if / where things break. This does not only help you but also team members. Including once that are not there yet.<br/>
**Code Style:** When you know that you have to write tests, you write some things slightly differently. Those slight differences usually improve the coding style. Sometimes, they are crucial. For example, if you have to thoroughly test your code you will make smaller chunks.<br/>
**Documentation:** Some test cases show a little bit of how the code is intended to be used.<br/>

## Informações importantes
- Se você rodar pytest no terminal, ele irá analisar todo o diretório atual e os subdiretórios dentro dele que contenham **test_** no início ou **_test.py** no final. Veja um exemplo abaixo
```
test_nome.py
ou
nome_test.py
```
- Dentro do arquivo que vai ser testado as funções devem iniciar com **test_** e sempre usar o **assert** para afirmar algo que será testado. Veja um exemplo abaixo:
```
def test_xxx():
	assert xxxx == 10
	assert blabla is None
```

### Boas práticas
Veja abaixo uma maneira que não acho interessante de testar o programa.
```
#---------------------------
#Arquivo ->    test_soma.py |
#---------------------------

def soma(a,b):
	return a+b

def test_soma():
	assert soma(1,1) == 3
	assert type(soma(1,1)) is int

#-----------------------------
#executar no terminal: pytest |
#-----------------------------
```
O modo que eu acho mais limpo de se testar o código, cria um arquivo e um **outro pra teste** e assim realiza o import das funções que deseja testar no arquivo apropriado pra teste.
```
#-------------------
#Arquivo -> soma.py |
#-------------------

def soma(a,b):
	return a+b

#---------------------------
#Arquivo ->    test_soma.py |
#---------------------------
from soma import *

def test_soma():
	assert soma(1,1) == 3
	assert type(soma(1,1)) is int

-----------------------------
executar no terminal: pytest |
-----------------------------
```





