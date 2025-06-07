# HotelPulse - Sistema de Gerenciamento Hoteleiro

HotelPulse é um sistema de gerenciamento hoteleiro de código aberto, projetado para facilitar a administração de hotéis e reservas. Ele suporta múltiplos hotéis, gerenciamento de quartos, reservas e integração com APIs externas.

## Funcionalidades
- Gerenciamento de hotéis (adicionar, listar, editar, excluir).
- Sistema de reservas com pop-up para cadastro de hóspedes.
- Interface moderna com Tailwind CSS e React.
- Backend em Python com Flask e banco de dados SQLite.
- Suporte para integração com APIs de OTAs (ex.: Booking.com) e gateways de pagamento (ex.: Mercado Pago).

## Pré-requisitos
- Node.js (para compilar React, se necessário)
- Python 3.8+ (para o backend)
- Git

## Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/akilessimiao/hotelpulse.git
   cd hotelpulse
   ```
2. Instale as dependências do backend:
   ```bash
   pip install -r requirements.txt
   ```
3. Inicie o backend:
   ```bash
   python src/app.py
   ```
4. Abra o `index.html` no navegador ou hospede no GitHub Pages para o frontend.

## Hospedagem no GitHub Pages
1. Crie um repositório público no GitHub (ex.: `akilessimiao/hotelpulse`).
2. Copie os arquivos da pasta `public` para a branch `gh-pages`.
3. Acesse o site em `https://akilessimiao.github.io/hotelpulse`.

## Configuração para Domínio Próprio
1. Adquira um domínio (ex.: via GoDaddy, Namecheap).
2. Configure um servidor para o backend (ex.: Heroku, Render).
3. Aponte o domínio para o GitHub Pages (frontend) e o backend via DNS (ex.: CNAME para frontend, A record para backend).
4. Configure HTTPS com um certificado SSL (ex.: Let’s Encrypt).

## Integrações Futuras
- **API de OTAs**: Adicione endpoints para sincronizar com Booking.com (consulte a documentação oficial da Booking para Channel Manager).
- **Pagamentos**: Integre Mercado Pago ou Stripe para processar Pix e cartões de crédito.
- **Backup**: Configure exportação de dados para Google Drive ou e-mail usando bibliotecas como `gspread` ou `smtplib`.

## Licença
Distribuído sob a licença MIT. Veja `LICENSE` para mais detalhes.

## Contribuições
Contribuições são bem-vindas! Crie um pull request ou abra uma issue no GitHub.
