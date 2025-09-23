# Aplicativo de Pesquisa PCO

Este diretório contém o aplicativo para coletar respostas da Pesquisa de Clima Organizacional (PCO).

## Funcionalidades

- Formulário interativo para coleta de respostas
- Armazenamento seguro dos dados
- Dashboard em tempo real com resultados
- Análises automáticas das respostas

## Como usar

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute o aplicativo:
```bash
streamlit run app.py
```

3. Acesse o aplicativo no navegador:
   - Aba "Responder Pesquisa": Para coletar novas respostas
   - Aba "Ver Resultados": Para visualizar análises

## Estrutura do Projeto

- `app.py`: Aplicativo principal
- `respostas/`: Pasta onde são salvas as respostas (criada automaticamente)
- Cada resposta é salva como um arquivo JSON com timestamp único

## Personalização

As perguntas podem ser personalizadas editando o dicionário `PERGUNTAS` no início do arquivo `app.py`.