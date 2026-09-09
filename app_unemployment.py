import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Unemployment Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Unemployment Analysis with Python")
st.markdown(
    "Explore unemployment trends, COVID-19 impact, monthly patterns, "
    "and policy-related insights."
)

@st.cache_data
def load_data():
    df = pd.read_csv("Unemployment in India.csv")

    # Clean text values
    for col in ["Region", "Date", "Frequency", "Area"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # Clean column names
    df.columns = [str(c).strip() for c in df.columns]

    # Rename columns
    df = df.rename(columns={
        "Region": "State",
        "Estimated Unemployment Rate (%)": "Unemployment_Rate",
        "Estimated Employed": "Employed",
        "Estimated Labour Participation Rate (%)": "Labour_Participation_Rate"
    })

    # Convert data types
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")

    numeric_cols = [
        "Unemployment_Rate",
        "Employed",
        "Labour_Participation_Rate"
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Remove duplicates and missing values
    df = df.drop_duplicates()
    df = df.dropna()

    # Date features
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Month_Name"] = df["Date"].dt.strftime("%b")
    df["Month_Label"] = df["Date"].dt.strftime("%b %Y")

    # COVID period used in the notebook
    df["Period"] = df["Date"].apply(
        lambda x: "Pre-COVID" if x < pd.Timestamp("2020-03-01")
        else "COVID period"
    )

    return df


df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

states = sorted(df["State"].unique())
areas = sorted(df["Area"].unique())
periods = ["Pre-COVID", "COVID period"]

selected_states = st.sidebar.multiselect(
    "Select State/Region",
    states,
    default=states
)

selected_areas = st.sidebar.multiselect(
    "Select Area",
    areas,
    default=areas
)

selected_periods = st.sidebar.multiselect(
    "Select Period",
    periods,
    default=periods
)

filtered_df = df[
    df["State"].isin(selected_states)
    & df["Area"].isin(selected_areas)
    & df["Period"].isin(selected_periods)
]

if filtered_df.empty:
    st.warning("No data matches the selected filters.")
    st.stop()

# KPI section
st.subheader("Dataset Overview")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Records", f"{len(filtered_df):,}")
c2.metric(
    "Average Unemployment",
    f"{filtered_df['Unemployment_Rate'].mean():.2f}%"
)
c3.metric(
    "Average Labour Participation",
    f"{filtered_df['Labour_Participation_Rate'].mean():.2f}%"
)
c4.metric(
    "States/Regions",
    f"{filtered_df['State'].nunique():,}"
)

st.divider()

# Monthly trend
st.subheader("📈 Unemployment Trend")

monthly_trend = (
    filtered_df.groupby("Date", as_index=False)["Unemployment_Rate"]
    .mean()
    .sort_values("Date")
)

fig = px.line(
    monthly_trend,
    x="Date",
    y="Unemployment_Rate",
    markers=True,
    title="Average Monthly Unemployment Rate",
    labels={
        "Date": "Month",
        "Unemployment_Rate": "Unemployment Rate (%)"
    }
)
st.plotly_chart(fig, use_container_width=True)

if not monthly_trend.empty:
    peak = monthly_trend.loc[
        monthly_trend["Unemployment_Rate"].idxmax()
    ]
    lowest = monthly_trend.loc[
        monthly_trend["Unemployment_Rate"].idxmin()
    ]

    st.info(
        f"Highest monthly average: {peak['Unemployment_Rate']:.2f}% "
        f"({peak['Date'].strftime('%b %Y')}). "
        f"Lowest: {lowest['Unemployment_Rate']:.2f}% "
        f"({lowest['Date'].strftime('%b %Y')})."
    )

# State and area analysis
col1, col2 = st.columns(2)

with col1:
    st.subheader("🗺️ Average Unemployment by State/Region")

    state_avg = (
        filtered_df.groupby("State")["Unemployment_Rate"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    fig_state = px.bar(
        state_avg,
        x="State",
        y="Unemployment_Rate",
        title="Average Unemployment Rate by State/Region",
        labels={
            "State": "State/Region",
            "Unemployment_Rate": "Average Unemployment Rate (%)"
        }
    )
    fig_state.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_state, use_container_width=True)

with col2:
    st.subheader("🏙️ Rural vs Urban")

    fig_area = px.box(
        filtered_df,
        x="Area",
        y="Unemployment_Rate",
        color="Area",
        title="Unemployment Rate by Area",
        labels={
            "Area": "Area",
            "Unemployment_Rate": "Unemployment Rate (%)"
        }
    )
    st.plotly_chart(fig_area, use_container_width=True)

# COVID analysis
st.subheader("🦠 COVID-19 Impact")

covid_summary = (
    filtered_df.groupby("Period")["Unemployment_Rate"]
    .agg(["mean", "median", "min", "max", "count"])
    .reindex(["Pre-COVID", "COVID period"])
)

st.dataframe(
    covid_summary.round(2),
    use_container_width=True
)

available_periods = covid_summary.dropna().index.tolist()

if "Pre-COVID" in available_periods and "COVID period" in available_periods:
    pre_mean = covid_summary.loc["Pre-COVID", "mean"]
    covid_mean = covid_summary.loc["COVID period", "mean"]
    change = covid_mean - pre_mean
    percent_change = (change / pre_mean) * 100

    m1, m2, m3 = st.columns(3)
    m1.metric("Pre-COVID", f"{pre_mean:.2f}%")
    m2.metric("COVID period", f"{covid_mean:.2f}%")
    m3.metric("Change", f"{change:.2f} pp", f"{percent_change:.2f}%")

    fig_covid = px.box(
        filtered_df,
        x="Period",
        y="Unemployment_Rate",
        color="Period",
        points="outliers",
        title="Unemployment Rate Before and During the COVID Period",
        labels={
            "Period": "Period",
            "Unemployment_Rate": "Unemployment Rate (%)"
        }
    )
    st.plotly_chart(fig_covid, use_container_width=True)

# Monthly patterns
st.subheader("📅 Monthly Patterns and Seasonal Trends")

monthly_pattern = (
    filtered_df.groupby("Month_Name")["Unemployment_Rate"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

fig_month = px.bar(
    monthly_pattern,
    x="Month_Name",
    y="Unemployment_Rate",
    title="Average Unemployment Rate by Month",
    labels={
        "Month_Name": "Month",
        "Unemployment_Rate": "Average Unemployment Rate (%)"
    }
)
st.plotly_chart(fig_month, use_container_width=True)

st.caption(
    "The dataset covers only 14 months, so the monthly comparison shows "
    "patterns but is not enough to confirm a strong recurring seasonal trend."
)

# Labour market explorer
st.subheader("🔎 Labour Market Explorer")

fig_scatter = px.scatter(
    filtered_df,
    x="Labour_Participation_Rate",
    y="Unemployment_Rate",
    size="Employed",
    color="Area",
    hover_name="State",
    animation_frame="Date",
    title="Labour Participation Rate vs Unemployment Rate",
    labels={
        "Labour_Participation_Rate": "Labour Participation Rate (%)",
        "Unemployment_Rate": "Unemployment Rate (%)",
        "Employed": "Employed"
    }
)
st.plotly_chart(fig_scatter, use_container_width=True)

# Correlation
st.subheader("📊 Labour-Market Correlation")

corr_cols = [
    "Unemployment_Rate",
    "Employed",
    "Labour_Participation_Rate"
]
corr = filtered_df[corr_cols].corr()

fig_corr = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
    title="Correlation Matrix of Labour-Market Indicators"
)
st.plotly_chart(fig_corr, use_container_width=True)

# Policy insights
st.subheader("🏛️ Policy and Social Insights")

st.markdown(
    """
- Governments can provide employment support during economic crises.
- Areas with higher unemployment may need more targeted support.
- Monitoring unemployment rates can help identify problems early.
- Training and job opportunities can help people return to work after economic shocks.
"""
)

# Data
with st.expander("View Cleaned Data"):
    st.dataframe(filtered_df, use_container_width=True)
