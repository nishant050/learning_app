import streamlit as st
from utils.plotting import image_search_button # Assuming this utility is available

def render():
    """
    Renders the syllabus and introduction page for The Streamlit Saga.
    """
    st.header("Syllabus: The Streamlit Saga")
    st.markdown("""
    Welcome, creator! This saga is your journey from a curious apprentice to a master builder of web applications. 
    You will learn not just the *how*, but the *why*, crafting everything from simple data displays to complex, interactive dashboards. 
    We begin with a single line of code and end with an app deployed to the world.
    """)
    
    st.subheader("Your 10-Chapter Journey")
    st.markdown("---")

    # Chapter 1
    st.markdown("### 📜 Chapter 1: Your First Web App - The Digital Thali")
    st.markdown("Just as a thali presents multiple dishes on one plate, you'll learn how Streamlit lets you serve text, data, and charts in one simple script. We'll start with `st.write` and build our very first, complete web application in under 10 minutes.")
    
    # Chapter 2
    st.markdown("### 📊 Chapter 2: The Art of Display - Text & Data")
    st.markdown("Go beyond basic text. Learn to master the display of information with `st.markdown`, `st.metric`, and the all-powerful `st.dataframe`. We'll cover how to make your data beautiful and readable, from financial reports to cricket scores.")

    # Chapter 3
    st.markdown("### 🎛️ Chapter 3: Making it Talk - Interactive Widgets")
    st.markdown("Transform your app from a static page into a dynamic conversation. This chapter introduces the core interactive elements: `st.button`, `st.slider`, `st.selectbox`, and `st.text_input`. Users will no longer just view your app; they will interact with it.")

    # Chapter 4
    st.markdown("### 🏛️ Chapter 4: Structuring Your App - Layouts & Containers")
    st.markdown("Learn the architectural principles of app design. We'll use `st.columns`, `st.tabs`, and `st.expander` to organize your content cleanly. This is how you build complex, professional-looking dashboards instead of simple, scrolling scripts.")

    # Chapter 5
    st.markdown("### 🧠 Chapter 5: The App's Memory - Understanding Session State")
    st.markdown("This is the breakthrough moment for any Streamlit developer. We'll demystify `st.session_state`, the mechanism that allows your app to remember information across interactions, enabling multi-step workflows, user personalization, and complex logic.")

    # Chapter 6
    st.markdown("### ⚡ Chapter 6: Need for Speed - Caching & Performance")
    st.markdown("Why do some apps feel instant while others lag? The secret is caching. Learn how to use `st.cache_data` and `st.cache_resource` to dramatically speed up your data loading and computations, ensuring a flawless user experience.")

    # Chapter 7
    st.markdown("### 📝 Chapter 7: The Organizer - Forms & Callbacks")
    st.markdown("Prevent your app from re-running on every widget interaction. Use `st.form` to batch user inputs together. We'll also dive into callback functions, providing a more intuitive and efficient way to trigger your app's logic.")

    # Chapter 8
    st.markdown("### 📚 Chapter 8: The Grand Library - Building Multi-Page Apps")
    st.markdown("Break free from a single page. This chapter covers Streamlit's native, file-based method for creating robust multi-page applications, just like the 'Grand Library' project itself. You'll learn how to structure your project for true scalability.")

    # Chapter 9
    st.markdown("### 🔗 Chapter 9: Beyond the App - Connecting to APIs & Databases")
    st.markdown("An app is only as powerful as its data. Learn the techniques to fetch live data from external APIs (like weather or stock prices) and connect securely to databases, turning your application into a real-time data powerhouse.")

    # Chapter 10
    st.markdown("### 🚀 Chapter 10: To the Cloud! - Deploying and Sharing Your App")
    st.markdown("An app isn't complete until it's shared. This final chapter provides a step-by-step guide to deploying your application to Streamlit Community Cloud for free. We'll cover environment management (`requirements.txt`) and best practices for a successful launch.")