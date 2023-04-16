import streamlit
import requests
import pandas
import snowflake.connector
from urllib.error import URLError
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

def get_fruit_load_list(my_cnx):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('from streamlit')")
    return "Thanks for adding " + new_fruit
    
# streamlit.title('My parents new healthy diner  🐔')
#streamlit.header('My parents new healthy diner 🥑🍞')
#streamlit.text('My parents new healthy diner 🥣 🥗 ')
#streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list = my_fruit_list.set_index('Fruit')
#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Avocado'])
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
# write your own comment -what does the next line do? 
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
   streamlit.error()
# streamlit.stop()
if streamlit.button("Get Fruit Load List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list(my_cnx)
  streamlit.dataframe(my_data_rows)
add_my_fruit = streamlit.text_input('What fruit would you like information about?')
if streamlit.button("Add a Fruit to the List"):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(fruit_choice)
  streamlit.text(back_from_function)

#add_my_fruit = streamlit.text_input('What fruit would you like information about?')
#streamlit.write("Thanks for adding" ,add_my_fruit);
#my_cur.execute("insert into fruit_load_list values('from streamlit')");
