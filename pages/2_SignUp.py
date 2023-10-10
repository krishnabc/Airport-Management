import streamlit as st 
import mysql.connector
st.title("Sign Up")

cnx = mysql.connector.connect(
    user="root",
    password="Krishna@9011",
    # password="Titanium@16",
    host="localhost",
    database="airport"
)
cursor = cnx.cursor()
def admin(username,password):
    sql = "select pwd from admin where username = %s"
    value = (username,)
    cursor.execute(sql,value)
    pwd = cursor.fetchall()
    if pwd[0][0] == password:
        return True
    else:
        return False

with st.form(key='form1'):
                    # Taking input details
                    NAME=st.text_input("NAME",key="name1")                  
                    EMAIL_ID=st.text_input("EMAIL_ID")
                    PHONE=st.text_input("PHONE")
                    PASSWORD=st.text_input(label="Password",type='password')

                    submit_button=st.form_submit_button(label="SignUp")
                    if submit_button:
                        query=('insert into userdetails' '(NAME,PHONE,EMAIL)' 'values(%s,%s,%s)')
                        values=(NAME,PHONE,EMAIL_ID)
                        cursor.execute(query,values)
                        cnx.commit()

                        sq=('select id from userdetails where email=%s')
                        values1=(EMAIL_ID,)
                        cursor.execute(sq,values1)                     
                        id = cursor.fetchall()
                        st.write(id)

                        query1=('insert into users' '(username,PASSWORD,user_id)' 'values(%s,md5(%s),%s)')
                        values1=(EMAIL_ID,PASSWORD,id[0][0])
                        cursor.execute(query1,values1)
                        cnx.commit()


                        # st.success('Sign Up Successfull')
                        st.success(" {} SignUp Successfully ".format(NAME))