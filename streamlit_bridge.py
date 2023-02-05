import streamlit as st
import pandas as pd
import PokerCount as pc

st.write('# de PokerCount van Rons')

if 'data' not in st.session_state:
    data = pd.DataFrame({'naam':[],'wit':[],'rood':[],'blauw':[],'groen':[],'zwart':[],'buyin':[]})
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
            'zwart':[st.session_state.input_zwart],
            'buyin':[st.session_state.input_buyin]})
    st.session_state.data = pd.concat([st.session_state.data, row])


dfForm = st.form(key='dfForm')
with dfForm:
    dfColumns = st.columns(7)
    with dfColumns[0]:
        st.text_input('NAAM', key='input_naam')
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
        st.text_input('BUY-IN (in €)', key='input_buyin')

    st.form_submit_button(on_click=add_dfForm)


chip_values = [0.05, 0.1, 0.2, 0.4, 1.0]

# players = [{"name": "Bram", "buy_in": 10, "end_score": [21,3,4,3,4]},
#            {"name": "Lukas", "buy_in": 10, "end_score": [21,22,12,15,4]},
#            {"name": "Rens", "buy_in": 10, "end_score": [8, 20, 11, 6, 5]},
#             {"name": "Brandt", "buy_in": 10, "end_score": [16, 4, 17, 9, 3]},
#            {"name": "Mojet", "buy_in": 10, "end_score": [2, 7, 10, 0, 1]}]

players = list()

data.set_index('naam')
for k, v in data.iterrows():
    player = {}
    player['name'] = v['naam'] 

    player['end_score'] = [int(v['wit']), int(v['rood']), int(v['blauw']), int(v['groen']), int(v['zwart'])]
    player['buy_in'] = int(v['buyin'])
    players.append(player)

if st.button('Bereken!'):
    winnings_losses = pc.calculate_winners(players, chip_values)
    
    output = pc.distribute_losses(winnings_losses)
    
    st.write(output)