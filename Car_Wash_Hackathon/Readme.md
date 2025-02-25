# Car Wash Data Analysis

## Overview

This project analyzes customer data from a car wash business to understand key insights, including conversion rates, referral effectiveness, and customer acquisition sources. The analysis uses **Python**, **Pandas**, **Matplotlib**, and **Seaborn** for data processing and visualization.

## Dataset

The dataset contains customer details, referral sources, and conversion metrics. Key columns include:

- **Customer Name** – Name of the customer.
- **Referral Source** – The platform that referred the customer (e.g., Social Media, Friends, Ads).
- **Number of Referrals** – How many people the customer has referred.
- **Converted** – Whether the customer availed the service (1 for Yes, 0 for No).

## Key Metrics & Visualizations

### 1️⃣ Social Media Conversion Rate

- Measures how many users from **Social Media** actually converted into customers.
- A **3D Pie Chart** is used to visualize the proportion of converted vs. non-converted users.

### 2️⃣ Referral Program Effectiveness

- Calculates the **average referrals per user**.
- Identifies the **Top 5 Referrers**.
- Uses a **Histogram** to show the distribution of referrals among users.

### 3️⃣ Who Recommended This?

- Breaks down customer acquisition by **Referral Source**.
- Uses a **2D Bar Chart** to compare different referral sources.

## How to Run the Code

1. Install required dependencies:
   ```bash
   pip install pandas matplotlib seaborn
   ```
2. Place the dataset (`data.csv`) in the project directory.
3. Run the script:
   ```bash
   python Social_Media.py
   ```

## Suggested Improvements

- Implement **interactive dashboards** using `plotly` or `streamlit`.
- Add **trend analysis** over time for referrals and conversions.
- Optimize performance for large datasets with `Dask` or `Vaex`.

---

Made with ❤️ for Data-Driven Decision Making! 🚀

