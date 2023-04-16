import streamlit
import requests
import pandas
streamlit.title('My parents new healthy diner  🐔')
streamlit.header('My parents new healthy diner 🥑🍞')
streamlit.text('My parents new healthy diner 🥣 🥗 ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Avocado'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
streamlit.header("Fruityvice Fruit Advice!")
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)
