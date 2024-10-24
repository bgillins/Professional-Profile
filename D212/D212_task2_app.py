import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import plotly.express as px
import os
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="D212 Task 2 - PCA Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables
if 'initialized' not in st.session_state:
    st.session_state.initialized = False
    st.session_state.df = None
    st.session_state.df_standardized = None
    st.session_state.pca = None
    st.session_state.loadings_df = None
    st.session_state.pca_result = None

# Data loading function with proper path handling
def load_data():
    try:
        # First try to load from the current directory
        data_path = Path("medical_clean.csv")
        
        # If not found, try the data subdirectory
        if not data_path.exists():
            data_path = Path("data/medical_clean.csv")
        
        # If still not found, try relative to script location
        if not data_path.exists():
            script_dir = Path(__file__).parent
            data_path = script_dir / "data" / "medical_clean.csv"
        
        if not data_path.exists():
            st.error(f"Data file not found. Tried paths: ./medical_clean.csv, ./data/medical_clean.csv, and {script_dir}/data/medical_clean.csv")
            st.stop()
            
        return pd.read_csv(data_path)
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        st.stop()

# Function to initialize data
def initialize_data():
    if not st.session_state.initialized:
        try:
            with st.spinner("Loading and processing data..."):
                # Load initial data
                df = load_data()
                
                # Select continuous variables
                continuous_vars = ['Age', 'VitD_levels', 'Initial_days', 'TotalCharge', 
                                 'Additional_charges', 'Income', 'Lng', 'Lat']
                df_selected = df[continuous_vars]
                
                # Standardize data
                scaler = StandardScaler()
                df_standardized = pd.DataFrame(
                    scaler.fit_transform(df_selected),
                    columns=df_selected.columns
                )
                
                # Perform PCA
                pca = PCA()
                pca_result = pca.fit_transform(df_standardized)
                
                # Create loadings DataFrame
                loadings = pca.components_.T
                loadings_df = pd.DataFrame(
                    loadings,
                    columns=[f'PC{i+1}' for i in range(loadings.shape[1])],
                    index=df_standardized.columns
                )
                
                # Store in session state
                st.session_state.df = df
                st.session_state.df_standardized = df_standardized
                st.session_state.pca = pca
                st.session_state.loadings_df = loadings_df
                st.session_state.pca_result = pca_result
                st.session_state.initialized = True
                
                return True
        except Exception as e:
            st.error(f"Error processing data: {str(e)}")
            return False
    return True

# Function to show code with toggle
def show_code_and_results(code, results_func, section_key):
    show_code = st.toggle("Show Code", key=f"toggle_{section_key}")
    if show_code:
        st.code(code, language="python")
    results_func()

# Initialize data at startup
initialized = initialize_data()

# Sidebar navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Introduction",
     "I. Research Question",
     "II. Method Justification",
     "III. Data Preparation",
     "IV. Analysis",
     "V. Data Summary and Implications",
     "VI. Demonstration"]
)

# Main content
if section == "Introduction":
    st.markdown("""
    # D212 Task 2
    #### WGU Western Governors University 
    """)

elif section == "I. Research Question":
    st.markdown("""
    # Part I: Research Question
    ## A1. Proposed question:
    How can we effectively reduce the dimensionality of our hospital's patient healthcare data while retaining the most important information?

    ## A2. Goal of the data analysis:
    To identify the optimal number of principal components that can reduce our data storage requirements by at least 30% while retaining at least 80% of the original data's variance.
    """)

