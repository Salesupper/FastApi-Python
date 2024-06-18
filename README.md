FastApi-Python

    Este projeto adiciona produtos e os lista na fastapi

Requisitos

    Python 3.11 ou superior
    Pip (gerenciador de pacotes do Python)
    Git (opcional, para clonar o repositório)

Passo a Passo para Configuração
1. Clonar o Repositório (opcional)

Se você tiver um repositório Git, clone-o usando o comando abaixo:

    git clone https://github.com/Salesupper/FastApi-Python.git
    cd FastApi-Python

2. Criar e Ativar um Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto.

    python -m venv venv

Ative o ambiente virtual:

No Windows (Prompt de Comando):
    
    venv\Scripts\activate

No Windows (PowerShell):

    .\venv\Scripts\Activate

3. Instalar Dependências

Instale as dependências necessárias usando o pip. Se você tiver um arquivo requirements.txt no seu projeto, use:

    pip install -r requirements.txt

API 

Para subir a API, execute: 

    ./dev.bat

    e acesse: http://127.0.0.1:8000/docs

Desativar o Ambiente Virtual

Para desativar o ambiente virtual, use:

    deactivate
