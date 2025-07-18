# chapters/chapter_6.py
#
# To be called by a main app.py
#
# Full Chapter Code: Invertibility: Can We Reverse the Spell?
# Word Count: ~6,200 words

import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time
import urllib.parse

# ---------------------------------------------------------------------
# UTILITY FUNCTION (as specified in the design guide)
# This should ideally be in a separate `utils/helpers.py` file and imported.
# ---------------------------------------------------------------------

def image_search_button(label, search_term, use_container_width=True):
    """
    Creates a Streamlit link button that searches Google Images in a new tab.
    This is a mandatory helper function as per the design guide.
    """
    encoded_term = urllib.parse.quote_plus(search_term)
    url = f"https://www.google.com/search?q={encoded_term}&tbm=isch"
    st.link_button(f"🖼️ See images of: {label}", url, use_container_width=use_container_width)

# ---------------------------------------------------------------------
# CHAPTER 3: RENDER FUNCTION
# ---------------------------------------------------------------------

def render():
    """
    Renders the full chapter on Invertibility, following the 7-part structure.
    """

    st.header("Chapter 3: Invertibility", divider="rainbow")
    st.title("Can We Reverse the Spell?")

    # ---------------------------------------------------------------------
    # INTRODUCTION - Setting the stage
    # ---------------------------------------------------------------------
    st.markdown("""
    Welcome back, seeker of patterns. In our previous chapters, we learned the art of transformation. We saw how matrices, like powerful spells, can stretch, squash, rotate, and shear the very fabric of space. We even discovered their secret heartbeats—the determinant—a single number that tells us how much a transformation expands or shrinks area.

    But with great power comes a profound question. When a magician casts a spell, can it always be undone? If we transform our world, can we always find our way back? This question of 'reversibility' is not just a philosophical curiosity; it is perhaps the single most important application of the determinant. It is the key that separates transformations that merely rearrange from those that truly destroy.

    Today, we embark on a journey to understand this very idea. We will explore the concept of **Invertibility**. Can we reverse the spell? Or are some transformations a point of no return? Let's begin not with numbers, but with something far more familiar: a humble pot of milk in an Indian kitchen.
    """)

    # ---------------------------------------------------------------------
    # PART 1: THE CORE IDEA (THE ANALOGY)
    # ---------------------------------------------------------------------
    st.subheader("Part 1: The Kitchen Alchemist and the Point of No Return", divider="grey")
    st.markdown("""
    Imagine you are in a kitchen, a place of wonderful transformations. You have a vessel of fresh, flowing milk. This is your starting point, your original, pristine space.

    **The Reversible Spell: Dissolving Sugar**

    First, you perform a simple act of alchemy. You take a spoonful of sugar and stir it into the milk until it dissolves completely. The milk is now sweeter; it has been 'transformed'. But is the sugar gone forever? Of course not. You know, with a deep, intuitive certainty, that if you were to patiently heat the milk and evaporate the water, you would be left with the milk solids and the sugar crystals. You can get the sugar back. The original components, though mixed, are not destroyed. This transformation is **reversible**. The information about the sugar is still present, encoded within the sweetness of the milk.

    **The Irreversible Spell: The Birth of Paneer**

    Now, let's try a different kind of alchemy. You take the same vessel of milk and bring it to a gentle boil. Then, you squeeze the juice of a lemon into it. You stir, and almost instantly, magic happens. The liquid milk begins to curdle. The proteins, once freely floating, now cling to each other, forming soft, white clumps of *paneer* (cottage cheese). The watery whey separates. You have performed another transformation, creating something new and delicious.

    But here is the crucial question: can you reverse *this* spell? Can you take the paneer and the whey, mix them back together, and get your original, flowing milk?
    """)

    image_search_button("Fresh Paneer being made from milk", "making paneer from milk")

    st.markdown("""
    No. The very thought seems absurd. The act of curdling is a fundamental, chemical change. The proteins have been denatured; their structure has been irrevocably altered. They have clumped together in a way that cannot be undone by simple stirring or waiting. You have passed a point of no return. You have lost the 'milk-ness' of the original liquid. This transformation is **irreversible**. Information has been destroyed. You cannot look at a block of paneer and know the exact swirls and currents that existed in the milk it came from.

    This, in its essence, is the difference between an invertible and a non-invertible (or **singular**) transformation.

    - **Invertible Transformation (like dissolving sugar):** It changes things, but it preserves all the original information. Because it preserves information, you can define a perfect "undo" operation.
    - **Singular Transformation (like making paneer):** It collapses the original substance into a new form, losing information in the process. There is no "undo" spell. The original state is lost to history.

    In the world of linear algebra, the determinant is our lemon juice test. It is the oracle that tells us, before we even perform the transformation, whether it will be like dissolving sugar or like curdling milk.

    If **det(A) ≠ 0**, the spell is reversible. The information is safe.
    If **det(A) = 0**, the spell is irreversible. The transformation is a one-way street. It has squashed our space, like turning 3D milk into a 2D-like solid, and there's no going back. This is why a matrix with a zero determinant is called **singular**—it represents a unique, singular moment of collapse.

    Keep this analogy of the paneer in your mind. It is the heart of everything we are about to explore. We will now build a visual playground to see this 'curdling' of space happen right before our eyes.
    """)

    # ---------------------------------------------------------------------
    # PART 2: THE MECHANISM (INTERACTIVE DISCOVERY)
    # ---------------------------------------------------------------------
    st.subheader("Part 2: The Geometric Paneer-Maker", divider="grey")
    st.markdown("""
    Let's move from the kitchen to our digital canvas. We will now build our own 'transformation machine' to see how space itself can be curdled.

    Below is an interactive laboratory. On the left, you see our 'original space'—a simple shape (let's call it our 'Geometric Lotus') defined by a few key points, along with our standard basis vectors, `î` (red) and `ĵ` (blue).

    On the right, you see the result of applying a transformation matrix **A** to everything on the left. You are the master of this transformation! Use the four sliders to control the elements of the matrix **A**.

    **Your Mission:**
    1.  Play with the sliders and observe how the Geometric Lotus and the basis vectors change on the right.
    2.  Keep a close eye on the **Determinant**, calculated for you in real-time. Notice how it corresponds to the area of the blue-red parallelogram on the right.
    3.  Crucially, experiment with the "**Attempt to Reverse**" button. What does it do? When does it succeed, and when does it fail? Try to make the determinant *exactly zero*. What happens to the transformed shape?
    """)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Controls (Your Spellbook)")
        a = st.slider("Matrix element [0, 0] (a)", -2.0, 2.0, 1.0, 0.1)
        b = st.slider("Matrix element [0, 1] (b)", -2.0, 2.0, 0.0, 0.1)
        c = st.slider("Matrix element [1, 0] (c)", -2.0, 2.0, 0.0, 0.1)
        d = st.slider("Matrix element [1, 1] (d)", -2.0, 2.0, 1.0, 0.1)

        matrix = np.array([[a, b], [c, d]])
        det = np.linalg.det(matrix)

        st.metric(label="Determinant (ad - bc)", value=f"{det:.2f}")

        if st.button("✨ Attempt to Reverse", use_container_width=True):
            st.session_state.reverse_attempt = True
        else:
            st.session_state.reverse_attempt = False

    # Define the 'Geometric Lotus' points
    lotus_points = np.array([
        [0, 0], [0.2, 0.8], [0.5, 0.6], [0.8, 0.8], [1.0, 0],
        [0.8, -0.2], [0.5, -0.4], [0.2, -0.2], [0, 0]
    ]).T

    # Basis vectors
    i_hat = np.array([1, 0])
    j_hat = np.array([0, 1])

    # Apply transformation
    transformed_lotus = matrix @ lotus_points
    transformed_i = matrix @ i_hat
    transformed_j = matrix @ j_hat

    # Create the plots
    fig = go.Figure()

    # Plot 1: Original Space
    fig.add_trace(go.Scatter(x=lotus_points[0, :], y=lotus_points[1, :], mode='lines+markers', name='Original Lotus', line=dict(color='purple')))
    fig.add_trace(go.Scatter(x=[0, i_hat[0]], y=[0, i_hat[1]], mode='lines', name='î', line=dict(color='red', width=4)))
    fig.add_trace(go.Scatter(x=[0, j_hat[0]], y=[0, j_hat[1]], mode='lines', name='ĵ', line=dict(color='blue', width=4)))


    # Plot 2: Transformed Space
    # Draw the transformed parallelogram first so it's in the background
    parallelogram_x = [0, transformed_i[0], transformed_i[0] + transformed_j[0], transformed_j[0], 0]
    parallelogram_y = [0, transformed_i[1], transformed_i[1] + transformed_j[1], transformed_j[1], 0]
    fig.add_trace(go.Scatter(x=parallelogram_x, y=parallelogram_y, fill="toself", fillcolor=f"rgba(135, 206, 250, {abs(det/4.0) if det != 0 else 0.5})", line=dict(color='rgba(0,0,0,0)'), name='Transformed Area'))


    fig.add_trace(go.Scatter(x=transformed_lotus[0, :], y=transformed_lotus[1, :], mode='lines+markers', name='Transformed Lotus', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=[0, transformed_i[0]], y=[0, transformed_i[1]], mode='lines', name='Transformed î', line=dict(color='#FF6969', width=4))) # Lighter red
    fig.add_trace(go.Scatter(x=[0, transformed_j[0]], y=[0, transformed_j[1]], mode='lines', name='Transformed ĵ', line=dict(color='#ADD8E6', width=4))) # Lighter blue

    fig.update_layout(
        xaxis=dict(range=[-3, 3]),
        yaxis=dict(range=[-3, 3]),
        width=700,
        height=500,
        showlegend=True,
        title="Left: Original Space  |  Right: Transformed Space"
    )
    fig.update_yaxes(scaleanchor="x", scaleratio=1)

    with col2:
        st.plotly_chart(fig, use_container_width=True)

        if st.session_state.reverse_attempt:
            if abs(det) > 1e-6: # Check if determinant is practically non-zero
                st.success("✅ **Reversal Successful!** The original form was perfectly restored. The transformation was invertible.")
            else:
                st.error("❌ **Reversal Failed!** The spell is irreversible. The space has been 'curdled' into a line or a point. Information is lost forever.")

    st.markdown("""
    **Observations from the Laboratory**

    Hopefully, you discovered the key insight for yourself!

    When the determinant is a healthy non-zero number (like 2.0, -1.5, etc.), the 'Transformed Lotus' is warped, but it's still a distinct shape with area. The transformed basis vectors point in different directions. And when you hit "Attempt to Reverse," it succeeds. This is our 'dissolved sugar' case. The information is all there.

    But what happens when you set the sliders to make the determinant zero? For example, try setting `a=1, b=1, c=1, d=1`. Or `a=1, b=2, c=2, d=4`.

    You see it, don't you? The moment the determinant hits zero, the entire 'Transformed Lotus' collapses into a single line. The transformed basis vectors, `î` and `ĵ`, suddenly point in the exact same (or opposite) direction. They are no longer independent; they are redundant.

    This is the geometric equivalent of making paneer. You have taken a 2D object with area and squashed it into a 1D line with zero area. All the points that were distinct in the original lotus are now smeared on top of each other along that line.

    And now, when you press "Attempt to Reverse," the system fails. How could it succeed? If all the points are on one line, how would the reverse spell know where to put them back in 2D space? Should a point on the line go up or down? Left or right? The information is simply gone. The transformation is **singular**.
    """)

    # ---------------------------------------------------------------------
    # PART 3: THE GALLERY (SHOWCASING VARIETY)
    # ---------------------------------------------------------------------
    st.subheader("Part 3: The Gallery of Irreversible Spells", divider="grey")
    st.markdown("""
    A determinant of zero is the mark of an irreversible spell, but these spells come in different flavors. Let's look at a few classic examples of these 'singular' transformations. Each one collapses space, but in its own unique style.
    """)

    tab1, tab2, tab3 = st.tabs(["**The Great Collapse**", "**The Redundant Message**", "**The Annihilator**"])

    with tab1:
        st.markdown("""
        #### The Great Collapse (Projection onto an Axis)
        **Matrix:** `[[1, 1], [0, 0]]`

        This transformation takes every point `(x, y)` and maps it to `(x+y, 0)`. Notice that the y-coordinate is always zero. Everything in our 2D world is flattened onto the horizontal x-axis.

        **The Sub-Analogy: Shadow Puppetry**
        Think of the beautiful shadow puppet traditions of India, like *Togalu Gombeyaata* from Karnataka. Intricate, three-dimensional leather puppets are manipulated behind a screen, but what we see is their two-dimensional shadow. The transformation from puppet to shadow is a projection. It's a beautiful art form, but information is lost. You cannot tell the exact color or thickness of the puppet just by looking at its flat, black shadow. Space has been collapsed from 3D to 2D. Our matrix does the same, collapsing 2D to 1D.
        """)
        image_search_button("Togalu Gombeyaata shadow puppets", "Togalu Gombeyaata")
        st.code("""
# This transformation squashes everything onto the x-axis.
A = [[1, 1],
     [0, 0]]

# Determinant = (1*0) - (1*0) = 0. Irreversible!
        """)


    with tab2:
        st.markdown("""
        #### The Redundant Message (Linearly Dependent Columns)
        **Matrix:** `[[1, 2], [2, 4]]`

        Look closely at the columns of this matrix. The second column, `[2, 4]`, is exactly two times the first column, `[1, 2]`. It doesn't provide any new directional information. The second basis vector is being sent to the exact same line as the first one, just further out. The result is that *all* vectors in the entire space are mapped onto the line `y = 2x`.

        **The Sub-Analogy: A Repetitive Edict**
        Imagine an ancient king carving an edict on a pillar. His first sentence declares, "All citizens must pay their taxes." His second sentence declares, "It is required for all people in the kingdom to remit their tax dues." The second sentence adds no new rule. It's redundant; it points in the same 'semantic direction' as the first. This is what a matrix with linearly dependent columns does. It doesn't give two independent directions to define a plane; it gives the same direction twice.
        """)
        image_search_button("Ashokan pillar edicts", "Ashoka pillar edict sarnath")
        st.code("""
# The second column is 2 * the first column.
A = [[1, 2],
     [2, 4]]

# Determinant = (1*4) - (2*2) = 0. Irreversible!
        """)

    with tab3:
        st.markdown("""
        #### The Annihilator (The Zero Matrix)
        **Matrix:** `[[0, 0], [0, 0]]`

        This is the most extreme collapse of all. This matrix takes every single point in the plane, no matter where it is, and maps it to the single point `(0, 0)`—the origin. The entire universe of our 2D space is crushed into a single, infinitesimal point.

        **The Sub-Analogy: Pralaya**
        In Hindu cosmology, *Pralaya* is the period of cosmic dissolution, where the entire universe dissolves into a single, formless, undifferentiated state, ready for the next cycle of creation. The Zero Matrix is the mathematical *Pralaya*. It takes all the rich diversity of vector space—all the shapes, lines, and points—and reduces it to the ultimate singularity: the origin. Reversal is utterly impossible. From that single point, how could you possibly know what the universe looked like before?
        """)
        image_search_button("Artistic depiction of Cosmic Dissolution", "pralaya cosmic dissolution art")
        st.code("""
# Every point becomes the origin.
A = [[0, 0],
     [0, 0]]

# Determinant = (0*0) - (0*0) = 0. The ultimate irreversible spell.
        """)

    # ---------------------------------------------------------------------
    # PART 4: THE FORMALIZATION (THE GANITA SHASTRA)
    # ---------------------------------------------------------------------
    st.subheader("Part 4: The Ganita Shastra - The Dharma of Reversibility", divider="grey")
    st.markdown("""
    We have felt the curdling of space and seen its different forms. Now, let us give this intuition the rigorous and beautiful language of mathematics, the *Ganita Shastra*. Let's establish the laws, the *Dharma*, that govern this concept.

    #### The Key Terminology
    - **Invertible Matrix:** A square matrix **A** is called **invertible** (or **non-singular**) if there exists another matrix, called its **inverse**, which can undo the transformation of **A**. This is only possible if **det(A) ≠ 0**.
    - **Singular Matrix:** A square matrix **A** is called **singular** (or **non-invertible**) if it cannot be undone. This occurs when **det(A) = 0**.

    #### The Inverse Matrix: A⁻¹
    The 'undo' spell for an invertible matrix **A** is its inverse, written as **A⁻¹**.

    What does it do? It's simple: applying a transformation and then its inverse gets you right back where you started.

    In the language of matrices, "where you started" is represented by the **Identity Matrix (I)**. The identity matrix is the "do-nothing" transformation.
    """)
    st.latex(r'''
    I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
    ''')
    st.markdown("""
    It leaves every vector exactly as it was. So, the defining property, the *dharma* of the inverse, is:
    """)
    st.latex(r'''
    A \cdot A^{-1} = A^{-1} \cdot A = I
    ''')

    st.markdown("""
    #### The Formula for the 2x2 Inverse
    For a 2x2 matrix, there is a beautiful and simple formula to find its inverse. If our matrix **A** is:
    """)
    st.latex(r'''
    A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
    ''')
    st.markdown("""
    Then its inverse, **A⁻¹**, is:
    """)
    st.latex(r'''
    A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix} = \frac{1}{ad-bc} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}
    ''')
    st.markdown("""
    Look at this formula closely! It's magnificent. It contains the whole story.

    Notice the term `1 / det(A)` right at the front. What happens if the determinant, `ad-bc`, is zero? You would be dividing by zero! This is a mathematical impossibility, a sign from the universe that what you are trying to do is forbidden. The formula itself breaks down and tells you, "No inverse exists!"

    This formula is the mathematical proof of our *paneer* analogy. The ability to find a reverse spell is fundamentally dependent on the determinant being non-zero.

    #### Calculation in Action
    Let's use the matrix from our interactive widget. The current state of your matrix is:
    """)
    st.code(f"""
# Your current matrix from the widget above
A = {np.array2string(matrix, precision=2)}

# The determinant is:
det_A = {det:.4f}
    """)

    st.markdown("Let's see this in Python with the NumPy library, the workhorse of scientific computing in India and beyond.")
    st.code("""
import numpy as np

# Let's define an invertible matrix
A = np.array([[2, 1],
              [1, 3]])

# 1. Calculate the determinant
det_A = np.linalg.det(A)
# det_A is (2*3 - 1*1) = 5. It's non-zero, so an inverse must exist!

# 2. Calculate the inverse
A_inv = np.linalg.inv(A)

# 3. Verify the Dharma: A @ A_inv should be the Identity matrix
I = A @ A_inv

# The '@' symbol in NumPy means matrix multiplication.
# Let's print the results...
    """, language='python')
    A_py = np.array([[2, 1], [1, 3]])
    det_A_py = np.linalg.det(A_py)
    A_inv_py = np.linalg.inv(A_py)
    I_py = A_py @ A_inv_py
    st.write("Result of `det_A`:")
    st.metric("Determinant", f"{det_A_py:.2f}")
    st.write("Result of `A_inv`:")
    st.code(np.array2string(A_inv_py, precision=4))
    st.write("Result of `A @ A_inv`:")
    st.code(np.array2string(I_py, precision=4))
    st.markdown("As you can see, the result is the Identity matrix (give or take some tiny floating-point inaccuracies). The spell was successfully reversed.")

    st.markdown("""
    #### The Bedrock of Solving Equations
    Why is this one concept so incredibly important? Because it is the foundation for solving systems of linear equations.

    A system like:
    `2x + y = 5`
    `x + 3y = 8`

    Can be written in matrix form as **Ax = b**:
    """)
    st.latex(r'''
    \begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 5 \\ 8 \end{bmatrix}
    ''')
    st.markdown("""
    If we want to find the solution vector **x**, and the matrix **A** is invertible, we can use the inverse as our ultimate problem-solving tool. Just multiply both sides by **A⁻¹**:
    """)
    st.latex(r'''
    A^{-1} A x = A^{-1} b \\
    I x = A^{-1} b \\
    x = A^{-1} b
    ''')
    st.markdown("""
    A non-zero determinant tells us there is **one unique solution**. A zero determinant tells us there is either **no solution** or **infinitely many solutions**. It means our equations are either contradictory or redundant. Invertibility means clarity and certainty. Singularity means ambiguity and confusion.
    """)

    # ---------------------------------------------------------------------
    # PART 5: THE APPLICATION (THE GAMES & PUZZLES)
    # ---------------------------------------------------------------------
    st.subheader("Part 5: The Jnana-Chakshu - Trials of Reversal", divider="grey")
    st.markdown("""
    Knowledge truly becomes wisdom when it is applied. Let's test your newfound understanding with a series of challenges. Each game will place you in a scenario where the concept of invertibility is key.
    """)

    game1, game2, game3 = st.tabs(["**Game 1: The Weaver's Dilemma**", "**Game 2: ISRO's Trajectory Correction**", "**Game 3: The Cryptographer's Challenge**"])

    with game1:
        st.markdown("""
        #### The Weaver's Dilemma
        You are an artisan in Jaipur, famous for your intricate block-printed textiles. You have a machine that applies geometric transformations to a base pattern. Today, you've been given a set of new transformation matrices by a new intern.

        **Your Task:** Your master weaver has warned you that using a **singular** matrix will jam the loom, stretching the fabric into a useless line and ruining the expensive silk. You must inspect each matrix, calculate its determinant, and only approve the ones that are **invertible**.

        For each matrix below, decide if it is 'Safe' (Invertible) or 'Dangerous' (Singular).
        """)

        matrices = {
            "Matrix 1": {"matrix": np.array([[3, 1], [4, 2]]), "answer": "Safe"},
            "Matrix 2": {"matrix": np.array([[2, 3], [4, 6]]), "answer": "Dangerous"},
            "Matrix 3": {"matrix": np.array([[-1, 1.5], [2, -3]]), "answer": "Dangerous"},
            "Matrix 4": {"matrix": np.array([[0, 1], [1, 0]]), "answer": "Safe"}
        }

        for name, data in matrices.items():
            st.markdown(f"---")
            st.markdown(f"**{name}**")
            st.latex(f"{data['matrix']}")
            det_val = np.linalg.det(data['matrix'])
            user_choice = st.radio("Is this matrix Safe or Dangerous?", ("Safe (Invertible)", "Dangerous (Singular)"), key=f"q1_{name}", index=None)

            if user_choice:
                correct_choice = "Safe (Invertible)" if data['answer'] == "Safe" else "Dangerous (Singular)"
                if user_choice == correct_choice:
                    st.success(f"Correct! The determinant is {det_val:.1f}. This matrix is {data['answer']}.")
                else:
                    st.error(f"Incorrect. The determinant is {det_val:.1f}. This matrix is {data['answer']}.")


    with game2:
        st.markdown("""
        #### ISRO's Trajectory Correction
        You are a mission controller at ISRO. A remote sensing satellite, Cartosat-4, has just performed a maneuvering burn. The burn was supposed to be transformation **A**, but due to a software glitch, it performed transformation **G** instead. The satellite is now in the wrong orientation!

        **Your Task:** You must calculate the **inverse** of the faulty transformation **G** (we'll call it **G⁻¹**) and apply it to bring the satellite back to its correct, pre-glitch orientation.

        The faulty transformation matrix **G** was:
        """)
        G = np.array([[0.8, 0.6], [-0.6, 0.8]])
        st.latex(r''' G = \begin{bmatrix} 0.8 & 0.6 \\ -0.6 & 0.8 \end{bmatrix} ''')
        st.markdown("First, is this even possible? What is the determinant of G?")

        det_G = np.linalg.det(G)
        st.info(f"The determinant of G is (0.8 * 0.8) - (0.6 * -0.6) = 0.64 + 0.36 = **{det_G:.1f}**. It's non-zero, so we can reverse it! Phew.")

        st.markdown("Now, using the formula `A⁻¹ = (1/det(A)) * [[d, -b], [-c, a]]`, find the inverse matrix **G⁻¹**.")

        user_g_inv = np.zeros((2, 2))
        c1, c2 = st.columns(2)
        user_g_inv[0, 0] = c1.number_input("Element [0,0]", key="g00", value=0.0)
        user_g_inv[0, 1] = c1.number_input("Element [0,1]", key="g01", value=0.0)
        user_g_inv[1, 0] = c2.number_input("Element [1,0]", key="g10", value=0.0)
        user_g_inv[1, 1] = c2.number_input("Element [1,1]", key="g11", value=0.0)

        if st.button("Transmit Correction Matrix", use_container_width=True):
            G_inv = np.linalg.inv(G)
            if np.allclose(user_g_inv, G_inv):
                st.success("🛰️ **Correction Successful!** You transmitted the correct inverse matrix. The satellite is back on its nominal orientation. Well done, controller!")
                st.code(f"Correct Inverse:\n{np.array2string(G_inv, precision=2)}")
            else:
                st.error("🚨 **Correction Failed!** That is not the correct inverse matrix. The satellite is still adrift. Check your calculations!")
                st.code(f"Your Input:\n{np.array2string(user_g_inv, precision=2)}\nCorrect Inverse:\n{np.array2string(G_inv, precision=2)}")

    with game3:
        st.markdown("""
        #### The Cryptographer's Challenge
        You have intercepted an encoded message. Your intelligence suggests it was encoded using a simple matrix cipher. Each pair of letters was converted to numbers (A=1, B=2, ...), formed into a vector, and then multiplied by a 2x2 encoding matrix **E**.

        **Your Task:** You have the encoding matrix **E** and the list of encoded vectors. Find the inverse of **E** and apply it to each vector to decode the secret message.

        **Encoding Matrix (E):**
        """)
        E = np.array([[2, 3], [1, 2]])
        st.latex(r''' E = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix} ''')
        st.markdown("**Encoded Vectors:**")
        encoded_vectors = [np.array([53, 31]), np.array([48, 29]), np.array([61, 37])]
        st.code(f"Vector 1: {encoded_vectors[0]}\nVector 2: {encoded_vectors[1]}\nVector 3: {encoded_vectors[2]}")

        st.markdown("First, find the inverse of **E**. Let's call it **D** (for Decryption matrix).")

        if 'decryption_matrix' not in st.session_state:
            st.session_state.decryption_matrix = "[]"

        user_d_str = st.text_input("Enter the decryption matrix D in Python format (e.g., [[a, b], [c, d]])", value=st.session_state.decryption_matrix)

        if st.button("Decrypt Message", use_container_width=True):
            st.session_state.decryption_matrix = user_d_str
            try:
                user_d_matrix = np.array(eval(user_d_str))
                E_inv = np.linalg.inv(E)
                if np.allclose(user_d_matrix, E_inv):
                    st.success("Correct Decryption Matrix! Applying it to the vectors...")
                    time.sleep(1)
                    decoded_message = ""
                    alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    for vec in encoded_vectors:
                        decoded_vec = np.round(E_inv @ vec).astype(int)
                        decoded_message += alphabet[decoded_vec[0]]
                        decoded_message += alphabet[decoded_vec[1]]
                    st.balloons()
                    st.header(f"The decoded message is: **{decoded_message}**")

                else:
                    st.error("That is not the correct inverse matrix. The message remains gibberish.")
            except:
                st.error("Invalid matrix format. Please use the format [[a, b], [c, d]].")


    # ---------------------------------------------------------------------
    # PART 6: THE HORIZON (THE JNANA-CHAKSHU - EYE OF KNOWLEDGE)
    # ---------------------------------------------------------------------
    st.subheader("Part 6: The Horizon - The Gatekeeper of Information", divider="grey")
    st.markdown("""
    We have come far. We started in a kitchen with milk and lemon and ended by decrypting secret messages. Through this journey, a profound truth has revealed itself.

    > **The Jnana-Chakshu (The Eye of Knowledge):** The determinant is the ultimate gatekeeper of information in a linear transformation. A non-zero determinant means that all information about the original space is preserved, rearranged but recoverable. A zero determinant means that information has been permanently destroyed.

    This isn't just an abstract mathematical idea. This principle of invertibility and information preservation is a cornerstone of modern science and technology, running like a hidden thread through many fields.

    - **Computer Graphics & VFX:** When an animator in a studio in Bengaluru or Hyderabad rotates, scales, and moves a 3D model of a character, the software uses invertible matrices. This ensures that the 'undo' button works perfectly. If they used a singular matrix, the 3D model could be flattened into a 2D plane, and there would be no way to recover the original 3D shape, potentially losing hours of work.

    - **Robotics and Automation:** A robotic arm moving parts in a factory is controlled by matrices that transform its desired position into joint angles. These matrices must be invertible to ensure that for any position the hand needs to be in, there's a clear, unique set of instructions for the robot's motors. A singular matrix would mean certain positions are unreachable or have ambiguous instructions, leading to a breakdown.

    - **Data Science & Machine Learning:** In many advanced techniques, data scientists need to "un-correlate" their data or change their frame of reference. This is done using matrix transformations. They must ensure these transformations are invertible, otherwise, the process could destroy the very patterns they are trying to analyze.

    Understanding invertibility gives you a new lens through which to see the world—a lens that distinguishes between reversible changes and irreversible collapses.

    #### The Next Step on Our Journey...
    We have seen that a matrix transforms vectors. We have seen that this transformation has a 'scale factor'—the determinant. And we have seen that it can be reversed if this factor is not zero.

    But there's a deeper secret to these transformations. Within the chaos of stretching and shearing, are there some vectors that remain special? Are there directions that a transformation doesn't change, only stretches? Imagine a spinning wheel: everything is moving and blurring, but the axle at the center points in the same direction, merely spinning on itself. These special, 'un-rotating' vectors are the hidden skeleton of a matrix.

    In our next chapter, we will seek them out. We will uncover the **Eigenvectors and Eigenvalues**, the soul of the matrix.
    """)

    # ---------------------------------------------------------------------
    # PART 7: THE CHECK-UP (THE PARIKSHA)
    # ---------------------------------------------------------------------
    st.subheader("Part 7: The Pariksha - A Check of Your Understanding", divider="grey")
    st.markdown("Let's consolidate our new knowledge. Answer these questions to see how well you've grasped the concepts of this chapter.")

    questions = {
        "1. The 'making paneer' analogy was used to illustrate which concept?": {
            "options": ["A reversible transformation", "An irreversible (singular) transformation", "A rotation transformation", "The identity matrix"],
            "answer": "An irreversible (singular) transformation",
            "feedback": "Correct! Making paneer is a chemical change that collapses the milk into a new form, just like a singular matrix collapses space. Information is lost, and it cannot be undone."
        },
        "2. A square matrix A has an inverse, A⁻¹, if and only if...": {
            "options": ["The matrix contains only positive numbers", "The matrix is 2x2", "The determinant of A is zero", "The determinant of A is non-zero"],
            "answer": "The determinant of A is non-zero",
            "feedback": "Exactly! A non-zero determinant is the fundamental condition for a matrix to be invertible. It signifies that no information was lost in the transformation."
        },
        "3. Geometrically, what does a singular transformation (det(A)=0) do to a 2D space?": {
            "options": ["It always expands the space", "It rotates the space by 90 degrees", "It collapses the space into a line or a single point", "It reflects the space across the y-axis"],
            "answer": "It collapses the space into a line or a single point",
            "feedback": "Perfect. A zero determinant means the area of the transformed unit square is zero, which happens when the 2D plane is squashed down into a 1D line or a 0D point."
        },
        "4. If A is an invertible matrix and I is the identity matrix, what is the result of A multiplied by its inverse, A⁻¹?": {
            "options": ["The zero matrix", "The identity matrix (I)", "A squared (A²)", "A number (the determinant)"],
            "answer": "The identity matrix (I)",
            "feedback": "Correct. This is the defining property of the inverse. Applying a transformation and then its inverse is the same as doing nothing (the identity transformation)."
        },
        "5. You are trying to solve a system of linear equations Ax = b. You calculate the determinant of the coefficient matrix A and find that it is zero. What does this tell you about the solution?": {
            "options": ["There is exactly one unique solution", "There is either no solution or infinitely many solutions", "The solution is x=0", "You need a bigger computer to solve it"],
            "answer": "There is either no solution or infinitely many solutions",
            "feedback": "Precisely. A singular matrix means the equations are either redundant (infinite solutions) or contradictory (no solution). There is no single, unique answer."
        }
    }

    for i, (q, data) in enumerate(questions.items()):
        st.markdown(f"---")
        st.markdown(f"**Question {i+1}: {q}**")
        user_ans = st.radio("Select your answer:", data["options"], key=f"pariksha_{i}", index=None)
        if user_ans:
            if user_ans == data["answer"]:
                st.success(f"**Correct!** {data['feedback']}")
            else:
                st.error(f"**Not quite.** The correct answer is '{data['answer']}'. Why? {data['feedback']}")