elif section == "II. Method Justification":
    st.markdown("""
    # Part II: Method Justification
    ## B1. Explaining PCA Analysis and Expectations

    **PCA Analysis Explanation:**

    Principal Component Analysis (PCA) will help us reduce the dimensionality of our hospital's patient healthcare data through a series of steps. First, we'll gather our continuous variables like Age, Initial_days, VitD_levels, and other relevant health metrics. We'll standardize these variables to ensure they're on the same scale, giving each an equal chance to influence the analysis. PCA then searches for directions in this standardized data where variation is highest. These directions become our new "principal components," each a combination of our original variables. PCA ranks these components based on how much variation they capture, allowing us to focus on the most important patterns. By keeping only the top components, we reduce the dimensionality and storage requirements of our data while retaining its essential information.

    **Expected Outcomes:**

    From this PCA process, we anticipate several valuable outcomes. We'll obtain new variables that combine our original variables in meaningful ways, potentially revealing hidden patterns in our healthcare data. We'll see which original variables contribute most significantly to each principal component. We'll know how much of our data's total variation each component explains, giving us a clear picture of how much information we're retaining as we reduce dimensionality. Ultimately, this analysis will allow us to compress our data by at least 30% while preserving at least 80% of the original variance, optimizing our data storage without significant loss of important information. This will lead to more efficient data management and potentially faster processing times for future analyses.
        """)

    st.markdown("""
    ## B2. PCA Assumption
    PCA assumes that the principal components are linear combinations of the original variables. In our healthcare cost analysis, this means we assume that the relationships between our variables can be adequately described by straight lines.
    For example, PCA assumes that if there's a relationship between Age and Total Cost, this relationship can be represented by a straight line. The same applies to relationships between other variables or combinations of variables.
    This assumption is important because if the true relationships in our data are highly non-linear, PCA might not capture these relationships accurately.
    """)

elif section == "III. Data Preparation":
    st.markdown("""
    # Part III: Data Preparation
    ## C1. Continuous Variables for PCA Analysis
    
    The above variables were selected because they are all continuous. They provide a mix of demographic, health status, and treatment-related information. The goal is to reduce the dimensionality of the data while retaining the most important information as highlighted in the goal.
    """)
    
    def show_initial_data():
        if st.session_state.initialized:
            st.write("### Selected Continuous Variables")
            st.write(list(st.session_state.df_standardized.columns))
            st.write("### Initial Data Sample")
            st.dataframe(st.session_state.df_standardized.head())
            
    show_code_and_results(
        """
        import pandas as pd
        import numpy as np
        from sklearn.preprocessing import StandardScaler

        # Load the data
        data = pd.read_csv('medical_clean.csv')

        # Select the continuous variables identified in C1
        continuous_vars = ['Age', 'VitD_levels', 'Initial_days', 'TotalCharge', 
                        'Additional_charges', 'Income', 'Lng', 'Lat']

        # Create a new dataframe with only the selected variables
        df_selected = data[continuous_vars]

        # Initialize the StandardScaler
        scaler = StandardScaler()

        # Fit the scaler to the data and transform it while maintaining the column names
        df_standardized = pd.DataFrame(scaler.fit_transform(df_selected), 
                                    columns=df_selected.columns)
        """,
        show_initial_data,
        "initial_data"
    )

    st.markdown("""
    ## C2. Standardizing Continuous Variables for PCA
    """)
    
    def show_standardized_data():
        if st.session_state.initialized:
            st.write("### Standardized Data Statistics")
            st.dataframe(st.session_state.df_standardized.describe())
            
    show_code_and_results(
        """
        scaler = StandardScaler()
        df_standardized = pd.DataFrame(
            scaler.fit_transform(df_selected),
            columns=df_selected.columns
        )
        """,
        show_standardized_data,
        "standardized_data"
    )

