# 📊 Dashboard de Análise - IN Junior

Um dashboard interativo desenvolvido com Streamlit para análise de dados de pesquisas de satisfação da IN Junior.

## 🎯 Funcionalidades

- 📈 **Análise de Satisfação**: Visualizações de satisfação geral dos membros
- ⏰ **Carga de Trabalho**: Análise de distribuição de horas e projetos
- 🏢 **Estrutura Organizacional**: Avaliação da organização e comunicação
- 💬 **Cultura de Feedback**: Métricas de feedback entre membros
- 🔄 **Cruzamentos de Dados**: Análises de correlação entre variáveis
- 📊 **Dados Detalhados**: Visualização e download dos dados processados

## 🚀 Como Executar

### Opção 1: Script automático (Recomendado)
```bash
./run_dashboard.sh
```

### Opção 2: Manual
```bash
# 1. Ativar ambiente virtual
source venv/bin/activate

# 2. Instalar dependências (se necessário)
pip install -r requirements.txt

# 3. Executar dashboard
streamlit run app.py
```

## 📂 Nova Estrutura Modular

O projeto foi organizado em módulos para facilitar manutenção e expansão:

```
/MVP_DashBoard_PCO
│
├── app.py                          # 🚀 Interface principal
├── run_dashboard.sh               # 🔧 Script de execução
├── requirements.txt               # 📦 Dependências
│
├── data_analysis/                 # 🔍 Módulos de análise
│   ├── survey_analyzer.py         # 📊 Classe principal de análise
│   └── cruzamentos/              # 🔄 Cruzamentos específicos
│       └── satisfacao_vs_carga.py # Exemplo de cruzamento
│
├── charts/                       # 📈 Módulos de visualização
│   ├── satisfaction_charts.py    # Gráficos de satisfação
│   ├── workload_charts.py        # Gráficos de carga de trabalho
│   ├── organizational_charts.py  # Gráficos organizacionais
│   └── feedback_charts.py        # Gráficos de feedback
│
└── utils/                        # 🛠️ Funções utilitárias
    └── helpers.py                # Funções auxiliares
```

## ➕ Como Adicionar Novos Cruzamentos

1. **Criar arquivo em `data_analysis/cruzamentos/`**:
```python
def analyze_novo_cruzamento(analyzer):
    # Sua lógica de análise
    pass

def create_novo_cruzamento_charts(analyzer):
    # Seus gráficos
    pass
```

2. **Importar no `app.py`**:
```python
from data_analysis.cruzamentos.novo_cruzamento import create_novo_cruzamento_charts
```

3. **Adicionar na interface**:
```python
with tab5:  # Aba Cruzamentos
    create_novo_cruzamento_charts(analyzer)
```

## 📋 Documentação Detalhada

Para informações completas sobre a estrutura e como expandir o projeto:
- 📖 [README_ESTRUTURA.md](README_ESTRUTURA.md) - Documentação detalhada da nova estrutura

## 🔧 Tecnologias Utilizadas

- **Frontend**: Streamlit
- **Visualização**: Plotly, Matplotlib, Seaborn
- **Análise de Dados**: Pandas, NumPy, SciPy
- **Estatística**: Correlações de Pearson, testes de significância

## ✅ Vantagens da Nova Estrutura

- 🧹 **Código Limpo**: Cada módulo tem responsabilidade específica
- 🔧 **Fácil Manutenção**: Alterações isoladas por funcionalidade
- ➕ **Expansível**: Simples adicionar novos cruzamentos e gráficos
- 👥 **Colaborativo**: Múltiplas pessoas podem trabalhar simultaneamente
- 🧪 **Testável**: Cada módulo pode ser testado independentemente

## 🎯 Próximos Passos

- [ ] Adicionar mais tipos de cruzamentos
- [ ] Implementar testes unitários
- [ ] Criar sistema de configuração
- [ ] Adicionar exportação de relatórios
- [ ] Melhorar documentação com exemplos

## 📞 Suporte

Para dúvidas ou problemas, consulte:
1. 📋 [README_ESTRUTURA.md](README_ESTRUTURA.md) para detalhes técnicos
2. 🐛 Seção "Solução de Problemas" na documentação
3. ✅ Verificar se o ambiente virtual está ativado
- ✅ **Dashboard Responsivo**: Interface organizada por abas
- ✅ **Download de Resultados**: Exportação dos dados processados

