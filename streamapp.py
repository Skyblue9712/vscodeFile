import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = r'streamapp.csv'
df = pd.read_csv(file_path)
# Set page configuration
st.set_page_config(page_title="Supermarket Sales Analysis", page_icon=":bar_chart:")
st.title("Supermarket Sales Analysis 📊",)
st.subheader("Dataset Overview")
st.dataframe(df.head())
if __name__ == '__main__':
    st.write("Welcome to the Supermarket Sales Analysis App!")
    st.sidebar.title("Navigation")
    app_mode = st.sidebar.selectbox("Choose the analysis type", ["Original Dataset", "Graphs"])

    if app_mode == "Original Dataset":
        st.write("## Original Dataset")
        st.dataframe(df)

    elif app_mode == "Graphs":
        st.write("## Data Visualization")

        selected_graph = st.sidebar.selectbox("Select a graph:", ["Total Sales by Product Line", "Monthly Sales", "Payment Method Distribution","Unit Price Distribution by Product Line","Quantity Distribution","Unit Price vs. Quantity","Gender Distribution","Gross Income Distribution by Branch","Correlation Matrix","Pairwise Relationships"])

        if selected_graph == "Total Sales by Product Line":
            # Graph 1: Bar chart - Product line sales
            st.subheader("Graph 1: Total Sales by Product Line")
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            sns.barplot(x='Product line', y='Total', data=df, ci=None, ax=ax1)
            plt.xticks(rotation=45)
            st.pyplot(fig1)

        elif selected_graph == "Monthly Sales":
            # Graph 2: Line chart - Monthly sales
            df['Date'] = pd.to_datetime(df['Date'])
            df['Month'] = df['Date'].dt.month
            monthly_sales = df.groupby('Month')['Total'].sum().reset_index()
            st.subheader("Graph 2: Monthly Sales")
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            sns.lineplot(x='Month', y='Total', data=monthly_sales, marker='o', ax=ax2)
            plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
            st.pyplot(fig2)

        elif selected_graph == "Payment Method Distribution":
            # Graph 3: Pie chart - Payment method distribution
            st.subheader("Graph 3: Payment Method Distribution")
            fig3, ax3 = plt.subplots(figsize=(8, 8))
            df['Payment'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax3)
            st.pyplot(fig3)

        elif selected_graph == "Unit Price Distribution by Product Line":
            st.subheader("Graph 4: Unit Price Distribution by Product Line")
            fig4, ax4 = plt.subplots(figsize=(10, 6))
            sns.boxplot(x='Product line', y='Unit price', data=df, ax=ax4)
            plt.xticks(rotation=45)
            st.pyplot(fig4)
        elif selected_graph == "Quantity Distribution":
            # Graph 5: Histogram - Quantity distribution
            st.subheader("Graph 5: Quantity Distribution")
            fig5, ax5 = plt.subplots(figsize=(10, 6))
            sns.histplot(df['Quantity'], bins=20, kde=True, ax=ax5)
            st.pyplot(fig5)
        elif selected_graph == "Unit Price vs. Quantity":
            # Graph 6: Scatter plot - Unit price vs. Quantity
            st.subheader("Graph 6: Unit Price vs. Quantity")
            fig6, ax6 = plt.subplots(figsize=(10, 6))
            sns.scatterplot(x='Unit price', y='Quantity', data=df, ax=ax6)
            st.pyplot(fig6)
        elif selected_graph == "Gender Distribution":
            st.subheader("Graph 7: Gender Distribution")
            fig7, ax7 = plt.subplots(figsize=(8, 6))
            sns.countplot(x='Gender', data=df, ax=ax7)
            st.pyplot(fig7)
        elif selected_graph == "Gross Income Distribution by Branch":
            st.subheader("Graph 8: Gross Income Distribution by Branch")
            fig8, ax8 = plt.subplots(figsize=(10, 6))
            sns.violinplot(x='Branch', y='gross income', data=df, ax=ax8)
            st.pyplot(fig8)
        elif selected_graph == "Correlation Matrix":
            st.subheader("Graph 9: Correlation Matrix")
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
            correlation_matrix = df[numeric_columns].corr()
            # Plot the heatmap
            fig9, ax9 = plt.subplots(figsize=(10, 8))
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax9)
            st.pyplot(fig9)
        elif selected_graph == "Pairwise Relationships":
            st.subheader("Graph 10: Pairwise Relationships")
            fig10 = sns.pairplot(df[['Unit price', 'Quantity', 'Total', 'gross income']])
            st.pyplot(fig10)
        else:
            st.warning("Please select a valid graph from the dropdown.")
# Graph 1: Bar chart - Product line sales
st.subheader("Graph 1: Total Sales by Product Line")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='Product line', y='Total', data=df, ci=None, ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)
# Graph 2: Line chart - Monthly sales
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
monthly_sales = df.groupby('Month')['Total'].sum().reset_index()
st.subheader("Graph 2: Monthly Sales")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.lineplot(x='Month', y='Total', data=monthly_sales, marker='o', ax=ax2)
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
st.pyplot(fig2)
# Graph 3: Pie chart - Payment method distribution
st.subheader("Graph 3: Payment Method Distribution")
fig3, ax3 = plt.subplots(figsize=(8, 8))
df['Payment'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax3)
st.pyplot(fig3)
# Graph 4: Boxplot - Unit price by Product line
st.subheader("Graph 4: Unit Price Distribution by Product Line")
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Product line', y='Unit price', data=df, ax=ax4)
plt.xticks(rotation=45)
st.pyplot(fig4)
# Graph 5: Histogram - Quantity distribution
st.subheader("Graph 5: Quantity Distribution")
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.histplot(df['Quantity'], bins=20, kde=True, ax=ax5)
st.pyplot(fig5)
# Graph 6: Scatter plot - Unit price vs. Quantity
st.subheader("Graph 6: Unit Price vs. Quantity")
fig6, ax6 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Unit price', y='Quantity', data=df, ax=ax6)
st.pyplot(fig6)
# Graph 7: Countplot - Gender distribution
st.subheader("Graph 7: Gender Distribution")
fig7, ax7 = plt.subplots(figsize=(8, 6))
sns.countplot(x='Gender', data=df, ax=ax7)
st.pyplot(fig7)
# Graph 8: Violin plot - Gross income distribution by Branch
st.subheader("Graph 8: Gross Income Distribution by Branch")
fig8, ax8 = plt.subplots(figsize=(10, 6))
sns.violinplot(x='Branch', y='gross income', data=df, ax=ax8)
st.pyplot(fig8)
# Graph 9: Heatmap - Correlation matrix
st.subheader("Graph 9: Correlation Matrix")
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numeric_columns].corr()
# Plot the heatmap
fig9, ax9 = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax9)
st.pyplot(fig9)
# Graph 10: Pairplot - Pairwise relationships
st.subheader("Graph 10: Pairwise Relationships")
fig10 = sns.pairplot(df[['Unit price', 'Quantity', 'Total', 'gross income']])
st.pyplot(fig10)

#End
