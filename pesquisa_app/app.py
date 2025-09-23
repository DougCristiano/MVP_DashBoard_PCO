import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import json
import os

from perguntas_config import PERGUNTAS

# Configurações da página. Ou seja, o título da página que irá aparecer na aba do navegador e se vai ser centralizado ou ocupar a tela toda (wide).
# Para saber mais, veja aqui no link: https://docs.streamlit.io/develop/api-reference/configuration/st.set_page_config Douglas aqui, não foi IA nenhuma kkkkk
st.set_page_config(
    page_title="Pesquisa de Clima - IN Junior",
    page_icon=":wolf:",
    layout="wide",
    menu_items={
        'Get Help': 'https://injunior.com.br/',}
)

# ## ALTERAÇÃO AQUI: Função 'salvar_resposta' foi modificada ##
def salvar_resposta(respostas):
    """Salva as respostas em um arquivo JSON e anexa a um arquivo CSV."""
    timestamp = datetime.now()
    respostas['timestamp'] = timestamp.isoformat()
    
    os.makedirs('respostas', exist_ok=True)

    # 1. Salvar em arquivo JSON individual
    arquivo_json = f"respostas/resposta_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
    with open(arquivo_json, 'w', encoding='utf-8') as f:
        json.dump(respostas, f, ensure_ascii=False, indent=4)

    # 2. Salvar/Anexar em um arquivo CSV consolidado
    try:
        df_resposta = pd.json_normalize(respostas)
        arquivo_csv = 'respostas/respostas_consolidadas.csv'
        escrever_cabecalho = not os.path.exists(arquivo_csv)
        df_resposta.to_csv(
            arquivo_csv, 
            mode='a', 
            header=escrever_cabecalho, 
            index=False, 
            encoding='utf-8-sig'
        )
    except Exception as e:
        st.error(f"Ocorreu um erro ao salvar o arquivo CSV: {e}")

def carregar_respostas():
    """Carrega todas as respostas dos arquivos JSON (para o dashboard)"""
    respostas = []
    if os.path.exists('respostas'):
        for arquivo in sorted(os.listdir('respostas')):
            if arquivo.endswith('.json'):
                with open(f'respostas/{arquivo}', 'r', encoding='utf-8') as f:
                    respostas.append(json.load(f))
    return respostas

def criar_dataframe_respostas(respostas):
    """Converte a lista de respostas em um DataFrame"""
    if not respostas:
        return pd.DataFrame()
    df = pd.json_normalize(respostas)
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def mostrar_resultados(df):
    """Mostra visualizações dos resultados"""
    if df.empty:
        st.warning("Ainda não há respostas para análise.")
        return

    st.header("📊 Resultados da Pesquisa")

    # Filtra colunas que são do tipo slider para os cálculos de média
    colunas_slider = []
    for secao in PERGUNTAS.values():
        for campo_id, config in secao['campos'].items():
            if config['tipo'] == 'slider':
                # Constrói o nome da coluna como o pandas.json_normalize faz
                colunas_slider.append(f"{secao['titulo'].lower().replace(' ', '_')}.{campo_id}")

    # Garante que as colunas existem no DataFrame antes de calcular a média
    colunas_existentes_para_media = [col for col in colunas_slider if col in df.columns]
    
    # Média geral de todas as respostas de slider
    media_geral = df[colunas_existentes_para_media].mean(axis=1).mean()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total de Respostas", len(df))
    with col2:
        st.metric("Média Geral de Satisfação", f"{media_geral:.2f}/5")

    st.subheader("Distribuição por Diretoria")
    # Acessa a coluna de diretoria com a nova chave
    areas_count = df['informacoes_pessoais.diretoria'].value_counts()
    fig = go.Figure(data=[go.Bar(x=areas_count.index, y=areas_count.values)])
    fig.update_layout(title="Número de Respostas por Diretoria", xaxis_title="Diretoria", yaxis_title="Número de Respostas")
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Médias de Satisfação por Categoria")
    # Agrupa as colunas por seção (título) e calcula a média para cada seção
    medias_por_secao = {}
    for secao_id, secao_conteudo in PERGUNTAS.items():
        titulo_secao = secao_conteudo['titulo']
        colunas_da_secao = [
            f"{secao_id}.{campo_id}" 
            for campo_id, config in secao_conteudo['campos'].items() 
            if config['tipo'] == 'slider' and f"{secao_id}.{campo_id}" in df.columns
        ]
        if colunas_da_secao:
            # Calcula a média de todas as respostas para as perguntas da seção
            media_secao = df[colunas_da_secao].stack().mean()
            medias_por_secao[titulo_secao] = media_secao

    # Cria um DataFrame com as médias para facilitar a plotagem
    df_medias = pd.DataFrame.from_dict(medias_por_secao, orient='index', columns=['Média']).sort_values(by='Média')

    fig = go.Figure(data=[go.Bar(
        x=df_medias['Média'],
        y=df_medias.index,
        orientation='h'
    )])
    fig.update_layout(title="Médias de Satisfação por Categoria", xaxis_title="Média (1-5)", yaxis_title="Categoria", height=400, xlim=[1, 5])
    st.plotly_chart(fig, use_container_width=True)


