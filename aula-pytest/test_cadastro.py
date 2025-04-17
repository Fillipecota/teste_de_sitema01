from funcao_cadastro import cadastro

def test_validar():
    assert cadastro("fellipe cota", "32", "480000-0000", "fillipescota@hotmail.com") ==  True