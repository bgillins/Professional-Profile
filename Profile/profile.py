import streamlit as st
import pandas as pd
from PIL import Image

def main():
        # Set page config
    st.set_page_config(page_title="Brandon Gillins - Profile", layout="wide")

    st.markdown("""
        <style>
        .main {
            background-color: #ffffff;  /* White background */
            color: #2d4a3e;  /* Forest green text */
        }
        .stMarkdown {
            color: #2d4a3e;  /* Forest green text */
        }
        .big-title {
            font-size: 48px !important;
            font-weight: bold !important;
            margin-bottom: 0px !important;
            text-align: center;
            color: #2d4a3e;  /* Forest green text */
        }
        .subtitle {
            font-size: 24px !important;
            text-align: center;
            margin-bottom: 20px !important;
            color: #2d4a3e;  /* Forest green text */
        }
        .experience-header {
            font-size: 18px !important;
            text-align: center;
            color: #2d4a3e;  /* Forest green text */
        }
        /* Left sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #2d4a3e;  /* Forest green background */
            padding: 20px;
        }
        [data-testid="stSidebar"] .stMarkdown {
            color: #ffffff !important;  /* White text in sidebar */
        }
        /* Button styling */
        div.stButton > button {
            width: 100%;
            background-color: #2d4a3e !important;  /* Forest green background */
            color: #ffffff !important;  /* White text */
            border: none;
            padding: 10px 15px;
            border-radius: 5px;
            font-weight: bold;
        }
        div.stButton > button:hover {
            background-color: #1f3830 !important;  /* Darker forest green on hover */
        }
        /* Section containers */
        .section-container {
            background-color: #ffffff;  /* White background */
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            border: 1px solid #2d4a3e;  /* Forest green border */
        }
        .profile-container {
            position: sticky;
            top: 0;
            padding-bottom: 20px;
        }
        /* Course sections */
        .course-header {
            color: #2d4a3e;  /* Forest green text */
            font-weight: bold;
            margin-bottom: 5px;
        }
        .course-description {
            margin-left: 20px;
            color: #2d4a3e;  /* Forest green text */
            font-size: 14px;
        }
        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 24px;
            background-color: #ffffff;  /* White background */
        }
        .stTabs [data-baseweb="tab"] {
            color: #2d4a3e;  /* Forest green text */
        }
        /* Links */
        .task-link {
            color: #2d4a3e !important;  /* Forest green links */
            text-decoration: underline;
        }
        /* Expander styling */
        div[data-testid="stExpander"] {
            background-color: #ffffff;  /* White background */
            border-radius: 5px;
            margin-bottom: 10px;
            border: 1px solid #2d4a3e;  /* Forest green border */
        }
        div[data-testid="stExpander"] > div[role="button"] {
            color: #2d4a3e;  /* Forest green text */
        }
        div[data-testid="stExpander"] div[data-testid="stMarkdownContainer"] {
            color: #2d4a3e;  /* Forest green text */
        }
        a {
            color: #2d4a3e !important;  /* Forest green links */
        }
        </style>
    """, unsafe_allow_html=True)
    # Main content columns
    left_col, right_col = st.columns([1, 2])

    with left_col:
        # Profile Photo and Contact in a container
        with st.container():
            # Profile Photo with fixed height
            try:
                image = Image.open('/Users/brandongillins/Python/Profile/Professional-Profile/Profile/assets/images/profile_pic.jpg')
                st.image(image, use_column_width=True, caption='')
            except:
                st.markdown("""
                    <div style="background-color: #2E2E2E; height: 300px; 
                    border-radius: 15px; display: flex; align-items: center; 
                    justify-content: center;">
                        <p style="color: #666;">Profile Photo</p>
                    </div>
                """, unsafe_allow_html=True)
            
            # Resume Download Button
            try:
                with open("/Users/brandongillins/Python/Profile/Professional-Profile/Profile/Resume.pdf", "rb") as file:
                    btn = st.download_button(
                        label="📄 Download Resume",
                        data=file,
                        file_name="Brandon_Gillins_Resume.pdf",
                        mime="application/pdf"
                    )
            except:
                st.button("📄 Download Resume", disabled=True)

        # Contact Information
        st.markdown("### Contact")
        st.markdown("""
        - 📧 [brandongillins@gmail.com](mailto:brandongillins@gmail.com)
        - 🔗 [LinkedIn Profile](https://www.linkedin.com/in/brandongillins)
        - 🌐 [Portfolio](https://bgillins.github.io/bg/)
        - 📍 Las Vegas, Nevada
        """)

        # Skills Section
        st.markdown("### Technical Skills")
        
        st.markdown("**Programming Languages & Tools**")
        st.markdown("""
        - Python (Pandas, NumPy, Scikit-learn)
        - SQL (Snowflake, PostgreSQL)
        - Databricks
        - Git/GitHub
        """)
        
        st.markdown("**Machine Learning & AI**")
        st.markdown("""
        - Natural Language Processing
        - Predictive Analytics
        - Large Language Models
        - Deep Learning
        """)
        
        st.markdown("**Data Visualization & BI**")
        st.markdown("""
        - Tableau
        - Power BI
        - Matplotlib
        - Seaborn
        """)

    with right_col:
        # Title Section
        st.markdown('<h1 class="big-title">BRANDON GILLINS</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">DATA SCIENTIST</p>', unsafe_allow_html=True)
        st.markdown('<p class="experience-header">3 YEARS DATA ANALYTICS EXPERIENCE</p>', unsafe_allow_html=True)

        # Summary Section
        st.markdown("### Professional Summary")
        st.markdown("""
            Results-driven Data Scientist with 3+ years of experience leveraging AI/ML to transform healthcare operations and customer experience. Demonstrated expertise in developing high-impact solutions that blend advanced analytics with practical business applications. Known for translating complex technical concepts into actionable insights for diverse stakeholders.

            **KEY ACHIEVEMENTS:**
            - Engineered an NLP-based model achieving 91% accuracy in detecting digital service adoption patterns, utilizing advanced techniques including TD-IDF, cosine similarity, Bag of Words, and XGBoost
            - Spearheaded customer experience analytics initiative analyzing 700+ daily customer interactions, identifying systematic issues impacting 3M+ members (2024) and 1M+ members (2023)
            - Developed an AI-powered commitment tracking system using prompt engineering to identify and monitor customer service promises, improving accountability and follow-through
            - Created and implemented a clinic-level HEDIS dashboard, now a cornerstone tool for healthcare analytics for Southwest Medical of Nevada.

            **CORE COMPETENCIES:**
            
            - Machine Learning & AI: Advanced NLP, Predictive Modeling, Prompt Engineering
            - Data Engineering: Python, Cloud Services, Database Design
            - Analytics & Visualization: Tableau, Data Analysis, Pattern Recognition
            - Leadership: Technical Training, Cross-functional Collaboration, Project Management
            - Communication: Stakeholder Engagement, Technical Documentation, Public Speaking

            Combining a unique background in mathematics education with deep technical expertise to effectively bridge the gap between complex data science solutions and business stakeholders. Proven track record of delivering scalable solutions that drive measurable improvements in healthcare operations and customer experience.
        """)

        # Experience Section
        st.markdown("### Work Experience")
        st.markdown("""
        ###### **Data Analyst 2 - UnitedHealth Group** (November 2023 - Present)
        - Conduct 3-5 in-depth analyses weekly on key consumer experience issues using tools like Snowflake, Databricks, and NLP search, driving actionable insights to enhance service quality and efficiency.
        - Play a pivotal role in an ongoing initiative aimed at obviating over 3 million calls this year, through detailed forecasting and analysis of call transcripts, text transcripts, claim data, and website activity.
        - Contributed to increasing the net promoter score by 7.2 points from 2022 to 2023 by leveraging comprehensive data analysis to identify and address critical consumer experience drivers.
        - Developed a machine learning model utilizing advanced NLP methods to track member migration to digital platforms, providing valuable insights into consumer behavior and digital adoption rates.
        - Creating innovative models incorporating Large Language Models (LLMs) to provide real-time information to advocates, aimed at reducing average handle time by 25%, enhancing operational efficiency and customer satisfaction.
                
        ###### **Data Analyst - Optum** (September 2022 - November 2023)
        - Accomplished a comprehensive analysis of Triple Weighted HEDIS Measures for 70,000+ patients in a quarterly reporting cycle, enabling Quality nurses to complete 13,000 chart reviews and close over 4,000 care gaps within 2 months.
        - Automated the creation of weekly reports for 100+ provider groups, reducing the report generation time from 12 hours to 2 hours and streamlining downstream distribution by pre-splitting lists based on providers, thereby boosting overall operational efficiency by 65% through the use of Python libraries (pandas, openpyxl, numpy).
        - Delivered 3 presentations to a guild of over 1,000 members at Optum Data Science, contributing to discussions on LangChain integration, AI prompt engineering, and JSON parsing, thereby fostering cross-functional expertise.
        - Developed extensive reporting tools that quantified the impact of the Pre-Visit team, resulting in a measurable increase in chart chase efficiency for the quality nursing team and favorable impacts on both current and YTD goals.
        - Conducted 3-8 ad-hoc SQL data pulls weekly on various HEDIS measures, enabling internal outreach teams to update their strategies on a daily to weekly basis, thereby reducing patient abrasion.
        
        ###### **Data Analyst - Swickard Auto Group** (January 2022 - September 2022)
        - Automated real-time ledger analytics within 45 days, integrating comprehensive metrics (product, sales, salary, bonus, vendor costs) into Power BI dashboards, contributing to cost-saving initiatives that resulted in $280K in savings by facilitating vendor switching.
        - Optimized data-driven vehicle pricing strategies by integrating weekly API data from vendors like Podium and Car Gurus, impacting 2,000+ vehicle listings and leading to a strategic realignment of marketing contracts.
        - Transformed daily employee sales tracking by executing hourly SQL data pulls, a leap from previous weekly retrievals, and implementing row-level security in Power BI. This led to a 15% reduction in reporting errors. Facilitated open daily communication between sales and data teams, fine-tuning the payout model, thereby becoming the validation source for future payroll structures.
        
        ###### **High School Mathematics Teacher** (July 2016 - December 2021)
        - Redesigned the math curriculum over a 2-year period, resulting in a 4-point ACT score increase for an average of 300 students annually.
        - Maintained high student engagement levels in 5 classes per semester, utilizing storytelling techniques based on real-world applications of mathematics.
        """)

        # Education Section
        st.markdown("### Education")
        
        # Master's Degree section with tabs for different course categories
        st.markdown("#### Master of Science - Data Analytics (Western Governors University, April 2024)")
        
        # Create tabs for different course categories
        core_tab, advanced_tab, capstone_tab = st.tabs(["Core Courses", "Advanced Analytics", "Capstone"])
        
        with core_tab:
            st.markdown("##### Core Data Analytics Track")
            
            with st.expander("D204 - The Data Analytics Journey"):
                st.markdown("""
                Built foundational understanding of the analytics lifecycle, from problem definition to solution deployment. 
                Created comprehensive project plans using Python to address real business metrics and KPIs.
                
                **Tasks:**
                - [Task 1 - Analytics Framework](https://d204-task1-link)
                """)
            
            with st.expander("D205 - Data Acquisition"):
                st.markdown("""
                Mastered SQL fundamentals for database manipulation and data extraction. 
                
                **Tasks:**
                - [Task 1 - Data Collection Framework](https://d205-task1-link)
                """)
            
            with st.expander("D206 - Data Cleaning"):
                st.markdown("""
                Implemented advanced data preprocessing techniques using Python.
                
                **Tasks:**
                - [Task 1 - Data Quality Assessment](https://d206-task1-link)
                - [Task 2 - Data Cleaning Implementation](https://d206-task2-link)
                """)
            
            with st.expander("D207 - Exploratory Data Analysis"):
                st.markdown("""
                Applied statistical methods using Python to uncover patterns in data.
                
                **Tasks:**
                - [Task 1 - Statistical Analysis](https://d207-task1-link)
                - [Task 2 - Pattern Recognition](https://d207-task2-link)
                """)

        with advanced_tab:
            st.markdown("##### Advanced Analytics")
            
            with st.expander("D208 - Predictive Modeling"):
                st.markdown("""
                Developed regression models using scikit-learn.
                
                **Tasks:**
                - [Task 1 - Model Development](https://d208-task1-link)
                - [Task 2 - Model Evaluation](https://d208-task2-link)
                """)
            
            with st.expander("D209 - Data Mining I"):
                st.markdown("""
                Implemented supervised learning models for classification and prediction tasks.
                
                **Tasks:**
                - [Task 1 - Feature Engineering](https://d209-task1-link)
                - [Task 2 - Feature Selection](https://d209-task2-link)
                """)
            
            with st.expander("D210 - Representation and Reporting"):
                st.markdown("""
                Created interactive dashboards using Tableau for executive decision support. Developed data storytelling skills to effectively communicate insights to diverse stakeholders.
                
                **Tasks:**
                - [Task 1 - Data Visualization Design](https://d210-task1-link)
                - [Task 2 - Executive Dashboard Creation](https://d210-task2-link)
                - [Task 3 - Storytelling with Data](https://d210-task3-link)
                """)

            with st.expander("D211 - Advanced Data Acquisition"):
                st.markdown("""
                Built complex SQL queries and ETL processes for large-scale data integration. Implemented data quality checks and automated data pipeline monitoring systems.
                
                **Tasks:**
                - [Task 1 - Advanced SQL Implementation](https://d211-task1-link)
                - [Task 2 - ETL Pipeline Development](https://d211-task2-link)
                - [Task 3 - Data Quality Framework](https://d211-task3-link)
                """)

            with st.expander("D212 - Data Mining II"):
                st.markdown("""
                Applied unsupervised learning techniques including clustering and dimensionality reduction. Developed association rule mining systems for pattern discovery in large datasets.
                
                **Tasks:**
                - [Task 1 - Clustering Analysis](https://d212-task1-link)
                - [Task 2 - Dimension Reduction](https://bgd212task2.streamlit.appp)
                - [Task 3 - Association Rules](https://professional-profile-d212.streamlit.app)
                """)

            with st.expander("D213 - Advanced Data Analytics"):
                st.markdown("""
                Implemented neural networks and time series models using TensorFlow/Keras.
                
                **Tasks:**
                - [Task 1 - Neural Network Implementation](https://d213-task1-link)
                - [Task 2 - Time Series Analysis](https://d213-task2-link)
                """)

        with capstone_tab:
            st.markdown("##### Capstone Project")
            
            with st.expander("D214 - Data Analytics Graduate Capstone"):
                st.markdown("""
                Completed an end-to-end analytics project combining multiple techniques.
                
                **Project:**
                - [Capstone Project Repository](https://capstone-link)
                - [Final Presentation](https://capstone-presentation-link)
                """)

        st.markdown("#### Bachelor of Arts, Mathematics (Western Governors University, 2014-2016)")

        # Projects Section
        st.markdown("### Notable Projects")
        st.markdown("""
        **Clinic-Level HEDIS Dashboard**
        - Created a dashboard widely used for tracking clinic goals and identifying gaps
        - Became an essential tool for healthcare analytics at Optum
        """)

if __name__ == "__main__":
    main()