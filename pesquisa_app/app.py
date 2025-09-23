import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import json
import os

# Importa as perguntas do arquivo de configuração
from perguntas_config import PERGUNTAS

# Configurações da página
st.set_page_config(
    page_title="Pesquisa de Clima - IN Junior",
    page_icon=":wolf:",
    layout="wide",
    menu_items={
        'Get Help': 'https://injunior.com.br/',
    }
)

# --- Funções de salvamento e carregamento (sem alterações) ---
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

# --- Função do Dashboard de Resultados (sem alterações) ---
def mostrar_resultados(df):
    """Mostra visualizações dos resultados"""
    if df.empty:
        st.warning("Ainda não há respostas para análise.")
        return

    st.header("📊 Resultados da Pesquisa")

    colunas_slider = []
    for secao_id, secao_conteudo in PERGUNTAS.items():
        for campo_id, config in secao_conteudo['campos'].items():
            if config['tipo'] == 'slider':
                colunas_slider.append(f"{secao_id}.{campo_id}")

    colunas_existentes_para_media = [col for col in colunas_slider if col in df.columns]
    
    media_geral = 0
    if colunas_existentes_para_media and not df[colunas_existentes_para_media].empty:
        media_geral = df[colunas_existentes_para_media].mean(axis=1).mean()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total de Respostas", len(df))
    with col2:
        st.metric("Média Geral de Satisfação", f"{media_geral:.2f}/5")

    if 'informacoes_pessoais.diretoria' in df.columns:
        st.subheader("Distribuição por Diretoria")
        areas_count = df['informacoes_pessoais.diretoria'].value_counts()
        fig_dir = go.Figure(data=[go.Bar(x=areas_count.index, y=areas_count.values)])
        fig_dir.update_layout(title="Número de Respostas por Diretoria", xaxis_title="Diretoria", yaxis_title="Número de Respostas")
        st.plotly_chart(fig_dir, use_container_width=True)
    
    st.subheader("Médias de Satisfação por Categoria")
    medias_por_secao = {}
    for secao_id, secao_conteudo in PERGUNTAS.items():
        titulo_secao = secao_conteudo['titulo']
        colunas_da_secao = [
            f"{secao_id}.{campo_id}" 
            for campo_id, config in secao_conteudo['campos'].items() 
            if config['tipo'] == 'slider' and f"{secao_id}.{campo_id}" in df.columns
        ]
        if colunas_da_secao:
            media_secao = df[colunas_da_secao].stack().mean()
            medias_por_secao[titulo_secao] = media_secao

    if medias_por_secao:
        df_medias = pd.DataFrame.from_dict(medias_por_secao, orient='index', columns=['Média']).sort_values(by='Média')
        
        fig_cat = go.Figure(data=[go.Bar(
            x=df_medias['Média'],
            y=df_medias.index,
            orientation='h'
        )])
        
        # ## CORREÇÃO EXATA AQUI ##
        # Trocado 'xlim' por 'xaxis_range'
        fig_cat.update_layout(
            title="Médias de Satisfação por Categoria", 
            xaxis_title="Média (1-5)", 
            yaxis_title="Categoria", 
            height=400, 
            xaxis_range=[1, 5]  # Esta é a linha corrigida
        )
        st.plotly_chart(fig_cat, use_container_width=True)
    else:
        st.info("Aguardando mais respostas para exibir as médias por categoria.")

