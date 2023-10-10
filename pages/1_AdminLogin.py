import json
import requests
import mysql.connector
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_lottie import st_lottie

loginSection = st.container()
headerSection = st.container()

dataFrameSerialization = "legacy"


# st.title("Admin Login")
cnx = mysql.connector.connect(
    user="root",
    password="Krishna@9011",
    #  password="Titanium@16",
    host="localhost",
    database="airport"
)
cursor = cnx.cursor(buffered=True)
def admin(username,password):
    sql = "select password from users where username = %s and user_id = 1 "
    value = (username,)
    cursor.execute(sql,value)
    passw = cursor.fetchall()
   
    st.write(passw[0][0])
    sql1 = "select md5(%s)"
    value1 = (password,)
    cursor.execute(sql1,value1)
    md5passw = cursor.fetchall()
    
    st.write(md5passw[0][0])
    if md5passw[0][0] == passw[0][0]:
        return True
    else:
        return False

def aLoggedInClicked(username,password):
    if admin(username,password):
        st.success("Login Successful")
        st.session_state['aloggedIn'] = True
    else:
        st.session_state['aloggedIn'] = False
        st.error("Invalid creds")

def admin_login():
    # st.write("lsf")
    with loginSection:
        if st.session_state['aloggedIn'] == False:
            st.header("Admin Login") 
            username = st.text_input(label="Username")
            password = st.text_input(label="Password",type='password')
            st.button("Login",on_click=aLoggedInClicked,args=(username,password))

with headerSection:
    url = requests.get("https://assets1.lottiefiles.com/packages/lf20_npJF362rsV.json")
    url_json = dict()
    if url.status_code == 200:
        url_json = url.json()
    st.title("AIRLINE MANAGEMENT SYSTEM :airplane:")
    st_lottie(url_json)

    if 'aloggedIn'not in st.session_state:
        st.session_state['aloggedIn']=False
        # st.write("check1")
        admin_login()
    else:
        if st.session_state['aloggedIn']:
            tab1, tab2 =st.tabs(["Add_Flight","Remove_Flight"])
            with tab1:
                st.subheader("Add Flights")
                with st.form(key='form1'):
                    Flight_id=st.text_input("Flight_id")
                    # Source=st.text_input("Source")
                    Source_id=st.text_input("Source_id")
                    # Scity=st.text_input("Scity")
                    # Destination=st.text_input("Destination")
                    Destination_id=st.text_input("Destination_id")
                    # Destination_City=st.text_input("Destination_City")
                    Departure_time=st.time_input("Departure_time")
                    Arrival_time=st.time_input("Arrival_time")
                    Price=st.text_input("Price")
                    Date=st.date_input(label="date")
                    Airline=st.text_input("Airline")

                    submit_button=st.form_submit_button(label="Add")
                    if submit_button:
                        # query=('INSERT INTO FLIGHT_IDS (FLIGHT_ID,SOURCE_ID,DESTINATION_ID)' 'VALUES (%s,%s,%s);')
                        # values=(Flight_id,Source_id,Destination_id)
                        # cursor.execute(query,values)
                        # cnx.commit()
                        # query=('INSERT INTO FLIGHT_DETAILS(FLIGHT_ID,DEPARTURE_TIME,ARRIVAL_TIME,PRICE,DATE,AIRLINE)' 'VALUES(%s,%s,%s,%s,%s,%s)')
                        # values=(Flight_id,Departure_time,Arrival_time,Price,Date,Airline)
                        # cursor.execute(query,values)
                        # cnx.commit()
                        query=('call Insert_Flight_Details(%s,%s,%s,%s,%s,%s,%s,%s)' )
                        values=(Flight_id,Departure_time,Arrival_time,Price,Date,Airline,Source_id,Destination_id)
                        cursor.execute(query,values)
                        cnx.commit()
                        
                        # cursor.close()
                        # cnx.close()
                        # cursor=cnx.cursor()
                        # cursor.execute(query,arg)
                        # cnx.commit()
                        st.success("Successfully {} Flight Added".format(Flight_id))
            if st.button("loggout"):
                st.session_state['aloggedIn']=False
                admin_login()
                st.success("Successfully LoggedOut")


            with tab2:
                if st.button("Show Flights"):
                    query = """SELECT * FROM FLIGHT_DETAILS F1 INNER JOIN FLIGHT_IDS F2 ON F1.FLIGHT_ID=F2.FLIGHT_ID
                                INNER JOIN SOURCE_DEST S ON F2.SOURCE_ID=S.AIRPORT_ID
                                INNER JOIN SOURCE_DEST S1 ON F2.DESTINATION_ID=S1.AIRPORT_ID;"""
                    cursor.execute(query)
                    flres = cursor.fetchall()
                    st.dataframe(flres)
                    # for row in flres:
                    #     st.table(row)
                

                f_id=st.text_input("Enter FLIGHT_ID")
                del_button=st.button(label="Delete")
                if del_button:
                    cursor.execute( "Select delete_flight_details('%s')" % f_id)
                    cnx.commit()
                    st.success("Successfully Deleted Flight {}".format(f_id))

        else:
            admin_login()

        


        