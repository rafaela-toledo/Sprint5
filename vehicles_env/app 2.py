import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('/Users/rafaelatoledo/Desktop/MeuProjeto5/vehicles_env/vehicles.csv')
st.header('Análise Exploratória de Dados de Veículos')
import pandas as pd
     import plotly.express as px
     import streamlit as st
     
     car_data = pd.read_csv('vehicles_us.csv') # lendo os dados
     hist_button = st.button('Criar histograma') # criar um botão
     
     if hist_button: # se o botão for clicado
         # escrever uma mensagem
         st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um histograma
         fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)


