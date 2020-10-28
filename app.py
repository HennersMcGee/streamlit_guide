from vega_datasets import data
import streamlit as st
import altair as alt
from test_env_var import env_var_exist

def main():
    df = load_data()
    page = st.sidebar.selectbox("Choose a page", ["Homepage", "Env Var"])

    if page == "Homepage":
        st.header("This is your data explorer.")
        st.write("Please select a page on the left.")
        st.write(df)
    elif page == "Exploration":
        st.title("Data Exploration")
        x_axis = st.selectbox("Choose a variable for the x-axis", df.columns, index=3)
        y_axis = st.selectbox("Choose a var for the y-axis", df.columns, index=4)
        visualize_data(df, x_axis, y_axis)
    elif page == "Env Var":
        st.title("Enviroment Variable")
        var_input = st.text_input("Name of enviroment variable to search for: ", "test_var1")
        env_var_exist(var_input)


@st.cache
def load_data():
    df = data.cars()
    return df

def visualize_data(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle(size=60).encode(
        x=x_axis,
        y=y_axis,
        color='Origin',
        tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
    ).interactive()

    st.write(graph)

if __name__ == "__main__":
    main()

