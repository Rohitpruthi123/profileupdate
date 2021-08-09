#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


st.title("Rohit Pruthi")
st.header(":email: rohitpruthi[at]gmail.com")

st.sidebar.image('pic.jpg', width = 150)

section = st.sidebar.radio("Please select a section",('Education', 'Experience', 'Achievements', 'Opinions'))


##########################################################################################################
if section == 'Education':
    st.header('Education :books:')
    
    st.markdown(
            """### [Indian Institue of Technology Roorkee](https://me.iitr.ac.in/)
Bachelors in Technology | Mechanical Engineering | 2003-2007 \n
GPA 8.15/10.00 | Summer Undergraduate Research Awardee""")

    st.header('Continuing Education :pencil2:')
    
    st.markdown(
"""
- Certified Scrum Product Owner | Scrum Foundation | June 2021 | [Credential](https://bcert.me/squbgmcqq)\n
- Azure Fundamentals | Microsoft | Jan 2020 | [Credential](https://www.credly.com/badges/2505be32-09b9-4217-9cc1-b12f98b6ddf7/linked_in_profile)\n
- Network Analysis | Data camp | Jun 2020 | [Credential] (https://www.datacamp.com/statement-of-accomplishment/course/60c300bc6b4ad01d0976a20925a6403766a0ca68)\n
- Learning from Data | Caltech | Dec 2016 | [Credential](https://courses.edx.org/certificates/e3eae4d1b172451aacbbca70f100f0a9)\n

- Edison Engineering Development Program | General Electric | 2008-2010 | [link](https://www.ge.com/research/careers/Edison-engineering-development)

""" 
    )
    
    st.header('LinkedIn Courses :open_file_folder:')

    st.markdown(
"""
- Becoming an AI first leader \n
- Product management tips \n
- Mistakes to avoid in machine learning \n
"""
        )
    
##########################################################################################################

elif section == 'Experience':
    st.header('Rolls Royce India :airplane:')
    
    st.markdown(
            """### [R2 Data Labs](https://www.rolls-royce.com/products-and-services/r2datalabs.aspx)
**Data Science Chapter Lead** | 2020- \n

- **Chapter lead** for 8 member data science team.
- Editor and curator of the monthly news letter and special interest external connect. 
- Responsible for **technical mentoring** and career development of team.

**Digital Solutions Lead** | 2019- \n

- Delivered **20 Mn GBP** value leading a 10 member team working on **Marketing Intelligence** program
- Proposed and developed innovation  projects  related  to  **intelligent  annotation**  and  **sparse  image  analysis**,  delivered minimum viable product, realizing **>1 Mn GBP** value in-year.
- Conceptualized and deployed **regression model development framework** for key factor analysis of **blade vibration test**. Reusable framework used for performance test rationalization as well leading to **1.7 Mn GBP** value delivery. 
- Formulated **mLogic -Machine Log interpreter console** to understand machine language for Rotatives (IIoT 4.0) - deployment not deemed feasible. 

**Decision Scientist** | 2018-2020 \n

- **Sulphidation and deterioration monitoring** machine learning framework and models for two civil aviation engine lines (Trent 700 and Trent 1000). 
- Involved in **data driven Root Cause Analysis**, nested model development for remaining useful life assessment of liner loss issues on a business aviation application.
- Led Proof Of Concept studies in text data assessment for customer and employee feedback (Gallup Surveys) using **Natural Language Processing** methods. 

""")

    st.header('General Electric :office:')
    
    st.markdown(
"""
### [Advanced Technology Operations, GE Power](https://www.ge.com/in/power)

- Involved in thermal system design and data driven decision making using simulations as well as test data for Gas Turbine systems. Key positions of responsibility listed below. 

**Technical Leader, Aero Thermal Design** | 2015-2018 \n

**Lead Engineer, Aero Thermal Design** | 2010-2015 \n

**Edison Engineering Development Program Graduate** | 2008-2010 \n


""" 
    )
    
elif section == 'Achievements':
    st.header('Awards & Recognitions :trophy:')
    
    st.markdown(
            """
- 2021 : *RR APAC Silver award* recognition for value delivery 
- 2018 : *Be This* award for a role model mentor 
- 2015 : *GE Young Achiever* award at the Engineering Recognition Day
- 2013 : *Innovation silver medal* for filing 10 patents

""")

    st.header('Notable Patents :rocket:')
    
    st.markdown(
            """
- 2020 : Apparatus and method for sealing turbine assembly (USPTO 10704405)
- 2016 : Inner turbine shell axial movement(USPTO 9488062), Seal end attachment (9353635)
- 2014 : Turbomachine seal assembly (8888445), Dual-flow steam turbine with steam cooling (8888437)
- 2013 : Adverse pressure gradient seal mechanism(8561997), Exhaust plenum flow splitter(8418717)

Check [here](https://patents.justia.com/inventor/rohit-pruthi) for details

""")
    
    st.header('Conferences and presentation :bar_chart:')
    
    st.markdown(
            """
- 2021 : Presented R2DL perspetive on application of ML/AI in aviation. [Link](https://youtu.be/o3b7dgq2q1k?t=5040)
- 2021 : Annotation frameworks with intelligence, AIML systems
- 2020 : Represented R2DL in sustainability and net zero discussions in various internal forums. 
- Prior : Represented team in Gas Turbine conferences in multiple forums


""")

elif section == 'Opinions':
    
    st.header('Marks, Mystery & Multicollinearity :information_source:')
    
    st.markdown(
            """
- Abstract : This was part of a lecture delivered at an Engineering college to students interested to learn machine learning and data science. [Read further here](https://github.com/aigym/ppscore/blob/main/MarksMysteryMulticollinearity.ipynb
)

""")
    st.header('The anti resume :information_source:')
    
    st.markdown(
            """
- In the competitive world of today, we are hardwired to impress. It is difficult to put down your failures to paper, but crucial to do so. Not only would it keep one grounded, it also shows that the path to eventual success, or a modicum of perception of personal achievement, is fraught with failure. [Read further here](https://www.linkedin.com/pulse/anti-resume-rohit-pruthi/)

""")

    st.header('Lessons Half Learnt :information_source:')
    
    st.markdown(
            """
- I remain a work in progress. Phew! That was relief writing down on paper (or a screen). Time to take stock. [Read further here](https://www.linkedin.com/pulse/lessons-half-learnt-rohit-pruthi/)

""")

    st.header('Book Review Factfullness :information_source:')
    
    st.markdown(
            """
- If you read Hans Rosling talk about the progress we have made as mankind, you will be inclined to rescind your words, bow down to the future and look at the glass half-ful, maybe even take a sip! I wish to be a possibilist like him some day. [Read further here](https://unsoporific.wordpress.com/2019/01/11/book-review-factfulness/)

""")
    
    
    st.header('Audio analysis lessons :information_source:')
    
    st.markdown(
            """
- We started working on a kaggle competition which deals with audio data. This notebook provides the learnings from audio analytics field. [Read further here](https://r2dldocs.z6.web.core.windows.net/doc-repo/blog/rfcx-approach-eda-feature-extraction-v1/)

""")
    

    
    