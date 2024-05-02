import streamlit as st
import pandas as pd

# ================================ CONFIGURAÇÕES ================================ #
st.set_page_config(layout='wide')

# ================================ VARIAVEIS ================================ #
list_caregory_despesa = ["Casa", "Cartões", "Fixo", "Variaveis"]

# Ler dados do arquivo CSV
def load_data():
    try:
        return pd.read_csv('dados.csv')
    except FileNotFoundError:
        # Se o arquivo não existir, retorna um DataFrame vazio com as colunas esperadas
        return pd.DataFrame(columns=['Descrição', 'Valor', 'Categoria', 'Parcelamento', 'Data'])

# Função para adicionar despesas
def add_expense(description, value, category, installmentCount, date):
    new_expense = pd.DataFrame(
        {'Descrição': [description], 
         'Valor': [value], 
         'Categoria': [category], 
         'Parcelamento': [installmentCount], 
         'Data': [date]})
    df = load_data()
    df = pd.concat([df, new_expense], ignore_index=True)

# Função para adicionar receitas
#def add_income(description, value, category):
#    new_income = pd.DataFrame({'Descrição': [description], 'Valor': [value], 'Categoria': [category]})
#    st.session_state['expenses'] = pd.concat([st.session_state['expenses'], new_income], ignore_index=True)

# Formulário para novas despesas
with st.form("Nova Despesa", clear_on_submit=True):
    st.write("Adicionar nova despesa")
    cols = st.columns([3, 2])
    desc = cols[0].text_input("Descrição")
    date = cols[1].date_input("Data", format="DD/MM/YYYY")
    col1, col2, col3 = st.columns(3)
    value = col1.number_input("Valor", min_value=0.00)
    part = col2.text_input("Parcelamento")
    category = col3.selectbox("Categoria", list_caregory_despesa)
    submitted = st.form_submit_button("Adicionar")
    if submitted:
        df = add_expense(desc, value, category, part, date)
        # Salvar em csv
        df.to_csv('dados.csv', index=False)
        # Carregar os dados ao iniciar o app


# Formulário para novas receitas
#with st.form("Nova Receita", clear_on_submit=True):
#    st.write("Adicionar nova receita")
#    desc = st.text_input("Descrição Receita")
#    value = st.number_input("Valor Receita", min_value=0.00)
#    category = st.selectbox("Categoria Receita", ["Salário", "Freelance", "Presente", "Outros"])
#    submitted = st.form_submit_button("Adicionar Receita")
#    if submitted:
#        add_income(desc, value, category)

# Tabela de despesas com botões de editar e excluir
st.write("Despesas do Mês")
df = load_data()
for i, row in df.iterrows():
    # Configura as colunas para descrição, valor, categoria, parcelamento, data, editar, excluir
    cols = st.columns([3, 1, 1, 1, 1, 2, 2])
    cols[0].write(row['Descrição'])
    cols[1].write(row['Valor'])
    cols[2].write(row['Categoria'])
    cols[3].write(row['Parcelamento'])
    cols[4].write(row['Data'])

    # Botões de editar e excluir com a lógica ainda não implementada
    if cols[5].button("✏️ Editar", key=f"edit{i}"):
        st.write("Editar (lógica não implementada)")
    if cols[6].button("⛔ Excluir", key=f"delete{i}"):
        st.write("Excluir (lógica não implementada)")