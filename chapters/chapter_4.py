# chapters/chapter_4.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import urllib.parse
from scipy.linalg import schur

# --- Mandatory Helper Function (as per guide) ---
# This would typically be in utils/plotting.py but is included here for completeness.
def image_search_button(label, search_term):
    """Creates a Streamlit link button that searches Google Images in a new tab."""
    encoded_term = urllib.parse.quote_plus(search_term)
    url = f"https://www.google.com/search?q={encoded_term}&tbm=isch"
    st.link_button(f"🖼️ See images of: {label}", url, use_container_width=True)

# --- Chapter Rendering Function ---
def render():
    """
    Renders Chapter 4: Eigenvectors & Eigenvalues, following the Version 3.1 blueprint.
    """
    st.title("Chapter 4: The Unchanging Path — Eigenvectors & Eigenvalues")

    # --- Part 1: The Core Idea (The Analogy) ---
    st.header("Part 1: The Core Idea — The Path of Dharma", divider="rainbow")
    st.markdown("""
    Imagine a great warrior-prince in the midst of the epic Kurukshetra war. The world around him is a storm of chaos—a swirling, twisting battlefield. Chariots clash, arrows fly, and the very ground seems to warp and shift with the strategies of the opposing army. This battlefield is our **linear transformation**—a force that changes the position of every warrior, every rock, and every grain of dust.

    The prince, however, is bound by his **Dharma**. His Dharma is not a physical location, but a sacred duty, an intrinsic path or principle that he must follow. No matter how the battlefield shifts, his core purpose remains steadfast.

    - If the army charges east (a 'shear' transformation), knocking everyone sideways, the prince, following his Dharma, might move forward along his designated path, but he does so without deviating from his core direction.
    - If the enemy lines expand (a 'scale' transformation), pushing everything outwards, his path remains true, though he may find himself covering more ground, his influence magnified.

    In this storm of transformation, most vectors (representing the paths of ordinary soldiers) are knocked off their original course. They point in new, unexpected directions after the transformation is applied. But there exists a special, almost magical direction—the prince's path of Dharma.

    This path is the **Eigenvector**.
    
    When the transformation of the battlefield acts on the prince who is on this path, his direction does not change. He stays true to his line. He might be pushed further down that path (stretched) or find his advance shortened (shrunk), but his direction is unaltered. The amount by which he is stretched or shrunk is his **Eigenvalue**. It is the measure of the transformation's impact *along* his sacred path.

    So, an Eigenvector is a special direction in space that is left unchanged by a transformation. An Eigenvalue is the scalar factor by which that vector is stretched or shrunk. Our mission in this chapter is not merely to find a mathematical curiosity, but to find the very soul of a transformation—its inherent, unchanging paths of Dharma.
    """)
    image_search_button("Kurukshetra Battlefield", "Kurukshetra war painting")
    image_search_button("Arjuna's Path of Dharma", "Arjuna chariot Krishna Mahabharata")

    # --- Part 2: The Mechanism (Interactive Discovery) ---
    st.header("Part 2: The Mechanism — Finding the Path of Dharma", divider="rainbow")
    st.markdown("""
    Let's step onto the battlefield ourselves. Below is an interactive simulation. We have a transformation matrix `T`, which represents the 'rules of the battlefield'. We also have a blue vector `v`, which you control. When we apply the transformation, we get the red vector, `T*v`.

    Your quest is to rotate the blue vector `v` and find the precise angle where it lines up perfectly with the red transformed vector `T*v`. When they are aligned, you have found an Eigenvector—a path of Dharma. The grid itself is also transformed to show you how the entire 'space' of the battlefield is being warped.
    """)

    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("The Battlefield's Law (T)")
        T = np.array([[3, 1], [0, 2]])
        st.latex(f"T = \\begin{{bmatrix}} 3 & 1 \\\\ 0 & 2 \\end{{bmatrix}}")
        
        st.subheader("Your Search Controls")
        angle_deg = st.slider("Rotate Input Vector (Angle in degrees)", 0, 360, 45, 1, key="c4_angle")
        angle_rad = np.deg2rad(angle_deg)
        
        v = np.array([np.cos(angle_rad), np.sin(angle_rad)])
        Tv = T @ v

        eigenvalues, eigenvectors = np.linalg.eig(T)
        
        is_eigenvector = False
        for i, eig_vec in enumerate(eigenvectors.T):
            # Normalize vectors for accurate dot product comparison
            dot_product = np.dot(v, eig_vec) / (np.linalg.norm(v) * np.linalg.norm(eig_vec))
            if np.abs(np.abs(dot_product) - 1.0) < 0.001:
                is_eigenvector = True
                found_eigenvalue = eigenvalues[i]
                break
    
    with col2:
        fig, ax = plt.subplots(figsize=(8, 8))
        
        # Plot transformed grid
        x = np.linspace(-6, 6, 20)
        y = np.linspace(-6, 6, 20)
        for i in x:
            ax.plot(T[0,0]*i + T[0,1]*y, T[1,0]*i + T[1,1]*y, color='lightgray', linestyle='-')
            ax.plot(T[0,0]*x + T[0,1]*i, T[1,0]*x + T[1,1]*i, color='lightgray', linestyle='-')
        
        # Plot original and transformed vectors
        ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Input Vector (v)')
        ax.quiver(0, 0, Tv[0], Tv[1], angles='xy', scale_units='xy', scale=1, color='red', label='Transformed Vector (T*v)')
        
        # Unit circle for reference
        circle = plt.Circle((0,0), 1, color='blue', fill=False, linestyle='--')
        ax.add_artist(circle)
        
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        ax.set_aspect('equal', adjustable='box')
        ax.grid(True)
        ax.set_title("Searching for Eigenvectors")
        ax.legend()
        st.pyplot(fig)

    if is_eigenvector:
        st.balloons()
        st.success(f"**DHARMA FOUND! You've discovered an Eigenvector!**")
        st.write(f"Notice how the blue and red vectors are perfectly aligned. The **Eigenvalue (λ)**, or the measure of impact along this path, is approximately **{found_eigenvalue:.2f}**. This is the factor by which your vector was stretched.")
    else:
        st.info("Keep searching! The red and blue arrows are not yet aligned. The path of Dharma awaits.")

    # --- Part 3: The Gallery (Showcasing Variety) ---
    st.header("Part 3: The Gallery of Transformations", divider="rainbow")
    st.markdown("Not all transformations are the same. Each has its own unique 'unchanging paths'. Let's explore a gallery of different transformations and their corresponding Eigenvectors.")
    
    tabs = st.tabs(["Stretching (Scaling)", "Slanting (Shear)", "Flipping (Reflection)", "Crushing (Projection)"])
    
    with tabs[0]:
        st.subheader("The Merchant's Fortune (Scaling)")
        st.markdown("Imagine a merchant whose wealth is described by two numbers: gold and silver. A good trading season (our transformation) doubles his gold and triples his silver.")
        st.latex("T_{scale} = \\begin{bmatrix} 2 & 0 \\\\ 0 & 3 \\end{bmatrix}")
        st.markdown("What are the 'dharmic paths' here? If he only has gold, a good season just gives him more gold. If he only has silver, he just gets more silver. These two directions—the axes themselves—are the Eigenvectors.")
        image_search_button("Ancient Indian Merchant", "ancient indian market scene")
    
    with tabs[1]:
        st.subheader("The River's Flow (Shear)")
        st.markdown("Consider the flow of the Ganga. The water in the middle moves faster than the water at the banks. This is a shear. A stick floating vertically will be tilted by the flow.")
        st.latex("T_{shear} = \\begin{bmatrix} 1 & 1 \\\\ 0 & 1 \\end{bmatrix}")
        st.markdown("But what if a stick is already pointing horizontally, along the direction of the flow? Its direction won't change; it will just be pushed along. This horizontal direction is the Eigenvector of the shear. Its Eigenvalue is 1, as it is not stretched.")
        image_search_button("Ganges River Flow", "ganges river Varanasi")

    with tabs[2]:
        st.subheader("The Mirror's Gaze (Reflection)")
        st.markdown("A reflection is a transformation. If you look into a mirror along the wall, your reflection seems to be on the other side. But what if you are a tiny light beam pointing *directly at* the mirror (perpendicular to it)?")
        st.latex("T_{reflect} = \\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix} \\text{ (reflection across x-axis)}")
        st.markdown("Your reflection comes straight back at you! The direction is perfectly preserved, but reversed. This is an Eigenvector with an Eigenvalue of -1. Any vector *along* the mirror is also an eigenvector—it doesn't change at all (Eigenvalue is 1).")
        image_search_button("Reflection in a Palace", "Jaipur City Palace mirror work")

    with tabs[3]:
        st.subheader("The Sun's Shadow (Projection)")
        st.markdown("Imagine the sun is directly overhead, casting shadows onto the ground. The ground is a line (our target space). This act of casting a shadow is a projection transformation.")
        st.latex("T_{project} = \\begin{bmatrix} 1 & 0 \\\\ 0 & 0 \\end{bmatrix} \\text{ (projection onto x-axis)}")
        st.markdown("Any object already lying flat on the ground (a vector on the x-axis) casts a shadow that is exactly itself. It's an Eigenvector with Eigenvalue 1. A vertical object (a vector on the y-axis) is crushed into a single point at the origin. It's also an Eigenvector, but its Eigenvalue is 0!")
        image_search_button("Konark Sun Temple Sundial", "Konark Sun Temple wheel")

    # --- Part 4: The Formalization (The Ganita Shastra) ---
    st.header("Part 4: The Ganita Shastra — The Mathematics of Dharma", divider="rainbow")
    st.markdown("""
    Our intuition is strong. We feel what an Eigenvector is. Now, let us give it a formal mathematical name and learn its laws, its *dharma* in the world of *Ganita* (mathematics).

    The entire concept is captured in one profound equation:
    """)
    st.latex("T \\vec{v} = \\lambda \\vec{v}")
    st.markdown("""
    Where:
    - **T** is the transformation matrix (the battlefield's rules).
    - **v** is the Eigenvector (the path of Dharma).
    - **λ** (lambda) is the Eigenvalue (the scalar impact factor).

    This equation states that applying the transformation **T** to the vector **v** results in the *exact same vector*, just scaled by a number **λ**.

    ### How do we find these sacred paths?

    We can't just guess and check forever. We need a system. Let's rearrange the equation.
    
    1.  Start with the core equation: `T*v = λ*v`
    2.  Bring everything to one side: `T*v - λ*v = 0`
    3.  To subtract these terms, we must express `λ*v` as a matrix-vector product. We use the Identity matrix `I`: `λ*I*v = λ*v`.
    4.  Substitute it back: `T*v - λ*I*v = 0`
    5.  Factor out the vector `v`: `(T - λI)v = 0`

    This final equation is the key! It says that there is some matrix `(T - λI)` which, when applied to our special vector `v`, crushes it to the zero vector. For this to happen with a non-zero vector `v`, the matrix `(T - λI)` must be "collapsible". In linear algebra, this means its **determinant must be zero**.

    `det(T - λI) = 0`

    Solving this equation for `λ` gives us the Eigenvalues! Once we have the Eigenvalues, we can plug them back into `(T - λI)v = 0` to find the corresponding Eigenvectors `v`.

    #### Worked Example (from Part 2)
    Let's find the Dharma of `T = [[3, 1], [0, 2]]` formally.
    """)
    st.code(f"""
    # Using Python and NumPy to find Eigenvalues and Eigenvectors
    import numpy as np

    T = np.array([[3, 1], 
                  [0, 2]])

    eigenvalues, eigenvectors = np.linalg.eig(T)

    print("Eigenvalues (λ):")
    print(eigenvalues) # Output will be [3., 2.]

    print("\\nEigenvectors (v):")
    print(eigenvectors) # Output will be columns of the matrix
    # 1st column corresponds to λ=3, 2nd column corresponds to λ=2
    """, language="python")

    st.markdown("As the code shows, the Eigenvalues are **λ=3** and **λ=2**. This means this transformation has two 'dharmic paths'. One stretches vectors by a factor of 3, and the other by a factor of 2. These are the values you found in the interactive demo!")

    # --- Part 5: The Application (The Games & Puzzles) ---
    st.header("Part 5: The Application — Puzzles of the Eigen-Verse", divider="rainbow")
    st.markdown("Knowledge becomes wisdom only when it is applied. Let's test your understanding with a few challenges.")

    game_tabs = st.tabs(["The ISRO Stability Test", "The Jaipur Artisan's Loom", "The Bengaluru Market Predictor"])
    with game_tabs[0]:
        st.subheader("🚀 The ISRO Stability Test")
        st.markdown("You are an engineer at ISRO analyzing a satellite's spin. An object spins stably only when it rotates around one of its principal axes, which are the Eigenvectors of its inertia tensor. Your job is to find a stable axis for the given tensor.")
        st.info("For a 3x3 matrix, finding this by hand is tough! This puzzle is about understanding the *concept*. Which of the following vectors remains unchanged in direction when transformed by T?")
        
        T_isro = np.array([[2, 0, 0], [0, 5, 0], [0, 0, 9]])
        st.latex("T_{inertia} = \\begin{bmatrix} 2 & 0 & 0 \\\\ 0 & 5 & 0 \\\\ 0 & 0 & 9 \\end{bmatrix}")

        options = ["v = [1, 1, 1]", "v = [0, 1, 0]", "v = [1, 2, 3]"]
        user_choice = st.radio("Choose the stable spin axis (the Eigenvector):", options, key="isro_game")

        if st.button("Check My Answer", key="isro_check"):
            if user_choice == "v = [0, 1, 0]":
                st.success("Correct! The vector [0, 1, 0] is an eigenvector. T*v = [0, 5, 0], which is 5 * v. The satellite will spin stably around this axis.")
            else:
                st.error("Not quite. If you transform that vector, its direction changes. For v=[1,1,1], T*v = [2,5,9], which points in a new direction.")

    with game_tabs[1]:
        st.subheader("🎨 The Jaipur Artisan's Loom")
        st.markdown("A master weaver in Jaipur is creating a new pattern. Her loom applies a shear transformation to the threads. To keep the border straight, she must align a central thread along the Eigenvector of the shear. Find that direction!")
        st.latex("T_{shear} = \\begin{bmatrix} 1 & 0.5 \\\\ 0 & 1 \\end{bmatrix}")
        st.markdown("Adjust the slider to find the angle of the thread that does not get tilted by the loom's shear.")
        angle_weave = st.slider("Angle of the Thread", 0, 180, 45, key="weave_game")
        if st.button("Test this Thread", key="weave_check"):
            if 0 <= angle_weave <= 1 or 179 <= angle_weave <= 180:
                 st.success("Perfect! A horizontal thread (0 or 180 degrees) is the Eigenvector for this shear. It runs straight and true!")
            else:
                 st.error("That thread gets tilted! Try again. Remember how shear transformations work from our gallery.")

    with game_tabs[2]:
        st.subheader("💹 The Bengaluru Market Predictor")
        st.markdown("You're a data scientist in Bengaluru modeling a simple two-stock market. Each month, the value of stocks transitions according to a matrix. An Eigenvector represents a stable portfolio mix—where the *proportion* of stocks doesn't change, only the total value.")
        st.latex("T_{market} = \\begin{bmatrix} 1.1 & 0.1 \\\\ 0.1 & 1.1 \\end{bmatrix}")
        st.markdown("Which portfolio mix is stable? (Hint: The Eigenvalue will be its monthly growth factor).")
        if "market_answer" not in st.session_state:
            st.session_state.market_answer = ""
        
        c1, c2 = st.columns(2)
        if c1.button("Mix A: 50% Stock 1, 50% Stock 2"):
            st.session_state.market_answer = "A"
        if c2.button("Mix B: 100% Stock 1, 0% Stock 2"):
            st.session_state.market_answer = "B"

        if st.session_state.market_answer == "A":
            st.success("Correct! A 50/50 mix ([1, 1]) is an eigenvector. T*v = [1.2, 1.2], which is 1.2 * v. This portfolio grows by 20% each month while keeping its 50/50 balance.")
        elif st.session_state.market_answer == "B":
            st.error("Incorrect. A portfolio of only Stock 1 ([1, 0]) becomes [1.1, 0.1] after one month, which is now a 91.6%/8.4% mix. The balance changed!")

    # --- Part 6: The Horizon (The Jnana-Chakshu - Eye of Knowledge) ---
    st.header("Part 6: The Horizon — The Jnana-Chakshu (Eye of Knowledge)", divider="rainbow")
    st.markdown("""
    We have found the path of Dharma. We have seen that within every transformation, there are fundamental, unshakable directions. This is not just a mathematical party trick; it is one of the most profound concepts in applied mathematics.

    Eigenvectors and Eigenvalues are the **soul of a matrix**. They reveal its fundamental properties and behavior.

    - **In Engineering (Civil & Mechanical):** When building a bridge in Mumbai or a new aircraft for the IAF, engineers use Eigenvalue analysis to find the natural frequencies of vibration. If an external force matches these frequencies, the structure can resonate and collapse. Finding the Eigenvalues means finding and avoiding catastrophe.
    
    - **In Data Science (The heart of Bengaluru's Tech Scene):** The most powerful dimensionality reduction technique, Principal Component Analysis (PCA), is nothing but finding the Eigenvectors of a dataset's covariance matrix. These Eigenvectors are the "principal components"—the directions of greatest variance. It's how we find the most important patterns in massive datasets, from customer behavior to financial markets. It finds the "Dharma of the Data".

    - **In Quantum Mechanics:** The entire universe at its most fundamental level is described by Eigenvalues. The Schrödinger equation is an Eigenvalue equation. Its Eigenvectors are the quantum states (like orbitals of an electron), and its Eigenvalues are the observable, quantized energy levels.

    The key takeaway is this: **Eigenvectors reveal the stable, intrinsic properties of any linear system, while Eigenvalues tell you the magnitude of the effect along those stable lines.**

    We have learned to see the hidden paths that give a transformation its character. But there's another, more fundamental property we must understand. Beyond how a matrix stretches specific vectors, how does it stretch or shrink *space itself*? What is the total impact of the transformation on area or volume? To understand that, we must venture forward and uncover the secret of the **Determinant**.
    """)
    image_search_button("Principal Component Analysis (PCA)", "PCA data visualization")


    # --- Part 7: The Check-up (The Pariksha) ---
    st.header("Part 7: The Check-up (The Pariksha)", divider="rainbow")
    st.markdown("Let's test the knowledge you have gained on this journey.")

    questions = {
        "1. In our core analogy, what does the Eigenvector represent?": {
            "options": ["The entire battlefield", "The strength of the army", "The warrior's unchanging path of Dharma", "A random soldier's path"],
            "correct": "The warrior's unchanging path of Dharma",
            "feedback": "Correct! The Eigenvector is the special direction that remains unchanged by the transformation, just like the warrior's Dharma."
        },
        "2. What is an Eigenvalue?": {
            "options": ["The direction of the Eigenvector", "The factor by which the Eigenvector is stretched or shrunk", "The size of the matrix", "A special type of matrix"],
            "correct": "The factor by which the Eigenvector is stretched or shrunk",
            "feedback": "Precisely! The Eigenvalue (λ) is the scalar that tells you the magnitude of the transformation's effect along the Eigenvector's path."
        },
        "3. If a vector `v` is an eigenvector of matrix `T` with an eigenvalue of 0, what does `T*v` equal?": {
            "options": ["v", "The zero vector [0, 0]", "A much longer vector", "This is impossible"],
            "correct": "The zero vector [0, 0]",
            "feedback": "Correct. T*v = 0*v, and anything multiplied by zero is the zero vector. This means the transformation completely collapses this direction."
        },
        "4. Which of these real-world applications is a primary use of Eigenvectors?": {
            "options": ["Calculating the area of a shape", "Finding the most significant patterns in data (PCA)", "Adding two vectors together", "Drawing a circle"],
            "correct": "Finding the most significant patterns in data (PCA)",
            "feedback": "Excellent! Principal Component Analysis is a powerful data science technique that relies entirely on finding the Eigenvectors of a dataset's covariance matrix to identify the most important trends."
        },
        "5. Mathematically, how do we begin the process of finding the Eigenvalues (λ) for a matrix T?": {
            "options": ["By solving det(T) = λ", "By solving det(T - λI) = 0", "By guessing vectors until one works", "By inverting the matrix T"],
            "correct": "By solving det(T - λI) = 0",
            "feedback": "That's the fundamental method! Setting the determinant of (T - λI) to zero gives us the characteristic equation, which we solve to find the eigenvalues."
        }
    }

    for i, (q, data) in enumerate(questions.items()):
        st.subheader(f"Question {i+1}")
        user_answer = st.radio(q, data["options"], key=f"q_{i}")
        if st.button("Submit Answer", key=f"b_{i}"):
            if user_answer == data["correct"]:
                st.success(data["feedback"])
            else:
                st.error(f"Not quite. The correct answer is: **{data['correct']}**. {data['feedback']}")
        st.markdown("---")