import json
import requests
import mysql.connector
from streamlit_option_menu import option_menu
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.switch_page_button import switch_page
import airport
from datetime import date
cnx = mysql.connector.connect(
    user="root",
    password="Krishna@9011",
    # password="Titanium@16",
    host="localhost",
    database="airport"
)
cursor = cnx.cursor()

st.header("Booking Preview")
st.divider()
if "src1" and "dest1" and "date1" not in st.session_state:
    st.success("Booking Confirmed")
    switch_page("airport")
else:
    with st.container():
        col1, col2, col3 =st.columns(3)
        
        with col1:
            
            # st.success(" {} SignUp Successfully ".format(st.session_state.name1))
            query_flightno = """select city from source_dest where airport_id = %s;"""
            val = (st.session_state.src1,)
            cursor.execute(query_flightno,val)
            flres = cursor.fetchall()
            for row in flres:
                st.subheader(row[0])
            query_flightno = """select airport_name from source_dest where airport_id = %s;"""
            val = (st.session_state.src1,)
            cursor.execute(query_flightno,val)
            flres = cursor.fetchall()
            for row in flres:
                st.write(row[0])
            query_flightno = """select fd.flight_id from flight_details fd inner join 
                                        flight_ids fid on fd.flight_id=fid.flight_id where
                                        (fid.source_id=%s and fid.destination_id=%s) and fd.date=%s;"""
            val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1,)
            cursor.execute(query_flightno,val)
            flres = cursor.fetchall()
            for row in flres:
                st.subheader(row[0])
            query_flightno = """select fd.departure_time from flight_details fd inner join 
                                        flight_ids fid on fd.flight_id=fid.flight_id where
                                        (fid.source_id=%s and fid.destination_id=%s) and fd.date=%s;"""
            val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1,)
            cursor.execute(query_flightno,val)
            flres = cursor.fetchall()
            for row in flres:
                st.write(row[0])
            query_flightno = """select fd.airline from flight_details fd inner join 
                                        flight_ids fid on fd.flight_id=fid.flight_id where
                                        (fid.source_id=%s and fid.destination_id=%s) and fd.date=%s;"""
            val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1,)
            cursor.execute(query_flightno,val)
            flres = cursor.fetchall()
            for row in flres:
                st.write(row[0])
            
            st.write("Number of passengers: ")
            st.write(st.session_state.pass_number)
            with col2:
                st.subheader("To")
            
            with col3:
                query_flightno = """select city from source_dest where airport_id = %s;"""
                val = (st.session_state.dest1,)
                cursor.execute(query_flightno,val)
                flres = cursor.fetchall()
                for row in flres:
                    st.subheader(row[0])
                query_flightno = """select airport_name from source_dest where airport_id = %s;"""
                val = (st.session_state.dest1,)
                cursor.execute(query_flightno,val)
                flres = cursor.fetchall()
                for row in flres:
                    st.write(row[0])
                query_flightno = """select fd.price from flight_details fd inner join 
                                        flight_ids fid on fd.flight_id=fid.flight_id where
                                        (fid.source_id=%s and fid.destination_id=%s) and fd.date=%s;"""
                val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1,)
                cursor.execute(query_flightno,val)
                flres = cursor.fetchall()
                for row in flres:
                        st.subheader(int(row[0])*st.session_state.pass_number)
                        price=int(row[0])*st.session_state.pass_number
                query_flightno = """select fd.arrival_time from flight_details fd inner join 
                                        flight_ids fid on fd.flight_id=fid.flight_id where
                                        (fid.source_id=%s and fid.destination_id=%s) and fd.date=%s;"""
                val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1,)
                cursor.execute(query_flightno,val)
                flres = cursor.fetchall()
                for row in flres:
                    st.write(row[0])
                query_flightno = """select fd.date from flight_details fd inner join 
                                        flight_ids fid on fd.flight_id=fid.flight_id where
                                        (fid.source_id=%s and fid.destination_id=%s) and fd.date=%s;"""
                val = (st.session_state.src1,st.session_state.dest1,st.session_state.date1,)
                cursor.execute(query_flightno,val)
                flres = cursor.fetchall()
                for row in flres:
                    st.write(row[0])
                
                st.write(st.session_state.option)
            st.write("Click the Below Button For Confirmation")
            if st.button("Confirm"):
                st.success("Booking Confirmed")
            