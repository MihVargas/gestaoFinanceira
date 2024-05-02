import streamlit as st
import pandas as pd

# Inicializando um dataframe para armazenar as despesas
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = pd.DataFrame(columns=['Descrição', 'Valor', 'Categoria'])

# Função para adicionar despesas
def add_expense(description, value, category):
    new_expense = {'Descrição': description, 'Valor': value, 'Categoria': category}
    st.session_state['expenses'] = st.session_state['expenses'].append(new_expense, ignore_index=True)

# Função para adicionar receitas
def add_income(description, value, category):
    new_income = {'Descrição': description, 'Valor': value, 'Categoria': category}
    st.session_state['expenses'] = st.session_state['expenses'].append(new_income, ignore_index=True)

# Formulário para novas despesas
with st.form("Nova Despesa"):
    st.write("Adicionar nova despesa")
    desc = st.text_input("Descrição")
    value = st.number_input("Valor", min_value=0.01)
    category = st.selectbox("Categoria", ["Alimentação", "Transporte", "Lazer", "Outros"])
    submitted = st.form_submit_button("Adicionar")
    if submitted:
        add_expense(desc, value, category)

# Formulário para novas receitas
with st.form("Nova Receita"):
    st.write("Adicionar nova receita")
    desc = st.text_input("Descrição Receita")
    value = st.number_input("Valor Receita", min_value=0.01)
    category = st.selectbox("Categoria Receita", ["Salário", "Freelance", "Presente", "Outros"])
    submitted = st.form_submit_button("Adicionar Receita")
    if submitted:
        add_income(desc, value, category)

# Tabela de despesas com botões de editar e excluir
st.write("Despesas Cadastradas")
for i, row in st.session_state['expenses'].iterrows():
    cols = st.columns([3, 2, 2, 1, 1])  # Configura as colunas para descrição, valor, categoria, editar, excluir
    cols[0].write(row['Descrição'])
    cols[1].write(row['Valor'])
    cols[2].write(row['Categoria'])
    if cols[3].button("Editar", key=f"edit{i}"):
        st.write("Editar (lógica não implementada)")
    if cols[4].button("Excluir", key=f"delete{i}"):
        st.write("Excluir (lógica não implementada)")
