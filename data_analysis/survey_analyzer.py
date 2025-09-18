"""
Classe para análise dos dados da pesquisa de satisfação da IN Junior
"""

import pandas as pd
import numpy as np


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
        
        # Converte colunas numéricas (escalas de 1-5, etc.)
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
