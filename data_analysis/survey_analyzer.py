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
        
        # Converte colunas numéricas (escalas de 1-5, etc.) - EXCETO as de workload
        numeric_columns = [
            'O quão organizada você considera a DE?',
            'O quão acessível é o seu/sua diretor(a)?',
            'Quão bem os integrantes de sua diretoria se comunicam entre si?',
            'Quanto você se relaciona com membros de outras diretorias?',
            'O quão satisfatória é a delegação de tarefas na sua diretoria?',
            'O quão você se sente preparado para realizar as suas tarefas de diretoria?',
            'Quão bem os integrantes da sua diretoria compartilham as responsabilidades pelas tarefas?',
            # 'Quantas horas por semana você gasta com tarefas de diretoria?',  # Mantém como string
            'O quanto você se sente preparado(a) para conceder feedback para os membros da sua equipe?',
            'O quanto você concede feedback para os membros da sua equipe?',
            'Com que frequência seu/sua diretor(a) ouve seus assessores para tomar decisões?',
            'Com que frequência você recebe feedback de seu/sua diretor(a)?',
            'De forma geral, o quanto você está satisfeito(a) com seu/sua gerente?',
            # 'Quantos projetos você está realizando na IN Junior atualmente?',  # Mantém como string
            # 'Quantas horas semanalmente você gasta com tarefas de projeto?',  # Mantém como string
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
                    'n_respostas': len(valid_responses),
                    'data': valid_responses
                }
                
                # Tenta calcular estatísticas se os dados são numéricos
                try:
                    numeric_responses = pd.to_numeric(valid_responses, errors='coerce').dropna()
                    if len(numeric_responses) > 0:
                        metrics['satisfacao_geral'].update({
                            'media': round(numeric_responses.mean(), 2),
                            'mediana': round(numeric_responses.median(), 2),
                            'desvio_padrao': round(numeric_responses.std(), 2),
                            'percentil_75': round(numeric_responses.quantile(0.75), 2),
                            'percentil_25': round(numeric_responses.quantile(0.25), 2),
                        })
                    else:
                        # Se não é numérico, apenas value_counts
                        metrics['satisfacao_geral']['value_counts'] = valid_responses.value_counts()
                except Exception as e:
                    # Fallback para dados categóricos
                    metrics['satisfacao_geral']['value_counts'] = valid_responses.value_counts()
        
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
                        'n_respostas': len(valid_responses),
                        'data': valid_responses
                    }
                    
                    # Tenta calcular estatísticas se os dados são numéricos
                    try:
                        numeric_responses = pd.to_numeric(valid_responses, errors='coerce').dropna()
                        if len(numeric_responses) > 0:
                            metrics[key].update({
                                'media': round(numeric_responses.mean(), 2),
                                'desvio_padrao': round(numeric_responses.std(), 2),
                            })
                        else:
                            metrics[key]['value_counts'] = valid_responses.value_counts()
                    except Exception as e:
                        metrics[key]['value_counts'] = valid_responses.value_counts()
        
        return metrics
    
    def analyze_workload_distribution(self):
        """Analisa distribuição de carga de trabalho com dados categóricos"""
        metrics = {}
        
        # Lista de possíveis nomes de colunas para cada métrica
        workload_columns = {
            'horas_semanais_diretoria': [
                'Quantas horas por semana você gasta com tarefas de diretoria?',
                'Horas diretoria',
                'Horas por semana - diretoria',
                'Quantas horas você dedica semanalmente às tarefas de diretoria?'
            ],
            'horas_semanais_projeto': [
                'Quantas horas semanalmente você gasta com tarefas de projeto?',
                'Horas projeto',
                'Horas por semana - projeto',
                'Quantas horas você dedica semanalmente aos projetos?'
            ],
            'projetos_simultaneos': [
                'Quantos projetos você está realizando na IN Junior atualmente?',
                'Número de projetos',
                'Projetos atuais',
                'Quantos projetos você está realizando atualmente?'
            ]
        }
        
        for metric_key, possible_columns in workload_columns.items():
            found_column = None
            
            # Tenta encontrar uma coluna exata
            for col_name in possible_columns:
                if col_name in self.df_processed.columns:
                    found_column = col_name
                    break
            
            # Se não encontrou, tenta busca parcial (case-insensitive)
            if not found_column:
                for df_col in self.df_processed.columns:
                    df_col_lower = df_col.lower()
                    
                    # Busca por palavras-chave específicas para cada métrica
                    if metric_key == 'horas_semanais_diretoria':
                        if ('hora' in df_col_lower and 'diretoria' in df_col_lower) or \
                           ('hora' in df_col_lower and 'semana' in df_col_lower and 'diretoria' in df_col_lower):
                            found_column = df_col
                            break
                    
                    elif metric_key == 'horas_semanais_projeto':
                        if ('hora' in df_col_lower and 'projeto' in df_col_lower) or \
                           ('hora' in df_col_lower and 'semana' in df_col_lower and 'projeto' in df_col_lower):
                            found_column = df_col
                            break
                    
                    elif metric_key == 'projetos_simultaneos':
                        if ('projeto' in df_col_lower and ('quantos' in df_col_lower or 'número' in df_col_lower or 'atual' in df_col_lower)) or \
                           ('projeto' in df_col_lower and 'junior' in df_col_lower):
                            found_column = df_col
                            break
            
            if found_column:
                raw_data = self.df_processed[found_column]
                valid_responses = raw_data.dropna()
                
                if len(valid_responses) > 0:
                    # Para dados categóricos, criamos contagens e outras estatísticas
                    value_counts = valid_responses.value_counts()
                    
                    metrics[metric_key] = {
                        'n_respostas': len(valid_responses),
                        'data': valid_responses,
                        'coluna_encontrada': found_column,
                        'value_counts': value_counts,
                        'categorias': list(value_counts.index),
                        'tipo_dados': 'categorico'
                    }
                    
                    # Se conseguir mapear para números (para estatísticas), faz isso também
                    numeric_mapping = self._get_numeric_mapping_for_workload(metric_key)
                    if numeric_mapping:
                        numeric_data = valid_responses.map(numeric_mapping).dropna()
                        if len(numeric_data) > 0:
                            metrics[metric_key].update({
                                'media': round(numeric_data.mean(), 2),
                                'mediana': round(numeric_data.median(), 2),
                                'desvio_padrao': round(numeric_data.std(), 2),
                                'maximo': numeric_data.max(),
                                'minimo': numeric_data.min(),
                                'numeric_data': numeric_data,
                                'tipo_dados': 'categorico_com_numerico'
                            })
        
        return metrics
    
    def _get_numeric_mapping_for_workload(self, metric_key):
        """Retorna mapeamento numérico apenas para estatísticas, sem alterar dados originais"""
        
        if metric_key == 'horas_semanais_diretoria':
            return {
                '1 a 5 horas': 3,
                '6 a 10 horas': 8,
                '11 a 15 horas': 13,
                'Mais de 15 horas': 18
            }
        
        elif metric_key == 'horas_semanais_projeto':
            return {
                '1 a 5 horas': 3,
                '6 a 10 horas': 8,
                '11 a 15 horas': 13,
                'Mais de 10 horas': 15,
                'Mais de 15 horas': 18
            }
        
        elif metric_key == 'projetos_simultaneos':
            return {
                'Nenhum': 0,
                'Um': 1,
                'Dois': 2,
                'Três': 3,
                'Mais de três': 4
            }
        
        return None
    
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
                        'n_respostas': len(valid_responses),
                        'data': valid_responses
                    }
                    
                    # Tenta calcular estatísticas se os dados são numéricos
                    try:
                        numeric_responses = pd.to_numeric(valid_responses, errors='coerce').dropna()
                        if len(numeric_responses) > 0:
                            metrics[key].update({
                                'media': round(numeric_responses.mean(), 2),
                                'desvio_padrao': round(numeric_responses.std(), 2),
                            })
                        else:
                            metrics[key]['value_counts'] = valid_responses.value_counts()
                    except Exception as e:
                        metrics[key]['value_counts'] = valid_responses.value_counts()
        
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
                        'n_respostas': len(valid_responses),
                        'data': valid_responses
                    }
                    
                    # Tenta calcular estatísticas se os dados são numéricos
                    try:
                        numeric_responses = pd.to_numeric(valid_responses, errors='coerce').dropna()
                        if len(numeric_responses) > 0:
                            metrics[key].update({
                                'media': round(numeric_responses.mean(), 2),
                                'desvio_padrao': round(numeric_responses.std(), 2),
                            })
                        else:
                            metrics[key]['value_counts'] = valid_responses.value_counts()
                    except Exception as e:
                        metrics[key]['value_counts'] = valid_responses.value_counts()
        
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
