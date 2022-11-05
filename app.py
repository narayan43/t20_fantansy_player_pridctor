import streamlit as st
import pickle
import pandas as pd
df=pd.read_csv('./data_frame.csv')
players=df['player_name'].unique()
apponent_team=df['appo_team'].unique()
vanues=df['Vanue'].unique()

# Title of the app
st.title("T20 Fintasy Pridctor")

#Player sellector
st.subheader('Ist team selectors')
player_s1 = st.multiselect(
    'Sellect players of singel Team1',
    players,
    players[0])
# sellect the team 
appo_team1=st.selectbox(
    "Sellect the Apponent team1",
    apponent_team,
)
# sellect the team 
inning1=st.selectbox(
    "Sellect the Inning of team1",
    [0,1]
)

# Sellect Data for  Second team 

st.subheader('2nd team selectors')
player_s2 = st.multiselect(
    'Sellect players of singel Team2',
    players,
    players[0])
# sellect the team 
appo_team2=st.selectbox(
    "Sellect the Apponent team2",
    apponent_team,
)
# sellect the team 
inning2=st.selectbox(
    "Sellect the Inning of team2",
    [0,1]
)
st.subheader('Sellect the vanue for the match')
vanue=st.selectbox(
    'Sellect the vanue for the match',
    vanues
)
# Predction section ------  ➠
button=st.button('Predict')
if button == True:
    players_dict_list=[]
    def func(pl_list,team,inning):
        for player in pl_list:
            dic={"player_name":None,"appo_team":None,'Vanue':None,'inning':None}
            dic['appo_team']=team
            dic['inning']=inning
            dic['player_name']=player
            dic['Vanue']=vanue
            players_dict_list.append(dic)
    func(player_s1,appo_team1,inning1)
    func(player_s2,appo_team2,inning2)
    new_data=pd.DataFrame(players_dict_list)
    model = pickle.load(open('./model.pkl', 'rb'))
    y_pred=model.predict(new_data)
    pred_data=pd.DataFrame(y_pred,columns=['runs',"wick"])
    data=new_data.iloc[:,:-3].merge(pred_data,left_index=True,right_index=True)
    col1, col2 = st.columns(2)

    with col1:
        st.header("Most runs by players")
        st.write(data[['player_name','runs']].sort_values(by="runs",ascending=False))

    with col2:
        st.header("Most wick by players")
        st.write(data[['player_name','wick']].sort_values(by="wick",ascending=False))