## 📈 Análises Disponíveis

### 😊 Satisfação Geral
- Distribuição da satisfação dos membros
- Estatísticas descritivas (média, mediana, percentis)
- Visualizações em histograma e box plot

### ⏰ Carga de Trabalho
- Horas semanais em diretoria e projetos
- Distribuição de projetos simultâneos
- Análise comparativa de workload

### 🏢 Estrutura Organizacional
- Avaliação da Diretoria Executiva
- Acessibilidade dos diretores
- Qualidade da comunicação interna

### 💬 Cultura de Feedback
- Preparação e frequência de feedback
- Análise da cultura de feedback da empresa
- Métricas de comunicação interna

## 🛠️ Instalação

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório**
```bash
git clone [url-do-repositorio]
cd [nome-do-repositorio]
```

2. **Crie um ambiente virtual (recomendado)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute o dashboard**
```bash
streamlit run app.py
```

5. **Acesse no navegador**
- O dashboard será aberto automaticamente em `http://localhost:8501`
- Se não abrir automaticamente, acesse o link manualmente

## 💻 Como Usar

### 1. Upload do Arquivo
- Use a barra lateral para fazer upload do arquivo CSV
- O arquivo deve conter os dados da pesquisa de satisfação
- Formatos suportados: `.csv`

### 2. Navegação
- **📊 Visão Geral**: Cards com métricas principais
- **😊 Satisfação**: Análise detalhada de satisfação
- **⏰ Carga de Trabalho**: Distribuição de horas e projetos
- **🏢 Estrutura Organizacional**: Avaliação organizacional
- **💬 Cultura de Feedback**: Métricas de feedback
- **📊 Dados Detalhados**: Visualização e download dos dados

### 3. Recursos Interativos
- **Zoom**: Clique e arraste nos gráficos
- **Hover**: Passe o mouse sobre os pontos para ver detalhes
- **Download**: Baixe os dados processados em CSV
- **Filtros**: Use as opções de visualização disponíveis

## 📋 Formato dos Dados

O CSV deve conter as seguintes colunas (ou similares):
- Colunas de satisfação (escalas numéricas 1-5)
- Horas semanais de trabalho
- Avaliações organizacionais
- Métricas de feedback
- Dados demográficos básicos

**Nota**: O sistema ignora automaticamente:
- Respostas em branco ou inválidas
- Campos de texto livre (conforme configurado)
- Dados inconsistentes

## 🔧 Estrutura do Projeto

```
projeto/
├── app.py                 # Aplicação principal Streamlit
├── requirements.txt       # Dependências Python
├── README.md             # Este arquivo
└── dados/                # Pasta para arquivos CSV (opcional)
```

## 🐛 Solução de Problemas

### Erro: "streamlit não é reconhecido"
```bash
# Usar python -m ao invés do comando direto
python -m streamlit run app.py
```

### Erro relacionado a caracteres especiais na pasta
- Mova o projeto para uma pasta sem caracteres especiais como `{}`, `[]`, etc.
- Exemplo: `C:\projetos\analise_in_junior\`

### Erro de dependências
```bash
# Reinstalar dependências
pip install --upgrade -r requirements.txt
```

### Problemas com upload de arquivo
- Verifique se o arquivo está em formato CSV
- Certifique-se de que o arquivo não está corrompido
- Teste com um arquivo CSV simples primeiro

## 📊 Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)**: Framework web para dashboards
- **[Pandas](https://pandas.pydata.org/)**: Manipulação de dados
- **[Plotly](https://plotly.com/python/)**: Visualizações interativas
- **[NumPy](https://numpy.org/)**: Computação numérica
- **[SciPy](https://scipy.org/)**: Análises estatísticas
- **[Seaborn](https://seaborn.pydata.org/)**: Visualizações estatísticas

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Em caso de dúvidas ou problemas:
- Abra uma issue no repositório
- Consulte a documentação do Streamlit: https://docs.streamlit.io/
- Verifique os logs de erro no terminal

---

**Desenvolvido para IN Junior** 📊💙