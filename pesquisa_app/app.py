import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
import json
import os

# Configurações da página
st.set_page_config(
    page_title="Pesquisa de Clima - IN Junior",
    page_icon="🐺",
    layout="wide"
)

# Estrutura das perguntas da pesquisa (sem alterações)
PERGUNTAS = {
    "dados_pessoais": {
        "titulo": "Dados Pessoais",
        "campos": {
            "nome": {
                "texto": "Qual é o seu nome?",
                "tipo": "text",
                "obrigatorio": True
            },
            "area": {
                "texto": "Em qual área você atua?",
                "tipo": "selectbox",
                "opcoes": ["", "Presidência", "Projetos", "Comercial", "Marketing", "Gestão de Pessoas", "Administrativo-Financeiro"],
                "obrigatorio": True
            },
            "tempo_empresa": {
                "texto": "Há quanto tempo você está na empresa? (em meses)",
                "tipo": "number",
                "min_value": 0,
                "obrigatorio": True
            }
        }
    },
    "satisfacao": {
        "titulo": "Satisfação Geral",
        "campos": {
            "satisfacao_geral": {
                "texto": "Qual seu nível de satisfação geral com a empresa?",
                "tipo": "slider",
                "min_value": 1,
                "max_value": 5,
                "obrigatorio": True
            },
            "satisfacao_area": {
                "texto": "Qual seu nível de satisfação com sua área?",
                "tipo": "slider",
                "min_value": 1,
                "max_value": 5,
                "obrigatorio": True
            },
            "satisfacao_lideranca": {
                "texto": "Qual seu nível de satisfação com a liderança?",
                "tipo": "slider",
                "min_value": 1,
                "max_value": 5,
                "obrigatorio": True
            }
        }
    },
    "ambiente": {
        "titulo": "Ambiente de Trabalho",
        "campos": {
            "clima_organizacional": {
                "texto": "Como você avalia o clima organizacional?",
                "tipo": "slider",
                "min_value": 1,
                "max_value": 5,
                "obrigatorio": True
            },
            "comunicacao": {
                "texto": "Como você avalia a comunicação na empresa?",
                "tipo": "slider",
                "min_value": 1,
                "max_value": 5,
                "obrigatorio": True
            },
            "trabalho_equipe": {
                "texto": "Como você avalia o trabalho em equipe?",
                "tipo": "slider",
                "min_value": 1,
                "max_value": 5,
                "obrigatorio": True
            }
        }
    },
    "desenvolvimento": {
        "titulo": "Desenvolvimento Profissional",
        "campos": {
            "oportunidades_crescimento": {
                "texto": "Como você avalia as oportunidades de crescimento?",
                "tipo": "slider",
                "min_value": 1,
                "max_value": 5,
                "obrigatorio": True
            },
            "capacitacao": {
                "texto": "Como você avalia as capacitações oferecidas?",
                "tipo": "slider",
                "min_value": 1,
                "max_value": 5,
                "obrigatorio": True
            },
            "feedback": {
                "texto": "Como você avalia o processo de feedback?",
                "tipo": "slider",
                "min_value": 1,
                "max_value": 5,
                "obrigatorio": True
            }
        }
    },
    "horas_dedicadas": {
        "titulo": "Dedicação de Tempo",
        "campos": {
            "horas_semanais": {
                "texto": "Quantas horas em média você dedica por semana?",
                "tipo": "number",
                "min_value": 0,
                "max_value": 40,
                "obrigatorio": True
            },
            "horas_capacitacao": {
                "texto": "Quantas horas você dedica para capacitação por semana?",
                "tipo": "number",
                "min_value": 0,
                "max_value": 20,
                "obrigatorio": True
            }
        }
    },
    "feedback_aberto": {
        "titulo": "Feedback Aberto",
        "campos": {
            "pontos_positivos": {
                "texto": "Quais os principais pontos positivos que você destacaria?",
                "tipo": "text_area",
                "obrigatorio": False
            },
            "pontos_melhoria": {
                "texto": "Quais pontos você acha que podem ser melhorados?",
                "tipo": "text_area",
                "obrigatorio": False
            },
            "sugestoes": {
                "texto": "Você tem alguma sugestão específica?",
                "tipo": "text_area",
                "obrigatorio": False
            }
        }
    }
}