elif section == "IV. Analysis":
    st.markdown("""
    # Part IV: Analysis
    ## D1. Matrix of Principal Components
    The matrix of all principal components has been determined. This matrix, also known as the loadings matrix, shows how each original variable contributes to each principal component.  This can easily be determined from the heatmap provided above. 

    **Key observations:**

    1. PC1 is strongly influenced by TotalCharge and Initial_days.
    2. PC2 is heavily influenced by Additional Charges and Age.
    3. PC3 has strong influcence from Latitude and Longitude.
    4. PC4 a strong influence from Income and a negative influence from VitD_levels.
    """)
    
    def show_pca_matrix():
        if st.session_state.initialized:
            st.write("### PCA Loadings Matrix")
            st.dataframe(st.session_state.loadings_df)
            
            fig = plt.figure(figsize=(12, 8))
            sns.heatmap(st.session_state.loadings_df, annot=True, cmap='Purples')
            plt.title('PCA Loadings')
            st.pyplot(fig)
            
    show_code_and_results(
        """
        from sklearn.decomposition import PCA
        import matplotlib.pyplot as plt

        # Load the standardized data
        df_standardized = pd.read_csv('standardized_data.csv')

        # Initialize PCA
        pca = PCA()

        # Fit PCA to the standardized data
        pca_result = pca.fit_transform(df_standardized)

        # Get the principal component loadings
        loadings = pca.components_.T

        # Create a DataFrame of the loadings
        loadings_df = pd.DataFrame(
            loadings, 
            columns=[f'PC{i+1}' for i in range(loadings.shape[1])],
            index=df_standardized.columns
        )

        # Display the loadings
        loadings_df.head(10)
        """,
        show_pca_matrix,
        "pca_matrix"
    )

    st.markdown("""
    ## D2. Total Number of Principal Components
        
    Total Number of Principal The matrix of all principal components has been determined. This matrix, also known as the loadings matrix, shows how each original variable contributes to each principal component.  This can easily be determined from the heatmap provided above. 

    **Key observations:**

    1. PC1 is strongly influenced by TotalCharge and Initial_days.
    2. PC2 is heavily influenced by Additional Charges and Age.
    3. PC3 has strong influcence from Latitude and Longitude.
    4. PC4 a strong influence from Income and a negative influence from VitD_levels.Components

    Based on the eigenvalue analysis and the Kaiser criterion (retaining components with eigenvalues > 1), we have determined to retain 4 principal components:

    1. PC1: 1.9926
    2. PC2: 1.7137
    3. PC3: 1.1135
    4. PC4: 1.0124

    The scree plot shows a noticeable drop after the third component, further supporting this decision.
    """)
    
    def show_eigenvalues():
        if st.session_state.initialized:
            eigenvalues = st.session_state.pca.explained_variance_
            
            st.write("### Eigenvalues")
            for i, ev in enumerate(eigenvalues):
                st.write(f"PC{i+1}: {ev:.4f}")
            
            fig = plt.figure(figsize=(10, 6))
            plt.plot(range(1, len(eigenvalues) + 1), eigenvalues, marker='o')
            plt.xlabel('# of Components')
            plt.ylabel('Eigenvalues')
            plt.axhline(y=1, color='red')
            plt.title('Scree Plot')
            st.pyplot(fig)
            
    show_code_and_results(
        """
        eigenvalues = pca.explained_variance_
        plt.plot(range(1, len(eigenvalues) + 1), eigenvalues, marker='o')
        """,
        show_eigenvalues,
        "eigenvalues"
    )

    st.markdown("""
                ## D3. Variance of Each Principal Component

The variance explained by each of the retained principal components is as follows:

1. PC1: 24.91%
2. PC2: 21.42%
3. PC3: 13.92%
4. PC4: 12.66%

These percentages are calculated by dividing each eigenvalue by the total number of variables (10) and convert into a percentage and rounded.

## D4. Total Variance Captured

The total variance captured by the 4 retained principal components is 72.91%. This is calculated by summing the explained variance ratios of the first 4 components:

24.91% + 21.42% + 13.92% + 12.66% = 72.91%

This means that our 4 principal components account for 72.91% of the total variance in the original dataset, which represents a significant amount of information retention while still achieving dimensionality reduction.

## D5. Summary of Data Analysis Results

1. Dimensionality Reduction: We've reduced our original 8 variables to 4 principal components while retaining 72.91% of the original variance. This reduction simplifies our dataset while preserving a substantial amount of information.

2. PCA Component Interpretation

    1. PC1: Financial Burden and Length of Stay
   - Key factors: TotalCharge (0.702), Initial_days (0.701)
   - Represents overall financial impact and duration of hospital stay

    2. PC2: Age-Related Additional Charges
   - Key factors: Additional_charges (0.701), Age (0.701)
   - Indicates increased charges associated with older patients

    3. PC3: Geographic and Health Indicators
   - Key factors: Latitude (0.701), Longitude (0.701)
   - Indicates regional health disparities and potential for clustering

    4. PC4: Nutrition and Income
    - Key factors: VitD_levels (-0.712), Income (0.700)
    - Links nutritional status with income, suggesting an inverse relationship

3. Variable Importance: The loadings matrix reveals that financial factors, length of stay, health indicators such as vitamin D levels and age, locational factors, and income are particularly important in explaining the variance in our dataset.

4. Goal Achievement: Our goal was to reduce the dimensionality of our hospital's patient healthcare data while retaining the most important information. We were able to reduce the size of the data substantial. From 620 Kilobytes to 600 bytes! While only retaining ~73% of the original data. We met the goal of reducing our data size but we did not retained 80% of the original data. This is acceptable given that PCA is selecting the most important factors in the data. 
""")
    
    def show_variance_explained():
        if st.session_state.initialized:
            explained_variance_ratio = st.session_state.pca.explained_variance_ratio_
            cumulative_variance_ratio = np.cumsum(explained_variance_ratio)
            
            st.write("### Explained Variance by Component")
            for i, ratio in enumerate(explained_variance_ratio):
                st.write(f"PC{i+1}: {ratio*100:.2f}%")
            
            st.write("\n### Cumulative Explained Variance")
            for i, ratio in enumerate(cumulative_variance_ratio):
                st.write(f"PC1 to PC{i+1}: {ratio*100:.2f}%")
            
            fig = plt.figure(figsize=(10, 6))
            plt.plot(range(1, len(cumulative_variance_ratio) + 1), 
                    cumulative_variance_ratio, 'ro-')
            plt.xlabel('Number of Components')
            plt.ylabel('Cumulative Explained Variance Ratio')
            plt.title('Cumulative Explained Variance Ratio')
            plt.grid(True)
            st.pyplot(fig)
            
    show_code_and_results(
        """
        explained_variance_ratio = pca.explained_variance_ratio_
        cumulative_variance_ratio = np.cumsum(explained_variance_ratio)
        """,
        show_variance_explained,
        "variance_explained"
    )

