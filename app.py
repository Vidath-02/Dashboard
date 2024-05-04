import pandas as pd
import streamlit as st
import plotly.express as px

# Setting page configuration
st.set_page_config(
    page_title="Dashboard",
    page_icon=":bar_chart:",
    layout="wide"
)

# Custom CSS to style the dashboard
st.markdown(
    """
    <style>
        /* Center align the main header and subheader */
        .center {
            text-align: center;
        }
        
        /* Add padding to the bordered container */
        .bordered {
            border: 2px solid #ddd;  /* Add a light gray border */
            border-radius: 10px;  /* Add border radius for rounded corners */
            padding: 20px;
            margin-bottom: 10px;  /* Add some space between elements */
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Add a shadow effect */
            background-color: #f9f9f9; /* Light gray background color */
        }       
    </style>
    """,
    unsafe_allow_html=True
)

# Bordered container for the entire dashboard
st.markdown('<div class="bordered">', unsafe_allow_html=True)

# Main header and subheader
st.markdown('<div class="center header"><h1>Global Superstore Dashboard<h1></div>', unsafe_allow_html=True)
st.markdown('<div class="center subheader"><h3>An Analysis of Sales Data<h3></div>', unsafe_allow_html=True)

# Read the data
df = pd.read_excel("cleaned_dataset.xlsx", engine='openpyxl')

# Creating three-column layout
col1, col2, col3 = st.columns(3)

# Box Plot
with col1:
        fig_box = px.box(df, x='Sub-Category', y='Quantity', title='Box Plot')
        fig_box.update_traces(marker=dict(color='green'))
        st.plotly_chart(fig_box, use_container_width=True)

# Bar Chart
with col2:
        fig_bar = px.bar(df, x='Ship Mode', y='Shipping Cost', title='Bar Chart')
        fig_bar.update_traces(marker=dict(color='#eba434')) 
        st.plotly_chart(fig_bar, use_container_width=True)

# Donut Chart
with col3:   
        fig_donut = px.pie(df, names='Order Priority', title='Donut Chart', hole=0.5)
        st.plotly_chart(fig_donut, use_container_width=True)

# Histogram
with col1:   
        fig_hist = px.histogram(df, x='Region', title='Histogram')
        fig_hist.update_traces(marker=dict(color='#800080'))
        st.plotly_chart(fig_hist, use_container_width=True)

# Area Chart
with col2:    
        fig_area = px.area(df, x='Market', y='Profit', title='Area Chart')
        st.plotly_chart(fig_area, use_container_width=True)

# Heatmap
with col3:
    sales_by_country = df.groupby('Country')['Sales'].sum().reset_index()
    top_10_countries = sales_by_country.nlargest(10, 'Sales')
    df_top_10_countries = df[df['Country'].isin(top_10_countries['Country'])]
    fig_heatmap_top_10 = px.density_heatmap(df_top_10_countries, x='Country', y='Sales', title='Heatmap of Top 10 Countries in Sales',color_continuous_scale='reds')
    st.plotly_chart(fig_heatmap_top_10, use_container_width=True)

