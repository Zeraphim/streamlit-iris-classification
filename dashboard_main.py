# -------------------------

# Library Imports

# Streamlit
import streamlit as st

# Data Analysis
import pandas as pd
import numpy as np

# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import plot_tree

# -------------------------

# Page configuration
st.set_page_config(
    page_title="Iris Classification", 
    page_icon="assets/icon/icon.png",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")

# -------------------------

# Sidebar

# page_selection = 'about'

page_selection = 'data_cleaning'

with st.sidebar:

    st.title('Iris Classification')

    # Page Button Navigation
    st.subheader("Pages")

    if st.button("About", use_container_width=True):
        page_selection = 'about'
    
    if st.button("Dataset", use_container_width=True):
        page_selection = 'dataset'

    if st.button("EDA", use_container_width=True):
        page_selection = "eda"

    if st.button("Data Cleaning / Pre-processing", use_container_width=True):
        page_selection = "data_cleaning"

    if st.button("Machine Learning", use_container_width=True): 
        page_selection = "machine_learning"

    if st.button("Prediction", use_container_width=True): 
        page_selection = "prediction"

    if st.button("Conclusion", use_container_width=True):
        page_selection = "conclusion"

    # Project Details
    st.subheader("Abstract")
    st.markdown("A Streamlit dashboard highlighting the results of a training two classification models using the Iris flower dataset from Kaggle.")
    st.markdown("📊 [Dataset](https://www.kaggle.com/datasets/arshid/iris-flower-dataset)")
    st.markdown("📗 [Google Colab Notebook](https://colab.research.google.com/drive/1KJDBrx3akSPUW42Kbeepj64ZisHFD-NV?usp=sharing)")
    st.markdown("by: `Zeraphim`")

# -------------------------

# Data

# Load data
iris_df = pd.read_csv("data/IRIS.csv")

# -------------------------

# Plots


def pie_chart(column, width, height, key):

    # Generate a pie chart
    pie_chart = px.pie(iris_df, names=iris_df[column].unique(), values=iris_df[column].value_counts().values)

    # Adjust the height and width
    pie_chart.update_layout(
        width=width,  # Set the width
        height=height  # Set the height
    )

    st.plotly_chart(pie_chart, use_container_width=True,  key=f"pie_chart_{key}")

def scatter_plot(column, width, height, key):

    # Generate a scatter plot
    scatter_plot = px.scatter(iris_df, x=iris_df['species'], y=iris_df[column])

    # Adjust the height and width
    scatter_plot.update_layout(
        width=width,  # Set the width
        height=height  # Set the height
    )

    st.plotly_chart(scatter_plot, use_container_width=True, key=f"scatter_plot_{key}")

def pairwise_scatter_plot(key):
    # Generate a pairwise scatter plot matrix
    scatter_matrix = px.scatter_matrix(
        iris_df,
        dimensions=iris_df.columns[:-1],  # Exclude the species column from dimensions
        color='species',  # Color by species
    )

    # Adjust the layout
    scatter_matrix.update_layout(
        width=500,  # Set the width
        height=500  # Set the height
    )

    st.plotly_chart(scatter_matrix, use_container_width=True, key=f"pairwise_scatter_plot_{key}")


# -------------------------

# Pages

# About Page
if page_selection == "about":
    st.header("ℹ️ About")

    st.markdown(""" 

    This notebook explores the Iris flower dataset by performing:
    1. Exploratory Data Analysis (EDA)
    2. Data Pre-processing
    3. Training two supervised classification models: **Decision Tree Classifier** and **Random Forest Regressor**
    4. Making predictions on a new **unseen data**


    """)

# Dataset Page
elif page_selection == "dataset":
    st.header("📊 Dataset")

    st.markdown("""

    The **Iris flower dataset** was introduced by **Ronald Fisher** in 1936, it is a dataset used widely in machine learning. Originally collected by Edgar Anderson, it includes **50 samples** each from three Iris species (**Iris Setosa**, **Iris Virginica**, and **Iris Versicolor**).  

    For each sample, four features are measured: sepal length, sepal width, petal length, and petal width (in centimeters). This dataset is commonly used to test classification techniques like support vector machines. The same dataset that is used for this data science activity was uploaded to Kaggle by the user named **Mathnerd**.

    **Content**  
    The dataset has **150** rows containing **5 primary attributes** that are related to the iris flower, the columns are as follows: **Petal Length**, **Petal Width**, **Sepal Length**, **Sepal width**, and **Class(Species)**.

    `Link:` https://www.kaggle.com/datasets/arshid/iris-flower-dataset            
                
    """)

    # Display the dataset
    st.subheader("Dataset displayed as a Data Frame")
    st.dataframe(iris_df, use_container_width=True, hide_index=True)

# EDA Page
elif page_selection == "eda":
    st.header("📈 Exploratory Data Analysis (EDA)")

    col = st.columns((3, 3, 3), gap='medium')

    with col[0]:

        with st.expander('Legend', expanded=True):
            st.write('''
                - Data: [Iris Flower Dataset](https://www.kaggle.com/datasets/arshid/iris-flower-dataset).
                - :orange[**Pie Chart**]: Distribution of the 3 Iris species in the dataset.
                - :orange[**Scatter Plots**]: Difference of Iris species' features.
                - :orange[**Pairwise Scatter Plot Matrix**]: Highlighting *overlaps* and *differences* among Iris species' features.
                ''')


        st.markdown('#### Class Distribution')
        pie_chart("species", 500, 350, 1)

    with col[1]:
        st.markdown('#### Sepal Length by Species')
        scatter_plot("sepal_length", 500, 300, 1)

        st.markdown('#### Sepal Width by Species')
        scatter_plot("sepal_width", 500, 300, 2)
        
    with col[2]:
        st.markdown('#### Petal Length by Species')
        scatter_plot("petal_length", 500, 300, 3)

        st.markdown('#### Petal Width by Species')
        scatter_plot("petal_width", 500, 300, 4)

    st.markdown('#### Pairwise Scatter Plot Matrix')
    pairwise_scatter_plot(1)

    # Insights Section
    st.header("💡 Insights")

    st.markdown('#### Class Distribution')
    pie_chart("species", 600, 500, 2)

    st.markdown("""
                
    Based on the results we can see that there's a **balanced distribution** of the `3 Iris flower species`. With this in mind, we don't need to perform any pre-processing techniques anymore to balance the classes since it's already balanced.
         
    """)

    st.markdown('#### Sepal Length by Species')
    scatter_plot("sepal_length", 600, 500, 5)

    st.markdown("""

    By using a **scatter plot** to visualize the **sepal length** associated with each iris species in the dataset. We can see that *there's a substantial difference* between the sepal length of each classes, indicating that this attribute of Iris species do vary.  

    However, it is important to note that there are some **outliers** which overlaps with other Iris species which may affect the model's ability to classify each species.
         
    """)

    st.markdown('#### Sepal Width by Species')
    scatter_plot("sepal_width", 600, 500, 6)

    st.markdown("""

    Using a scatter plot again for the **sepal width**, results show that the sepal width of each Iris species do vary but outliers still exist.
         
    """)
    
    st.markdown('#### Petal Length by Species')
    scatter_plot("petal_length", 600, 500, 7)

    st.markdown("""

    Another scatter plot for the **Petal Length** highlights the difference between the petal length of the Iris species. Outliers does not deviate that much and overlapping is fairly low especially for *Iris Setosa*.
         
    """)

    st.markdown('#### Petal Width by Species')
    scatter_plot("petal_width", 600, 500, 8)

    st.markdown("""

    Lastly, the scatter plot for the **Petal Width** depicts a clear difference between the Iris flower's Petal Width based on the 3 species. However, there's an overlap of values between **Iris Versicolor** and **Iris Virginica** which might affect the training of our classification model.
         
    """)

    st.markdown('#### Pairwise Scatter Plot Matrix')
    pairwise_scatter_plot(2)

    st.markdown("""

    To highlight the *differences* and *overlaps* between Iris species' features, we now use a **Pairwise Scatter Plot Matrix** from Seaborn library to observe patterns, separability, and correlations between feature pairs of different Iris species. The results highlight the differences between Iris species' features.  

    Based on the results, **Iris Setosa** forms a distinct cluster separate from the other 2 species (Versicolor and Virginica) in terms of petal length and petal width. However, in terms of sepal width and sepal length there's a clear overlap with the other 2 species.  

    **Iris Versicolor** on the other hand shows a clear overlap with Iris Virginica's features especially in terms of *sepal length*, *sepal width*, *petal length*, and *petal width*. It is also worth noting that Iris Versicolor shows no overlap with Iris setosa in terms of *petal length* and *petal width*.

    Lastly, **Iris Virginica's** features tend to overlap with the other 2 species in terms of *sepal length* and *sepal width*. There's a distinct overlap as well with Iris Versicolor's *petal length* and *petal width*.  
         
    """)

# Data Cleaning Page
elif page_selection == "data_cleaning":
    st.header("🧼 Data Cleaning and Data Pre-processing")

    st.dataframe(iris_df.head(), use_container_width=True, hide_index=True)

    st.markdown("""

    Since the distribution of Iris species in our dataset is **balanced** and there are **0 null values** as well in our dataset. We will be proceeding alredy with creating the **Embeddings** for the *species* column and **Train-Test split** for training our machine learning model.
         
    """)

    encoder = LabelEncoder()

    iris_df['species_encoded'] = encoder.fit_transform(iris_df['species'])

    st.dataframe(iris_df.head(), use_container_width=True, hide_index=True)

    st.markdown("""

    Now we converted the values of **species** column to numerical values using `LabelEncoder`. The **species_encoded** column can now be used as a label for training our supervised model.
         
    """)

    # Mapping of the Iris species and their encoded equivalent

    unique_species = iris_df['species'].unique()
    unique_species_encoded = iris_df['species_encoded'].unique()

    # Create a new DataFrame
    species_mapping_df = pd.DataFrame({'Species': unique_species, 'Species Encoded': unique_species_encoded})

    # Display the DataFrame
    st.dataframe(species_mapping_df, use_container_width=True, hide_index=True)

    st.markdown("""

    With the help of **embeddings**, Iris-setosa is now represented by a numerical value of **0**, Iris-versicolor represented by **1**, and Iris-virginica represented by **2**.
         
    """)

    st.subheader("Train-Test Split")

    # Select features and target variable
    features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    X = iris_df[features]
    y = iris_df['species_encoded']

    st.code("""

    # Select features and target variable
    features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    X = iris_df[features]
    y = iris_df['species_encoded']

            
    """)

    st.markdown("""

    Now we select the features and labels for training our model.  
    The potential `features` that we can use are **sepal_length**, **sepal_width**, **petal_length**, and **petal_width**.  
    As for the `label` we can use the **species_encoded** column derived from the *species* column.
         
    """)

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    st.code("""

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
                
    """)

    st.subheader("X_train")
    st.dataframe(X_train, use_container_width=True, hide_index=True)

    st.subheader("X_test")
    st.dataframe(X_test, use_container_width=True, hide_index=True)

    st.subheader("y_train")
    st.dataframe(y_train, use_container_width=True, hide_index=True)

    st.subheader("y_test")
    st.dataframe(y_test, use_container_width=True, hide_index=True)

    st.markdown("After splitting our dataset into `training` and `test` set. We can now proceed with **training our supervised models**.")

# Machine Learning Page
elif page_selection == "machine_learning":
    st.header("🤖 Machine Learning")

# Prediction Page
elif page_selection == "prediction":
    st.header("👀 Prediction")

# Conclusions Page
elif page_selection == "conclusion":
    st.header("📝 Conclusion")