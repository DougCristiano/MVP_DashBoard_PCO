# 📊 Dashboard de Análise - IN Junior

Dashboard interativo para análise de dados da pesquisa de satisfação da IN Junior, desenvolvido em Python com Streamlit.

## 🚀 Funcionalidades

- ✅ **Upload de CSV**: Interface web para upload de arquivos
- ✅ **Análise Automática**: Processamento e limpeza automática dos dados
- ✅ **Visualizações Interativas**: Gráficos responsivos com Plotly
- ✅ **Métricas Profissionais**: Estatísticas descritivas completas
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
- Colunas de satisfação (escalas numéricas 1-7)
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