# 📁 Nova Estrutura Modular do Dashboard

## 🎯 Objetivo
Separação do código em módulos organizados para facilitar manutenção, expansão e criação de novos cruzamentos de dados.

## � Estrutura de Diretórios

```
/MVP_DashBoard_PCO
│
├── app.py                          # 🚀 Interface principal do Streamlit
├── requirements.txt                # 📦 Dependências do projeto
├── README.md                       # 📖 Documentação principal
├── README_ESTRUTURA.md            # 📋 Este arquivo (documentação da estrutura)
│
├── data_analysis/                  # 🔍 Módulos de análise de dados
│   ├── __init__.py
│   ├── survey_analyzer.py          # 📊 Classe principal INJuniorSurveyAnalyzer
│   └── cruzamentos/               # 🔄 Cruzamentos específicos de dados
│       ├── __init__.py
│       └── satisfacao_vs_carga.py  # Exemplo: Satisfação vs Carga de Trabalho
│
├── charts/                        # 📈 Módulos de visualização
│   ├── __init__.py
│   ├── satisfaction_charts.py     # Gráficos de satisfação
│   ├── workload_charts.py         # Gráficos de carga de trabalho
│   ├── organizational_charts.py   # Gráficos organizacionais
│   └── feedback_charts.py         # Gráficos de feedback
│
└── utils/                         # 🛠️ Funções utilitárias
    ├── __init__.py
    └── helpers.py                 # Funções auxiliares (ex: display_metrics_cards)
```

## 🚀 Como Executar

### 1. Ativar o ambiente virtual
```bash
source venv/bin/activate
```

### 2. Executar o dashboard
```bash
streamlit run app.py
```

## ➕ Como Adicionar Novos Cruzamentos

### 1. Criar novo arquivo de cruzamento
Crie um arquivo em `data_analysis/cruzamentos/` seguindo o padrão:

```python
# data_analysis/cruzamentos/seu_novo_cruzamento.py

import streamlit as st
import plotly.express as px
import pandas as pd
from scipy import stats

def analyze_seu_cruzamento(analyzer):
    """
    Analisa correlação entre variáveis X e Y
    
    Args:
        analyzer: Instância do INJuniorSurveyAnalyzer
        
    Returns:
        dict: Resultados da análise
    """
    # Sua lógica de análise aqui
    pass

def create_seu_cruzamento_charts(analyzer):
    """Cria gráficos do seu cruzamento"""
    st.subheader("🔄 Seu Novo Cruzamento")
    
    # Sua lógica de visualização aqui
    pass
```

### 2. Importar no app.py
```python
from data_analysis.cruzamentos.seu_novo_cruzamento import create_seu_cruzamento_charts
```

### 3. Adicionar na interface
No `app.py`, adicione sua função na aba "Cruzamentos":

```python
with tab5:  # Aba Cruzamentos
    st.subheader("Análises de Cruzamento")
    create_satisfaction_workload_charts(analyzer)
    create_seu_cruzamento_charts(analyzer)  # Sua nova função
```

## 📈 Como Adicionar Novos Tipos de Gráficos

### 1. Criar novo módulo em charts/
```python
# charts/seu_novo_chart.py

import streamlit as st
import plotly.express as px

def create_seu_novo_chart(analyzer):
    """Cria seu novo tipo de gráfico"""
    # Sua lógica aqui
    pass
```

### 2. Atualizar charts/__init__.py
```python
from .seu_novo_chart import create_seu_novo_chart

__all__ = [
    # ... outros gráficos
    'create_seu_novo_chart'
]
```

### 3. Usar no app.py
```python
from charts.seu_novo_chart import create_seu_novo_chart
```

## 🔧 Funções Utilitárias

Para adicionar novas funções auxiliares, edite `utils/helpers.py`:

```python
def sua_nova_funcao(dados):
    """Sua nova função utilitária"""
    # Sua lógica aqui
    pass
```

## ✅ Vantagens da Nova Estrutura

- **🧹 Código mais limpo**: Cada módulo tem responsabilidade específica
- **🔧 Fácil manutenção**: Alterações isoladas por funcionalidade
- **➕ Expansibilidade**: Simples adicionar novos cruzamentos e gráficos
- **👥 Colaboração**: Múltiplas pessoas podem trabalhar em módulos diferentes
- **🧪 Testabilidade**: Cada módulo pode ser testado independentemente
- **📚 Reutilização**: Funções podem ser reutilizadas em diferentes contextos

## 🎯 Próximos Passos Sugeridos

1. **Adicionar mais cruzamentos**:
   - Satisfação vs Feedback
   - Carga de trabalho vs Comunicação
   - Engajamento vs Estrutura organizacional

2. **Criar testes unitários**:
   - Testes para cada módulo
   - Validação de dados

3. **Adicionar configurações**:
   - Arquivo de configuração para parâmetros
   - Personalização de cores e temas

4. **Melhorar documentação**:
   - Docstrings completas
   - Exemplos de uso

## 🐛 Solução de Problemas

