# dashboard.py

import streamlit as st
import pandas as pd
import psycopg2

# Function to establish a connection to the PostgreSQL database
def connect_to_database():
    connection_params = {
        'host': 'localhost',
        'port': '5432',
        'database': 'dash_board_for_telecom',
        'user': 'postgres',
        'password': 'Nurye@68793',
    }

    return psycopg2.connect(**connection_params)

# Function to load data from the PostgreSQL database using psycopg2
def load_data(table_name):
    conn = connect_to_database()
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Function to add a new record to the specified table
def add_record(table_name, data):
    conn = connect_to_database()
    cursor = conn.cursor()

    columns = ', '.join(data.keys())
    values = ', '.join([f"'{value}'" for value in data.values()])

    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    cursor.execute(query)
    conn.commit()

    conn.close()

# Function to delete a record from the specified table
def delete_record(table_name, record_id):
    conn = connect_to_database()
    cursor = conn.cursor()

    query = f"DELETE FROM {table_name} WHERE id = {record_id}"
    cursor.execute(query)
    conn.commit()

    conn.close()

# Function to show updated tables after performing operations
def show_updated_tables():
    st.subheader("Updated User Engagement Table")
    updated_user_engagement_data = load_data("user_engagement")
    st.dataframe(updated_user_engagement_data)

    st.subheader("Updated Satisfaction Analysis Table")
    updated_satisfaction_analysis_data = load_data("satisfaction_analysis")
    st.dataframe(updated_satisfaction_analysis_data)

    st.subheader("Updated Customer Table")
    updated_customer_data = load_data("customers")
    st.dataframe(updated_customer_data)

# Set Streamlit page configuration
st.set_page_config(page_title="Telecom Dashboard", page_icon=":bar_chart:")

# Add CSS styles
# Add CSS styles
st.markdown("""
    <style>
        body {
            background-color: #00ff00; /* Green background */
            color: #333;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .stSiteHeader {
            background-color: #0000ff; /* Blue header */
            color: #fff;
        }
        .sidebar .sidebar-content {
            background-color: #333;
            color: #fff;
        }
        .sidebar .sidebar-content .block-container {
            margin-top: 20px;
        }
        .streamlit-table {
            overflow-x: auto;
        }
        h1, h2, h3 {
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)


# Streamlit app
def main():
    st.title("Telecom Database Dashboard")

    # Display tables checkbox
    display_tables = st.sidebar.checkbox("Display Tables", value=True)

    if display_tables:
        # Display tables
        st.subheader("User Engagement Table")
        user_engagement_data = load_data("user_engagement")
        st.dataframe(user_engagement_data)

        st.subheader("Satisfaction Analysis Table")
        satisfaction_analysis_data = load_data("satisfaction_analysis")
        st.dataframe(satisfaction_analysis_data)

        st.subheader("Customer Table")
        customer_data = load_data("customers")
        st.dataframe(customer_data)

    # Add, delete, and modify records
    st.sidebar.header("Data Operations")

    # Add Record
    st.sidebar.subheader("Add Record")
    add_table = st.sidebar.selectbox("Select Table for Add", ["user_engagement", "satisfaction_analysis", "customers"], key="add_table")
    add_data = {}
    add_columns = st.text_input(f"Enter column names for {add_table} separated by commas", key="add_columns")
    for column in add_columns.split(","):
        add_data[column.strip()] = st.sidebar.text_input(f"Enter {column.strip()}", key=f"add_{column.strip()}")

    if st.sidebar.button("Add Record"):
        add_record(add_table, add_data)
        show_updated_tables()

    # Delete Record
    st.sidebar.subheader("Delete Record")
    delete_table = st.sidebar.selectbox("Select Table for Delete", ["user_engagement", "satisfaction_analysis", "customers"], key="delete_table")
    delete_id = st.sidebar.text_input("Enter ID to Delete", key="delete_id")

    if st.sidebar.button("Delete Record"):
        delete_record(delete_table, delete_id)
        show_updated_tables()

    # Modify Record
    st.sidebar.subheader("Modify Record")
    modify_table = st.sidebar.selectbox("Select Table for Modify", ["user_engagement", "satisfaction_analysis", "customers"], key="modify_table")
    modify_id = st.sidebar.text_input("Enter ID to Modify", key="modify_id")

    modify_data = {}
    modify_columns = st.text_input(f"Enter column names for {modify_table} separated by commas", key="modify_columns")
    for column in modify_columns.split(","):
        modify_data[column.strip()] = st.sidebar.text_input(f"Enter New {column.strip()}", key=f"modify_{column.strip()}")

    if st.sidebar.button("Modify Record"):
        # Assuming you have a column named 'id' as the primary key
        delete_record(modify_table, modify_id)
        add_record(modify_table, modify_data)
        show_updated_tables()

if __name__ == '__main__':
    main()
