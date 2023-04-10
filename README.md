# C214 - Engenharia de Software

Repositório contendo todos os códigos desenvolvidos para a disciplina de C214 - Engenharia de Software do INATEL.

<h4 align="left"> 
	Autor :pencil2:
</h4>

<p align="left">
 <a href="https://github.com/maycolteles">Maycol Teles Costa Dionisio Pereira</a> 
</p>

*********************

## Sumário :clipboard:

* [Requisitos](#requirements)
* [Setup e Instalação](#setup-installation)
* [Como Usar](#how-to-use)

*********************
##  Requisitos :pencil: <a name="requirements"></a>

* [Python 3.6+](https://www.python.org/)
* Pip 20.0+ (vem junto com o Python 3)

*********************
##  Setup e Instalação :white_check_mark: <a name="setup-installation"></a>

### Clonando o repositório :file_folder:
Primeiramente, para ter uma cópia local do projeto para executá-lo/testá-lo, clone o repositório em uma pasta na sua máquina:

```
git clone git@github.com:MaycolTeles/C214.git
```

### Criando e Ativando um Ambiente Virtual :open_file_folder:
É recomendado instalar todas as suas dependências dentro de um [virtualenv](https://docs.python.org/3/tutorial/venv.html) (ambiente virtual ou venv). Para isso - dentro da pasta do repositório clonado - crie um novo `virtualenv`:

```
python3 -m virtualenv venv
```

Caso o comando acima não funcione, você pode tentar executar

```
python -m virtualenv venv
```

Caso ainda sim você esteja obtendo um erro, verifique se o pacote `virtualenv` está instalado. Em caso negativo, execute:

```
pip install virtualenv
```

Agora, ative o ambiente virtual (para Linux/MacOS):

```
source venv/bin/activate
```

ou (para Windows):

```
venv\Scripts\activate
```

### Instalando as Dependências :wrench:
Para instalar todas as dependências necessárias deste projeto, execute o seguinte comando no seu terminal (no mesmo diretório do arquivo `requirements.txt`) com o ambiente virtual ativado:

```
pip install -r requirements.txt
```

##  Como Usar :man_technologist: <a name="how-to-use"></a>

Para executar os arquivos, basta abrir e executar o arquivo `run.py` em cada subdiretório que ele contém o código necessário para executar aquele submódulo específico.
