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

Task 2 — Bayesian Change Point Analysis of Brent Oil Prices
Overview

This task applies Bayesian Change Point Analysis to historical Brent crude oil prices in order to identify structural breaks in the time series. These change points represent moments where the statistical properties of oil prices (such as the mean level) shift significantly, often due to major geopolitical, economic, or supply–demand events.

The analysis uses a probabilistic Bayesian framework implemented in PyMC, allowing uncertainty to be explicitly modeled and quantified rather than relying on fixed deterministic breakpoints.

Objective

The main goals of Task 2 are:

Detect one or more structural change points in Brent oil prices

Estimate price regimes before and after the change point

Quantify uncertainty in the timing and magnitude of changes

Provide an interpretable statistical foundation for linking price shifts to real-world events

This approach improves on simple visual inspection or classical break tests by producing posterior distributions instead of single-point estimates.

Dataset

Source file: BrentOilPrices.csv

Key columns:

Date — observation date

Price — Brent crude oil price (USD)

Preprocessing Steps

Converted Date to datetime format

Sorted observations chronologically

Removed missing or invalid values

Indexed prices for time-series modeling

Methodology
Bayesian Change Point Model

The model assumes that oil prices follow two distinct regimes:

A pre-change regime with mean μ₁

A post-change regime with mean μ₂

A latent change point τ that separates the two regimes

Formally:

Prices before τ are drawn from Normal(μ₁, σ)

Prices after τ are drawn from Normal(μ₂, σ)

The change point τ is treated as a random variable with a discrete prior

This structure allows the model to infer:

When the change occurred

How large the shift in price level was

How uncertain those estimates are

Inference & Sampling

Framework: PyMC (Bayesian probabilistic programming)

Sampling method:

NUTS (No-U-Turn Sampler) for continuous parameters

Metropolis step for the discrete change point

Configuration:

draws = 2000

tune = 1000

chains = 4

target_accept = 0.9

The model was sampled using MCMC, and convergence was assessed through:

Trace plots

Effective sample sizes

Absence of divergent transitions

Outputs

The analysis produces:

Posterior distribution of the change point location

Estimated means before and after the change

Credible intervals capturing uncertainty

Diagnostics confirming stable sampling behavior

These outputs allow interpretation of both timing and magnitude of regime shifts rather than relying on a single deterministic breakpoint.

Interpretation

The detected change point corresponds to a statistically meaningful shift in Brent oil price behavior. Such shifts often align with:

Global geopolitical shocks

Oil supply disruptions

Financial crises

Major policy or production changes

Because the model is Bayesian, results should be interpreted probabilistically, not as exact dates.

Limitations

The model assumes a single dominant change point

Variance is assumed constant across regimes

External explanatory variables are not directly included

Results are associative, not causal

These limitations are acknowledged and addressed conceptually in future extensions.

Future Work (Optional Extensions)

Potential improvements include:

Incorporating macroeconomic variables such as GDP, inflation, or exchange rates

Extending to multiple change points

Applying Markov-Switching models to explicitly model calm vs volatile regimes

Using VAR models to study dynamic interactions between oil prices and economic indicators

Project Structure (Relevant Files)
.
├── data/
│   └── BrentOilPrices.csv
├── notebooks/
│   └── task2_change_point_analysis.ipynb
├── README.md

Key Takeaway

This task demonstrates how Bayesian change point modeling can uncover meaningful structural breaks in oil prices while explicitly accounting for uncertainty — a critical advantage when analyzing volatile economic time series.

# Brent Oil Prices Dashboard

## Setup

### Backend
1. Activate venv: `source venv/Scripts/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Run server: `python app.py`
4. API endpoints:
   - `/api/prices/`
   - `/api/changepoints/`
   - `/api/events/`

### Frontend
1. `cd src`
2. Install dependencies: `npm install`
3. Run app: `npm start`
4. Open `http://localhost:3000`

### Features
- Interactive price chart
- Change point visualization
- Event overlay with highlights
- Date range filter
- Key indicators: average price & volatility
## Dashboard Screenshots

### Overview
![Dashboard Overview](screenshots/dashboard_overview.png)

### Event Highlight
![Event Highlight](screenshots/event_highlight.png)

### Drill-down Example
![Drill-down Example](screenshots/drilldown_example.png)

Running the Full Dashboard (Backend + Frontend)
📦 Prerequisites

Python 3.10+

Node.js 18+

npm

Virtual environment (venv)

🔹 Step 1: Start Backend (Flask)
1. Navigate to backend folder
cd backend

2. Activate virtual environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run Flask server
python app.py


You should see:

Running on http://127.0.0.1:5000


Backend is now running.

🔹 Step 2: Start Frontend (React)

Open a new terminal (keep backend running).

1. Navigate to project root
cd ..

2. Install frontend dependencies (if not installed)
npm install

3. Start React app
npm start


Frontend runs at:

http://localhost:3000

🔹 Important

Backend must run on:

http://127.0.0.1:5000


Frontend must run on:

http://localhost:3000


Both must be running at the same time.

## 📊 Dashboard Screenshots

### 🔹 Dashboard Overview
![Overview](screenshots/dashboard_overview.png)

### 🔹 Date Filtering
![Filtering](screenshots/date_filtering.png)

### 🔹 Event Highlight
![Event Highlight](screenshots/event_highlight.png)

### 🔹 Responsive Design

Desktop:
![Desktop](screenshots/desktop_view.png)

Tablet:
![Tablet](screenshots/tablet_view.png)

Mobile:
![Mobile](screenshots/mobile_view.png)