def main():
    st.title(":wolf: Pesquisa de Clima Organizacional - IN Junior")

    tab1, tab2 = st.tabs(["Responder Pesquisa", "Ver Resultados"])

    with tab1:
        st.header("🗣️ Sua opinião é importante!")
        st.markdown("Para as afirmações a seguir, utilize a escala de 1 a 5, onde **1 significa 'Discordo Totalmente'** e **5 significa 'Concordo Totalmente'**.")

        with st.form("formulario_pesquisa"):
            respostas_form = {}
            # Itera sobre os IDs das seções para usar como chave
            for secao_id, conteudo in PERGUNTAS.items():
                st.subheader(conteudo['titulo'])
                respostas_form[secao_id] = {}
                for campo_id, config in conteudo['campos'].items():
                    key = f"{secao_id}.{campo_id}"
                    if config['tipo'] == 'text':
                        respostas_form[secao_id][campo_id] = st.text_input(config['texto'], key=key)
                    elif config['tipo'] == 'selectbox':
                        respostas_form[secao_id][campo_id] = st.selectbox(config['texto'], options=config['opcoes'], key=key)
                    elif config['tipo'] == 'number':
                        respostas_form[secao_id][campo_id] = st.number_input(config['texto'], min_value=config.get('min_value'), max_value=config.get('max_value'), key=key, value=None, placeholder="Digite um número...")
                    elif config['tipo'] == 'slider':
                        respostas_form[secao_id][campo_id] = st.slider(config['texto'], min_value=config['min_value'], max_value=config['max_value'], key=key)
                    elif config['tipo'] == 'text_area':
                        respostas_form[secao_id][campo_id] = st.text_area(config['texto'], key=key)
            
            submitted = st.form_submit_button("Enviar Respostas")
            
            if submitted:
                erros = []
                for secao_id, conteudo in PERGUNTAS.items():
                    for campo_id, config in conteudo['campos'].items():
                        if config['obrigatorio']:
                            resposta = respostas_form[secao_id][campo_id]
                            if resposta is None or str(resposta).strip() == "":
                                erros.append(f"O campo '{config['texto']}' é obrigatório.")

                if erros:
                    for erro in erros:
                        st.error(erro)
                else:
                    salvar_resposta(respostas_form)
                    st.success("Respostas salvas com sucesso! Obrigado pela participação!")
                    st.balloons()

    with tab2:
        respostas = carregar_respostas()
        df = criar_dataframe_respostas(respostas)
        mostrar_resultados(df)

if __name__ == "__main__":
    main()