### Erro de importação
```bash
# Sempre ativar o ambiente virtual primeiro
source venv/bin/activate

# Verificar se está no diretório correto
pwd
# Deve mostrar: /home/ayrtonss/Desktop/INJunior/MVP_DashBoard_PCO
```

### Erro ao executar Streamlit
```bash
# Verificar se as dependências estão instaladas
pip list

# Reinstalar se necessário
pip install -r requirements.txt
```

## 🎯 Separação de Responsabilidades

### 📊 `app.py` - Interface Principal
- **Responsabilidade**: Interface do usuário, navegação, upload de arquivos
- **Conteúdo**: 
  - Configuração do Streamlit
  - Upload de arquivos
  - Estrutura de tabs
  - Chamadas para módulos específicos

### 🔍 `data_analysis/` - Análise de Dados
- **`survey_analyzer.py`**: Classe principal para processamento e análise
- **`cruzamentos/`**: Submódulo para análises de correlação/cruzamento
  - Cada arquivo representa um cruzamento específico
  - Facilita adição de novos cruzamentos

### 📈 `charts/` - Visualizações
- **Cada arquivo**: Um tipo específico de gráfico
- **Vantagem**: Reutilização fácil e manutenção isolada
- **Padrão**: Funções que recebem `analyzer` e criam gráficos no Streamlit

### 🛠️ `utils/` - Utilitários
- **`helpers.py`**: Funções auxiliares como cards de métricas
- **Expandível**: Para formatações, validações, etc.

## ➕ Como Adicionar Novos Cruzamentos

### 1. Criar novo arquivo em `cruzamentos/`

```python
# data_analysis/cruzamentos/novo_cruzamento.py

def analyze_novo_cruzamento(analyzer):
    """Análise do novo cruzamento"""
    # Sua lógica de análise aqui
    pass

def create_novo_cruzamento_charts(analyzer):
    """Gráficos do novo cruzamento"""
    # Seus gráficos aqui
    pass
```

### 2. Importar no `app.py`

```python
from data_analysis.cruzamentos.novo_cruzamento import create_novo_cruzamento_charts
```

### 3. Adicionar na aba de Cruzamentos

```python
with tab5:  # Aba Cruzamentos
    st.subheader("Análises de Cruzamento")
    
    # Cruzamentos existentes
    create_satisfaction_workload_charts(analyzer)
    
    # Novo cruzamento
    create_novo_cruzamento_charts(analyzer)
```

## 📊 Exemplo de Cruzamento Implementado

**Arquivo**: `data_analysis/cruzamentos/satisfacao_vs_carga.py`

**Funcionalidades**:
- ✅ Análise de correlação Pearson
- ✅ Gráficos de dispersão com linha de tendência
- ✅ Tabela resumo estatístico
- ✅ Interpretação automática dos resultados
- ✅ Testes de significância estatística

**Análises incluídas**:
- Satisfação vs Horas Diretoria
- Satisfação vs Horas Projeto  
- Satisfação vs Carga Total

## 🚀 Vantagens da Nova Estrutura

### ✅ **Modularidade**
- Cada funcionalidade em seu próprio arquivo
- Fácil de manter e debugar
- Possibilita trabalho em equipe

### ✅ **Escalabilidade**
- Adicionar novos cruzamentos é simples
- Não polui o arquivo principal
- Estrutura clara e organizada

### ✅ **Reutilização**
- Gráficos podem ser reutilizados em outros contextos
- Análises podem ser chamadas independentemente
- Código mais limpo e profissional

### ✅ **Manutenibilidade**
- Bugs isolados em módulos específicos
- Testes mais fáceis de implementar
- Documentação mais organizada

## 🔧 Para Desenvolvedores

### Convenções de Nomenclatura
- **Análises**: `analyze_nome_da_analise(analyzer)`
- **Gráficos**: `create_nome_charts(analyzer)`
- **Arquivos**: `snake_case.py`
- **Funções**: Sempre recebem `analyzer` como parâmetro

### Padrão de Retorno das Análises
```python
{
    'metric_name': {
        'correlacao': float,
        'p_value': float, 
        'significativo': bool,
        'data': DataFrame,
        'n_amostras': int
    }
}
```

### Imports Necessários
- **Gráficos**: `streamlit`, `plotly.express`, `plotly.graph_objects`
- **Análises**: `pandas`, `numpy`, `scipy.stats`
- **Utilitários**: Conforme necessidade

## 📋 Próximos Passos Sugeridos

1. **Implementar mais cruzamentos**:
   - Satisfação vs Estrutura Organizacional
   - Carga de Trabalho vs Feedback
   - Engajamento vs Satisfação

2. **Adicionar testes unitários**:
   - Criar `tests/` com testes para cada módulo

3. **Melhorar documentação**:
   - Docstrings mais detalhadas
   - Exemplos de uso

4. **Otimizações**:
   - Cache de dados processados
   - Lazy loading de gráficos
   - Validações de entrada mais robustas

---

Esta estrutura permite que o projeto cresça de forma organizada e profissional! 🎉
