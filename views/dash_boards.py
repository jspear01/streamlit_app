import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIG ---
st.title("📊 H-1B Data Dashboard")
st.write("Exploring H-1B employer data across fiscal years.")

# --- DATA LOADING ---
@st.cache_data
def load_data():
    file_path = "data/employerinformation.csv"
    # Load data
    #df = pd.read_csv(file_path, sep='\t', encoding='utf-16', low_memory=False)
    df = pd.read_csv(file_path, sep='\t', encoding='latin1', low_memory=False)
    
    # Cleaning column names: trim, lower, snake_case
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Numeric conversions for approval/denial columns (removing commas)
    cols_to_fix = [
        'new_employment_approval', 'new_employment_denial', 
        'continuation_approval', 'continuation_denial',
        'change_of_employer_approval', 'change_of_employer_denial'
    ]
    
    for col in cols_to_fix:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce').fillna(0).astype(int)
            
    # Drop rows without an employer name
    df = df.dropna(subset=['employer_(petitioner)_name'])
    return df

# Load the data
with st.spinner("Loading data..."):
    df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Options")
years = sorted(df['fiscal_year'].unique())
selected_year = st.sidebar.selectbox("Select Fiscal Year", ["All"] + list(years))

# Filter dataframe based on selection
if selected_year != "All":
    filtered_df = df[df['fiscal_year'] == selected_year]
else:
    filtered_df = df

# --- KPI METRICS ---
st.subheader(f"Key Metrics for {selected_year if selected_year != 'All' else 'All Years'}")
col1, col2, col3 = st.columns(3)

total_approvals = filtered_df['new_employment_approval'].sum()
total_denials = filtered_df['new_employment_denial'].sum()
# Basic approval rate calculation
total_adjudications = total_approvals + total_denials
approval_rate = (total_approvals / total_adjudications) * 100 if total_adjudications > 0 else 0

col1.metric("New Approvals", f"{total_approvals:,}")
col2.metric("New Denials", f"{total_denials:,}")
col3.metric("Approval Rate", f"{approval_rate:.2f}%")

# --- VISUALIZATIONS ---

# 1. Trend of Approvals over years (Line Chart)
st.markdown("---")
st.subheader("📈 Trend of H-1B Approvals")
yearly_data = df.groupby('fiscal_year')['new_employment_approval'].sum().reset_index()
fig_trend = px.line(
    yearly_data, 
    x='fiscal_year', 
    y='new_employment_approval',
    title="Total New Employment Approvals by Fiscal Year",
    labels={'new_employment_approval': 'Approvals', 'fiscal_year': 'Year'},
    markers=True,
    template="plotly_dark"
)
st.plotly_chart(fig_trend, use_container_width=True)

# 2. Top Employers (Horizontal Bar Chart)
st.markdown("---")
st.subheader(f"🏆 Top 10 Employers in {selected_year if selected_year != 'All' else 'All Years'}")
top_employers = (
    filtered_df.groupby('employer_(petitioner)_name')['new_employment_approval']
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_employers = px.bar(
    top_employers,
    x='new_employment_approval',
    y='employer_(petitioner)_name',
    orientation='h',
    title="Top 10 Employers by New Approvals",
    labels={'new_employment_approval': 'Approvals', 'employer_(petitioner)_name': 'Employer'},
    color='new_employment_approval',
    color_continuous_scale='Blues',
    template="plotly_dark"
)
# Order from highest to lowest on Y axis
fig_employers.update_layout(yaxis={'categoryorder':'total ascending'})
st.plotly_chart(fig_employers, use_container_width=True)

# 3. Industry Distribution (Pie Chart)
st.markdown("---")
st.subheader("🏢 Industry Distribution")
industry_data = filtered_df.groupby('industry_(naics)_code').size().reset_index(name='count')
# Focus on Top 10 industries
top_industries = industry_data.sort_values('count', ascending=False).head(10)

fig_pie = px.pie(
    top_industries, 
    values='count', 
    names='industry_(naics)_code',
    title="Distribution of Petitions by Top 10 Industries",
    hole=0.4,
    template="plotly_dark"
)
st.plotly_chart(fig_pie, use_container_width=True)

# --- DATA TABLE ---
st.markdown("---")
if st.checkbox("Show Raw Data Sample"):
    st.write(filtered_df.head(100))
