import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configuração da página
st.set_page_config(
    page_title="Dashboard - Análise IN Junior",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

class INJuniorSurveyAnalyzer:
    """Classe para análise dos dados da pesquisa de satisfação da IN Junior"""
    
    def __init__(self, df):
        """
        Inicializa o analisador com um DataFrame
        
        Args:
            df (DataFrame): DataFrame com os dados da pesquisa
        """
        self.df = df.copy()
        self.df_processed = None
        self._clean_and_process_data()
        
    def _clean_and_process_data(self):
        """Limpa e processa os dados iniciais"""
        self.df_processed = self.df.copy()
        
        # Remove linhas completamente vazias
        self.df_processed = self.df_processed.dropna(how='all')
        
        # Converte colunas numéricas (escalas de 1-5, 1-5, etc.)
        numeric_columns = [
            'O quão organizada você considera a DE?',
            'O quão acessível é o seu/sua diretor(a)?',
            'Quão bem os integrantes de sua diretoria se comunicam entre si?',
            'Quanto você se relaciona com membros de outras diretorias?',
            'O quão satisfatória é a delegação de tarefas na sua diretoria?',
            'O quão você se sente preparado para realizar as suas tarefas de diretoria?',
            'Quão bem os integrantes da sua diretoria compartilham as responsabilidades pelas tarefas?',
            'Quantas horas por semana você gasta com tarefas de diretoria?',
            'O quanto você se sente preparado(a) para conceder feedback para os membros da sua equipe?',
            'O quanto você concede feedback para os membros da sua equipe?',
            'Com que frequência seu/sua diretor(a) ouve seus assessores para tomar decisões?',
            'Com que frequência você recebe feedback de seu/sua diretor(a)?',
            'De forma geral, o quanto você está satisfeito(a) com seu/sua gerente?',
            'Quantos projetos você está realizando na IN Junior atualmente?',
            'Quantas horas semanalmente você gasta com tarefas de projeto?',
            'O quão satisfeito(a) você está com a atuação da sua equipe no(s) projeto(s) que você participa?',
            'O quão satisfeito(a) você está com o seu desempenho nas tarefas de projeto?',
            'O quanto você acha os plantões relevantes para a realização de um projeto?',
            'Quão organizada é a nossa salinha?',
            'O quanto você acha importante participar dos eventos da empresa? (RG\'s, reuniões, p{IN}zza...)',
            'O quanto você se sente ouvido(a) dentro da empresa?',
            'O quão satisfeito(a) você está com a IN Junior?',
            'Qual a carga horária diária do seu estágio/trabalho?'
        ]
        
        # Converte para numérico, colocando NaN para valores inválidos
        for col in numeric_columns:
            if col in self.df_processed.columns:
                self.df_processed[col] = pd.to_numeric(self.df_processed[col], errors='coerce')
    
    def calculate_satisfaction_metrics(self):
        """Calcula métricas de satisfação geral"""
        metrics = {}
        
        satisfaction_col = 'O quão satisfeito(a) você está com a IN Junior?'
        if satisfaction_col in self.df_processed.columns:
            valid_responses = self.df_processed[satisfaction_col].dropna()
            if len(valid_responses) > 0:
                metrics['satisfacao_geral'] = {
                    'media': round(valid_responses.mean(), 2),
                    'mediana': round(valid_responses.median(), 2),
                    'desvio_padrao': round(valid_responses.std(), 2),
                    'n_respostas': len(valid_responses),
                    'percentil_75': round(valid_responses.quantile(0.75), 2),
                    'percentil_25': round(valid_responses.quantile(0.25), 2),
                    'data': valid_responses
                }
        
        return metrics
    
    def analyze_organizational_structure(self):
        """Analisa métricas relacionadas à estrutura organizacional"""
        metrics = {}
        
        org_metrics = {
            'organizacao_de': 'O quão organizada você considera a DE?',
            'acessibilidade_diretor': 'O quão acessível é o seu/sua diretor(a)?',
            'comunicacao_interna': 'Quão bem os integrantes de sua diretoria se comunicam entre si?'
        }
        
        for key, col in org_metrics.items():
            if col in self.df_processed.columns:
                valid_responses = self.df_processed[col].dropna()
                if len(valid_responses) > 0:
                    metrics[key] = {
                        'media': round(valid_responses.mean(), 2),
                        'desvio_padrao': round(valid_responses.std(), 2),
                        'n_respostas': len(valid_responses),
                        'data': valid_responses
                    }
        
        return metrics
    
    def analyze_workload_distribution(self):
        """Analisa distribuição de carga de trabalho"""
        metrics = {}
        
        workload_metrics = {
            'horas_semanais_diretoria': 'Quantas horas por semana você gasta com tarefas de diretoria?',
            'horas_semanais_projeto': 'Quantas horas semanalmente você gasta com tarefas de projeto?',
            'projetos_simultaneos': 'Quantos projetos você está realizando na IN Junior atualmente?'
        }
        
        for key, col in workload_metrics.items():
            if col in self.df_processed.columns:
                valid_responses = self.df_processed[col].dropna()
                if len(valid_responses) > 0:
                    metrics[key] = {
                        'media': round(valid_responses.mean(), 2),
                        'mediana': round(valid_responses.median(), 2),
                        'desvio_padrao': round(valid_responses.std(), 2),
                        'maximo': valid_responses.max(),
                        'minimo': valid_responses.min(),
                        'n_respostas': len(valid_responses),
                        'data': valid_responses
                    }
        
        return metrics
    
    def analyze_feedback_culture(self):
        """Analisa a cultura de feedback na empresa"""
        metrics = {}
        
        feedback_metrics = {
            'preparacao_feedback': 'O quanto você se sente preparado(a) para conceder feedback para os membros da sua equipe?',
            'frequencia_feedback_dado': 'O quanto você concede feedback para os membros da sua equipe?',
            'frequencia_feedback_recebido': 'Com que frequência você recebe feedback de seu/sua diretor(a)?'
        }
        
        for key, col in feedback_metrics.items():
            if col in self.df_processed.columns:
                valid_responses = self.df_processed[col].dropna()
                if len(valid_responses) > 0:
                    metrics[key] = {
                        'media': round(valid_responses.mean(), 2),
                        'desvio_padrao': round(valid_responses.std(), 2),
                        'n_respostas': len(valid_responses),
                        'data': valid_responses
                    }
        
        return metrics
    
    def analyze_engagement_metrics(self):
        """Analisa métricas de engajamento"""
        metrics = {}
        
        engagement_metrics = {
            'importancia_eventos': 'O quanto você acha importante participar dos eventos da empresa? (RG\'s, reuniões, p{IN}zza...)',
            'sentimento_ouvido': 'O quanto você se sente ouvido(a) dentro da empresa?'
        }
        
        for key, col in engagement_metrics.items():
            if col in self.df_processed.columns:
                valid_responses = self.df_processed[col].dropna()
                if len(valid_responses) > 0:
                    metrics[key] = {
                        'media': round(valid_responses.mean(), 2),
                        'desvio_padrao': round(valid_responses.std(), 2),
                        'n_respostas': len(valid_responses),
                        'data': valid_responses
                    }
        
        return metrics
    
    def generate_summary_report(self):
        """Gera relatório resumo com todas as métricas"""
        report = {
            'info_geral': {
                'total_respostas': len(self.df_processed),
                'colunas_analisadas': len(self.df_processed.columns)
            },
            'satisfacao': self.calculate_satisfaction_metrics(),
            'estrutura_organizacional': self.analyze_organizational_structure(),
            'carga_trabalho': self.analyze_workload_distribution(),
            'cultura_feedback': self.analyze_feedback_culture(),
            'engajamento': self.analyze_engagement_metrics()
        }
        
        return report

def create_satisfaction_charts(analyzer):
    """Cria gráficos de satisfação usando Plotly"""
    satisfaction_data = analyzer.calculate_satisfaction_metrics()
    
    if 'satisfacao_geral' in satisfaction_data:
        data = satisfaction_data['satisfacao_geral']['data']
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Histograma
            fig_hist = px.histogram(
                x=data, 
                nbins=5,
                title="Distribuição da Satisfação Geral",
                labels={'x': 'Nível de Satisfação', 'count': 'Frequência'},
                color_discrete_sequence=['#1f77b4']
            )
            fig_hist.update_layout(showlegend=False)
            st.plotly_chart(fig_hist, use_container_width=True)
        
        with col2:
            # Box plot
            fig_box = px.box(
                y=data,
                title="Box Plot - Satisfação Geral",
                labels={'y': 'Nível de Satisfação'}
            )
            fig_box.update_traces(marker_color='#ff7f0e')
            st.plotly_chart(fig_box, use_container_width=True)

def create_workload_charts(analyzer):
    """Cria gráficos de carga de trabalho usando Plotly"""
    workload_data = analyzer.analyze_workload_distribution()
    
    if workload_data:
        col1, col2 = st.columns(2)
        
        # Histogramas de horas
        if 'horas_semanais_diretoria' in workload_data:
            with col1:
                data = workload_data['horas_semanais_diretoria']['data']
                fig_dir = px.histogram(
                    x=data,
                    title="Distribuição - Horas Diretoria/Semana",
                    labels={'x': 'Horas', 'count': 'Frequência'},
                    color_discrete_sequence=['#2ca02c']
                )
                st.plotly_chart(fig_dir, use_container_width=True)
        
        if 'horas_semanais_projeto' in workload_data:
            with col2:
                data = workload_data['horas_semanais_projeto']['data']
                fig_proj = px.histogram(
                    x=data,
                    title="Distribuição - Horas Projeto/Semana",
                    labels={'x': 'Horas', 'count': 'Frequência'},
                    color_discrete_sequence=['#d62728']
                )
                st.plotly_chart(fig_proj, use_container_width=True)
        
        # Box plot comparativo
        if 'horas_semanais_diretoria' in workload_data and 'horas_semanais_projeto' in workload_data:
            dir_data = workload_data['horas_semanais_diretoria']['data']
            proj_data = workload_data['horas_semanais_projeto']['data']
            
            fig_compare = go.Figure()
            fig_compare.add_trace(go.Box(y=dir_data, name='Diretoria', marker_color='#2ca02c'))
            fig_compare.add_trace(go.Box(y=proj_data, name='Projeto', marker_color='#d62728'))
            fig_compare.update_layout(
                title="Comparação de Carga de Trabalho",
                yaxis_title="Horas/Semana"
            )
            st.plotly_chart(fig_compare, use_container_width=True)

def create_organizational_charts(analyzer):
    """Cria gráficos da estrutura organizacional"""
    org_data = analyzer.analyze_organizational_structure()
    
    if org_data:
        # Gráfico de barras com as médias
        metrics_names = []
        metrics_values = []
        
        name_mapping = {
            'organizacao_de': 'Organização DE',
            'acessibilidade_diretor': 'Acessibilidade Diretor',
            'comunicacao_interna': 'Comunicação Interna'
        }
        
        for key, data in org_data.items():
            metrics_names.append(name_mapping.get(key, key))
            metrics_values.append(data['media'])
        
        if metrics_names:
            fig = px.bar(
                x=metrics_names,
                y=metrics_values,
                title="Avaliação da Estrutura Organizacional (Médias)",
                labels={'x': 'Aspecto', 'y': 'Média (1-5)'},
                color=metrics_values,
                color_continuous_scale='viridis'
            )
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

def create_feedback_charts(analyzer):
    """Cria gráficos da cultura de feedback"""
    feedback_data = analyzer.analyze_feedback_culture()
    
    if feedback_data:
        metrics_names = []
        metrics_values = []
        
        name_mapping = {
            'preparacao_feedback': 'Preparação p/ Feedback',
            'frequencia_feedback_dado': 'Frequência Feedback Dado',
            'frequencia_feedback_recebido': 'Frequência Feedback Recebido'
        }
        
        for key, data in feedback_data.items():
            metrics_names.append(name_mapping.get(key, key))
            metrics_values.append(data['media'])
        
        if metrics_names:
            fig = px.bar(
                x=metrics_names,
                y=metrics_values,
                title="Cultura de Feedback (Médias)",
                labels={'x': 'Aspecto', 'y': 'Média (1-5)'},
                color=metrics_values,
                color_continuous_scale='plasma'
            )
            fig.update_layout(showlegend=False)
            st.plotly_chart(fig, use_container_width=True)

def display_metrics_cards(report):
    """Exibe cards com métricas principais"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="📊 Total de Respostas",
            value=report['info_geral']['total_respostas']
        )
    
    with col2:
        if 'satisfacao_geral' in report['satisfacao']:
            satisfaction = report['satisfacao']['satisfacao_geral']
            st.metric(
                label="😊 Satisfação Média",
                value=f"{satisfaction['media']}/5",
            )
    
    with col3:
        if 'horas_semanais_diretoria' in report['carga_trabalho']:
            hours = report['carga_trabalho']['horas_semanais_diretoria']
            st.metric(
                label="⏰ Horas Diretoria/Semana",
                value=f"{hours['media']}h",
                delta=f"Max: {hours['maximo']}h"
            )
    
    with col4:
        if 'horas_semanais_projeto' in report['carga_trabalho']:
            hours = report['carga_trabalho']['horas_semanais_projeto']
            st.metric(
                label="🚀 Horas Projeto/Semana",
                value=f"{hours['media']}h",
                delta=f"Max: {hours['maximo']}h"
            )

# Interface principal do Streamlit
def main():
    st.title("📊 Dashboard de Análise - IN Junior")
    st.markdown("---")
    
    # Sidebar para upload do arquivo
    st.sidebar.header("📁 Upload de Dados")
    uploaded_file = st.sidebar.file_uploader(
        "Escolha o arquivo CSV da pesquisa:",
        type=['csv'],
        help="Faça upload do arquivo CSV com os dados da pesquisa de satisfação"
    )
    
    if uploaded_file is not None:
        try:
            # Carrega os dados
            df = pd.read_csv(uploaded_file)
            
            # Inicializa o analisador
            analyzer = INJuniorSurveyAnalyzer(df)
            
            # Gera o relatório
            report = analyzer.generate_summary_report()
            
            # Exibe cards com métricas principais
            st.subheader("📈 Visão Geral")
            display_metrics_cards(report)
            
            # Tabs para diferentes análises
            tab1, tab2, tab3, tab4, tab5 = st.tabs([
                "😊 Satisfação",
                "⏰ Carga de Trabalho",
                "🏢 Estrutura Organizacional",
                "💬 Cultura de Feedback",
                "📊 Dados Detalhados"
            ])
            
            with tab1:
                st.subheader("Análise de Satisfação")
                create_satisfaction_charts(analyzer)
                
                if 'satisfacao_geral' in report['satisfacao']:
                    sat = report['satisfacao']['satisfacao_geral']
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.info(f"**Média:** {sat['media']}/5")
                    with col2:
                        st.info(f"**Mediana:** {sat['mediana']}/5")
                    with col3:
                        st.info(f"**Desvio Padrão:** {sat['desvio_padrao']}")
            
            with tab2:
                st.subheader("Análise de Carga de Trabalho")
                create_workload_charts(analyzer)
                
                # Tabela resumo
                if report['carga_trabalho']:
                    st.subheader("Resumo da Carga de Trabalho")
                    workload_summary = []
                    for key, data in report['carga_trabalho'].items():
                        workload_summary.append({
                            'Métrica': key.replace('_', ' ').title(),
                            'Média': data['media'],
                            'Mediana': data['mediana'],
                            'Máximo': data['maximo'],
                            'N° Respostas': data['n_respostas']
                        })
                    
                    if workload_summary:
                        st.dataframe(pd.DataFrame(workload_summary), use_container_width=True)
            
            with tab3:
                st.subheader("Estrutura Organizacional")
                create_organizational_charts(analyzer)
            
            with tab4:
                st.subheader("Cultura de Feedback")
                create_feedback_charts(analyzer)
            
            with tab5:
                st.subheader("Dados Detalhados")
                
                # Opções de visualização
                view_option = st.radio(
                    "Escolha o que visualizar:",
                    ["Dados Processados", "Estatísticas Resumidas", "Dados Originais"]
                )
                
                if view_option == "Dados Processados":
                    st.dataframe(analyzer.df_processed, use_container_width=True)
                
                elif view_option == "Estatísticas Resumidas":
                    numeric_cols = analyzer.df_processed.select_dtypes(include=[np.number]).columns
                    if len(numeric_cols) > 0:
                        st.dataframe(analyzer.df_processed[numeric_cols].describe(), use_container_width=True)
                    else:
                        st.warning("Nenhuma coluna numérica encontrada para estatísticas.")
                
                else:  # Dados Originais
                    st.dataframe(df, use_container_width=True)
                
                # Download dos dados processados
                csv = analyzer.df_processed.to_csv(index=False)
                st.download_button(
                    label="📥 Download dos Dados Processados",
                    data=csv,
                    file_name="dados_processados_in_junior.csv",
                    mime="text/csv"
                )
        
        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {str(e)}")
            st.info("Verifique se o arquivo CSV está no formato correto.")
    
    else:
        st.info("👆 Por favor, faça upload do arquivo CSV na barra lateral para começar a análise.")
        
        # Instruções
        with st.expander("ℹ️ Instruções de Uso"):
            st.markdown("""
            ### Como usar este dashboard:
            
            1. **Upload do Arquivo**: Use a barra lateral para fazer upload do arquivo CSV da pesquisa
            2. **Visualização Automática**: O dashboard processará os dados automaticamente
            3. **Navegação por Abas**: Use as abas para explorar diferentes aspectos da análise
            4. **Métricas Interativas**: Todos os gráficos são interativos - você pode fazer zoom, filtrar, etc.
            
            ### Funcionalidades:
            - ✅ Análise automática de dados ausentes
            - ✅ Cálculo de métricas estatísticas profissionais
            - ✅ Visualizações interativas
            - ✅ Download dos dados processados
            - ✅ Interface responsiva
            """)

if __name__ == "__main__":
    main()