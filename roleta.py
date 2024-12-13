
import streamlit as st
import random

# Lista de valores possíveis para os prêmios
prizes = [0.5, 1, 2, 3, 5]  # Valores em reais
random.shuffle(prizes)  # Embaralha os prêmios para diminuir repetições

# Estado persistente para armazenar prêmios disponíveis e histórico
if "prizes" not in st.session_state:
    st.session_state.prizes = prizes

if "history" not in st.session_state:
    st.session_state.history = []

st.title("numero premiado")

st.write("compre o seu numero premiado e veja quanto você ganhou!")

# Função para selecionar o prêmio
def select_number(num):
    if st.session_state.prizes:  # Verifica se ainda há prêmios
        prize = st.session_state.prizes.pop(0)  # Retira o próximo prêmio
        st.session_state.history.append((num, prize))
        st.success(f"Você escolheu o número {num} e ganhou R$ {prize:.2f}!")
    else:
        st.warning("Todos os prêmios foram usados! Reiniciando prêmios.")
        st.session_state.prizes = [0.5, 1, 2, 3, 0.5,]
        random.shuffle(st.session_state.prizes)

# Criação dos botões para os números de 1 a 10
cols = st.columns(5)  # Divide em colunas para melhor organização
for i in range(1, 11):
    col = cols[(i-1) % 5]
    if col.button(f"{i}"):
        select_number(i)

# Exibe o histórico de prêmios
if st.session_state.history:
    st.subheader("Histórico de escolhas:")
    for num, prize in st.session_state.history:
        st.write(f"Número: {num}, Prêmio: R$ {prize:.2f}")

# Botão para reiniciar o jogo
if st.button("Reiniciar Jogo"):
    st.session_state.prizes = [0.5, 1, 2, 3, 5]
    random.shuffle(st.session_state.prizes)
    st.session_state.history = []
    st.success("Jogo reiniciado com sucesso!")