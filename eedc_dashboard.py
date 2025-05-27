import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_excel("Enugu-Electricity-Distribution-Plc.-Monthly-Energy-Cap-May-2025.xlsx")

# Create total energy cap column
df["Energy Cap"] = df[
    ["January Cap (kWh)", "February Cap (kWh)", "March Cap (kWh)",
     "April Cap (kWh)", "May Cap (kWh)"]
].sum(axis=1)

# Streamlit app
st.set_page_config(page_title="EEDC Dashboard", layout="wide")
st.title("🔌 EEDC Monthly Energy Cap Dashboard (Jan–May 2025)")
st.markdown("""
This dashboard presents **monthly electricity cap data** for feeders under the Enugu Electricity Distribution Company (EEDC) between **January and May 2025**. 
Use the filters on the left to explore energy distribution and identify areas of high or low energy allocation.
""")

# Sidebar filter for Business Unit
bu_options = df["Business Unit"].unique()
selected_bu = st.sidebar.selectbox("Select Business Unit (BU)", bu_options)

# Filter data by BU
filtered_df = df[df["Business Unit"] == selected_bu]

# Display filtered data
st.subheader(f"Feeder Data for {selected_bu}")
st.dataframe(filtered_df)

# Total Energy Cap for selected BU
total_energy = filtered_df["Energy Cap"].sum()
st.metric(label=f"Total Energy Cap in {selected_bu}", value=f"{total_energy:,.0f} kWh")

# Bar chart: Energy Cap by Feeder
fig_bar = px.bar(
    filtered_df,
    x="Feeder",
    y="Energy Cap",
    color="Feeder",
    title=f"Energy Cap Distribution by Feeder in {selected_bu}",
    labels={"Energy Cap": "Total Energy Cap (kWh)"},
)
st.plotly_chart(fig_bar, use_container_width=True)

# Optional line chart if you convert monthly data to long format
if st.checkbox("Show Monthly Trend by Feeder"):
    # Reshape data
    long_df = pd.melt(
        filtered_df,
        id_vars=["Feeder"],
        value_vars=[
            "January Cap (kWh)", "February Cap (kWh)", "March Cap (kWh)",
            "April Cap (kWh)", "May Cap (kWh)"
        ],
        var_name="Month",
        value_name="Monthly Cap"
    )

    # Clean month labels
    long_df["Month"] = long_df["Month"].str.replace(" Cap \(kWh\)", "", regex=True)

    # Line chart
    fig_line = px.line(
        long_df,
        x="Month",
        y="Monthly Cap",
        color="Feeder",
        title=f"Monthly Energy Cap Trend in {selected_bu}",
        markers=True
    )
    st.plotly_chart(fig_line, use_container_width=True)

    # Footer
    st.markdown("""
    ---
    Built with ❤️ using [Streamlit](https://streamlit.io/) | [View Source on GitHub](https://github.com/Udeibom/eedc-dashboard)
    """)
