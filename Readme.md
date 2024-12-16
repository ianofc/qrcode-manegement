QR Code Management

Uma aplicação gráfica simples desenvolvida em Python com Tkinter para criar QR Codes de forma prática. Insira um link, clique no botão e gere QR Codes que podem ser visualizados diretamente na interface e salvos localmente.



Funcionalidades

Geração rápida de QR Codes a partir de links.

Visualização dos QR Codes diretamente na interface gráfica.

Salva os QR Codes gerados no formato .png para uso posterior.

Interface amigável e minimalista.



Pré-requisitos

Antes de executar o projeto, certifique-se de ter:

Python 3.x instalado.

As bibliotecas necessárias instaladas:

pip install pyqrcode pillow




Como usar

1. Clone o repositório:

git clone https://github.com/seuusuario/qrcode-management.git


2. Navegue até o diretório do projeto:

cd qrcode-management


3. Execute o script principal:

python app.py


4. Insira o link no campo de texto e clique em "Generate QR Code". O QR Code será exibido na interface e salvo como qrcode.png no diretório do projeto.




Tecnologias utilizadas

Python: Linguagem principal.

Tkinter: Para criar a interface gráfica.

pyqrcode: Para gerar QR Codes.

Pillow: Para manipulação e exibição de imagens.




Estrutura do Projeto

app.py: Código principal da aplicação.

qrcode.png: Arquivo gerado ao criar um QR Code.




Melhorias Futuras

Suporte para personalização do QR Code (cores, tamanhos, logotipos).

Inclusão de uma opção para salvar os QR Codes em diretórios personalizados.

Geração de múltiplos QR Codes em lote.

Integração com bancos de dados para gerenciar e armazenar QR Codes.




Contribuições

Contribuições são bem-vindas! Se tiver sugestões ou melhorias, abra uma issue ou envie um pull request.


