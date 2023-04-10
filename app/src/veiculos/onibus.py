"""
"""

from src.veiculos.veiculo import Veiculo


class Onibus(Veiculo):
    """"""
    _assentos: int

    def __init__(self, placa: str, ano: int, assentos: int) -> None:
        """
        """
        self._assentos = assentos

        super().__init__(placa, ano)

    def setAssentos(self, assentos: int) -> None:
        """
        """
        self._assentos = assentos

    def getAssentos(self) -> int:
        """
        """
        return self._assentos

    def exibirDados(self) -> None:
        """
        """
        super().exibirDados()

        print("ASSENTOS: ", self._assentos)
