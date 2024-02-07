from dotenv import load_dotenv
load_dotenv() #load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#Configure the API Key
genai.configure(api_key=os.getenv("api_key"))

#Function to load Google Gemini model and provode query as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

#Function to retrieve query from SQL DB

def read_sql_query(sql,db):
    con=sqlite3.connect(db)
    cur=con.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    con.commit()
    con.close()
    for i in rows:
        print(i)
    return rows

#Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in CS class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="CS"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

#Streamlit App

st.set_page_config(page_title="Retrieve any SQL query")
st.header("LLM App To Retrieve SQL Data")

question=st.text_input("Query: ",key="input")

submit=st.button("Enter")

# Submit
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is: ")
    for row in response:
        print(row)
        st.header(row)