# --- Função Principal (GRANDES ALTERAÇÕES AQUI) ---
def main():
    st.title(":wolf: Pesquisa de Clima Organizacional - IN Junior")

    tab1, tab2 = st.tabs(["Responder Pesquisa", "Ver Resultados"])

    with tab1:
        # Inicializa o estado da sessão para controlar a etapa e as respostas
        if 'step' not in st.session_state:
            st.session_state.step = 0
        if 'respostas' not in st.session_state:
            st.session_state.respostas = {}

        # Converte as chaves do dicionário em uma lista para navegar pelas etapas
        lista_secoes_id = list(PERGUNTAS.keys())
        secao_id_atual = lista_secoes_id[st.session_state.step]
        conteudo_secao_atual = PERGUNTAS[secao_id_atual]

        st.header(f"Etapa {st.session_state.step + 1}/{len(lista_secoes_id)}: {conteudo_secao_atual['titulo']}")

        if st.session_state.step == 0:
             st.markdown("Para as afirmações a seguir, utilize a escala de 1 a 5, onde **1 significa 'Discordo Totalmente'** e **5 significa 'Concordo Totalmente'**.")

        # Container para as perguntas da etapa atual
        with st.container():
            # Itera e exibe apenas as perguntas da seção/etapa atual
            for campo_id, config in conteudo_secao_atual['campos'].items():
                key = f"{secao_id_atual}.{campo_id}"
                # Recupera o valor salvo se já existir, para não perder ao navegar
                valor_salvo = st.session_state.respostas.get(secao_id_atual, {}).get(campo_id, None)

                resposta = None
                if config['tipo'] == 'text':
                    resposta = st.text_input(config['texto'], key=key, value=valor_salvo)
                elif config['tipo'] == 'selectbox':
                    # Garante que o valor salvo seja válido, ou usa o padrão
                    opcoes = config['opcoes']
                    index = opcoes.index(valor_salvo) if valor_salvo in opcoes else 0
                    resposta = st.selectbox(config['texto'], options=opcoes, key=key, index=index)
                elif config['tipo'] == 'number':
                    resposta = st.number_input(config['texto'], min_value=config.get('min_value'), max_value=config.get('max_value'), key=key, value=valor_salvo, placeholder="Digite um número...")
                elif config['tipo'] == 'slider':
                    resposta = st.slider(config['texto'], min_value=config['min_value'], max_value=config['max_value'], key=key, value=valor_salvo or config['min_value'])
                elif config['tipo'] == 'text_area':
                    resposta = st.text_area(config['texto'], key=key, value=valor_salvo)

                # Salva a resposta no estado da sessão em tempo real
                if secao_id_atual not in st.session_state.respostas:
                    st.session_state.respostas[secao_id_atual] = {}
                st.session_state.respostas[secao_id_atual][campo_id] = resposta

        # Navegação entre as etapas
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            if st.session_state.step > 0:
                if st.button("⬅️ Anterior"):
                    st.session_state.step -= 1
                    st.rerun()

        with col3:
            # Se não for a última etapa, mostra o botão "Próximo"
            if st.session_state.step < len(lista_secoes_id) - 1:
                if st.button("Próximo ➡️"):
                    # Validação da etapa atual antes de avançar
                    erros = []
                    for campo_id, config in conteudo_secao_atual['campos'].items():
                        if config['obrigatorio']:
                            resposta_atual = st.session_state.respostas[secao_id_atual][campo_id]
                            if resposta_atual is None or str(resposta_atual).strip() == "":
                                erros.append(f"O campo '{config['texto']}' é obrigatório.")
                    
                    if erros:
                        for erro in erros:
                            st.error(erro)
                    else:
                        st.session_state.step += 1
                        st.rerun()
            
            # Se for a última etapa, mostra o botão "Enviar"
            else:
                if st.button("✅ Enviar Respostas"):
                    # Validação final (incluindo a última página)
                    erros = []
                    for sid, conteudo in PERGUNTAS.items():
                        for cid, config in conteudo['campos'].items():
                            if config['obrigatorio']:
                                resposta = st.session_state.respostas.get(sid, {}).get(cid)
                                if resposta is None or str(resposta).strip() == "":
                                    erros.append(f"O campo '{config['texto']}' (na etapa '{conteudo['titulo']}') é obrigatório.")
                    
                    if erros:
                        for erro in erros:
                            st.error(erro)
                    else:
                        salvar_resposta(st.session_state.respostas)
                        st.success("Respostas salvas com sucesso! Obrigado pela participação!")
                        st.balloons()
                        # Limpa o estado para um novo preenchimento
                        del st.session_state.step
                        del st.session_state.respostas


    with tab2:
        respostas = carregar_respostas()
        df = criar_dataframe_respostas(respostas)
        mostrar_resultados(df)

if __name__ == "__main__":
    main()