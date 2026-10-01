# Projetos de Visão Computacional com Python

Repositório contendo uma coleção de **mini projetos desenvolvidos durante o curso de Inteligência Artificial Aplicada em Python**, com foco em técnicas de **Visão Computacional**, incluindo detecção e reconhecimento de faces, identificação de pontos faciais e reconhecimento de gestos por meio da webcam.

Os projetos foram desenvolvidos utilizando **Python**, **Jupyter Notebooks** e scripts Python, explorando diferentes bibliotecas e abordagens para processamento de imagens e interação com a câmera.

## Projetos

### 👤 Detect Face

Projeto voltado para **detecção e reconhecimento facial**, utilizando a webcam e imagens como fonte de entrada.

O projeto possui diferentes exemplos:

* **Contagem de faces:** utiliza a webcam para detectar as faces presentes na imagem e informar a quantidade encontrada.
* **Detecção facial:** identifica a face e os olhos encontrados na imagem capturada pela webcam, apresentando visualmente as regiões detectadas.
* **Reconhecimento facial com imagens:** utiliza imagens armazenadas na pasta `img` para realizar a detecção e o reconhecimento de faces utilizando a biblioteca `face_recognition`.
* **Detecção utilizando scikit-image:** realiza uma abordagem semelhante ao exemplo anterior, porém sem utilizar a biblioteca `face_recognition`, utilizando recursos do `scikit-image`.
* **Comparação de imagens:** permite selecionar uma imagem e verificar se a pessoa presente nela corresponde a alguma das imagens de referência utilizadas pelo programa.

Os exemplos de reconhecimento e detecção com imagens foram desenvolvidos utilizando **Jupyter Notebooks**, enquanto outros exemplos foram implementados diretamente em scripts Python.

### 🧠 FaceMesh

Projeto de **detecção de pontos faciais (Face Mesh)** utilizando a webcam.

A aplicação identifica a face e apresenta diversos pontos de referência sobre o rosto, permitindo visualizar as características faciais de maneira semelhante aos sistemas de rastreamento facial utilizados em aplicações de Visão Computacional e realidade aumentada.

### ✋ Hand Tracking

Projeto de **detecção e rastreamento de mãos** utilizando a webcam.

A aplicação identifica a mão e verifica a quantidade de dedos levantados. A quantidade de dedos detectada pode ser utilizada para executar diferentes ações no computador, como **abrir arquivos ou programas**.

O projeto demonstra uma forma de utilizar **gestos como mecanismo de interação com o computador**.

## Tecnologias utilizadas

Os projetos foram desenvolvidos utilizando diferentes bibliotecas e ferramentas do ecossistema Python:

* **Python**
* **Jupyter Notebook**
* **OpenCV**
* **dlib 19.22**
* **face_recognition**
* **scikit-image**
* **MediaPipe**
* **NumPy**

As bibliotecas utilizadas podem variar de acordo com cada projeto.

## Ambiente

Os projetos foram desenvolvidos utilizando **Python 3.10**.

Nos projetos que utilizam `dlib`, foi utilizada a versão:

```text
dlib 19.22
```

## Instalação

Após clonar o repositório, recomenda-se criar um ambiente virtual:

```bash
python -m venv .env
```

No Windows PowerShell, ative o ambiente:

```powershell
.\.env\Scripts\Activate.ps1
```

Depois, instale as dependências:

```bash
python -m pip install -r requirements.txt
```

## Execução

Os exemplos desenvolvidos como scripts Python podem ser executados utilizando:

```bash
python nome_do_arquivo.py
```

Para executar os exemplos desenvolvidos em Jupyter Notebook, abra os arquivos `.ipynb` utilizando **Jupyter Notebook**, **JupyterLab** ou **Visual Studio Code**.

Uma das opções para iniciar o Jupyter Notebook é:

```bash
jupyter notebook
```

## Objetivo

Os projetos foram desenvolvidos durante o curso de **Inteligência Artificial Aplicada em Python**, com o objetivo de explorar, de forma prática, conceitos relacionados à **Visão Computacional e Inteligência Artificial**.

Entre os conceitos explorados estão:

* Detecção de faces;
* Reconhecimento facial;
* Comparação de imagens;
* Detecção de características faciais;
* Rastreamento de mãos;
* Reconhecimento de gestos;
* Utilização da webcam como entrada;
* Automação de ações no computador a partir de gestos.

## Observações

Os projetos possuem finalidade **educacional e experimental**, servindo como exercícios práticos desenvolvidos durante o curso.

As bibliotecas de terceiros utilizadas possuem suas próprias licenças e condições de uso, que devem ser respeitadas conforme os respectivos projetos.

---

**Projeto de aula — Curso de Inteligência Artificial Aplicada em Python**
