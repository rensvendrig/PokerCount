import streamlit as st
import pandas as pd

st.write('# de PokerCount van Rons')

if 'data' not in st.session_state:
    data = pd.DataFrame({'naam':[]'wit':[],'rood':[],'blauw':[],'groen':[],'zwart':[]})
    st.session_state.data = data

data = st.session_state.data

st.dataframe(data)

def add_dfForm():
    row = pd.DataFrame({
            'naam':[st.session_state.input_naam],
            'wit':[st.session_state.input_wit],
            'rood':[st.session_state.input_rood],
            'blauw':[st.session_state.input_blauw],
            'groen':[st.session_state.input_groen],
            'zwart':[st.session_state.input_zwart]}
            'buy-in (in €)':[st.session_state.input_buyin],)
    st.session_state.data = pd.concat([st.session_state.data, row])


dfForm = st.form(key='dfForm')
with dfForm:
    dfColumns = st.columns(4)
    with dfColumns[0]:
        st.text_input('naam', key='input_naam')
    with dfColumns[1]:
        st.text_input('wit', key='input_wit')
    with dfColumns[2]:
        st.text_input('rood', key='input_rood')
    with dfColumns[3]:
        st.text_input('blauw', key='input_blauw')
    with dfColumns[4]:
        st.text_input('groen', key='input_groen')
    with dfColumns[5]:
        st.text_input('zwart', key='input_zwart')
    with dfColumns[6]:
        st.text_input('zwart', key='input_buyin')
    st.form_submit_button(on_click=add_dfForm)
