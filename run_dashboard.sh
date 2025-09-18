#!/bin/bash

# Script para executar o Dashboard IN Junior
# Uso: ./run_dashboard.sh

echo "🚀 Iniciando Dashboard IN Junior..."
echo "📂 Ativando ambiente virtual..."

# Ativa o ambiente virtual
source venv/bin/activate

echo "✅ Ambiente virtual ativado!"
echo "🔧 Verificando dependências..."

# Verifica se as dependências estão instaladas
if ! python -c "import streamlit, pandas, plotly" 2>/dev/null; then
    echo "❌ Dependências faltando. Instalando..."
    pip install -r requirements.txt
fi

echo "🌟 Iniciando Streamlit..."
echo "🌐 Acesse: http://localhost:8501"
echo "⚡ Para parar: Ctrl+C"
echo ""

# Executa o Streamlit
streamlit run app.py
