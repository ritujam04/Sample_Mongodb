import pymongo
import streamlit as st

ur = "mongodb+srv://rituja0412:FjUH75668F6XouHM@cluster0.r2uid.mongodb.net/sample_database?retryWrites=true&w=majority"

client = pymongo.MongoClient(ur)

db = client["sample_database"]

collection = db['sample1']

st.title("Sample MangoDB Project")

st.write("Enter your Info: ")
name = st.text_input("Name: ")
roll = st.number_input("Roll No.: ")
bt = st.button("Save")
record = {
    "name": name,
    "Roll": roll
}

if bt:
    collection.insert_one(record)
    st.write("Data Inserted Successfully")