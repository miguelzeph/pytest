#---------------------------
#Arquivo ->    test_soma.py |
#---------------------------
from soma import *

# ------------Testar a função SOMA()--------------
def test_soma():
	assert soma(1,1) == 2
def test_soma_igual_int():
	assert type(soma(1,1)) is int
def test_soma_igual_a_negativo(valor=0):
	assert soma(-10,1) < valor
#--------------------------------------------------

# ------------Testar a função SOMA_TUDO()--------------
def test_soma_tudo():
	assert soma_tudo(1,1,1) == 3
def test_soma_tudo_igual_int():
	assert type(soma_tudo(1,1,100)) is int
#--------------------------------------------------
