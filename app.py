import pandas as pd
import streamlit as st
import plotly.express as px

# Setting page configuration
st.set_page_config(
    page_title="Sales Dashboard",
    page_icon=":chart_with_upwards_trend:",
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
st.markdown('<div class="center header"><h1>Global Sales Dashboard<h1></div>', unsafe_allow_html=True)
st.markdown('<div class="center subheader"><h3>Analyze Your Sales Data<h3></div>', unsafe_allow_html=True)

# Read the data
sales_data = pd.read_excel("cleaned_dataset.xlsx", engine='openpyxl')

# Define chart configurations
charts_info = [
    {"type": "box", "x": "Sub-Category", "y": "Quantity", "title": "Box Plot", "color": "Sub-Category"},
    {"type": "bar", "x": "Ship Mode", "y": "Shipping Cost", "title": "Bar Chart", "color": "Ship Mode"},
    {"type": "pie", "names": "Order Priority", "title": "Donut Chart", "hole": 0.5},
]

# Create and display charts in the same line
col1, col2, col3 = st.columns(3)

for index, info in enumerate(charts_info):
    with eval(f"col{index+1}"):
        if "type" in info:
            try:
                if info["type"] == "pie":
                    fig = getattr(px, info["type"])(sales_data, names=info.get("names"), title=info.get("title"), hole=info.get("hole", 0.5))
                else:
                    fig = getattr(px, info["type"])(sales_data, x=info.get("x"), y=info.get("y"), title=info.get("title"), color=info.get("color"))
                st.plotly_chart(fig, use_container_width=True)
            except KeyError:
                st.write("Invalid chart configuration: ", info)
                continue
        else:
            st.write("Invalid chart configuration: ", info)

# Close bordered container
st.markdown("</div>", unsafe_allow_html=True)
