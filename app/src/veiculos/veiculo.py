"""
"""

from typing import Optional, Union


class Veiculo:
    """
    """
    _placa: Optional[str]
    _ano: Optional[int]

    def __init__(self, placa: Optional[str]=None, ano: Optional[int]=None) -> None:
        """
        """
        self._placa = placa
        self._ano = ano

    def setPlaca(self, placa: str) -> None:
        """
        """
        self._placa = placa

    def setAno(self, ano: Union[int, str]) -> None:
        """
        """
        if isinstance(ano, str):
            self._ano = int(ano)

        else:
            self._ano = ano

    def getPlaca(self) -> Optional[str]:
        """
        """
        return self._placa

    def getAno(self) -> Optional[int]:
        """
        """
        return self._ano
    
    def exibirDados(self) -> None:
        """
        """
        print("PLACA: ", self._placa)
        print("ANO: ", self._ano)
