"""
"""

from caminhao import Caminhao
from onibus import Onibus


def main() -> None:
    """
    """
    caminhao = Caminhao(placa="1234ABC", ano=2021, eixos=6)
    onibus = Onibus(placa="ABC1234", ano=2020, assentos=42)

    print("DADOS CAMINHÃO:")
    caminhao.exibirDados()

    print("DADOS ÔNIBUS:")
    onibus.exibirDados()


if __name__ == "__main__":
    main()
