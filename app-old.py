import streamlit as st
import requests
import pandas as pd
import plotly.express as px

print("INICIANDO O PAINEL DE PREÇOS - COMPRAS PÚBLICAS (API ARP)")

def plot_price_trend(df, descricao_item):
    df['dataVigenciaInicio'] = pd.to_datetime(df['dataVigenciaInicio'])
    df = df.sort_values('dataVigenciaInicio')

    fig = px.line(
        df,
        x='dataVigenciaInicio',
        y='valorUnitario',
        markers=True,
        labels={
            'dataVigenciaInicio': 'Data de Vigência',
            'valorUnitario': 'Valor Unitário (R$)'
        },
        title=f'Evolução dos Preços - {descricao_item}',
        template='plotly_white'
    )

    fig.update_traces(line_color='blue', marker=dict(size=6, color='blue'))
    fig.update_yaxes(tickprefix='R$ ', showgrid=True)
    fig.update_layout(
        title_font_size=20,
        title_x=0.5,
        hovermode='x unified',
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True)
    )

    return fig

st.set_page_config(page_title="Dashboard ComprasGov", layout="wide")

st.title("🔍 Painel de Preços - Compras Públicas (API ARP)")

# Entradas do usuário
codigo_item = st.text_input("Informe o código do item CATMAT:", "27138")
data_inicio = st.date_input("Data de início da vigência:", pd.to_datetime("2025-01-01"))
data_fim = st.date_input("Data de fim da vigência:", pd.to_datetime("2025-04-30"))

if st.button("Consultar Dados do Produto/Serviço"):
    # url = "https://dadosabertos.compras.gov.br/modulo-arp/2_consultarARPItem"
    url = "https://dadosabertos.compras.gov.br/modulo-arp/2_consultarARPItem?pagina=1&tamanhoPagina=10&dataVigenciaInicial=2025-01-01&dataVigenciaFinal=2025-04-30&codigoItem=27138"
    params = {
        "pagina": 1,
        "tamanhoPagina": 10,
        "dataVigenciaInicial": data_inicio.strftime("%Y-%m-%d"),
        "dataVigenciaFinal": data_fim.strftime("%Y-%m-%d"),
        "codigoItem": codigo_item
    }

    with st.spinner("Consultando dados..."):
        # resposta = requests.get(url, params=params)
        resposta = requests.get(url)
        print(f"Resposta da API: {resposta.status_code}")
        dados_json = resposta.json().get("resultado", [])
        print(f"Dados retornados: {dados_json}")
        if resposta.status_code == 200:
            dados_json = resposta.json().get("resultado", [])
            print(f"Dados retornados: {dados_json}")
            if dados_json:
                df = pd.DataFrame(dados_json)
                df["dataVigenciaInicial"] = pd.to_datetime(df["dataVigenciaInicial"])
                df["valorUnitario"] = pd.to_numeric(df["valorUnitario"], errors='coerce')

                st.success(f"{len(df)} registros encontrados.")

                # Gráfico de preços
                # fig = px.box(
                #     df,
                #     x=df["dataVigenciaInicial"].dt.to_period("M").astype(str),
                #     y="valorUnitario",
                #     title="📈 Preços por Mês de Vigência",
                #     labels={"x": "Mês", "valorUnitario": "Valor Unitário (R$)"}
                # )
                
                fig = plot_price_trend(df, df["descricaoItem"])
                
                st.plotly_chart(fig, use_container_width=True)

                # Tabela de dados
                st.dataframe(df[[
                    "descricaoItem", "valorUnitario", "nomeRazaoSocialFornecedor", 
                    "nomeUnidadeGerenciadora", "nomeModalidadeCompra", "dataVigenciaInicial", "dataVigenciaFinal"
                ]])

                # Exportar CSV
                csv = df.to_csv(index=False)
                st.download_button("📥 Baixar resultados em CSV", csv, "resultado.csv")
            else:
                st.warning("Nenhum dado retornado para os filtros informados.")
        else:
            st.error(f"Erro ao acessar a API: {resposta.status_code}")