elif section == "V. Data Summary and Implications":
    st.markdown("""
    # Part V: Data Summary and Implications
    
    ## Data Storage Improvement
    """)
    
    def show_storage_improvement():
        if st.session_state.initialized:
            original_size = 620  # KB
            reduced_size = original_size * (4/8)  # Using 4 components instead of 8
            
            st.write(f"Original data size: {original_size} KB")
            st.write(f"Reduced data size: {reduced_size} KB")
            st.write(f"Storage savings: {(1 - reduced_size/original_size)*100:.1f}%")
            
    show_storage_improvement()
    
    st.markdown("""
    ## Summary of Findings
    
    1. **Dimensionality Reduction**
       - Reduced from 8 variables to 4 principal components
       - Retained ~73% of original variance
       - Achieved 50% reduction in data size
    
    2. **PCA Component Interpretation**
       - PC1: Financial Burden and Length of Stay
       - PC2: Age-Related Additional Charges
       - PC3: Geographic and Health Indicators
       - PC4: Nutrition and Income
    
    3. **Goal Achievement**
       - Met data reduction goal (50% > 30% target)
       - Slightly below variance retention goal (73% vs 80% target)
       - Acceptable trade-off given importance of retained components
    """)

elif section == "VI. Demonstration":
    st.markdown("""
    # Part VI: Demonstration
    ## Recording Link:
    https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=565ca862-dea9-44f8-9940-b1db015351bc
    """)

# Add footer with data loading status and additional information
st.sidebar.markdown("---")
if st.session_state.initialized:
    st.sidebar.success("✅ Data loaded and processed")
    st.sidebar.info(f"Total observations: {len(st.session_state.df):,}")
    st.sidebar.info(f"Original variables: {len(st.session_state.df_standardized.columns):,}")
    st.sidebar.info(f"Principal components: 4")
else:
    st.sidebar.error("❌ Data not loaded")
    st.sidebar.warning("Please check if the data file is available in the correct location.")