import streamlit
import pandas
streamlit.title('My parents new healthy diner  🐔')
streamlit.header('My parents new healthy diner 🥑🍞')
streamlit.text('My parents new healthy diner 🥣 🥗 ')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
