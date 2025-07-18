# pages/history.py
# This file contains the content for the "History of Algebra" tab.
# Like the chapter files, it has a single `render()` function.

import streamlit as st

def render():
    """Renders the History of Algebra page."""
    st.header("A Brief History of Algebra 📜")
    st.markdown("""
    Algebra, the bedrock of so many mathematical and scientific fields, has a rich and fascinating history that spans continents and millennia. It didn't emerge fully formed but evolved through the contributions of numerous civilizations.
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Page_from_al-Khwarizmi%27s_al-Jabr.jpg/800px-Page_from_al-Khwarizmi%27s_al-Jabr.jpg",
             caption="A page from 'The Compendious Book on Calculation by Completion and Balancing' by Muhammad ibn Musa al-Khwarizmi.")

    st.subheader("Ancient Origins: Babylon and Egypt")
    st.markdown("""
    The earliest roots of algebra can be traced back to the ancient Babylonians, who developed an advanced arithmetical system. They were able to solve linear and quadratic equations using algorithmic procedures. Clay tablets dating from around 1800 BC show problems involving finding unknown numbers, which is the essence of algebra.
    
    Similarly, the Egyptians, as seen in the Rhind Mathematical Papyrus, also solved equations, though their methods were often more rhetorical (described in words) than symbolic.
    """)

    st.subheader("The Father of Algebra: Al-Khwarizmi")
    st.markdown("""
    The word "algebra" itself comes from the Arabic word **"al-jabr"**, which was part of the title of a landmark book written around 820 AD by the Persian mathematician **Muhammad ibn Musa al-Khwarizmi**. His book, *Al-kitāb al-mukhtaṣar fī ḥisāb al-jabr wa-l-muqābala* ("The Compendious Book on Calculation by Completion and Balancing"), was revolutionary.

    - **Al-Jabr**: This refers to "completion" or "restoring"—the process of moving a negative term from one side of an equation to the other to make it positive.
    - **Al-Muqābala**: This means "balancing"—the process of subtracting the same quantity from both sides of an equation.
    
    Al-Khwarizmi's work was the first to treat algebra as an independent discipline and introduced systematic and logical methods for solving equations.
    """)

    st.subheader("The Leap to Abstraction: From Diophantus to Modernity")
    st.markdown("""
    While al-Khwarizmi provided the methods, the Greek mathematician **Diophantus of Alexandria** (c. 250 AD) had earlier introduced symbolism into algebra, using symbols for unknown numbers and powers. This is known as "syncopated algebra."
    
    The true leap to modern, symbolic algebra occurred in Europe during the Renaissance and beyond. **François Viète** in the 16th century introduced the use of letters to represent both parameters and unknowns, allowing for the study of general formulas rather than just specific problems. **René Descartes**, in the 17th century, bridged the gap between algebra and geometry with his invention of Cartesian coordinates, giving birth to analytic geometry—the very foundation of the visualizations in this app!
    
    From there, the field blossomed into abstract algebra, which studies algebraic structures like groups, rings, and fields, forming the language of modern mathematics and physics.
    """)