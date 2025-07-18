# chapters/chapter_3.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch
from utils.plotting import setup_plot, image_search_button # Assumes both are in plotting.py

def render():
    """
    Renders the massively expanded Chapter 3 on Matrix Determinants.
    Voice: An "Indian Feynman" - intuitive, story-driven, and culturally resonant.
    Word Count Goal: 6000+ words.
    """

    st.title("Chapter 3: The Atma of the Matrix (The Determinant)")
    st.markdown("---")

    # ==============================================================================
    # PART 1: THE CORE IDEA (THE ANALOGY)
    # ==============================================================================
    st.header("Part 1: The Secret of the Rangoli ✨")
    st.markdown("""
    Namaste! Let's begin not with dry numbers, but with something beautiful and familiar. Imagine you are in your family's courtyard during Diwali. Your mother or grandmother is creating a *Rangoli* or a *Kolam*. She starts with a simple chalk grid on the floor. On this grid, she decides to draw a beautiful square pattern, let's say one that covers a certain area—one square meter.

    Now, imagine a mischievous god (like a friendly *Asura* who loves mathematics) comes along and casts a spell on the very fabric of the courtyard. This spell is a **Transformation**. The grid lines of the courtyard stretch and skew. The east-west lines might get closer, while the north-south lines might stretch and tilt.

    The chalk of the Rangoli is magically bound to the grid lines. So, as the courtyard's grid shifts, the beautiful square pattern is also forced to stretch, skew, and morph into a new shape—a parallelogram.

    The most important question is: **How much has the *area* of our Rangoli pattern changed?**

    Did the spell double the space it takes up, making it grander? Did it squish it to half its size, making it more intricate? Did it, perhaps, flip the pattern over as if we are seeing its reflection in a pond?

    Every magical spell—every *transformation*—has a secret number, a unique essence or *'Atma'*, that tells us exactly this. This number is its **Determinant**.

    - If the new Rangoli covers **twice** the area, the determinant of the spell is **2**.
    - If it's squished to **half** the area, the determinant is **0.5**.
    - If the spell somehow **flips the orientation** of the Rangoli (imagine the pattern's top-right corner is now its top-left), the determinant becomes **negative**. A determinant of **-1** means it flipped but kept the same area.
    - And here is the most profound part: What if the spell is so powerful that it squishes the entire two-dimensional Rangoli into a single, straight line? The pattern is ruined! It has **zero area**. In this case, the determinant of the spell is **0**. This is a special, irreversible kind of magic.

    The Determinant isn't just a number. It is the measure of the transformation's power to scale area. It is the soul, the *Atma*, of the matrix. Let's build a machine to explore this magic.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kolam_in_Tamil_Nadu.JPG/1280px-Kolam_in_Tamil_Nadu.JPG", caption="A traditional Kolam, whose area we can imagine transforming. The geometry is the key.")


    # ==============================================================================
    # PART 2: THE MECHANISM (THE TRANSFORMATION ENGINE)
    # ==============================================================================
    st.header("Part 2: The Yantra of Transformation")
    st.markdown("""
    Let's build a machine, a *Yantra*, to control this space-bending magic ourselves. This machine is controlled by a **Matrix**. Think of the matrix as the four magic numbers that define the entire spell.

    Below, you have a visualization.
    - The **Blue Square** is our original Rangoli pattern. It sits on the original, perfect grid. Its area is exactly 1.
    - The **Red Shape** is the transformed Rangoli after the spell. Notice how it's now a parallelogram.
    - On the left, you have four sliders. These are the controls for our Yantra, the four numbers in our 2x2 matrix.

    **Your Mission:** Don't worry about the math yet. Just *play*. Be a curious child. Slide the controls and observe. Build an intuition for the cause and effect.

    - What happens to the red area when you increase 'a' or 'd'?
    - What do 'b' and 'c' do? They seem to introduce a 'tilt' or 'shear'.
    - Watch the **Determinant** value. How does it correspond to the red area? See if you can intuitively feel when it's about to become positive, negative, or zero.
    """)

    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.subheader("The Four Levers of the Yantra")
        st.latex("T = \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}")
        a = st.slider("Matrix element 'a' (Horizontal stretch of î)", -2.5, 2.5, 1.0, 0.1, key="c3_a")
        b = st.slider("Matrix element 'b' (Horizontal stretch of ĵ)", -2.5, 2.5, 0.0, 0.1, key="c3_b")
        c = st.slider("Matrix element 'c' (Vertical stretch of î)", -2.5, 2.5, 0.0, 0.1, key="c3_c")
        d = st.slider("Matrix element 'd' (Vertical stretch of ĵ)", -2.5, 2.5, 1.0, 0.1, key="c3_d")

        T = np.array([[a, b], [c, d]])
        det_T = np.linalg.det(T)
        st.markdown("---")
        st.metric(label="✨ Atma (Determinant)", value=f"{det_T:.2f}")

    with col2:
        # Define the original square and basis vectors
        square = np.array([[0,0], [0,1], [1,1], [1,0], [0,0]])
        i_hat = np.array([1, 0])
        j_hat = np.array([0, 1])

        # Apply the transformation
        transformed_square = (T @ square.T).T
        transformed_i_hat = T @ i_hat
        transformed_j_hat = T @ j_hat

        fig, ax = plt.subplots(figsize=(8, 8))

        # Plot the transformed square
        ax.add_patch(Polygon(square, closed=True, color='blue', alpha=0.3, label='Original Rangoli (Area = 1)'))
        ax.add_patch(Polygon(transformed_square, closed=True, color='red', alpha=0.5, label=f'Transformed Rangoli (Area = {det_T:.2f})'))

        # Plot original basis vectors
        ax.quiver(0, 0, i_hat[0], i_hat[1], angles='xy', scale_units='xy', scale=1, color='blue', width=0.015, label="Original î")
        ax.quiver(0, 0, j_hat[0], j_hat[1], angles='xy', scale_units='xy', scale=1, color='green', width=0.015, label="Original ĵ")

        # Plot transformed basis vectors
        ax.quiver(0, 0, transformed_i_hat[0], transformed_i_hat[1], angles='xy', scale_units='xy', scale=1, color='#FF4B4B', width=0.015, label="Transformed î")
        ax.quiver(0, 0, transformed_j_hat[0], transformed_j_hat[1], angles='xy', scale_units='xy', scale=1, color='#4BFF4B', width=0.015, label="Transformed ĵ")

        setup_plot(ax, "The Yantra in Action", xlim=(-5, 5), ylim=(-5, 5))
        ax.legend()
        st.pyplot(fig)

    st.markdown("""
    **A Deeper Intuition:** Look at the colored arrows, the **basis vectors**.
    - The matrix column `[a, c]` is simply the new landing spot for the original blue vector `î`.
    - The matrix column `[b, d]` is the new landing spot for the original green vector `ĵ`.
    
    The entire transformation, all the stretching and squishing of infinite space, is completely defined by just telling those two original vectors where to go! The area of the parallelogram formed by these two new vectors is *exactly* the determinant. The determinant is the area of the parallelogram spanned by the transformed basis vectors.
    """)
    st.markdown("---")


    # ==============================================================================
    # PART 3: THE GALLERY (SHOWCASING VARIETY)
    # ==============================================================================
    st.header("Part 3: A Gallery of Magical Spells")
    st.markdown("""
    Just as there are different mantras for different effects, there are different types of matrices for different transformations. Let's look at a few famous ones. Think of this as a tour of a master artisan's workshop, seeing the different block prints they can create.
    """)

    st.info("Click the buttons to see real-world images that evoke these mathematical ideas!")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["**Identity (No Change)**", "**Scaling (Enlarging)**", "**Rotation (Spinning)**", "**Shear (Tilting)**", "**Singular (Collapse)**"])

    with tab1:
        st.subheader("The Identity Matrix: The 'Shanti' Mantra")
        st.markdown("""
        This is the spell of no change. It leaves everything as it is. It's the equivalent of chanting a mantra for peace, "Shanti, Shanti, Shanti." The original blue square and the red transformed one are perfectly on top of each other.
        - The `î` vector `[1, 0]` stays at `[1, 0]`.
        - The `ĵ` vector `[0, 1]` stays at `[0, 1]`.
        The area doesn't change, so the determinant is **1**.
        """)
        st.latex("I = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix} \implies \\det(I) = 1")
        image_search_button("Sacred Geometry Yantra", "sri yantra sacred geometry")

    with tab2:
        st.subheader("The Scaling Matrix: The 'Vistar' Spell")
        st.markdown("""
        This spell, *Vistar* (meaning 'to expand'), uniformly grows or shrinks everything. If you make the diagonal elements 2, the area becomes 4 times larger! Think of zooming into a beautiful pattern on a pashmina shawl.
        - The `î` vector `[1, 0]` goes to `[k, 0]`.
        - The `ĵ` vector `[0, 1]` goes to `[0, k]`.
        The area scales by the product of the diagonal elements.
        """)
        s = st.slider("Scaling factor 'k'", 0.0, 3.0, 1.5, 0.1, key='scale_k')
        st.latex(f"S = \\begin{{bmatrix}} {s} & 0 \\\\ 0 & {s} \\end{{bmatrix}} \implies \\det(S) = {s*s:.2f}")
        image_search_button("Jaipur Block Printing", "jaipur block printing patterns")

    with tab3:
        st.subheader("The Rotation Matrix: The 'Chakra' Spell")
        st.markdown("""
        This spell rotates the entire courtyard, like a spinning *Chakra* or a dancer performing a pirouette. Notice that no matter how much you rotate, the *area* of the Rangoli never changes. That's why the determinant of a pure rotation is always **1**. The orientation doesn't flip, so it's not -1.
        """)
        angle_deg = st.slider("Rotation angle 'θ' (in degrees)", -180.0, 180.0, 45.0, 1.0, key='rot_angle')
        angle_rad = np.deg2rad(angle_deg)
        cos_t, sin_t = np.cos(angle_rad), np.sin(angle_rad)
        st.latex(f"R = \\begin{{bmatrix}} {cos_t:.2f} & {-sin_t:.2f} \\\\ {sin_t:.2f} & {cos_t:.2f} \\end{{bmatrix}} \implies \\det(R) = {cos_t**2 - (-sin_t*sin_t):.2f}")
        image_search_button("Mughal Lattice (Jaali)", "mughal jaali patterns")

    with tab4:
        st.subheader("The Shear Matrix: The 'Tircha' Spell")
        st.markdown("""
        This spell, *Tircha* (meaning 'tilted' or 'askew'), pushes layers of space across each other, like a deck of cards being pushed from the side. Look at the designs in old Mughal architecture or some woven textiles; you'll see this shearing effect. It's fascinating that even though the shape is distorted, its area is preserved! The determinant remains **1**.
        """)
        m = st.slider("Shearing factor 'm'", -2.0, 2.0, 1.0, 0.1, key='shear_m')
        st.latex(f"H = \\begin{{bmatrix}} 1 & {m} \\\\ 0 & 1 \\end{{bmatrix}} \implies \\det(H) = 1")
        image_search_button("Woven Ikat Patterns", "ikat textile patterns india")

    with tab5:
        st.subheader("The Singular Matrix: The 'Brahma's Arrow' Spell")
        st.markdown("""
        This is the most extreme spell. In the Mahabharata, a powerful weapon, a *Brahmastra*, could cause total devastation. A singular matrix is the mathematical equivalent: it takes all of two-dimensional space and collapses it onto a single line or even a single point. All area is annihilated.
        The determinant is **0**. This is the mark of collapse. There is no going back from this; you cannot "un-collapse" a line back into a plane. The magic is irreversible.
        """)
        st.latex(f"Z = \\begin{{bmatrix}} 2 & 1 \\\\ 2 & 1 \\end{{bmatrix}} \implies \\det(Z) = (2)(1) - (1)(2) = 0")
        image_search_button("Line drawings", "one line drawing art")

    st.markdown("---")

    # ==============================================================================
    # PART 4: THE FORMALIZATION (THE GANITA SHASTRA)
    # ==============================================================================
    st.header("Part 4: The Language of the Sages (The Formal Mathematics)")
    st.markdown("""
    We have played, we have built intuition. Now, let's learn the formal language of the ancient sages of mathematics, the *Ganita Shastra*. This will allow us to wield this power with precision.
    """)

    st.subheader("4.1. The 2x2 Determinant: The 'ad-bc' Sutra")
    st.markdown("""
    For a 2x2 matrix, the formula—the *sutra*—to calculate its determinant is wonderfully simple. You've been seeing it in action all along.

    Given a matrix:
    """)
    st.latex(f"T = \\begin{{bmatrix}} a & b \\\\ c & d \\end{{bmatrix}}")
    st.markdown("""
    The determinant, written as `det(T)` or `|T|`, is:
    """)
    st.latex("\\det(T) = (a \\times d) - (b \\times c)")
    st.markdown("""
    It's the product of the main diagonal (top-left to bottom-right) minus the product of the anti-diagonal (top-right to bottom-left).

    Let's check with the matrix from our Yantra:
    """)
    st.latex(f"T = \\begin{{bmatrix}} {a:.1f} & {b:.1f} \\\\ {c:.1f} & {d:.1f} \\end{{bmatrix}}")
    st.latex(f"\\det(T) = ({a:.1f} \\times {d:.1f}) - ({b:.1f} \\times {c:.1f}) = {a*d:.2f} - {b*c:.2f} = {det_T:.2f}")
    st.success(f"The formula matches our observed value: **{det_T:.2f}**")

    st.subheader("4.2. Expanding Our Universe: The 3x3 Determinant")
    st.markdown("""
    Our world isn't flat like a Rangoli. We live in three dimensions! We need a way to measure how a transformation scales **volume**. Imagine transforming a clay cube into some new 3D shape (a parallelepiped). The 3x3 determinant tells us the scaling factor for its volume.

    One common method is the **Rule of Sarrus**, a visual mnemonic.
    Given a matrix:
    """)
    st.latex("M = \\begin{bmatrix} a & b & c \\\\ d & e & f \\\\ g & h & i \\end{bmatrix}")
    st.markdown("""
    To calculate its determinant, we write down the first two columns again to the right of the matrix:
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Sarrus_rule_v2.svg/300px-Sarrus_rule_v2.svg.png", caption="The Rule of Sarrus for 3x3 determinants.")
    st.markdown("""
    Then we add the products of the 'downward' diagonals and subtract the products of the 'upward' diagonals.
    """)
    st.latex("\\det(M) = (aei + bfg + cdh) - (ceg + afh + bdi)")
    st.warning("This visual trick ONLY works for 3x3 matrices! For anything larger, we need a more powerful method, like cofactor expansion.")

    st.subheader("4.3. Fundamental Properties of Determinants (The Dharma)")
    st.markdown("""
    Determinants follow certain fundamental laws, a *Dharma*, that are universally true. Understanding these is key to mastery.

    1.  **Identity Dharma (`det(I) = 1`):** The determinant of an identity matrix is always 1. This makes sense; an identity transformation doesn't change anything, so the area/volume scaling factor is 1.

    2.  **Transpose Dharma (`det(Aᵀ) = det(A)`):** The determinant of a matrix is the same as its transpose. Swapping rows and columns doesn't change the underlying scaling behavior.
        
    3.  **Multiplication Dharma (`det(AB) = det(A)det(B)`):** This is the most magical! If you apply one transformation (B) and then another (A), the total scaling factor is just the product of their individual scaling factors. A spell that doubles area followed by one that triples it results in a total scaling of 2 * 3 = 6.

    4.  **Row Swap Dharma:** If you swap two rows in a matrix, the determinant's sign flips (`det(B) = -det(A)`). This corresponds to flipping the orientation of space. Imagine swapping the places of the transformed `î` and `ĵ` vectors—it's like looking at the resulting parallelogram from the back.
    
    5.  **Scalar Multiple Dharma:** If you multiply one row by a scalar `k`, the determinant is multiplied by `k`. This is because you are stretching the resulting shape in one direction by that factor. If you multiply the *entire* n x n matrix by `k`, then `det(kA) = kⁿdet(A)`.
    """)
    st.markdown("---")

    # ==============================================================================
    # PART 5: THE APPLICATION (THE KHEL AND KASRAT)
    # ==============================================================================
    st.header("Part 5: Games and Exercises (Khel aur Kasrat)")
    st.markdown("Theory is one thing, but true understanding comes from applying it. Let's play some games!")

    game_tabs = st.tabs(["**Game 1: The ISRO Launch**", "**Game 2: Jaipur Artisan**", "**Game 3: The Astrologer's Puzzle**", "**Game 4: 3D Architect**"])

    with game_tabs[0]:
        st.subheader("🚀 Game 1: The ISRO Launch Pad")
        st.markdown("""
        You are a scientist at ISRO, preparing to launch the next Mangalyaan mission. The launch requires a final transformation to orient the probe. If this transformation is **singular** (determinant = 0), the probe's coordinate system will collapse into a line, and the mission will fail catastrophically!

        **Your Task:** Use the main Yantra controls in Part 2. Can you create **three different non-singular matrices**? One that expands the area, one that shrinks it, and one that flips it. The key is to avoid a determinant of 0 at all costs!
        """)
        if abs(det_T) < 0.01:
            st.error("🚨 LAUNCH ABORT! Determinant is zero! The coordinate space has collapsed. Try again!")
        elif det_T > 1:
            st.success(f"✅ Launch Success! Determinant is {det_T:.2f}. The probe's space is expanded. A stable transformation.")
        elif det_T < 0:
            st.success(f"✅ Launch Success! Determinant is {det_T:.2f}. The probe's space is flipped but stable.")
        else: # 0 < det_T <= 1
            st.success(f"✅ Launch Success! Determinant is {det_T:.2f}. The probe's space is compressed but stable.")

    with game_tabs[1]:
        st.subheader("🎨 Game 2: The Jaipur Textile Artisan")
        st.markdown("""
        You are an artisan block-printing a beautiful saree. You have a square block of wood (area 1). The client wants a new parallelogram design that has a specific area.

        **Your Task:** Use the main Yantra controls in Part 2 to create a transformation matrix whose determinant **exactly matches the target area** given below.
        """)
        target_det = st.select_slider("Select a target design area (determinant):", options=[-2.0, -0.5, 1.5, 2.5], value=1.5)
        st.write(f"Your current determinant is: **{det_T:.2f}**")
        if abs(det_T - target_det) < 0.05:
            st.balloons()
            st.success(f"Marvellous! You've crafted the perfect design with an area of {target_det}!")
        else:
            st.warning("The area is not quite right. Adjust the levers of the Yantra.")

    with game_tabs[2]:
        st.subheader(" ज्योतिष Game 3: The Astrologer's Puzzle")
        st.markdown("""
        An ancient astrologer has left behind a cryptic matrix. He says that for the stars to align, the determinant of his matrix must be zero. A crucial number, 'x', has been lost to time.

        **Your Task:** Find the value of 'x' that makes the determinant of the following matrix equal to zero.
        """)
        st.latex(r"A = \begin{bmatrix} 2 & 4 \\ 3 & x \end{bmatrix}")
        st.markdown(r"We need `det(A) = 0`, which means `(2)(x) - (4)(3) = 0`.")
        st.markdown(r"So, `2x - 12 = 0`. What must `x` be?")
        x_answer = st.number_input("Enter your calculated value for x:", value=0, step=1)
        if st.button("Check my answer"):
            if x_answer == 6:
                st.success("Correct! When x=6, the determinant is 0. The stars are aligned!")
            else:
                st.error("Not quite. Remember, we need 2x = 12.")

    with game_tabs[3]:
        st.subheader("🏛️ Game 4: The 3D Architect")
        st.markdown("""
        Now for a real challenge. You are designing a modern building in Mumbai and need to transform a 1x1x1 meter cube of granite. Calculate the determinant of the 3x3 matrix below to find out how the volume changes.
        """)
        st.latex(r"M = \begin{bmatrix} 1 & 0 & 2 \\ 3 & 4 & 1 \\ 0 & 5 & 1 \end{bmatrix}")
        st.markdown("Use the Rule of Sarrus: `(aei + bfg + cdh) - (ceg + afh + bdi)`")
        vol_answer = st.number_input("Calculate the determinant (the new volume):", value=0)
        if st.button("Check Volume"):
            # (1*4*1 + 0*1*0 + 2*3*5) - (2*4*0 + 1*1*5 + 0*3*1) = (4 + 0 + 30) - (0 + 5 + 0) = 34 - 5 = 29
            if vol_answer == 29:
                st.success("Brilliant! The volume of the granite block is now 29 cubic meters. That's a significant expansion!")
            else:
                st.error("Incorrect. Let's trace the calculation: (1*4*1 + 0*1*0 + 2*3*5) - (2*4*0 + 1*1*5 + 0*3*1) = (4 + 30) - (5) = 29.")

    st.markdown("---")


    # ==============================================================================
    # PART 6: THE HORIZON (THE JNANA-CHAKSHU)
    # ==============================================================================
    st.header("Part 6: The Eye of Knowledge (What's Next?)")
    st.markdown("""
    The determinant is not just an academic curiosity. It is a *Jnana-Chakshu*, an eye of knowledge, that helps us see deeper into the nature of systems. Its applications are vast and touch many aspects of modern Indian science and technology.

    ### **Invertibility: Can We Reverse the Spell?**
    This is the single most important application. A transformation can only be reversed if its determinant is **non-zero**.
    - If `det(A) ≠ 0`, the matrix `A` has an **inverse**, written `A⁻¹`. This inverse is the "undo" spell. If you stretched the Rangoli, the inverse squishes it back perfectly.
    - If `det(A) = 0`, the spell is irreversible. You've squashed the world into a line. There is no information on how to 'un-squash' it. This is why a determinant of zero is also called **singular**—it's a point of no return.

    This concept is the bedrock of solving systems of linear equations. If the determinant of the coefficient matrix is non-zero, we know there is a unique solution.

    ### **Cramer's Rule: A Formula for Solutions**
    Named after Gabriel Cramer, this rule uses determinants to directly solve for the variables in a system of linear equations, like those used to model economic policies or circuit diagrams. While computationally expensive for large systems, it's a beautiful theoretical result. For a system `Ax = b`:
    
    `xᵢ = det(Aᵢ) / det(A)`
    
    where `Aᵢ` is the matrix `A` with the i-th column replaced by the vector `b`.

    ### **Eigenvalues and Eigenvectors: The Soul's True Directions**
    This is where it gets truly profound. For any given transformation, there are special vectors that do not change their direction—they only stretch. These are the *Eigenvectors* (the 'self-vectors'), and the amount they stretch by is the *Eigenvalue*. To find them, we must solve this characteristic equation:

    `det(A - λI) = 0`

    Here, `λ` is the eigenvalue we are looking for. We are literally searching for a value `λ` that makes the matrix `A - λI` singular! This is a cornerstone of modern data science, used in everything from **Google's PageRank** to analyzing stock market trends for an investment firm in Mumbai.

    ### **Real-World Indian Applications:**
    - **ISRO, Bengaluru**: When launching a satellite, its orientation in 3D space is controlled by rotation matrices. Calculating determinants ensures the orientation commands are valid and non-collapsing.
    - **Bollywood VFX, Mumbai**: When a CGI artist creates a 3D model of a spaceship for a movie like *Brahmāstra*, every stretch, rotation, and movement is a matrix transformation. The determinant is used in the background rendering engine to calculate surface areas and volumes correctly for lighting and physics simulations.
    - **Data Science, Hyderabad/Bengaluru**: Data scientists analyzing customer behavior use a tool called a **Covariance Matrix**. The determinant of this matrix, related to the "Generalized Variance," tells them how spread out the data is. A small determinant might imply strong correlation between variables (e.g., people who buy *samosas* also tend to buy *chai*).

    The determinant tells us if a system has a unique, reversible state. This naturally leads us to our next chapter: **Inverse and Transpose of Matrices**, where we will learn how to actually compute the "undo" spell.
    """)
    st.markdown("---")

    # ==============================================================================
    # PART 7: THE CHECK-UP (THE PARIKSHA)
    # ==============================================================================
    st.header("Part 7: Test Your Understanding (Pariksha)")
    st.markdown("Let's see how much of the sages' wisdom you have absorbed.")

    q1 = st.radio(
        "**Question 1:** An artist in Chennai applies a transformation with a determinant of **-3** to her square canvas. What is the result?",
        (
            'The canvas is now a parallelogram with one-third the area and is flipped.',
            'The canvas is now a parallelogram with three times the area and is flipped.',
            'The canvas is now a parallelogram with three times the area and has the same orientation.',
            'The canvas collapses to a line.'
        ),
        index=None, key="q1"
    )

    q2 = st.radio(
        "**Question 2:** Why is the determinant of a pure rotation matrix always 1?",
        (
            'Because rotation makes shapes bigger.',
            'Because rotation flips the orientation of shapes.',
            'Because rotation preserves the area of shapes and does not flip their orientation.',
            'Because rotation matrices only have sine and cosine values.'
        ),
        index=None, key="q2"
    )

    q3 = st.radio(
        "**Question 3:** You are given a matrix `A` with `det(A) = 4`. What is the determinant of the matrix `2A` if `A` is a 3x3 matrix?",
        (
            '4',
            '8',
            '16',
            '32'
        ),
        index=None, key="q3"
    )

    q4 = st.radio(
        "**Question 4:** What is the most critical real-world implication of a matrix having a determinant of 0?",
        (
            'The transformation is very complex.',
            'The transformation involves negative numbers.',
            'The transformation is irreversible, and the system might not have a unique solution.',
            'The transformation is computationally easy to perform.'
        ),
        index=None, key="q4"
    )

    q5 = st.radio(
        "**Question 5:** If `det(A) = 2` and `det(B) = 5`, what is `det(A @ B)` where `@` is matrix multiplication?",
        (
            '7',
            '10',
            '2.5',
            'Cannot be determined.'
        ),
        index=None, key="q5"
    )
    
    st.markdown("---")
    if st.button("Submit My Answers"):
        # Q1
        if q1 == 'The canvas is now a parallelogram with three times the area and is flipped.':
            st.success("Q1: Correct! The magnitude `| -3 | = 3` gives the area scaling, and the negative sign indicates an orientation flip.")
        else:
            st.error("Q1: Not quite. Remember the two roles of the determinant: the number for scaling and the sign for orientation.")

        # Q2
        if q2 == 'Because rotation preserves the area of shapes and does not flip their orientation.':
            st.success("Q2: Exactly! Rotation is a 'rigid' motion. It changes position but not intrinsic properties like area.")
        else:
            st.error("Q2: Think about what happens to the area of the red shape in the Chakra spell visualization.")

        # Q3
        if q3 == '32':
            st.success("Q3: Excellent! You remembered the Scalar Multiple Dharma. For an n x n matrix, `det(kA) = kⁿdet(A)`. Here, `n=3`, so `det(2A) = 2³ * det(A) = 8 * 4 = 32`.")
        else:
            st.error("Q3: Close! Review the Scalar Multiple Dharma. The exponent matters!")
            
        # Q4
        if q4 == 'The transformation is irreversible, and the system might not have a unique solution.':
            st.success("Q4: Perfect! This is the most crucial takeaway. A zero determinant signals collapse and non-invertibility.")
        else:
            st.error("Q4: Think about the 'Brahma's Arrow' spell. What is its most significant feature?")

        # Q5
        if q5 == '10':
            st.success("Q5: Correct! You've mastered the Multiplication Dharma: `det(AB) = det(A)det(B)`. So, `2 * 5 = 10`.")
        else:
            st.error("Q5: Revisit the 'Dharma' of multiplication. How do sequential spells combine their power?")