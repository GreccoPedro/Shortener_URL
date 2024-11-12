import pyshorteners
import streamlit as st

def shorten_url(url): # funcion que acorta la url con la url de parametro
    s = pyshorteners.Shortener()    #objeto propio de la libreria
    try:
        shortened_url = s.tinyurl.short(url) #llamada al metodo que acorta la url
        return shortened_url
    except Exception as e: #capturar posibles errores y proporcionar un mensaje informativo de error
        return f"Error al acortar la URL: {e}"
        
#creacion de app web (streamlit)
st.set_page_config(page_title="URL Shortener",page_icon="", layout="centered")
st.image('images/tijeras.png', use_container_width=True)
st.title('URL Shortener')
url = st.text_input('Enter the URL')
if st.button('Generate shortened URL'): #si se pulsa, llama la funcion
    st.write('URL shortened: ', shorten_url(url))
    
