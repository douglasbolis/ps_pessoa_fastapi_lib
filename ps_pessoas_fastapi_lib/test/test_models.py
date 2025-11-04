import pytest
from pydantic import ValidationError
from ps_pessoas_fastapi_lib.model.models import PessoaBase, EnderecoBase

# ====================================================================
#                      TESTES DE PESSOA BASE
# ====================================================================

def test_pessoa_base_cria_com_sucesso():
    # Teste para garantir que dados válidos criam a instância
    nome = "João da Silva"
    idade = 30
    email = "joao@exemplo.com"
    telefone = "99999-8888"

    pessoa_valida = PessoaBase(nome=nome, idade=idade, email=email, telefone=telefone)

    assert pessoa_valida.nome == nome
    assert pessoa_valida.idade == idade
    assert pessoa_valida.email == email
    assert pessoa_valida.telefone == telefone
# fim_def

def test_pessoa_base_falha_nome_muito_curto():
    # O nome com min_length<2
    with pytest.raises(ValidationError):
        PessoaBase(
            nome="J",
            idade=30,
            email="joao@exemplo.com"
        )
    # fim_with
# fim_def

def test_pessoa_base_falha_idade_invalida():
    # A idade < 0 e > 200
    with pytest.raises(ValidationError):
        # Idade negativa
        PessoaBase(
            nome="João",
            idade=-5,
            email="joao@exemplo.com"
        )
    # fim_with

    with pytest.raises(ValidationError):
        # Idade muito alta
        PessoaBase(
            nome="João",
            idade=250,
            email="joao@exemplo.com"
        )
    # fim_with
# fim_def

# ====================================================================
#                      TESTES DE ENDERECO BASE
# ====================================================================

def test_endereco_base_cria_com_sucesso():
    logradouro = "Rua Teste"
    bairro = "Centro"
    cidade = "Serra"
    estado = "ES"
    cep = "29160000"

    endereco_valido = EnderecoBase(logradouro=logradouro, bairro=bairro, cidade=cidade, estado=estado, cep=cep)

    assert endereco_valido.logradouro == logradouro
    assert endereco_valido.bairro == bairro
    assert endereco_valido.cidade == cidade
    assert endereco_valido.estado == estado
    assert endereco_valido.cep == cep
# fim_def

def test_endereco_base_falha_estado_muito_longo():
    # O estado com max_length>2
    with pytest.raises(ValidationError):
        EnderecoBase(
            logradouro="Rua Teste",
            bairro="Centro",
            cidade="Serra",
            estado="ESP",  # Mais de 2 caracteres
            cep="29160000"
        )
    # fim_with
# fim_def
