import streamlit as st
from PIL import Image

st.set_page_config(
    page_title='Home', 
    page_icon=""
)

#image_path = '/Users/Luan/repos/ftc_programacao_python/'
image = Image.open( 'logo.png' )
st.sidebar.image( image, width=120)

st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('## Fastest Delivery in Town')
st.sidebar.markdown("""___""")

st.write("# Curry Company Growth Dashboard")
st.markdown(
    """
    Growth Dashboard foi construído para acomoanharas métricas de crescimento dos Entregadores e Restaurantes.
    ### Como utilizar esse Growth Dashboard?
    - Vusão Empresa:
        - Visão Gerencial: Métricas gerais de comportamento.
        - Visão Tática: Indicadores semanais de crescimento.
        - Visão Geográfica: Insights de geolocalização.
    - Visão Entregador:
        - Acompanhamento dos indicadores semanais de crescimento.
    - Visão Restautante:
        - Indicadores semanaisde crescimento dos restaurantes
    ### Ask for Help
    - Time de Data Science no Discord
        - @meigarom
    """)