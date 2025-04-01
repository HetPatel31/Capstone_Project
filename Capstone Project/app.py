import streamlit as st  # Import Streamlit for building the web app
import pandas as pd  # Import pandas for data handling
import matplotlib.pyplot as plt  # Import matplotlib for visualizations
import seaborn as sns  # Import seaborn for statistical data visualization

# Load dataset
df = pd.read_csv('HR-Employee-Attrition.csv')  # Read the HR employee attrition dataset

# Set up Streamlit page
st.set_page_config(page_title="HR Attrition EDA", layout="wide")  # Configure the Streamlit page settings
st.title("📊 HR Attrition EDA Dashboard 🚀")  # Set the title of the dashboard
st.sidebar.header("🔍 Navigation")  # Add a sidebar header for navigation

# Theme Toggle 🎨
theme = st.sidebar.radio("🎨 Select Theme:", ["🌞 Light Mode", "🌙 Dark Mode"])  # Radio button for theme selection

# Apply Theme
if theme == "🌙 Dark Mode":
    dark_style = {
        "backgroundColor": "#1E1E1E",  # Dark background
        "textColor": "#FFFFFF",  # White text
        "gridColor": "#666666"  # Gray grid lines
    }
    plt.style.use("dark_background")  # Apply dark theme to matplotlib
    sns.set_style("darkgrid")  # Apply dark grid style in seaborn
else:
    dark_style = {
        "backgroundColor": "#FFFFFF",  # White background
        "textColor": "#000000",  # Black text
        "gridColor": "#DDDDDD"  # Light gray grid lines
    }
    plt.style.use("default")  # Apply default matplotlib theme
    sns.set_style("whitegrid")  # Apply white grid seaborn style

# Select visualization 📊
viz_option = st.sidebar.selectbox("📊 Choose a visualization", [
    "📌 Count Plot - Categorical Features",
    "📌 Box Plot - Numerical Features",
    "📌 Histogram - Numerical Distribution",
    "📌 Correlation Heatmap"
])  # Sidebar dropdown menu for visualization selection

# Count Plot - Categorical Features 🏷️
if viz_option == "📌 Count Plot - Categorical Features":
    st.header("🏷️ Count Plot for Categorical Features")  # Section header
    categorical_features = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'OverTime']
    selected_feature = st.selectbox("🔍 Select a categorical feature:", categorical_features)  # Dropdown for selecting categorical feature

    fig, ax = plt.subplots(figsize=(8, 4))  # Create a figure and axis for the plot
    sns.countplot(data=df, x=selected_feature, palette='viridis', ax=ax)  # Generate count plot

    # Apply Theme
    ax.set_facecolor(dark_style["backgroundColor"])  # Set background color based on theme
    ax.xaxis.label.set_color(dark_style["textColor"])  # Set x-axis label color
    ax.yaxis.label.set_color(dark_style["textColor"])  # Set y-axis label color
    ax.tick_params(colors=dark_style["textColor"])  # Set tick colors
    
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    st.pyplot(fig)  # Display the plot in Streamlit

# Box Plot - Numerical Features 📦
elif viz_option == "📌 Box Plot - Numerical Features":
    st.header("📦 Box Plots for Numerical Features")  # Section header
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns  # Get numerical columns
    selected_feature = st.selectbox("🔍 Select a numerical feature:", numerical_features)  # Dropdown for numerical feature selection

    fig, ax = plt.subplots(figsize=(8, 4))  # Create figure and axis
    sns.boxplot(data=df, x=selected_feature, palette='coolwarm', ax=ax)  # Generate box plot

    # Apply Theme
    ax.set_facecolor(dark_style["backgroundColor"])  # Set background color based on theme
    ax.xaxis.label.set_color(dark_style["textColor"])  # Set x-axis label color
    ax.yaxis.label.set_color(dark_style["textColor"])  # Set y-axis label color
    ax.tick_params(colors=dark_style["textColor"])  # Set tick colors

    st.pyplot(fig)  # Display the plot in Streamlit

# Histogram - Numerical Distribution 📊
elif viz_option == "📌 Histogram - Numerical Distribution":
    st.header("📊 Histograms for Numerical Features")  # Section header
    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns  # Get numerical columns
    selected_feature = st.selectbox("🔍 Select a numerical feature:", numerical_features)  # Dropdown for numerical feature selection

    fig, ax = plt.subplots(figsize=(8, 4))  # Create figure and axis
    sns.histplot(df[selected_feature], bins=30, kde=True, color='blue', ax=ax)  # Generate histogram with KDE

    # Apply Theme
    ax.set_facecolor(dark_style["backgroundColor"])  # Set background color based on theme
    ax.xaxis.label.set_color(dark_style["textColor"])  # Set x-axis label color
    ax.yaxis.label.set_color(dark_style["textColor"])  # Set y-axis label color
    ax.tick_params(colors=dark_style["textColor"])  # Set tick colors

    st.pyplot(fig)  # Display the plot in Streamlit

# Correlation Heatmap 🔥
elif viz_option == "📌 Correlation Heatmap":
    st.header("🔥 Correlation Heatmap")  # Section header
    fig, ax = plt.subplots(figsize=(12, 6))  # Create figure and axis
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)  # Generate correlation heatmap

    # Apply Theme
    ax.set_facecolor(dark_style["backgroundColor"])  # Set background color based on theme
    ax.xaxis.label.set_color(dark_style["textColor"])  # Set x-axis label color
    ax.yaxis.label.set_color(dark_style["textColor"])  # Set y-axis label color
    ax.tick_params(colors=dark_style["textColor"])  # Set tick colors

    st.pyplot(fig)  # Display the plot in Streamlit

st.sidebar.text("🚀 EDA Dashboard for HR Attrition Analysis")  # Sidebar footer text