# Dashboard de Análise PCO

Este diretório contém o aplicativo de análise de dados da Pesquisa de Clima Organizacional (PCO).

## Funcionalidades

- Análise de dados de pesquisas existentes
- Visualização de métricas e tendências
- Correlações entre diferentes aspectos
- Análise temporal dos dados

## Como usar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o aplicativo:
```bash
streamlit run app.py
```

3. Carregue um arquivo de dados (CSV ou Excel) com as respostas da pesquisa

## Estrutura de Dados

O aplicativo espera um arquivo com as seguintes categorias de colunas:

- Escalas (1-5): Para perguntas de satisfação
- Horas: Métricas de tempo dedicado
- Quantidades: Outras métricas numéricas