# ## ALTERAÇÃO AQUI: Função 'salvar_resposta' foi modificada ##
def salvar_resposta(respostas):
    """Salva as respostas em um arquivo JSON e anexa a um arquivo CSV."""
    timestamp = datetime.now()
    respostas['timestamp'] = timestamp.isoformat()
    
    # Garante que o diretório de respostas exista
    os.makedirs('respostas', exist_ok=True)

    # 1. Salvar em arquivo JSON individual (comportamento original)
    arquivo_json = f"respostas/resposta_{timestamp.strftime('%Y%m%d_%H%M%S')}.json"
    with open(arquivo_json, 'w', encoding='utf-8') as f:
        json.dump(respostas, f, ensure_ascii=False, indent=4)

    # 2. Salvar/Anexar em um arquivo CSV consolidado (nova funcionalidade)
    try:
        # Normaliza (achata) o dicionário de respostas para que ele possa ser salvo no formato de tabela
        df_resposta = pd.json_normalize(respostas)
        
        arquivo_csv = 'respostas/respostas_consolidadas.csv'
        
        # Verifica se o arquivo CSV já existe para decidir se o cabeçalho deve ser escrito
        escrever_cabecalho = not os.path.exists(arquivo_csv)
        
        # Anexa a nova resposta ao arquivo CSV
        # mode='a' significa 'append' (anexar)
        # encoding='utf-8-sig' é recomendado para compatibilidade com Excel
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
        # Ordena os arquivos para garantir a ordem cronológica na análise temporal
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

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Respostas", len(df))
    with col2:
        media_satisfacao = df['satisfacao.satisfacao_geral'].mean()
        st.metric("Média de Satisfação Geral", f"{media_satisfacao:.2f}/5")
    with col3:
        media_clima = df['ambiente.clima_organizacional'].mean()
        st.metric("Média do Clima Organizacional", f"{media_clima:.2f}/5")

    st.subheader("Distribuição por Área")
    areas_count = df['dados_pessoais.area'].value_counts()
    fig = go.Figure(data=[go.Bar(x=areas_count.index, y=areas_count.values)])
    fig.update_layout(title="Número de Respostas por Área", xaxis_title="Área", yaxis_title="Número de Respostas")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Médias de Satisfação")
    colunas_satisfacao = [col for col in df.columns if col.startswith(('satisfacao.', 'ambiente.', 'desenvolvimento.'))]
    medias = df[colunas_satisfacao].mean().sort_values(ascending=True)
    fig = go.Figure(data=[go.Bar(
        x=medias.values,
        y=[col.split('.')[-1].replace('_', ' ').title() for col in medias.index],
        orientation='h'
    )])
    fig.update_layout(title="Médias de Satisfação por Categoria", xaxis_title="Média (1-5)", yaxis_title="Categoria", height=400)
    st.plotly_chart(fig, use_container_width=True)

    if len(df) > 1:
        st.subheader("Análise Temporal")
        df_temporal = df.set_index('timestamp').sort_index()
        metricas_tempo = ['satisfacao.satisfacao_geral', 'ambiente.clima_organizacional']
        for metrica in metricas_tempo:
            media_movel = df_temporal[metrica].rolling('7D').mean()
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df_temporal.index, y=df_temporal[metrica], mode='markers', name='Respostas Individuais'))
            fig.add_trace(go.Scatter(x=media_movel.index, y=media_movel.values, mode='lines', name='Média Móvel (7 dias)', line=dict(width=3)))
            fig.update_layout(title=f"Evolução - {metrica.split('.')[-1].replace('_', ' ').title()}", xaxis_title="Data", yaxis_title="Valor (1-5)")
            st.plotly_chart(fig, use_container_width=True)

def main():
    st.title("🐺 Pesquisa de Clima Organizacional - IN Junior")

    tab1, tab2 = st.tabs(["Responder Pesquisa", "Ver Resultados"])

    with tab1:
        st.header("🗣️ Sua opinião é importante!")

        with st.form("formulario_pesquisa"):
            respostas_form = {}
            for secao, conteudo in PERGUNTAS.items():
                st.subheader(conteudo['titulo'])
                respostas_form[secao] = {}
                for campo, config in conteudo['campos'].items():
                    if config['tipo'] == 'text':
                        respostas_form[secao][campo] = st.text_input(config['texto'], key=f"{secao}.{campo}")
                    elif config['tipo'] == 'selectbox':
                        respostas_form[secao][campo] = st.selectbox(config['texto'], options=config['opcoes'], key=f"{secao}.{campo}")
                    elif config['tipo'] == 'number':
                        respostas_form[secao][campo] = st.number_input(config['texto'], min_value=config.get('min_value'), max_value=config.get('max_value'), key=f"{secao}.{campo}", value=None, placeholder="Digite um número...")
                    elif config['tipo'] == 'slider':
                        respostas_form[secao][campo] = st.slider(config['texto'], min_value=config['min_value'], max_value=config['max_value'], key=f"{secao}.{campo}")
                    elif config['tipo'] == 'text_area':
                        respostas_form[secao][campo] = st.text_area(config['texto'], key=f"{secao}.{campo}")
            
            submitted = st.form_submit_button("Enviar Respostas")
            
            if submitted:
                erros = []
                for secao, conteudo in PERGUNTAS.items():
                    for campo, config in conteudo['campos'].items():
                        if config['obrigatorio']:
                            resposta = respostas_form[secao][campo]
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