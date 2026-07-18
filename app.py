import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="IPL 2026 Data Analytics Dashboard",
    page_icon="🏏",
    layout="wide"
)

# -------------------- SIDEBAR --------------------
# -------------------- SIDEBAR --------------------
st.sidebar.title("🏏 IPL 2026 Dashboard")

st.sidebar.markdown("""
### Dashboard Sections

- 📊 Dataset Overview
- 🏏 Batting Analysis
- 🎯 Bowling Analysis
- 🏟️ Team & Venue Analysis

---

### Technologies Used

- Python
- Pandas
- Plotly
- Streamlit
""")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "📂 Select Analysis",
    [
        "Dashboard",
        "Batting Analysis",
        "Bowling Analysis",
        "Team Analysis",
        "Venue Analysis"
    ]
)

# -------------------- TITLE --------------------
st.title("🏏 IPL 2026 Data Analytics Dashboard")

st.markdown("""
Welcome to the **IPL 2026 Data Analytics Dashboard**.

This dashboard presents interactive insights from the IPL 2026 season using **Python, Pandas, Plotly, and Streamlit**.

### Key Insights

- 🏏 Batting Performance
- 🎯 Bowling Performance
- 🏟️ Team Analysis
- 📍 Venue Analysis
""")

# -------------------- LOAD DATA --------------------
df = pd.read_csv("data/ipl_2026_deliveries.csv")
show_dashboard = page == "Dashboard"
show_batting = page == "Batting Analysis"
show_bowling = page == "Bowling Analysis"
show_team = page == "Team Analysis"
show_venue = page == "Venue Analysis"

# -------------------- DATASET OVERVIEW --------------------

if show_dashboard:
    st.header("📊 Dataset Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Deliveries", len(df))

    with col2:
        st.metric("Total Matches", df["match_id"].nunique())

    with col3:
        st.metric("Total Players", df["striker"].nunique())

    st.divider()
