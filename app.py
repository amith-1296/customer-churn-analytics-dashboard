import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Page configuration
st.set_page_config(
    page_title="Customer Churn Analytics Dashboard",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #667eea;
    }
    .title-text {
        color: #667eea;
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle-text {
        color: #764ba2;
        font-size: 1.2em;
        text-align: center;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<div class="title-text">🎯 Customer Churn Analytics Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Real-time insights for data-driven decision making</div>', unsafe_allow_html=True)

# Sample data
data = {
    'Geography': ['France', 'Germany', 'Spain'],
    'Churn_Rate': [16.2, 32.4, 16.7],
    'Customers': [2500, 3200, 2100]
}

age_data = {
    'Age_Group': ['20-30', '30-40', '40-50', '50-60'],
    'Churn_Rate': [9.8, 17.5, 56.2, 45.8]
}

product_data = {
    'Products': ['1 Product', '2 Products', '3+ Products'],
    'Churn_Rate': [27.7, 7.6, 82.7]
}

gender_data = {
    'Gender': ['Male', 'Female'],
    'Churn_Rate': [19.2, 21.8]
}

card_type_data = {
    'Card_Type': ['Platinum', 'Gold', 'Silver', 'Diamond'],
    'Churn_Rate': [12.5, 18.3, 28.1, 25.2]
}

satisfaction_data = {
    'Satisfaction': ['Very Low (1)', 'Low (2)', 'Medium (3)', 'High (4-5)'],
    'Churn_Rate': [45.3, 28.7, 8.2, 2.1]
}

tenure_data = {
    'Tenure': ['0-1 Year', '1-2 Years', '2-5 Years', '5+ Years'],
    'Churn_Rate': [42.5, 18.3, 7.8, 2.1]
}

feature_data = {
    'Feature': ['Age', 'Number of Products', 'Balance', 'Is Active Member', 'Geography'],
    'Importance': [0.245, 0.189, 0.156, 0.143, 0.098]
}

# Convert to DataFrames
df_geo = pd.DataFrame(data)
df_age = pd.DataFrame(age_data)
df_product = pd.DataFrame(product_data)
df_gender = pd.DataFrame(gender_data)
df_card = pd.DataFrame(card_type_data)
df_satisfaction = pd.DataFrame(satisfaction_data)
df_tenure = pd.DataFrame(tenure_data)
df_features = pd.DataFrame(feature_data)

# Key Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="📉 Churn Rate", value="20.4%", delta="-2.1%")

with col2:
    st.metric(label="👥 Total Customers", value="10,000", delta="+500")

with col3:
    st.metric(label="✅ Active Members", value="51.5%", delta="+3.2%")

with col4:
    st.metric(label="💰 Avg Balance", value="$76K", delta="+$2K")

st.divider()

# Create tabs for better organization
tab1, tab2, tab3 = st.tabs(["📊 Overview", "🔍 Detailed Analysis", "📈 Predictors"])

with tab1:
    st.subheader("Key Churn Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Geography
        fig_geo = px.bar(
            df_geo,
            x='Geography',
            y='Churn_Rate',
            title='📍 Churn Rate by Geography',
            color='Churn_Rate',
            color_continuous_scale='RdYlGn_r',
            labels={'Churn_Rate': 'Churn Rate (%)', 'Geography': 'Region'},
            text='Churn_Rate'
        )
        fig_geo.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        st.plotly_chart(fig_geo, use_container_width=True)
    
    with col2:
        # Age Group
        fig_age = px.bar(
            df_age,
            x='Age_Group',
            y='Churn_Rate',
            title='👤 Churn Rate by Age Group',
            color='Churn_Rate',
            color_continuous_scale='Blues',
            labels={'Churn_Rate': 'Churn Rate (%)', 'Age_Group': 'Age Group'},
            text='Churn_Rate'
        )
        fig_age.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        st.plotly_chart(fig_age, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        # Product Count
        fig_product = px.bar(
            df_product,
            x='Products',
            y='Churn_Rate',
            title='📦 Churn by Product Count',
            color='Churn_Rate',
            color_continuous_scale='Purples',
            labels={'Churn_Rate': 'Churn Rate (%)', 'Products': 'Product Count'},
            text='Churn_Rate'
        )
        fig_product.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        st.plotly_chart(fig_product, use_container_width=True)
    
    with col4:
        # Gender
        fig_gender = px.bar(
            df_gender,
            x='Gender',
            y='Churn_Rate',
            title='👤 Churn by Gender',
            color='Churn_Rate',
            color_continuous_scale='Viridis',
            labels={'Churn_Rate': 'Churn Rate (%)', 'Gender': 'Gender'},
            text='Churn_Rate'
        )
        fig_gender.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        st.plotly_chart(fig_gender, use_container_width=True)

with tab2:
    st.subheader("Detailed Churn Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Card Type
        fig_card = px.bar(
            df_card,
            x='Card_Type',
            y='Churn_Rate',
            title='💳 Churn by Card Type',
            color='Churn_Rate',
            color_continuous_scale='Reds',
            labels={'Churn_Rate': 'Churn Rate (%)', 'Card_Type': 'Card Type'},
            text='Churn_Rate'
        )
        fig_card.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        st.plotly_chart(fig_card, use_container_width=True)
    
    with col2:
        # Satisfaction Level
        fig_satisfaction = px.bar(
            df_satisfaction,
            x='Satisfaction',
            y='Churn_Rate',
            title='😊 Satisfaction vs Churn',
            color='Churn_Rate',
            color_continuous_scale='RdYlGn_r',
            labels={'Churn_Rate': 'Churn Rate (%)', 'Satisfaction': 'Satisfaction Level'},
            text='Churn_Rate'
        )
        fig_satisfaction.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        st.plotly_chart(fig_satisfaction, use_container_width=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        # Tenure
        fig_tenure = px.bar(
            df_tenure,
            x='Tenure',
            y='Churn_Rate',
            title='⏳ Churn by Tenure',
            color='Churn_Rate',
            color_continuous_scale='Greens',
            labels={'Churn_Rate': 'Churn Rate (%)', 'Tenure': 'Customer Tenure'},
            text='Churn_Rate'
        )
        fig_tenure.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        st.plotly_chart(fig_tenure, use_container_width=True)
    
    with col4:
        # Summary statistics
        st.info("""
        ### 📊 Key Insights
        
        - **Highest Churn**: Customers with 3+ products (82.7%)
        - **Lowest Satisfaction**: Very Low satisfaction has highest churn (45.3%)
        - **Geographic Risk**: Germany shows highest churn (32.4%)
        - **Tenure Impact**: New customers (0-1 year) most likely to churn (42.5%)
        - **Gender**: Minimal difference between genders (19.2% vs 21.8%)
        """)

with tab3:
    st.subheader("Top Churn Predictors")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig_features = px.bar(
            df_features.sort_values('Importance', ascending=True),
            y='Feature',
            x='Importance',
            orientation='h',
            title='⭐ Feature Importance for Churn Prediction',
            color='Importance',
            color_continuous_scale='Viridis',
            labels={'Importance': 'Importance Score', 'Feature': 'Feature'},
            text='Importance'
        )
        fig_features.update_traces(texttemplate='%{text:.3f}', textposition='outside')
        st.plotly_chart(fig_features, use_container_width=True)
    
    with col2:
        st.success("""
        ### 🎯 Recommendations
        
        1. **Focus on Age**: Strongest predictor
        2. **Retain Active Members**: Higher activity = lower churn
        3. **Optimize Products**: Balance is important
        4. **Monitor Geography**: Geographic targeting needed
        5. **Early Engagement**: Critical in first year
        """)

st.divider()

# Footer
st.markdown("""
---
### 📌 About This Dashboard
This Customer Churn Analytics Dashboard provides actionable insights into customer churn patterns across multiple dimensions.
Use these insights to develop targeted retention strategies and improve customer lifetime value.

**Dataset**: Customer Churn Analysis | **Last Updated**: November 2024
""")
