
# 📊 Dashboard de Preços - Compras Públicas (API ComprasGov)

Este projeto é um dashboard em Streamlit que consulta preços públicos a partir da API do ComprasGov (modulo-arp), permitindo buscar por código de item CATMAT e analisar a variação de preços ao longo do tempo.

## 🔧 Tecnologias
- Python
- Streamlit
- Plotly
- Docker

---

## ▶️ Execução local com Docker

```bash
git clone https://github.com/SEU_USUARIO/dashboard-comprasgov.git
cd dashboard-comprasgov

# Execute a aplicação
docker-compose up --build
```

Acesse em: [http://localhost:8501](http://localhost:8501)

---

## 🚀 Deploy gratuito no Railway

### 1. Crie uma conta
Acesse [https://railway.app](https://railway.app) e faça login com GitHub.

### 2. Crie um novo projeto
- Clique em **"New Project"**
- Escolha **"Deploy from GitHub Repo"**
- Selecione o repositório `dashboard-comprasgov`

### 3. Deploy com Docker
- O Railway detectará o `Dockerfile`
- Clique em **"Deploy Now"**
- A aplicação será publicada em uma URL como:
  ```
  https://dashboard-comprasgov.up.railway.app
  ```

---

## 📥 API usada

[ComprasGov - API módulo ARP](https://dadosabertos.compras.gov.br/modulo-arp/2_consultarARPItem)

Exemplo de uso:

```
https://dadosabertos.compras.gov.br/modulo-arp/2_consultarARPItem?pagina=1&tamanhoPagina=10&dataVigenciaInicial=2025-01-01&dataVigenciaFinal=2025-04-30&codigoItem=27138
```

---

## 📄 Licença

Projeto público e gratuito para fins de transparência e pesquisa de preços em contratações públicas.

---

Criado por [Seu Nome] ✨