# -------------------- TOP RUN SCORERS --------------------
if show_batting:

    st.header("🏏 Top 10 Run Scorers")

    top_batsmen = (
        df.groupby("striker")["runs_of_bat"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    top_batsmen_df = top_batsmen.reset_index()
    top_batsmen_df.columns = ["Batsman", "Runs"]

    fig1 = px.bar(
        top_batsmen_df,
        x="Batsman",
        y="Runs",
        text="Runs",
        color="Runs",
        color_continuous_scale="Blues",
        title="Top 10 Run Scorers"
    )

    fig1.update_traces(textposition="outside")

    st.plotly_chart(fig1, use_container_width=True)

    st.divider()

# -------------------- TOP SIX HITTERS --------------------
if show_batting:

    st.header("💥 Top 10 Six Hitters")

    top_six_hitters = (
        df[df["runs_of_bat"] == 6]
        .groupby("striker")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    top_six_hitters_df = top_six_hitters.reset_index()
    top_six_hitters_df.columns = ["Batsman", "Sixes"]

    fig2 = px.bar(
        top_six_hitters_df,
        x="Batsman",
        y="Sixes",
        text="Sixes",
        color="Sixes",
        color_continuous_scale="Reds",
        title="Top 10 Six Hitters"
    )

    fig2.update_traces(textposition="outside")

    st.plotly_chart(fig2, use_container_width=True)

    st.divider()

# -------------------- TEAM RUNS --------------------
if show_team:

    st.header("🏏 Team-wise Total Runs")

    team_runs = (
        df.groupby("batting_team")["runs_of_bat"]
        .sum()
        .sort_values(ascending=False)
    )

    team_runs_df = team_runs.reset_index()
    team_runs_df.columns = ["Team", "Runs"]

    fig4 = px.bar(
        team_runs_df,
        x="Team",
        y="Runs",
        text="Runs",
        color="Runs",
        color_continuous_scale="Purples",
        title="Team-wise Total Runs"
    )

    fig4.update_traces(textposition="outside")
    fig4.update_layout(
        xaxis_title="Team",
        yaxis_title="Runs"
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.divider()

# -------------------- HIGHEST INDIVIDUAL SCORES --------------------
if show_batting:

    st.header("🏆 Top 10 Highest Individual Scores")

    highest_scores = (
        df.groupby(["match_id", "striker"])["runs_of_bat"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    highest_scores_df = highest_scores.reset_index()
    highest_scores_df.columns = ["Match ID", "Batsman", "Runs"]

    fig5 = px.bar(
        highest_scores_df,
        x="Batsman",
        y="Runs",
        text="Runs",
        color="Runs",
        color_continuous_scale="Viridis",
        hover_data=["Match ID"],
        title="Highest Individual Scores"
    )

    fig5.update_traces(textposition="outside")

    st.plotly_chart(fig5, use_container_width=True)

    st.divider()

# -------------------- MOST FOURS --------------------
if show_batting:

    st.header("🏏 Top 10 Players with Most Fours")

    top_fours = (
        df[df["runs_of_bat"] == 4]
        .groupby("striker")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    top_fours_df = top_fours.reset_index()
    top_fours_df.columns = ["Batsman", "Fours"]

    fig6 = px.bar(
        top_fours_df,
        x="Batsman",
        y="Fours",
        text="Fours",
        color="Fours",
        color_continuous_scale="Blues",
        title="Most Fours"
    )

    fig6.update_traces(textposition="outside")

    st.plotly_chart(fig6, use_container_width=True)

    st.divider()

# -------------------- MOST DOT BALLS --------------------
if show_bowling:

    st.header("🎯 Top 10 Bowlers with Most Dot Balls")

    top_dot_balls = (
        df[df["runs_of_bat"] == 0]
        .groupby("bowler")
        .size()
        .sort_values(ascending=False)
        .head(10)
    )

    top_dot_balls_df = top_dot_balls.reset_index()
    top_dot_balls_df.columns = ["Bowler", "Dot Balls"]

    fig7 = px.bar(
        top_dot_balls_df,
        x="Bowler",
        y="Dot Balls",
        text="Dot Balls",
        color="Dot Balls",
        color_continuous_scale="Oranges",
        title="Most Dot Balls"
    )

    fig7.update_traces(textposition="outside")

    st.plotly_chart(fig7, use_container_width=True)

    st.divider()

# -------------------- BEST BOWLING FIGURES --------------------
if show_bowling:

    st.header("🔥 Best Bowling Figures")

    bowler_wickets = df[
        df["wicket_type"].isin([
            "bowled",
            "caught",
            "lbw",
            "stumped",
            "caught and bowled",
            "hit wicket"
        ])
    ]

    best_bowling = (
        bowler_wickets.groupby("bowler")["wicket_type"]
        .count()
        .sort_values(ascending=False)
        .head(10)
    )

    best_bowling_df = best_bowling.reset_index()
    best_bowling_df.columns = ["Bowler", "Wickets"]

    fig8 = px.bar(
        best_bowling_df,
        x="Bowler",
        y="Wickets",
        text="Wickets",
        color="Wickets",
        color_continuous_scale="Greens",
        title="Best Bowling Figures"
    )

    fig8.update_traces(textposition="outside")

    st.plotly_chart(fig8, use_container_width=True)

    st.divider()

# -------------------- HIGHEST TEAM SCORES --------------------
if show_team:

    st.header("🚀 Top 10 Highest Team Scores")

    highest_team_scores = (
        df.groupby(["match_id", "innings", "batting_team"])["runs_of_bat"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    highest_team_scores_df = highest_team_scores.reset_index()
    highest_team_scores_df.columns = ["Match ID", "Innings", "Team", "Runs"]

    fig9 = px.bar(
        highest_team_scores_df,
        x="Team",
        y="Runs",
        text="Runs",
        color="Runs",
        color_continuous_scale="Plasma",
        hover_data=["Match ID", "Innings"],
        title="Highest Team Scores"
    )

    fig9.update_traces(textposition="outside")

    st.plotly_chart(fig9, use_container_width=True)

    st.divider()

# -------------------- VENUE ANALYSIS --------------------
if show_venue:

    st.header("🏟️ Venue-wise Total Runs")

    venue_analysis = (
        df.groupby("venue")["runs_of_bat"]
        .sum()
        .sort_values(ascending=False)
    )

    venue_analysis_df = venue_analysis.reset_index()
    venue_analysis_df.columns = ["Venue", "Runs"]

    fig10 = px.bar(
        venue_analysis_df,
        x="Venue",
        y="Runs",
        text="Runs",
        color="Runs",
        color_continuous_scale="Cividis",
        title="Venue-wise Total Runs"
    )

    fig10.update_layout(xaxis_tickangle=-45)
    fig10.update_traces(textposition="outside")

    st.plotly_chart(fig10, use_container_width=True)

    st.divider()

# -------------------- FOOTER --------------------
st.markdown("---")

st.caption(
    "Developed by Madhumitha G | IPL 2026 Data Analytics Dashboard | Python • Pandas • Plotly • Streamlit"
)