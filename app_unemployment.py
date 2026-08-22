import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Unemployment Analytics | India",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# THEME
# Coral + Violet + Peach
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN BACKGROUND
       ===================================================== */

    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(
                circle at 8% 8%,
                rgba(231, 111, 81, 0.28),
                transparent 30%
            ),
            radial-gradient(
                circle at 92% 12%,
                rgba(124, 58, 237, 0.24),
                transparent 32%
            ),
            radial-gradient(
                circle at 48% 96%,
                rgba(244, 162, 97, 0.12),
                transparent 28%
            ),
            linear-gradient(
                135deg,
                #f3ddd5 0%,
                #eadbea 52%,
                #e1dff0 100%
            ) !important;

        min-height: 100vh;
    }


    [data-testid="stHeader"] {
        background: rgba(234, 219, 234, 0.72) !important;
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255,255,255,0.45);
    }


    .block-container {
        padding-top: 1.25rem;
        padding-bottom: 3rem;
    }


    /* =====================================================
       SIDEBAR
       ===================================================== */

    [data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                rgba(232, 211, 205, 0.97) 0%,
                rgba(225, 216, 235, 0.97) 100%
            ) !important;

        border-right: 1px solid rgba(124, 58, 237, 0.14);

        box-shadow:
            5px 0 24px rgba(88, 67, 96, 0.08);
    }


    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4 {
        color: #2b2430 !important;
    }


    [data-testid="stSidebar"] label {
        color: #2b2430 !important;
        font-weight: 700 !important;
    }


    [data-testid="stSidebar"] .stCaption {
        color: #665c68 !important;
    }


    /* =====================================================
       GENERAL TEXT
       ===================================================== */

    [data-testid="stAppViewContainer"] p,
    [data-testid="stAppViewContainer"] li {
        color: #2b2430 !important;
    }


    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        color: #2b2430 !important;
    }


    /* =====================================================
       HEADER
       ===================================================== */

    .eyebrow {
        color: #7c3aed !important;
        font-size: 0.75rem;
        font-weight: 850;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 0.35rem;
    }


    .main-subtitle {
        color: #665c68 !important;
        font-size: 1rem;
        margin-top: -0.35rem;
        margin-bottom: 1.35rem;
    }


    /* =====================================================
       KPI CARDS
       ===================================================== */

    [data-testid="stMetric"] {
        background:
            linear-gradient(
                135deg,
                rgba(247, 241, 237, 0.98),
                rgba(240, 232, 243, 0.96)
            ) !important;

        border: 1px solid rgba(124, 58, 237, 0.16) !important;

        border-radius: 18px !important;

        padding: 1rem !important;

        box-shadow:
            0 10px 25px rgba(76, 53, 91, 0.10);

        transition:
            transform 0.18s ease,
            box-shadow 0.18s ease;
    }


    [data-testid="stMetric"]:hover {
        transform: translateY(-3px);

        box-shadow:
            0 15px 30px rgba(76, 53, 91, 0.15);
    }


    [data-testid="stMetricLabel"] {
        color: #665c68 !important;
        font-weight: 700 !important;
    }


    [data-testid="stMetricValue"] {
        color: #2b2430 !important;
        font-weight: 850 !important;
    }


    [data-testid="stMetricDelta"] {
        color: #e76f51 !important;
        font-weight: 700 !important;
    }


    /* =====================================================
       SELECT / MULTISELECT
       ===================================================== */

    [data-baseweb="select"] > div {
        background:
            rgba(247, 241, 237, 0.96) !important;

        border: 1px solid rgba(107, 91, 111, 0.25) !important;

        color: #2b2430 !important;

        border-radius: 10px !important;
    }


    [data-baseweb="select"] span {
        color: #2b2430 !important;
    }


    [data-baseweb="select"] input {
        color: #2b2430 !important;

        -webkit-text-fill-color: #2b2430 !important;
    }


    /* =====================================================
       TABS
       ===================================================== */

    .stTabs [data-baseweb="tab"] {
        color: #665c68 !important;
        font-weight: 700 !important;
    }


    .stTabs [aria-selected="true"] {
        color: #7c3aed !important;
    }


    /* =====================================================
       INFO / WARNING / SUCCESS
       ===================================================== */

    [data-testid="stAlert"] {
        background:
            linear-gradient(
                135deg,
                rgba(247, 241, 237, 0.96),
                rgba(240, 232, 243, 0.96)
            ) !important;

        border: 1px solid rgba(107, 91, 111, 0.18) !important;

        border-left: 5px solid #e76f51 !important;

        color: #2b2430 !important;

        border-radius: 14px !important;

        box-shadow:
            0 8px 22px rgba(76, 53, 91, 0.07);
    }


    [data-testid="stAlert"] p {
        color: #2b2430 !important;
    }


    /* =====================================================
       DATASET OVERVIEW CARDS
       ===================================================== */

    .overview-card {
        background:
            linear-gradient(
                135deg,
                rgba(247, 241, 237, 0.98),
                rgba(240, 232, 243, 0.96)
            );

        border: 1px solid rgba(124, 58, 237, 0.14);

        border-radius: 16px;

        padding: 1rem;

        min-height: 105px;

        box-shadow:
            0 8px 22px rgba(76, 53, 91, 0.08);
    }


    .overview-label {
        color: #776e7c;

        font-size: 0.78rem;

        font-weight: 700;

        margin-bottom: 0.35rem;
    }


    .overview-value {
        color: #2b2430;

        font-size: 1.25rem;

        font-weight: 850;
    }


    .overview-note {
        color: #8a8190;

        font-size: 0.72rem;

        margin-top: 0.25rem;
    }


    /* =====================================================
       DATA QUALITY NOTE
       ===================================================== */

    .quality-note {
        background:
            linear-gradient(
                135deg,
                rgba(247, 241, 237, 0.97),
                rgba(240, 232, 243, 0.97)
            );

        border-left: 5px solid #7c3aed;

        border-radius: 14px;

        padding: 1rem 1.1rem;

        margin: 0.8rem 0 1.2rem 0;

        color: #2b2430;

        box-shadow:
            0 8px 20px rgba(76, 53, 91, 0.07);
    }


    /* =====================================================
       DOWNLOAD BUTTON
       ===================================================== */

    .stDownloadButton button {
        background:
            linear-gradient(
                135deg,
                #e76f51,
                #7c3aed
            ) !important;

        color: #ffffff !important;

        border: none !important;

        border-radius: 10px !important;

        font-weight: 750 !important;

        box-shadow:
            0 8px 18px rgba(124, 58, 237, 0.18);
    }


    .stDownloadButton button:hover {
        background:
            linear-gradient(
                135deg,
                #d95c3d,
                #6d28d9
            ) !important;
    }


    /* =====================================================
       DATAFRAME
       ===================================================== */

    [data-testid="stDataFrame"] {
        border-radius: 14px !important;

        border: 1px solid rgba(107, 91, 111, 0.18) !important;

        overflow: hidden;
    }


    /* =====================================================
       CAPTION
       ===================================================== */

    [data-testid="stCaptionContainer"] {
        color: #665c68 !important;
    }


    /* =====================================================
       DIVIDER
       ===================================================== */

    hr {
        border-color: rgba(107, 91, 111, 0.20) !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# DATA LOADING
# =========================================================

@st.cache_data
def load_data():

    candidate_paths = [
        Path("Unemployment in India.csv"),
        Path("83bab4c3-8b64-40f4-a929-018f283898c3.csv"),
    ]

    data_path = next(
        (
            p
            for p in candidate_paths
            if p.exists()
        ),
        None
    )

    # Fallback: search local CSV files
    if data_path is None:

        local_csvs = list(
            Path(".").glob("*.csv")
        )

        data_path = next(
            (
                p
                for p in local_csvs
                if "unemployment" in p.name.lower()
            ),
            None
        )

    if data_path is None:

        raise FileNotFoundError(
            "CSV file not found. Place "
            "'Unemployment in India.csv' beside 'app_unemployment.py'."
        )

    # -----------------------------------------------------
    # Read raw data
    # -----------------------------------------------------

    raw_df = pd.read_csv(
        data_path
    )

    # Clean column names
    raw_df.columns = [
        str(c).strip()
        for c in raw_df.columns
    ]

    raw_shape = raw_df.shape

    raw_duplicate_count = int(
        raw_df.duplicated().sum()
    )

    # -----------------------------------------------------
    # Rename columns
    # -----------------------------------------------------

    rename_map = {
        "Region":
            "State",

        "Estimated Unemployment Rate (%)":
            "Unemployment_Rate",

        "Estimated Employed":
            "Employed",

        "Estimated Labour Participation Rate (%)":
            "Labour_Participation_Rate",
    }

    df = raw_df.rename(
        columns=rename_map
    ).copy()

    # Normalize text values before validation / duplicate detection
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    # Count duplicates after text normalization
    normalized_duplicate_count = int(
        df.duplicated().sum()
    )

    # -----------------------------------------------------
    # Check required columns
    # -----------------------------------------------------

    required_columns = [
        "State",
        "Date",
        "Unemployment_Rate",
        "Employed",
        "Labour_Participation_Rate",
        "Area",
    ]

    missing_required_columns = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if missing_required_columns:

        raise ValueError(
            "Required columns are missing: "
            + ", ".join(missing_required_columns)
        )

    # -----------------------------------------------------
    # Date conversion
    # -----------------------------------------------------

    df["Date"] = pd.to_datetime(
        df["Date"],
        dayfirst=True,
        errors="coerce"
    )

    # -----------------------------------------------------
    # Numeric conversion
    # -----------------------------------------------------

    numeric_columns = [
        "Unemployment_Rate",
        "Employed",
        "Labour_Participation_Rate",
    ]

    for col in numeric_columns:

        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    # -----------------------------------------------------
    # Missing required rows
    # -----------------------------------------------------

    missing_required_mask = (
        df[required_columns]
        .isna()
        .any(axis=1)
    )

    missing_required_rows = int(
        missing_required_mask.sum()
    )

    # -----------------------------------------------------
    # Duplicate removal
    # -----------------------------------------------------

    duplicate_mask = df.duplicated()

    df = df.loc[
        ~duplicate_mask
    ].copy()

    # -----------------------------------------------------
    # Remove incomplete rows
    # -----------------------------------------------------

    df = (
        df
        .dropna(
            subset=required_columns
        )
        .copy()
    )

    # -----------------------------------------------------
    # Extra features
    # -----------------------------------------------------

    df["Year"] = (
        df["Date"].dt.year
    )

    df["Month"] = (
        df["Date"].dt.month
    )

    df["Month_Name"] = (
        df["Date"]
        .dt.strftime("%b")
    )

    df["Month_Label"] = (
        df["Date"]
        .dt.strftime("%b %Y")
    )

    # -----------------------------------------------------
    # COVID classification
    # -----------------------------------------------------

    df["Period"] = np.where(
        df["Date"]
        < pd.Timestamp("2020-03-01"),
        "Pre-COVID",
        "COVID period"
    )

    # -----------------------------------------------------
    # Quality summary
    # -----------------------------------------------------

    cleaned_shape = df.shape

    rows_removed = (
        raw_shape[0]
        -
        cleaned_shape[0]
    )

    if len(df) > 0:

        date_min = df["Date"].min()
        date_max = df["Date"].max()

    else:

        date_min = pd.NaT
        date_max = pd.NaT

    state_count = (
        df["State"].nunique()
    )

    area_values = sorted(
        df["Area"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    if "Frequency" in df.columns:

        frequency_values = sorted(
            df["Frequency"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )

    else:

        frequency_values = []

    quality = {
        "raw_rows": raw_shape[0],
        "raw_columns": raw_shape[1],
        "raw_duplicates": normalized_duplicate_count,
        "missing_required_rows": missing_required_rows,
        "cleaned_rows": cleaned_shape[0],
        "rows_removed": rows_removed,
        "state_count": state_count,
        "area_values": area_values,
        "frequency_values": frequency_values,
        "date_min": date_min,
        "date_max": date_max,
    }

    return (
        df,
        raw_df,
        data_path.name,
        quality,
    )


# =========================================================
# LOAD DATA
# =========================================================

try:

    (
        df,
        raw_df,
        file_name,
        quality
    ) = load_data()

except Exception as error:

    st.error(
        f"Could not load the dataset: {error}"
    )

    st.stop()


# =========================================================
# DOWNLOAD HELPER
# =========================================================

def chart_download(
    dataframe,
    filename
):

    st.download_button(
        "⬇️ Download current table (CSV)",

        dataframe.to_csv(
            index=False
        ).encode("utf-8"),

        file_name=filename,

        mime="text/csv",
    )


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    "## 🎛️ Dashboard Controls"
)

st.sidebar.caption(
    f"Loaded: {file_name}"
)

all_states = sorted(
    df["State"]
    .dropna()
    .unique()
)

selected_states = st.sidebar.multiselect(
    "States / regions",

    all_states,

    default=all_states[:8]
)

selected_area = st.sidebar.multiselect(
    "Area type",

    sorted(
        df["Area"]
        .dropna()
        .unique()
    ),

    default=sorted(
        df["Area"]
        .dropna()
        .unique()
    )
)


# =========================================================
# FILTER DATA
# =========================================================

filtered = df[
    df["State"].isin(
        selected_states
    )
    &
    df["Area"].isin(
        selected_area
    )
].copy()


if filtered.empty:

    st.warning(
        "No rows match the current filters. "
        "Please widen the filters."
    )

    st.stop()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="eyebrow">
        DATA STORY • INDIA • 2019–2020
    </div>
    """,
    unsafe_allow_html=True
)


st.title(
    "Unemployment Analytics Dashboard"
)


st.markdown(
    """
    <div class="main-subtitle">
        Explore unemployment trends, regional differences,
        labour-market relationships, and the COVID-19 shock
        through interactive analysis.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DATASET OVERVIEW
# =========================================================

st.subheader(
    "Dataset Overview"
)


date_range_text = "—"

if (
    pd.notna(quality["date_min"])
    and
    pd.notna(quality["date_max"])
):

    date_range_text = (
        f"{quality['date_min'].strftime('%b %Y')}"
        f" – "
        f"{quality['date_max'].strftime('%b %Y')}"
    )


frequency_text = (
    ", ".join(
        quality["frequency_values"]
    )
    if quality["frequency_values"]
    else "Not specified"
)


area_text = (
    ", ".join(
        quality["area_values"]
    )
    if quality["area_values"]
    else "Not specified"
)


o1, o2, o3, o4 = st.columns(4)


with o1:

    st.markdown(
        f"""
        <div class="overview-card">
            <div class="overview-label">
                Original dataset
            </div>
            <div class="overview-value">
                {quality['raw_rows']:,} rows
            </div>
            <div class="overview-note">
                {quality['raw_columns']} columns
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with o2:

    st.markdown(
        f"""
        <div class="overview-card">
            <div class="overview-label">
                Cleaned dataset
            </div>
            <div class="overview-value">
                {quality['cleaned_rows']:,} rows
            </div>
            <div class="overview-note">
                {quality['rows_removed']:,} rows removed
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with o3:

    st.markdown(
        f"""
        <div class="overview-card">
            <div class="overview-label">
                Coverage
            </div>
            <div class="overview-value">
                {date_range_text}
            </div>
            <div class="overview-note">
                {quality['state_count']} regions represented
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with o4:

    st.markdown(
        f"""
        <div class="overview-card">
            <div class="overview-label">
                Structure
            </div>
            <div class="overview-value">
                {frequency_text}
            </div>
            <div class="overview-note">
                Areas: {area_text}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown(
    f"""
    <div class="quality-note">
        <strong>Data quality:</strong>
        {quality['raw_duplicates']:,} duplicate rows were detected,
        and {quality['missing_required_rows']:,} rows contained missing
        values in required analysis fields before cleaning.
        The final analysis uses {quality['cleaned_rows']:,} clean observations.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# KPI SECTION
# =========================================================

avg_unemployment = (
    filtered[
        "Unemployment_Rate"
    ].mean()
)


median_unemployment = (
    filtered[
        "Unemployment_Rate"
    ].median()
)


avg_employed = (
    filtered[
        "Employed"
    ].mean()
)


avg_participation = (
    filtered[
        "Labour_Participation_Rate"
    ].mean()
)


peak_row = filtered.loc[
    filtered[
        "Unemployment_Rate"
    ].idxmax()
]


k1, k2, k3, k4, k5 = st.columns(5)


with k1:

    st.metric(
        "Average unemployment",
        f"{avg_unemployment:.2f}%"
    )


with k2:

    st.metric(
        "Median unemployment",
        f"{median_unemployment:.2f}%"
    )


with k3:

    st.metric(
        "Average employed",
        f"{avg_employed / 1e6:.2f}M"
    )


with k4:

    st.metric(
        "Labour participation",
        f"{avg_participation:.2f}%"
    )


with k5:

    st.metric(
        "Peak observation",
        f"{peak_row['Unemployment_Rate']:.2f}%"
    )

    st.caption(
        f"{peak_row['State']} • "
        f"{peak_row['Date'].strftime('%b %Y')}"
    )


st.info(
    "Every visualization below has a specific analytical purpose. "
    "Use the filters on the left to focus the analysis on selected "
    "states or area types."
)


# =========================================================
# TABS
# =========================================================

(
    tab_trends,
    tab_covid,
    tab_regional,
    tab_relationships,
    tab_insights
) = st.tabs(
    [
        "📈 Trends",
        "🦠 COVID-19",
        "🗺️ Regional",
        "🔎 Relationships",
        "💡 Insights",
    ]
)


# =========================================================
# TAB 1 — TRENDS
# =========================================================

with tab_trends:

    # -----------------------------------------------------
    # Overall Trend
    # -----------------------------------------------------

    st.subheader(
        "Overall unemployment trend"
    )


    trend = (
        filtered
        .groupby(
            "Date",
            as_index=False
        )[
            "Unemployment_Rate"
        ]
        .mean()
        .sort_values(
            "Date"
        )
    )


    trend_fig = px.line(

        trend,

        x="Date",

        y="Unemployment_Rate",

        markers=True,

        title=(
            "Average Unemployment "
            "Rate Over Time"
        ),

        labels={
            "Date":
                "Date",

            "Unemployment_Rate":
                "Unemployment Rate (%)"
        },

        template="plotly_white"
    )


    trend_fig.update_traces(

        line=dict(
            color="#e76f51",
            width=4
        ),

        marker=dict(
            color="#7c3aed",
            size=8
        )
    )


    trend_fig.update_layout(

        height=460,

        hovermode="x unified",

        paper_bgcolor="#f7f1ed",

        plot_bgcolor="#f7f1ed",

        font_color="#2b2430",

        title_font_color="#2b2430",

        xaxis=dict(
            gridcolor="#ddd3cd"
        ),

        yaxis=dict(
            gridcolor="#ddd3cd"
        )
    )


    st.plotly_chart(
        trend_fig,
        use_container_width=True
    )


    st.markdown(
        """
        **Why this matters:**  
        This is the core time-series view. It shows the direction
        of unemployment, turning points, and periods of major change.
        """
    )


    # -----------------------------------------------------
    # Missing Values
    # -----------------------------------------------------

    st.subheader(
        "Data-quality check: missing values before cleaning"
    )


    missing_map = (
        raw_df.isna()
        .astype(int)
    )


    missing_fig = px.imshow(

        missing_map,

        aspect="auto",

        color_continuous_scale=[
            "#f7f1ed",
            "#db2777"
        ],

        labels={
            "x":
                "Columns",

            "y":
                "Rows",

            "color":
                "Missing"
        },

        title=(
            "Missing-Value Map "
            "(Original Dataset)"
        ),

        template="plotly_white"
    )


    missing_fig.update_layout(

        height=360,

        paper_bgcolor="#f7f1ed",

        plot_bgcolor="#f7f1ed",

        font_color="#2b2430",

        title_font_color="#2b2430"
    )


    st.plotly_chart(
        missing_fig,
        use_container_width=True
    )


    st.markdown(
        """
        **Why this matters:**  
        This heatmap uses the original dataset before cleaning.
        It documents where missing values existed and supports
        the data-cleaning stage of the project.
        """
    )


    # -----------------------------------------------------
    # State Explorer
    # -----------------------------------------------------

    st.subheader(
        "Interactive state trend explorer"
    )


    chosen_state = st.selectbox(

        "Choose one state / region",

        sorted(
            filtered[
                "State"
            ].unique()
        )
    )


    state_trend = (
        filtered[
            filtered[
                "State"
            ]
            ==
            chosen_state
        ]
        .sort_values(
            "Date"
        )
    )


    state_fig = px.line(

        state_trend,

        x="Date",

        y="Unemployment_Rate",

        markers=True,

        title=(
            f"Unemployment Trend — "
            f"{chosen_state}"
        ),

        labels={
            "Date":
                "Date",

            "Unemployment_Rate":
                "Unemployment Rate (%)"
        },

        template="plotly_white"
    )


    state_fig.update_traces(

        line=dict(
            color="#7c3aed",
            width=4
        ),

        marker=dict(
            color="#e76f51",
            size=8
        )
    )


    state_fig.update_layout(

        height=420,

        hovermode="x unified",

        paper_bgcolor="#f7f1ed",

        plot_bgcolor="#f7f1ed",

        font_color="#2b2430",

        title_font_color="#2b2430",

        xaxis=dict(
            gridcolor="#ddd3cd"
        ),

        yaxis=dict(
            gridcolor="#ddd3cd"
        )
    )


    st.plotly_chart(
        state_fig,
        use_container_width=True
    )


    st.markdown(
        """
        **Why this matters:**  
        National averages can hide local shocks. Selecting a state
        lets you investigate whether its unemployment moved in the
        same direction as the broader pattern.
        """
    )


    # -----------------------------------------------------
    # Top States
    # -----------------------------------------------------

    st.subheader(
        "Highest-average unemployment states"
    )


    state_avg = (
        filtered

        .groupby(
            "State"
        )[
            "Unemployment_Rate"
        ]

        .mean()

        .sort_values(
            ascending=False
        )

        .reset_index(
            name="Average_Unemployment"
        )
    )


    top_n = min(
        15,
        len(state_avg)
    )


    ranking_fig = px.bar(

        state_avg

        .head(
            top_n
        )

        .sort_values(
            "Average_Unemployment"
        ),

        x="Average_Unemployment",

        y="State",

        orientation="h",

        text="Average_Unemployment",

        color="Average_Unemployment",

        color_continuous_scale=[
            "#e76f51",
            "#7c3aed"
        ],

        title=(
            f"Top {top_n} States by "
            "Average Unemployment Rate"
        ),

        labels={
            "Average_Unemployment":
                "Average Unemployment Rate (%)"
        },

        template="plotly_white"
    )


    ranking_fig.update_traces(

        texttemplate="%{text:.2f}%",

        textposition="outside"
    )


    ranking_fig.update_layout(

        height=560,

        coloraxis_showscale=False,

        paper_bgcolor="#f7f1ed",

        plot_bgcolor="#f7f1ed",

        font_color="#2b2430",

        title_font_color="#2b2430"
    )


    st.plotly_chart(
        ranking_fig,
        use_container_width=True
    )


    st.markdown(
        """
        **Why this matters:**  
        Ranking highlights where sustained unemployment pressure
        was highest across the selected period. It is a screening
        view, not a judgment of a state's overall economy.
        """
    )


    chart_download(
        state_avg,
        "state_unemployment_ranking.csv"
    )


    # -----------------------------------------------------
    # Monthly Pattern
    # -----------------------------------------------------

    st.subheader(
        "Monthly pattern exploration"
    )


    month_order = [

        pd.Timestamp(
            2020,
            month,
            1
        ).strftime("%b")

        for month in range(
            1,
            13
        )
    ]


    monthly = (
        filtered

        .groupby(
            "Month_Name"
        )[
            "Unemployment_Rate"
        ]

        .mean()

        .reindex(
            month_order
        )

        .dropna()
    )


    seasonal_df = (
        monthly

        .reset_index()

        .rename(
            columns={
                "Month_Name":
                    "Month",

                "Unemployment_Rate":
                    "Average_Unemployment"
            }
        )
    )


    seasonal_fig = px.bar(

        seasonal_df,

        x="Month",

        y="Average_Unemployment",

        text="Average_Unemployment",

        color="Average_Unemployment",

        color_continuous_scale=[
            "#f4a261",
            "#7c3aed"
        ],

        title=(
            "Average Unemployment Rate "
            "by Calendar Month"
        ),

        labels={
            "Average_Unemployment":
                "Average Unemployment Rate (%)"
        },

        template="plotly_white"
    )


    seasonal_fig.update_traces(

        texttemplate="%{text:.2f}%",

        textposition="outside"
    )


    seasonal_fig.update_layout(

        height=420,

        coloraxis_showscale=False,

        paper_bgcolor="#f7f1ed",

        plot_bgcolor="#f7f1ed",

        font_color="#2b2430",

        title_font_color="#2b2430"
    )


    st.plotly_chart(
        seasonal_fig,
        use_container_width=True
    )


    st.markdown(
        """
        **Why this matters:**  
        The monthly view searches for recurring patterns. Because
        the dataset spans a relatively short period, this should be
        interpreted as an exploratory monthly pattern rather than
        definitive long-term seasonality.
        """
    )


# =========================================================
# TAB 2 — COVID-19
# =========================================================

with tab_covid:

    st.subheader(
        "COVID-19 impact"
    )


    period_summary = (
        filtered

        .groupby(
            "Period"
        )[
            "Unemployment_Rate"
        ]

        .agg(
            [
                "mean",
                "median",
                "min",
                "max",
                "count"
            ]
        )

        .reindex(
            [
                "Pre-COVID",
                "COVID period"
            ]
        )
    )


    period_table = (
        period_summary

        .reset_index()

        .rename(
            columns={
                "mean":
                    "Average",

                "median":
                    "Median",

                "min":
                    "Minimum",

                "max":
                    "Maximum",

                "count":
                    "Observations"
            }
        )
    )


    st.dataframe(

        period_table.style.format(
            {
                "Average":
                    "{:.2f}%",

                "Median":
                    "{:.2f}%",

                "Minimum":
                    "{:.2f}%",

                "Maximum":
                    "{:.2f}%"
            }
        ),

        use_container_width=True
    )


    # -----------------------------------------------------
    # COVID Distribution
    # -----------------------------------------------------

    covid_box = px.box(

        filtered,

        x="Period",

        y="Unemployment_Rate",

        color="Period",

        points="outliers",

        color_discrete_map={

            "Pre-COVID":
                "#0f766e",

            "COVID period":
                "#db2777"
        },

        title=(
            "Unemployment Distribution "
            "Before and During COVID-19"
        ),

        labels={
            "Unemployment_Rate":
                "Unemployment Rate (%)"
        },

        template="plotly_white"
    )


    covid_box.update_layout(

        height=460,

        paper_bgcolor="#f7f1ed",

        plot_bgcolor="#f7f1ed",

        font_color="#2b2430",

        title_font_color="#2b2430"
    )


    st.plotly_chart(
        covid_box,
        use_container_width=True
    )


    st.markdown(
        """
        **Why this matters:**  
        The box plot compares the full distribution, not just
        the average. It shows whether unemployment shifted upward
        and whether the spread changed during the COVID period.
        """
    )


    # -----------------------------------------------------
    # COVID KPIs
    # -----------------------------------------------------

    pre = (

        period_summary.loc[
            "Pre-COVID",
            "mean"
        ]

        if "Pre-COVID"
        in period_summary.index

        else np.nan
    )


    covid = (

        period_summary.loc[
            "COVID period",
            "mean"
        ]

        if "COVID period"
        in period_summary.index

        else np.nan
    )


    change_pp = (

        covid - pre

        if pd.notna(pre)
        and pd.notna(covid)

        else np.nan
    )


    change_pct = (

        (change_pp / pre) * 100

        if pd.notna(change_pp)
        and pre != 0

        else np.nan
    )


    c1, c2, c3 = st.columns(3)


    with c1:

        st.metric(

            "Pre-COVID average",

            (
                f"{pre:.2f}%"

                if pd.notna(pre)

                else "—"
            )
        )


    with c2:

        st.metric(

            "COVID-period average",

            (
                f"{covid:.2f}%"

                if pd.notna(covid)

                else "—"
            )
        )


    with c3:

        st.metric(

            "Change",

            (
                f"{change_pp:+.2f} pp"

                if pd.notna(change_pp)

                else "—"
            ),

            (
                f"{change_pct:+.1f}% vs pre-COVID"

                if pd.notna(change_pct)

                else None
            )
        )


    st.markdown(
        """
        <div class="quality-note">
            <strong>Interpretation:</strong>
            The observed change shows how unemployment shifted around
            the COVID period in this dataset. It should not be interpreted
            as proof that COVID-19 alone caused the observed change.
        </div>
        """,
        unsafe_allow_html=True
    )


    # -----------------------------------------------------
    # State-Level COVID Change
    # -----------------------------------------------------

    state_period = (
        filtered

        .groupby(
            [
                "State",
                "Period"
            ]
        )[
            "Unemployment_Rate"
        ]

        .mean()

        .unstack()
    )


    if {
        "Pre-COVID",
        "COVID period"
    }.issubset(
        state_period.columns
    ):


        state_period[
            "Change_pp"
        ] = (

            state_period[
                "COVID period"
            ]

            -

            state_period[
                "Pre-COVID"
            ]
        )


        changes = (
            state_period[
                "Change_pp"
            ]

            .dropna()

            .sort_values()
        )


        extreme_changes = (

            pd.concat(
                [
                    changes.head(7),
                    changes.tail(7)
                ]
            )

            .reset_index()

            .drop_duplicates()
        )


        covid_change_fig = px.bar(

            extreme_changes

            .sort_values(
                "Change_pp"
            ),

            x="Change_pp",

            y="State",

            orientation="h",

            color="Change_pp",

            color_continuous_scale=[
                "#0f766e",
                "#f4a261",
                "#db2777"
            ],

            title=(
                "Largest State-Level "
                "Changes in Unemployment"
            ),

            labels={
                "Change_pp":
                    "Change in unemployment "
                    "(percentage points)"
            },

            template="plotly_white"
        )


        covid_change_fig.update_layout(

            height=560,

            coloraxis_showscale=False,

            paper_bgcolor="#f7f1ed",

            plot_bgcolor="#f7f1ed",

            font_color="#2b2430",

            title_font_color="#2b2430"
        )


        st.plotly_chart(
            covid_change_fig,
            use_container_width=True
        )


        st.markdown(
            """
            **Why this matters:**  
            The national COVID effect was not uniform. This view
            identifies where unemployment rose most sharply and
            where the change was smaller.
            """
        )


# =========================================================
# TAB 3 — REGIONAL
# =========================================================

with tab_regional:

    st.subheader(
        "Rural vs Urban labour-market conditions"
    )


    area_summary = (
        filtered

        .groupby(
            "Area"
        )

        .agg(

            Average_Unemployment=(
                "Unemployment_Rate",
                "mean"
            ),

            Median_Unemployment=(
                "Unemployment_Rate",
                "median"
            ),

            Observations=(
                "Unemployment_Rate",
                "size"
            )
        )

        .round(2)
    )


    st.dataframe(
        area_summary,
        use_container_width=True
    )


    # -----------------------------------------------------
    # Area Distribution
    # -----------------------------------------------------

    area_box = px.box(

        filtered,

        x="Area",

        y="Unemployment_Rate",

        color="Area",

        points="outliers",

        color_discrete_sequence=[
            "#0f766e",
            "#7c3aed"
        ],

        title=(
            "Unemployment Distribution "
            "by Area Type"
        ),

        labels={
            "Unemployment_Rate":
                "Unemployment Rate (%)"
        },

        template="plotly_white"
    )


    area_box.update_layout(

        height=470,

        paper_bgcolor="#f7f1ed",

        plot_bgcolor="#f7f1ed",

        font_color="#2b2430",

        title_font_color="#2b2430"
    )


    st.plotly_chart(
        area_box,
        use_container_width=True
    )


    st.markdown(
        """
        **Why this matters:**  
        Comparing rural and urban distributions shows not only
        different average levels, but also the spread and presence
        of unusual observations.
        """
    )


    # -----------------------------------------------------
    # State × Area
    # -----------------------------------------------------

    state_area = (
        filtered

        .groupby(
            [
                "State",
                "Area"
            ]
        )[
            "Unemployment_Rate"
        ]

        .mean()

        .reset_index()
    )


    state_area_fig = px.bar(

        state_area,

        x="State",

        y="Unemployment_Rate",

        color="Area",

        barmode="group",

        color_discrete_sequence=[
            "#0f766e",
            "#7c3aed"
        ],

        title=(
            "Average Unemployment by "
            "State and Area Type"
        ),

        labels={
            "Unemployment_Rate":
                "Average Unemployment Rate (%)"
        },

        template="plotly_white"
    )


    state_area_fig.update_layout(

        height=620,

        xaxis_tickangle=-45,

        paper_bgcolor="#f7f1ed",

        plot_bgcolor="#f7f1ed",

        font_color="#2b2430",

        title_font_color="#2b2430"
    )


    st.plotly_chart(
        state_area_fig,
        use_container_width=True
    )


    st.markdown(
        """
        **Why this matters:**  
        This regional comparison helps identify whether rural/urban
        differences are persistent across states or concentrated in
        specific locations.
        """
    )


# =========================================================
# TAB 4 — RELATIONSHIPS
# =========================================================

with tab_relationships:

    st.subheader(
        "Interactive labour-market relationship"
    )


    bubble_df = (
        filtered

        .copy()

        .sort_values(
            "Date"
        )
    )


    bubble_df[
        "Date_Label"
    ] = (

        bubble_df[
            "Date"
        ]

        .dt.strftime(
            "%b %Y"
        )
    )


    bubble_fig = px.scatter(

        bubble_df,

        x="Labour_Participation_Rate",

        y="Unemployment_Rate",

        size="Employed",

        color="Area",

        hover_name="State",

        hover_data={

            "Labour_Participation_Rate":
                ":.2f",

            "Unemployment_Rate":
                ":.2f",

            "Employed":
                ":,.0f",

            "Area":
                True,

            "Date_Label":
                True
        },

        animation_frame="Date_Label",

        animation_group="State",

        size_max=45,

        color_discrete_sequence=[
            "#0f766e",
            "#7c3aed"
        ],

        title=(
            "Interactive Labour-Market Explorer"
        ),

        labels={

            "Labour_Participation_Rate":
                "Labour Participation Rate (%)",

            "Unemployment_Rate":
                "Unemployment Rate (%)",

            "Employed":
                "Estimated Employed"
        },

        template="plotly_white"
    )


    bubble_fig.update_layout(

        height=650,

        paper_bgcolor="#f7f1ed",

        plot_bgcolor="#f7f1ed",

        font_color="#2b2430",

        title_font_color="#2b2430"
    )


    # -----------------------------------------------------
    # Slow animation
    # -----------------------------------------------------

    try:

        if (
            bubble_fig.layout.updatemenus
            and len(bubble_fig.layout.updatemenus) > 0
            and len(
                bubble_fig.layout.updatemenus[0].buttons
            ) > 0
        ):

            bubble_fig.layout.updatemenus[
                0
            ].buttons[
                0
            ].args[
                1
            ][
                "frame"
            ][
                "duration"
            ] = 1500


            bubble_fig.layout.updatemenus[
                0
            ].buttons[
                0
            ].args[
                1
            ][
                "transition"
            ][
                "duration"
            ] = 800

    except Exception:

        pass


    st.plotly_chart(
        bubble_fig,
        use_container_width=True
    )


    st.markdown(
        """
        **Why this matters:**  
        The animation adds time to the labour-market relationship.
        The x-axis tracks labour participation, the y-axis tracks
        unemployment, and bubble size represents estimated employment.
        """
    )


    # -----------------------------------------------------
    # Correlation
    # -----------------------------------------------------

    correlation_columns = [
        "Unemployment_Rate",
        "Employed",
        "Labour_Participation_Rate"
    ]


    correlation_matrix = (
        filtered[
            correlation_columns
        ]

        .corr()
    )


    correlation_fig = px.imshow(

        correlation_matrix,

        text_auto=".2f",

        color_continuous_scale=[
            "#7c3aed",
            "#f7f1ed",
            "#db2777"
        ],

        zmin=-1,

        zmax=1,

        title=(
            "Correlation Matrix of "
            "Labour-Market Indicators"
        ),

        template="plotly_white"
    )


    correlation_fig.update_layout(

        height=470,

        paper_bgcolor="#f7f1ed",

        plot_bgcolor="#f7f1ed",

        font_color="#2b2430",

        title_font_color="#2b2430"
    )


    st.plotly_chart(
        correlation_fig,
        use_container_width=True
    )


    st.markdown(
        """
        **Why this matters:**  
        Correlation measures linear association between indicators.
        It can reveal useful relationships, but it does not prove that
        one variable causes another.
        """
    )


# =========================================================
# TAB 5 — INSIGHTS
# =========================================================

with tab_insights:

    st.subheader(
        "Data-driven findings"
    )


    state_avg_insights = (
        filtered

        .groupby(
            "State"
        )[
            "Unemployment_Rate"
        ]

        .mean()

        .sort_values(
            ascending=False
        )
    )


    area_avg = (
        filtered

        .groupby(
            "Area"
        )[
            "Unemployment_Rate"
        ]

        .mean()

        .sort_values(
            ascending=False
        )
    )


    monthly_avg = (
        filtered

        .groupby(
            "Month_Name"
        )[
            "Unemployment_Rate"
        ]

        .mean()
    )


    highest_state = (
        state_avg_insights.index[0]
    )


    highest_state_value = (
        state_avg_insights.iloc[0]
    )


    highest_area = (
        area_avg.index[0]
    )


    highest_area_value = (
        area_avg.iloc[0]
    )


    highest_month = (
        monthly_avg.idxmax()
    )


    highest_month_value = (
        monthly_avg.max()
    )


    # -----------------------------------------------------
    # Findings
    # -----------------------------------------------------

    st.info(
        f"Highest-average state/region: "
        f"**{highest_state} — "
        f"{highest_state_value:.2f}%**"
    )


    st.info(
        f"Highest-average area type: "
        f"**{highest_area} — "
        f"{highest_area_value:.2f}%**"
    )


    st.info(
        f"Highest monthly average: "
        f"**{highest_month} — "
        f"{highest_month_value:.2f}%**"
    )


    st.info(
        f"Peak individual observation: "
        f"**{peak_row['Unemployment_Rate']:.2f}%** "
        f"in **{peak_row['State']}** during "
        f"**{peak_row['Date'].strftime('%b %Y')}**"
    )


    # -----------------------------------------------------
    # Policy Insights
    # -----------------------------------------------------

    st.subheader(
        "Economic and social policy insights"
    )


    st.success(
        """
        **Targeted regional support:**  
        Prioritize employment and reskilling programmes in
        regions with persistently high unemployment.
        """
    )


    st.success(
        """
        **Crisis-response readiness:**  
        Maintain temporary wage, hiring, or income-support
        mechanisms that can scale quickly during major shocks.
        """
    )


    st.success(
        """
        **Rural/urban tailoring:**  
        Use area-specific labour policies where the data shows
        persistent differences between rural and urban outcomes.
        """
    )


    st.success(
        """
        **Early-warning monitoring:**  
        Track unemployment together with labour participation
        to detect weakening labour-market conditions earlier.
        """
    )


    # -----------------------------------------------------
    # Limitations
    # -----------------------------------------------------

    st.subheader(
        "Limitations"
    )


    st.warning(
        """
        • The dataset covers a limited time window, so monthly
          patterns should be treated as exploratory rather than
          proof of long-term seasonality.

        • The COVID comparison is observational and does not
          isolate every other economic factor that changed during 2020.

        • Correlation does not establish causation.
        """
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()


st.caption(
    "Unemployment Analysis with Python • "
    "Interactive Streamlit Deployment • "
    "Built from the cleaned project dataset"
)