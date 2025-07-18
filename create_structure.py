import os
from pathlib import Path

# --- Configuration ---
# Define the directories and files to be created.
# This makes it easy to add more later.
DIRECTORIES = ["chapters", "pages", "utils"]

# A dictionary where keys are filenames and values are the initial content.
# This helps pre-populate files with useful boilerplate code.
FILES_TO_CREATE = {
    "app.py": """\
# Main entry point for the Streamlit app.
import streamlit as st

# Import the render functions from your chapter files
# TODO: Uncomment these as you create the chapter files.
# from chapters import chapter_1, chapter_2, chapter_3, chapter_4, chapter_5

# Import the render function from your pages
from pages import history

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="The Eigen-Verse Explorer",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- 2. DEFINE TABS ---
st.title("The Eigen-Verse Explorer")
tab_explorer, tab_history = st.tabs(["The Eigen-Verse Explorer 🚀", "History of Algebra 📜"])

# --- 3. "EIGEN-VERSE EXPLORER" TAB CONTENT ---
with tab_explorer:
    st.sidebar.title("Navigation")
    st.sidebar.markdown("Select a chapter to begin your journey.")

    # A dictionary that maps chapter names to their respective render functions.
    # TODO: Fill this dictionary as you complete each chapter's .py file.
    chapters = {
        "Introduction": None,  # Special case for the intro page
        # "Chapter 1: Vectors": chapter_1.render,
        # "Chapter 2: Transformations": chapter_2.render,
        # "Chapter 3: Determinant": chapter_3.render,
        # "Chapter 4: Eigenvectors & Eigenvalues": chapter_4.render,
        # "Chapter 5: Application": chapter_5.render
    }

    selected_chapter_name = st.sidebar.radio(
        "Select a Chapter:",
        chapters.keys()
    )

    # --- Display the selected chapter ---
    if selected_chapter_name == "Introduction":
        st.header("Welcome to the Eigen-Verse Explorer!")
        st.image("https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTYyNjQ0NzYxOA&ixlib=rb-1.2.1&q=80&w=1080", caption="A visual representation of abstract space.")
        st.markdown('''
        This is an interactive journey to **see** and **feel** the core concepts of Linear Algebra.
        
        **Use the sidebar on the left to navigate between the chapters.**
        
        Ready to begin? Select **Chapter 1** from the sidebar.
        ''')
    else:
        # Look up the render function from the dictionary and call it.
        render_function = chapters[selected_chapter_name]
        if render_function:
            render_function()
        else:
            st.warning("This chapter has not been implemented yet.")

    st.sidebar.markdown("---")
    st.sidebar.info("Created with a passion for visual learning.")

# --- 4. "HISTORY OF ALGEBRA" TAB CONTENT ---
with tab_history:
    # Call the render function from the history.py file.
    history.render()
""",

    "chapters/__init__.py": "# This file makes 'chapters' a Python package.",
    "pages/__init__.py": "# This file makes 'pages' a Python package.",
    "utils/__init__.py": "# This file makes 'utils' a Python package.",

    "utils/plotting.py": """\
# utils/plotting.py
# This file contains helper functions used across multiple chapters for plotting.
# Keeping them here avoids code duplication and keeps chapter files cleaner.

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# TODO: Add your plot_vectors and setup_plot functions here.

def plot_vectors(vectors, colors, ax, labels=None):
    \"\"\"Plots a list of vectors on a given Matplotlib Axes object.\"\"\"
    st.info("Plotting function is ready to be filled in!")
    pass # Replace with your function code

def setup_plot(ax, title, xlim=(-5, 5), ylim=(-5, 5)):
    \"\"\"Sets up a standard 2D plot for our visualizations.\"\"\"
    st.info("Setup plot function is ready to be filled in!")
    pass # Replace with your function code
""",

    "pages/history.py": """\
# pages/history.py
# This file contains the content for the "History of Algebra" tab.
import streamlit as st

def render():
    \"\"\"Renders the History of Algebra page.\"\"\"
    st.header("A Brief History of Algebra 📜")
    st.markdown('''
    **This page is ready for your content!**
    
    Start by writing about the origins of algebra in ancient civilizations,
    the contributions of Al-Khwarizmi, and the evolution towards modern
    abstract algebra.
    
    You can use `st.subheader()`, `st.markdown()`, and `st.image()` to structure your content.
    ''')
"""
}

# Add chapter files programmatically
for i in range(1, 6):
    chapter_filename = f"chapters/chapter_{i}.py"
    FILES_TO_CREATE[chapter_filename] = f"""\
# chapters/chapter_{i}.py
# This file will contain the code for Chapter {i}.
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# You will likely need to import your plotting functions from the utils directory
# from utils.plotting import plot_vectors, setup_plot

def render():
    \"\"\"Renders Chapter {i} of the Eigen-Verse Explorer.\"\"\"
    st.header("Chapter {i}: [Your Title Here]")
    st.markdown('''
    This is the content area for Chapter {i}.
    
    Start building your interactive lesson here using `st.slider`, `st.button`,
    and plotting with Matplotlib.
    ''')
    
    st.warning("This chapter is under construction.")
"""

# --- Main Script Logic ---
def create_project_structure():
    """
    Creates the directories and files for the Streamlit project.
    """
    print("🚀 Starting to build the Streamlit project structure...")
    
    # Get the directory where the script is running
    root = Path(".")

    # 1. Create Directories
    for directory in DIRECTORIES:
        path = root / directory
        path.mkdir(exist_ok=True)
        print(f"✅ Created/Ensured directory: {path}/")

    # 2. Create Files with boilerplate content
    for filepath, content in FILES_TO_CREATE.items():
        path = root / filepath
        # Ensure the parent directory exists before writing the file
        path.parent.mkdir(exist_ok=True) 
        path.write_text(content, encoding="utf-8")
        print(f"✅ Created file: {path}")

    print("\n🎉 Project structure created successfully!")
    print("\nWhat to do next:")
    print("1. Fill in the `TODO` sections in the generated Python files with your code.")
    print("2. Once you've added your content, run the app from your terminal with:")
    print("\n   streamlit run app.py\n")


if __name__ == "__main__":
    create_project_structure()