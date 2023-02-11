import streamlit as st
from House import House

if 'house' not in st.session_state:
    st.session_state['house'] = House()

house = st.session_state['house']


def open_door():
    if house.is_door_closed():
        house.open_door()
        house.process_moment()
        st.session_state['action'] = 'door is now open'
    else:
        do_nothing()


def close_door():
    if house.is_door_open():
        house.close_door()
        house.process_moment()
        st.session_state['action'] = 'door is now closed'
    else:
        do_nothing()


def start_heating():
    if house.is_heating_off():
        house.start_heating()
        house.process_moment()
        st.session_state['action'] = 'heating is now on'
    else:
        do_nothing()


def stop_heating():
    if house.is_heating_on():
        house.stop_heating()
        house.process_moment()
        st.session_state['action'] = 'heating is now off'
    else:
        do_nothing()


def do_nothing():
    house.process_moment()
    st.session_state['action'] = "you've done nothing"


st.title('House')

st.write('The house has one door, two windows, and a heating unit.')

st.subheader('What do you want to do?')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.button("Open the door", on_click=open_door)

with col2:
    st.button("Close the door", on_click=close_door)

with col3:
    st.button("Turn on the heating", on_click=start_heating)

with col4:
    st.button("Turn off the heating", on_click=stop_heating)

with col5:
    st.button("Do nothing", on_click=do_nothing)


st.write(f"the door is {house.door}\n")
st.write(f"the heating is {house.heating}")
st.write(f"the temp is {house.temp}C")

if 'action' in st.session_state:
    st.info(st.session_state['action'])