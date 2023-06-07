import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter_3d(
    df.query("year==2007"),
    x="gdpPercap",
    z="lifeExp",
    y="pop",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    log_y=True,
    size_max=60,
    title="Country Life Expectation vs. GDP per Capita (2007)"
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)
