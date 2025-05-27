⚡ EEDC Monthly Energy Cap Dashboard (Jan–May 2025)
This interactive dashboard provides insights into the monthly energy caps distributed across Business Units (BU) and Feeders under the Enugu Electricity Distribution Company (EEDC) from January to May 2025.

It was built using Pandas, Plotly, and Streamlit, with the goal of practicing data analysis and visual storytelling while solving a real-world problem — monitoring and analyzing energy distribution.

📊 Key Features
Visualize energy caps by Business Unit and Feeder

Identify top and bottom performing feeders

Analyze monthly trends (if available)

Clean and responsive layout for exploration

📁 Dataset
The dataset used is a manually collated file titled:
Enugu-Electricity-Distribution-Plc.-Monthly-Energy-Cap-May-2025.xlsx
It contains the energy cap (in MWh) assigned to various feeders across EEDC Business Units for each month between January and May 2025.

🚀 Getting Started
Requirements
Ensure you have Python 3.8+, Anaconda, or pip and the following packages:

streamlit
pandas
plotly

Install them using:
pip install streamlit pandas plotly

Run the App:
Save the dashboard file as eedc_dashboard.py
Place it in the same folder as the Excel file
Open Anaconda Prompt or your terminal in that folder
Run:
streamlit run eedc_dashboard.py

Your default browser will open the dashboard at http://localhost:8501

Screenshot:
![EEDC Dashboard Screenshot](plot.png)


✍️ Author
👤 Caleb Udeibom
📅 Week: 3
📬 LinkedIn: www.linkedin.com/in/caleb-udeibom-3495a023b

📌 Future Plans:
Expand data coverage from Jan 2024 to May 2025
Add anomaly detection for feeders with erratic trends
Compare EEDC’s energy distribution with other states or DISCOs
Build advanced dashboards using Dash or Power BI
