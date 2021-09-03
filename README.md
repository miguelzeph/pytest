# Pytest 

Primeiramente o pytest é um Framework e não uma biblioteca, é utilizado para realizar testes no seu código (como o próprio nome já diz)... Ou seja, ele vai avaliar os seus **assert** nas funções/classes python que você deseja testar.

## Instalação do Pytest
```
Instalar o pytest
pip install pytest
```

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

obs: execute sempre o **pytest** com verbose (**-v**) 
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
#executar no terminal: pytest -v |
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

#-----------------------------
#executar no terminal: pytest -v |
#-----------------------------
```
[source: Learn Pytest in 60 Minutes : Python Unit Testing Framework](https://www.youtube.com/watch?v=bbp_849-RZ4) <br/>
[source: Pytest Tutorial em Português](https://www.youtube.com/watch?v=eG4oiOE95aM)

# Pytest-cov (COVERAGE)
Essa é uma **extensão** do framework pytest, funciona da seguinte maneira, enquanto o **pytest** verifica as falhas que ocorreram durante o teste (dando-te uma **%** de FAILED e PASSED), o **pytest-cov** mostra literamente a **cobertura (coverage) realizada pelo teste**... ele te retorna uma porcentagem, mas se você usar o comando **--cov-report=html** você poderá visualizar ainda os locais que não foram passados pelo teste (fica escrito em vermelho missing) no escript, basta abrir o **index.html** dentro da pasta html que ele cria na raiz executada.

## Instalando Extensão Pytest-COV (COVERAGE)
```
Instalar extensões do pytest ( pytest-cov)
pip install pytest-cov
```

## Como executar
Execução básica ( --cov=PATH )
```
pytest py.test --cov=./ 
```

Criando uma saída em HTML - **RECOMENDADO** porque assim você pode ver quais linhas não foram verificadas!
```
pytest --cov=./ --cov-report=html
```
[source: Unit Testing in Python — The Basics](https://medium.com/swlh/unit-testing-in-python-basics-21a9a57418a0)


