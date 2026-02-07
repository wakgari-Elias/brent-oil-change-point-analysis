# brent-oil-change-point-analysis
Brent oil is a global benchmark  Many countries and companies price oil contracts using Brent  If Brent price changes → global economic impact
# Brent Oil Price Change Point Analysis  
### Task 1 – Analytical Foundation & Data Understanding

## Project Overview
This project analyzes how major geopolitical, economic, and policy-driven events have impacted Brent crude oil prices over time. The goal is to detect structural breaks in oil price behavior and associate them with real-world events using statistical and Bayesian methods.

This repository currently contains **Task 1**, which establishes the analytical foundation required for change point modeling in later stages.

---

## Business Context
Oil markets are highly sensitive to geopolitical shocks, policy decisions, and global economic conditions. Sudden price changes introduce risk and uncertainty for:

- Investors managing portfolios
- Policymakers designing energy and economic strategies
- Energy companies planning operations and supply chains

Understanding *when* and *why* price behavior changes is essential for informed decision-making.

---

## Task 1 Objectives
Task 1 focuses on building a strong foundation for analysis by:

- Defining a clear data analysis workflow
- Understanding Brent oil price time series properties
- Compiling a structured dataset of major oil-market events
- Documenting assumptions, limitations, and communication strategy

No predictive modeling is performed at this stage.

---

## Repository Structure

```text
brent-oil-change-point-analysis/
│
├── data/
│   ├── raw/
│   │   └── BrentOilPrices.csv
│   └── events/
│       └── oil_market_events.csv
│
├── notebooks/
│   └── task1_initial_eda.ipynb
│
├── reports/
│   └── task1_analysis_workflow.md
│
├── src/
│   └── generate_event_data.py
│
├── .github/
│   └── workflows/
│       └── unittests.yml
│
├── requirements.txt
├── README.md
Data Description
Brent Oil Prices

Source: Historical Brent oil prices

Frequency: Daily

Fields:

Date: Observation date

Price: Brent oil price (USD per barrel)

Event Dataset

A structured dataset of 15 major geopolitical and economic events was programmatically generated based on historical records. Events include wars, OPEC decisions, sanctions, and global crises that plausibly impacted oil prices.

Events are intentionally independent of the price data to avoid circular reasoning.

Initial Data Analysis

The exploratory analysis includes:

Visualization of raw price trends

Log return transformation

Stationarity testing using the Augmented Dickey-Fuller test

Volatility clustering analysis

These diagnostics motivate the use of Bayesian Change Point Models in subsequent tasks.

Assumptions & Limitations
Assumptions

Brent oil price reflects global oil market conditions

Structural changes occur close to major events

Daily data resolution is sufficient

Limitations

Statistical change points indicate correlation, not causation

Multiple events may overlap in time

External macroeconomic variables are not yet included

Continuous Integration

A GitHub Actions workflow validates Task 1 by checking:

Presence of raw and event datasets

Minimum event count

Required file structure

Python 3.11 compatibility

Next Steps

Future tasks will introduce:

Bayesian Change Point Detection using PyMC

Quantification of price regime shifts

Interactive dashboards for stakeholder communication

Author

Prepared for data science analysis and policy-focused insight generation.