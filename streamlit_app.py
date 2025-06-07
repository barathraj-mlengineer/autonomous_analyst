import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data import csv_loader, db_connector
from agent.groq_mixtral_agent import run_agent
from pdf import pdf_exporter
import admin_panel
import seaborn as sns
st.set_page_config(page_title="Autonomous Data Analyst AI", layout="wide")

menu = st.sidebar.radio("Navigation", ["Dashboard", "Admin"])

if menu == "Dashboard":
    st.title("📊 Autonomous Data Analyst")
    uploaded_file = st.file_uploader("Upload CSV File")
    query = st.text_input("Or write a PostgreSQL query")

    if uploaded_file:
        df = csv_loader.load_csv(uploaded_file)
    elif query:
        df = db_connector.fetch_postgres_data(query)
    else:
        df = None

    if df is not None:
        st.dataframe(df)
        st.markdown("### Summary by AI")
        summary = run_agent(f"Give a summary analysis for this dataframe:\n{df.head(10).to_markdown()}")
        st.info(summary)

        st.markdown("### Histogram")
        fig, ax = plt.subplots()
        df.hist(ax=ax)
        plt.tight_layout(pad=3.0)
        st.pyplot(fig)

# ========================
# Scatter Plot
# ========================
        st.markdown("### Scatter Plot")

        numerical_cols = df.select_dtypes(include='number').columns.tolist()
        if len(numerical_cols) >= 2:
            x_axis = st.selectbox("Select X-axis for Scatter Plot", numerical_cols, key="scatter_x")
            y_axis = st.selectbox("Select Y-axis for Scatter Plot", numerical_cols, key="scatter_y")
            fig, ax = plt.subplots()
            ax.scatter(df[x_axis], df[y_axis], alpha=0.7)
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            ax.set_title(f"{y_axis} vs {x_axis}")
            plt.tight_layout(pad=3.0)
            st.pyplot(fig)
        else:
            st.warning("Not enough numerical columns for scatter plot.")

# ========================
# Line Chart
# ========================
        st.markdown("### Line Chart")
        if len(numerical_cols) >= 2:
            x_line = st.selectbox("Select X-axis for Line Chart", numerical_cols, key="line_x")
            y_line = st.selectbox("Select Y-axis for Line Chart", numerical_cols, key="line_y")
            fig, ax = plt.subplots()
            ax.plot(df[x_line], df[y_line])
            ax.set_xlabel(x_line)
            ax.set_ylabel(y_line)
            ax.set_title(f"{y_line} over {x_line}")
            plt.tight_layout(pad=3.0)
            st.pyplot(fig)
        else:
            st.warning("Not enough numerical columns for line chart.")

# ========================
# Bar Chart
# ========================
        st.markdown("### Bar Chart")

# Pick categorical and numerical columns
        categorical_cols = df.select_dtypes(include='object').columns.tolist()
        if categorical_cols and numerical_cols:
            cat_col = st.selectbox("Select Categorical Column", categorical_cols, key="bar_cat")
            num_col = st.selectbox("Select Numerical Column", numerical_cols, key="bar_num")

            bar_data = df.groupby(cat_col)[num_col].mean().sort_values()

            fig, ax = plt.subplots()
            bar_data.plot(kind="bar", ax=ax)
            ax.set_ylabel(f"Average {num_col}")
            ax.set_title(f"Average {num_col} by {cat_col}")
            plt.tight_layout(pad=3.0)
            st.pyplot(fig)
        else:
            st.warning("Need both categorical and numerical columns for bar chart.")

# ========================
# Heatmap
# ========================
        st.markdown("### Heatmap")

        numerical_df = df.select_dtypes(include=['number'])

        if numerical_df.shape[1] >= 2:
          fig, ax = plt.subplots()
          sns.heatmap(numerical_df.corr(), annot=True, cmap="coolwarm", ax=ax)
          st.pyplot(fig)
        else:
          st.warning("Not enough numerical columns to generate a heatmap.")

# ========================
# Pie Chart
# ========================
        st.markdown("### Pie Chart from Categorical Column")

        if categorical_cols:
           selected_col = st.selectbox("Select a categorical column", categorical_cols, key="pie_col")
           category_counts = df[selected_col].value_counts()

           fig, ax = plt.subplots()
           ax.pie(category_counts.values,
           labels=category_counts.index,
           autopct='%1.1f%%',
           startangle=90)
           ax.axis('equal')
           plt.tight_layout(pad=3.0)
           st.pyplot(fig)
        else:
           st.warning("No categorical columns found for pie chart.")



        if st.button("📥 Download PDF Report"):
            fig_path = "chart.png"
            fig.savefig(fig_path)
            pdf_exporter.generate_pdf(summary, fig_path)
            with open("report.pdf", "rb") as f:
                st.download_button("Download Report", f, file_name="report.pdf")

elif menu == "Admin":
    admin_panel.show_admin()