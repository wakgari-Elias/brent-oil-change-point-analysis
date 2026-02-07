# Task 1: Laying the Foundation for Analysis

## Objective
This analysis aims to understand how major geopolitical, economic, and policy-driven events affect Brent oil prices. The focus is on identifying structural changes in price behavior over time and preparing the groundwork for Bayesian change point modeling.

---

## Data Analysis Workflow

1. **Data Ingestion**
   - Load historical Brent oil price data
   - Parse dates and ensure chronological order

2. **Exploratory Data Analysis**
   - Visualize raw price trends
   - Identify major shocks and long-term movements

3. **Time Series Transformation**
   - Compute log returns to stabilize variance
   - Prepare data for statistical testing

4. **Time Series Diagnostics**
   - Trend inspection
   - Stationarity testing using Augmented Dickey-Fuller test
   - Volatility clustering analysis

5. **Event Data Integration**
   - Compile a structured dataset of major oil-market-related events
   - Align statistical change points with historical events

6. **Model Preparation**
   - Justify Bayesian change point modeling choices
   - Define expected outputs and limitations

---

## Event Data Compilation

A dataset of 15 major geopolitical, economic, and policy events was programmatically generated. Events include wars, OPEC decisions, sanctions, and global economic shocks that plausibly affected oil prices.

---

## Assumptions and Limitations

### Assumptions
- Brent oil price reflects global oil market dynamics
- Structural breaks occur close to major real-world events
- Daily price data is sufficient to capture regime changes

### Limitations
- Statistical change points indicate correlation, not causation
- Multiple overlapping events may influence prices simultaneously
- External macroeconomic variables are not included

Correlation in time does not prove that an event caused a price change; it only indicates a temporal association.

---

## Communication Channels

- Technical reports (PDF or Medium-style blog)
- Interactive dashboards for stakeholders
- Visual summaries for policymakers and investors

---

## Understanding the Model Choice

Change point models identify moments when the statistical properties of a time series change. In oil markets, these models are effective for detecting regime shifts caused by geopolitical or economic shocks.

---

## Expected Outputs and Limitations

Expected outputs include:
- Probabilistic estimates of change point dates
- Estimated price levels before and after changes
- Quantified uncertainty

Limitations include model simplicity and uncertainty in event attribution.
