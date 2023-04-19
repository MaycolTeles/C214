"""
"""

from veiculo import Veiculo


class Caminhao(Veiculo):
    """"""
    _eixos: int

    def __init__(self, placa: str, ano: int, eixos: int) -> None:
        """
        """
        self._eixos = eixos

        super().__init__(placa, ano)

    def setEixos(self, eixos: int) -> None:
        """
        """
        self._eixos = eixos

    def getEixos(self) -> int:
        """
        """
        return self._eixos

    def exibirDados(self) -> None:
        """
        """
        super().exibirDados()

        print("EIXOS: ", self._eixos)
