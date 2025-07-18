# app.py

import streamlit as st
import urllib.parse

# --- Import Chapter Modules ---
# Import existing Eigen-Verse chapters
from chapters import chapter_1, chapter_2, chapter_3, chapter_4, chapter_5, chapter_6

# Import the new Streamlit Saga chapters
from streamlit_chapters import chapter_1 as streamlit_chapter_1
from streamlit_chapters import chapter_2 as streamlit_chapter_2
from streamlit_chapters import chapter_3 as streamlit_chapter_3
from streamlit_chapters import chapter_4 as streamlit_chapter_4
from streamlit_chapters import chapter_5 as streamlit_chapter_5
from streamlit_chapters import introduction as streamlit_intro

from dharma_sindhu_saga import chapter_0_syllabus as dharma_syllabus
from dharma_sindhu_saga import chapter_1 as dharma_chapter_1
from dharma_sindhu_saga import chapter_2 as dharma_chapter_2


# --- MANDATORY HELPER FUNCTION (from LESSON_DESIGN_GUIDE.md) ---
# This should ideally be in a utils/plotting.py file, but is included here for simplicity.
def image_search_button(label, search_term):
    """Creates a Streamlit link button that searches Google Images in a new tab."""
    encoded_term = urllib.parse.quote_plus(search_term)
    url = f"https://www.google.com/search?q={encoded_term}&tbm=isch"
    st.link_button(f"🖼️ See images of: {label}", url, use_container_width=True)

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="The Grand Library",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- SIDEBAR - TOP LEVEL NAVIGATION ---
st.sidebar.title("🌌 The Grand Library")
st.sidebar.markdown("Select your learning saga below.")

# Top-level navigation to choose the learning path (Saga)
learning_path = st.sidebar.radio(
    "Choose your Saga:",
    ("Eigen-Verse Explorer", "The Streamlit Saga", "The Dharma-Kshetra Saga")
)

st.sidebar.markdown("---")


# --- MAIN APP LOGIC ---

# === PATH 1: EIGEN-VERSE EXPLORER ===
if learning_path == "Eigen-Verse Explorer":
    st.sidebar.header("Eigen-Verse Explorer")
    st.sidebar.markdown("A game to build your intuition for Linear Algebra.")

    # Dictionary mapping chapter names to their render functions
    chapters = {
        "Introduction": None,
        "Chapter 1: Vectors": chapter_1.render,
        "Chapter 2: Transformations": chapter_2.render,
        "Chapter 3: Determinant": chapter_3.render,
        "Chapter 4: Eigenvectors & Eigenvalues": chapter_4.render,
        "Chapter 5: Application": chapter_5.render,
        "Chapter 6: Inverse of a Matrix": chapter_6.render
    }

    selected_chapter_name = st.sidebar.radio(
        "Select a Chapter:",
        chapters.keys(),
        key="eigen_verse_chapters" # Unique key for this radio widget
    )

    # Render the selected chapter or the introduction
    if selected_chapter_name == "Introduction":
        st.title("Welcome to the Eigen-Verse Explorer! 🚀")
        
        # Using the mandatory image_search_button instead of st.image with a URL
        image_search_button("Abstract Space", "abstract space art")
        
        st.markdown("""
        This is not your typical math class. This is an interactive journey to **see** and **feel** the core concepts of Linear Algebra.
        
        **Use the sidebar on the left to navigate between the chapters of your explorer's log.**
        
        Ready to begin? Select **Chapter 1** from the sidebar.
        """)
    else:
        render_function = chapters[selected_chapter_name]
        render_function()

# === PATH 2: THE STREAMLIT SAGA ===
elif learning_path == "The Streamlit Saga":
    st.sidebar.header("The Streamlit Saga")
    st.sidebar.markdown("A journey from scratch to advanced Streamlit skills.")

    # Dictionary for the Streamlit Saga chapters
    streamlit_chapters = {
        "Introduction - Syllabus": streamlit_intro.render,
        "Chapter 1: Your First Web App - The Digital Thali": streamlit_chapter_1.render,
        "Chapter 2: The Art of Display - Text & Data": streamlit_chapter_2.render,
        "Chapter 3: Making it Talk - Interactive Widgets": streamlit_chapter_3.render,
        "Chapter 4: Structuring Your App - Layouts & Containers": streamlit_chapter_4.render,
        "Chapter 5: The App's Memory - Understanding Session State": streamlit_chapter_5.render,
        # Future Streamlit chapters will be added here
    }

    selected_chapter_name = st.sidebar.radio(
        "Select a Chapter:",
        streamlit_chapters.keys(),
        key="streamlit_saga_chapters" # Unique key for this radio widget
    )
    
    # Render the selected Streamlit chapter
    render_function = streamlit_chapters[selected_chapter_name]
    render_function()

# === PATH 3: THE DHARMA-KSHETRA SAGA ===
elif learning_path == "The Dharma-Kshetra Saga":
    st.sidebar.header("📜 The Dharma-Kshetra Saga")
    st.sidebar.markdown("Explore the history of Haryana through the lens of Dharma.")

    # Dictionary mapping chapter names to their render functions
    dharma_chapters = {
        "Syllabus: The Full Journey": dharma_syllabus.render,
        # When you create Chapter 1, you will add it here
        "Chapter 1: The Seed of Dharma": dharma_chapter_1.render,
        "Chapter 2: Echoes of the Mahabharata": dharma_chapter_2.render,
        #"Chapter 3: The Field of Righteousness": dharma_chapter_3.render,
        #"Chapter 4: The Land of Beginnings": dharma_chapter_4.render,
        #"Chapter 5: The Land of Endings": dharma_chapter_5.render,
        #"Chapter 6: The Land of Destiny": dharma_chapter_6.render
    }

    selected_chapter_name = st.sidebar.radio(
        "Select a Chapter:",
        dharma_chapters.keys(),
        key="dharma_saga_chapters"  # A unique key is essential!
    )

    # Execute the render function for the selected chapter
    render_function = dharma_chapters[selected_chapter_name]
    render_function()


# --- COMMON SIDEBAR FOOTER ---
st.sidebar.markdown("---")
st.sidebar.info("Created by an AI with a passion for visual learning.")