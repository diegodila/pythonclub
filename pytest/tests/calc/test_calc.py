import pytest
from calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora("hp")

@pytest.fixture(
    params=[['hp'], ['canon'], ['palmeiras']]
)
def calc2(request):
    return Calculadora(request.param)

@pytest.mark.meu_seg
def test_soma(calc):
    assert calc.soma(2,2) == 4
    
@pytest.mark.skip(reason="Ainda nao implementado")
def test_testinho():
    assert false
    
@pytest.mark.teste_parametro
@pytest.mark.parametrize(
    'entrada',
    [3,5,6,8,9,2]
)
def test_multiplas_somas(calc,entrada):
    print(entrada)
    print('Aqui')
    assert calc.soma(entrada,entrada) == entrada+entrada
    
    
    
@pytest.mark.teste_parametro_2
@pytest.mark.parametrize(
    'entry, passed_features, expected_response',
        [
            ([{'customer_id': 123}, 
              {'customer_id': 234}],
             [{'amount': 5000}, {'amount': 6000}],
             [{'customer_id': 123, 'amount': 5000},
              {'customer_id': 234, 'amount': 6000}]),
            ([{'customer_id': 123, 'id_pais': 'Brasil'}, 
                      {'customer_id': 234, 'id_pais': 'Argentina'}],
                     [{'amount': 5000}, {'amount': 6000}],
                     [{'customer_id': 123, 'id_pais': 'Brasil', 'amount': 5000},
                      {'customer_id': 234, 'id_pais': 'Argentina', 'amount': 6000}])
        ]
)
def test_multiplas_somas(calc,entry, passed_features, expected_response):
    print(f'ENTRY:{entry}\nPASSED:{passed_features}\nEXPECTED{expected_response}')
    print('Aqui')
    
    
@pytest.mark.teste_parametro_3
@pytest.mark.parametrize(
    'entry, passed_features, expected_response',
        [(1,2,3),(3,4,5),([{"diego":10}, {'customer_id: 234'}, {'dfi':20}],[{"diego":000}, {'customer_id: 004'}, {'dfi':0}], [{"diego":330}, {'customer_id: 134'}, {'dfi':3333}])]
)
def test_multiplas_somas(calc,entry, passed_features, expected_response):
    print(f'ENTRY: {entry}\nPASSED: {passed_features}\nEXPECTED: {expected_response}')
    print('Aqui')

def dividir(a, b):
    return a / b

@pytest.mark.teste_error
def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError, match='divisao'):
        dividir(10, 0)
        
@pytest.mark.teste_error_2
def test_divisao_por_zero_2():
    with pytest.raises(ZeroDivisionError, match='division'):
        dividir(10, 0)
        
        
@pytest.mark.teste_param_4
def test_multiplas_somas4(calc2):
    print(calc2.marca)