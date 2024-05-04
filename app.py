import pandas as pd
import streamlit as st
import plotly.express as px

# Import Data
df = pd.read_excel("cleaned_dataset.xlsx", engine='openpyxl')

# Set Page Configuration
st.set_page_config(page_title="Dashboard", page_icon=":bar_chart:", layout="wide")

# Custom CSS to Style the Dashboard
st.markdown("""
    <style>
        .center {
            text-align: center;
        }
        .bordered {
            border: 2px solid #ddd;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 10px;
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            background-color: #f9f9f9;
        }
    </style>
""", unsafe_allow_html=True)

# Bordered Container for the Entire Dashboard
st.markdown('<div class="bordered">', unsafe_allow_html=True)

# Main Header and Subheader
st.markdown('<div class="center header"><h1>Global Superstore Dashboard</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="center subheader"><h3>An Analysis of Sales Data</h3></div>', unsafe_allow_html=True)

# Creating Three-Column Layout
col1, col2, col3 = st.columns(3)

# Visualizations
fig_box = px.box(df, x='Sub-Category', y='Quantity', title='Box Plot')
fig_box.update_traces(marker=dict(color='green'))

fig_bar = px.bar(df, x='Ship Mode', y='Shipping Cost', title='Bar Chart')
fig_bar.update_traces(marker=dict(color='#eba434'))

fig_donut = px.pie(df, names='Order Priority', title='Donut Chart', hole=0.5)

fig_hist = px.histogram(df, x='Region', title='Histogram')
fig_hist.update_traces(marker=dict(color='#800080'))

fig_area = px.area(df, x='Market', y='Profit', title='Area Chart')

sales_by_country = df.groupby('Country')['Sales'].sum().reset_index()
top_10_countries = sales_by_country.nlargest(10, 'Sales')
df_top_10_countries = df[df['Country'].isin(top_10_countries['Country'])]
fig_heatmap_top_10 = px.density_heatmap(df_top_10_countries, x='Country', y='Sales', title='Heatmap of Top 10 Countries in Sales', color_continuous_scale='reds')

# Display Visualizations
with col1:
    st.plotly_chart(fig_box, use_container_width=True)
    st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    st.plotly_chart(fig_bar, use_container_width=True)
    st.plotly_chart(fig_area, use_container_width=True)

with col3:
    st.plotly_chart(fig_donut, use_container_width=True)
    st.plotly_chart(fig_heatmap_top_10, use_container_width=True)