# chapters/chapter_1.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from utils.plotting import plot_vectors, setup_plot

def render():
    """
    Renders a completely revised Chapter 1, designed with the Feynman technique in mind.
    It uses storytelling, simple analogies, and interactive games to build intuition.
    """

    st.header("Chapter 1: A Map, A Bridge, and a Shortcut 🧭")

    # --- 1. THE CORE IDEA (A TREASURE MAP) ---
    st.markdown("""
    Forget everything you *think* you know about vectors. Let's start with something simpler: a treasure map.

    Imagine a pirate gives you an instruction: **"From the old oak tree, go 4 paces East, then 3 paces North."**
    """)
    
    col1, col2 = st.columns([1, 1.2])

    with col1:
        st.markdown("""
        That single instruction—which has both a **distance** and a **direction**—is the secret behind our first big idea. It's a complete package. It tells you exactly where to go.
        
        That's it. That's the core concept.
        
        Mathematicians, being fans of fancy words, call this special type of instruction a **vector**.
        
        So, a vector isn't a scary thing. It's just a pirate's instruction.
        """)
        st.info("💡 **Aha! Moment:** A vector is just an instruction with a magnitude (how far) and a direction (which way).")

    with col2:
        fig, ax = plt.subplots()
        ax.quiver(0, 0, 4, 3, angles='xy', scale_units='xy', scale=1, color='brown', label='The Pirate\'s Instruction')
        ax.scatter(0, 0, color='green', s=150, zorder=3, marker='P', label='Old Oak Tree')
        ax.scatter(4, 3, color='gold', s=150, zorder=3, marker='X', label='Treasure!')
        setup_plot(ax, "The Treasure Map", xlim=(-1, 6), ylim=(-1, 6))
        ax.legend()
        st.pyplot(fig)
    
    st.divider()

    # --- 2. A COMPLICATION (THE WOBBLY BRIDGE) ---
    st.subheader("The Adventure Gets Complicated...")
    st.markdown("""
    Okay, you follow the instruction. But to get there, you have to cross a wobbly rope bridge over a river. As you walk across, the bridge itself is being pushed sideways by a strong wind!

    So now you have **two instructions** happening at the same time:
    1.  **Your walking instruction** (where you *try* to go).
    2.  **The wind's push instruction** (where the bridge *drags* you).

    Where do you actually end up? Let's find out! Use the sliders to change your walk and the wind's push. The green arrow shows your **actual path**—the shortcut from start to finish.
    """)

    col3, col4 = st.columns([1, 1.2])

    with col3:
        st.markdown("##### Your Controls")
        walk_x = st.slider("Your Walk (East/West)", -5.0, 5.0, 4.0, 0.1, key="c1_walk_x")
        walk_y = st.slider("Your Walk (North/South)", -5.0, 5.0, 3.0, 0.1, key="c1_walk_y")
        wind_x = st.slider("Wind's Push (East/West)", -5.0, 5.0, 1.0, 0.1, key="c1_wind_x")
        wind_y = st.slider("Wind's Push (North/South)", -5.0, 5.0, -2.0, 0.1, key="c1_wind_y")

        v_walk = np.array([walk_x, walk_y])
        v_wind = np.array([wind_x, wind_y])
        v_result = v_walk + v_wind

        st.success(f"**Your final path (the 'shortcut' vector):** `[{v_result[0]:.1f}, {v_result[1]:.1f}]`")

    with col4:
        fig2, ax2 = plt.subplots()
        # Plot the "head-to-tail" addition
        ax2.quiver(v_walk[0], v_walk[1], v_wind[0], v_wind[1], angles='xy', scale_units='xy', scale=1, color='cyan', linestyle='dashed')
        
        plot_vectors(
            [v_walk, v_wind, v_result],
            ['blue', 'cyan', 'green'],
            ax2,
            labels=['Your Walk', 'Wind\'s Push', 'Actual Path (Resultant)']
        )
        setup_plot(ax2, "Your Walk + Wind's Push", xlim=(-8, 8), ylim=(-8, 8))
        ax2.legend()
        st.pyplot(fig2)

    st.divider()

    # --- 3. FROM PICTURES TO NUMBERS ---
    st.subheader("Talking to the Machine: The Language of Vectors")
    st.markdown("""
    Drawing arrows is great for our brains, but computers prefer numbers. So, we translate our pirate instructions into a simple code: `[East/West, North/South]`.

    - `Your Walk: [4, 3]` means "4 East, 3 North."
    - `Wind's Push: [1, -2]` means "1 East, 2 South."

    And here’s the most beautiful part. To find the final path, you just add the numbers!
    
    - **East/West parts:** `4 + 1 = 5`
    - **North/South parts:** `3 + (-2) = 1`
    - **Resulting Path:** `[5, 1]`

    This is called **vector addition**. You just add the corresponding components. Try it yourself with the calculator below!
    """)
    
    col5, col6 = st.columns(2)
    with col5:
        st.markdown("##### Vector Calculator")
        c_v1_x = st.number_input("Vector 1: X", value=2.0, key="c1_calc1x")
        c_v1_y = st.number_input("Vector 1: Y", value=3.0, key="c1_calc1y")
    with col6:
        st.markdown("➕") # Just for visual spacing
        c_v2_x = st.number_input("Vector 2: X", value=1.0, key="c1_calc2x")
        c_v2_y = st.number_input("Vector 2: Y", value=-1.0, key="c1_calc2y")

    sum_x = c_v1_x + c_v2_x
    sum_y = c_v1_y + c_v2_y
    st.latex(f"[{c_v1_x}, {c_v1_y}] + [{c_v2_x}, {c_v2_y}] = [{sum_x}, {sum_y}]")

    st.divider()

    # --- 4. THE GAME (VECTOR LANDER) ---
    st.subheader("Game Time: Vector Lander 🚀")
    st.markdown("""
    You're the pilot of a spaceship. Your mission is to land on the red target planet.
    
    **The Catch:** You're flying through an asteroid field that constantly pushes your ship (the **blue vector**). You only control your engine's **boost** (the **orange vector**).
    
    Your ship's final path will be the **SUM** of the asteroid push and your engine boost. Can you choose the right boost to land on the target?
    """)
    
    # Initialize game state
    if 'vl_target' not in st.session_state:
        st.session_state.vl_target = np.random.uniform(-4, 4, 2)
        st.session_state.vl_asteroid = np.random.uniform(-2, 2, 2)
        st.session_state.vl_attempts = 0
        st.session_state.vl_won = False

    if st.button("Generate New Target & Asteroid Field"):
        st.session_state.vl_target = np.random.uniform(-4, 4, 2)
        st.session_state.vl_asteroid = np.random.uniform(-2, 2, 2)
        st.session_state.vl_attempts = 0
        st.session_state.vl_won = False
        st.rerun()

    game_col1, game_col2 = st.columns([1, 1.2])

    with game_col1:
        st.markdown("##### Pilot Controls")
        boost_x = st.slider("Engine Boost (Left/Right)", -5.0, 5.0, 0.0, 0.1, key="c1_boost_x")
        boost_y = st.slider("Engine Boost (Up/Down)", -5.0, 5.0, 0.0, 0.1, key="c1_boost_y")
        
        v_boost = np.array([boost_x, boost_y])
        v_asteroid = st.session_state.vl_asteroid
        v_final_path = v_boost + v_asteroid
        
        st.info(f"Asteroid Push: `[{v_asteroid[0]:.1f}, {v_asteroid[1]:.1f}]`")
        st.warning(f"Your Boost: `[{v_boost[0]:.1f}, {v_boost[1]:.1f}]`")
        st.success(f"Resulting Path: `[{v_final_path[0]:.1f}, {v_final_path[1]:.1f}]`")
        
        st.write(f"Attempts: {st.session_state.vl_attempts}")
        
        if st.button("🚀 LAUNCH!"):
            st.session_state.vl_attempts += 1
            distance = np.linalg.norm(v_final_path - st.session_state.vl_target)
            if distance < 0.25: # Win radius
                st.session_state.vl_won = True
            else:
                st.session_state.vl_won = False

    with game_col2:
        fig3, ax3 = plt.subplots()
        plot_vectors(
            [v_asteroid, v_boost, v_final_path],
            ['blue', 'orange', 'green'],
            ax3,
            labels=['Asteroid Push', 'Your Boost', 'Final Path']
        )
        ax3.scatter(st.session_state.vl_target[0], st.session_state.vl_target[1], color='red', s=200, zorder=3, marker='*', label='Target Planet')
        setup_plot(ax3, "Vector Lander Mission", xlim=(-5, 5), ylim=(-5, 5))
        ax3.legend()
        st.pyplot(fig3)

    if st.session_state.vl_won:
        st.balloons()
        st.success(f"**TOUCHDOWN!** You landed the ship in {st.session_state.vl_attempts} attempts! You've mastered vector addition!")

    st.divider()

    # --- 5. WHAT'S NEXT? (NEW SECTION) ---
    st.subheader("Your Journey Has Just Begun... ✨")
    st.markdown("""
    Congratulations, Explorer! You've mastered the first fundamental secret of this universe: **any number of 'instructions' can be combined into a single, final instruction.** This is the essence of vector addition.
    
    You might be thinking, "Cool, I can add arrows. So what?"
    
    Well, you've just unlocked the language to describe...
    - 🎮 **Physics in Video Games:** How does a character jump while moving forward? It's a `jump_vector + move_vector`! How does a rocket steer in space? `thrust_vector + gravity_vector`.
    - 🎨 **Computer Graphics:** How does a 3D model get rotated or scaled on your screen? Every point (vertex) on the model is a vector, and these vectors are being manipulated.
    - 🤖 **Machine Learning:** How does an algorithm group similar data points? It often treats data as vectors in a high-dimensional space and measures the "distance" and "direction" between them.

    The next question is even more exciting: What if we could build a *machine* that transforms **every single vector** in the universe all at once, in a predictable way? A machine that could stretch, shrink, or rotate the very fabric of space?
    
    Such a machine exists. It's called a **Matrix**, and it's what we'll explore in **Chapter 2**.
    """)

    st.divider()
    
    # --- 6. KNOWLEDGE CHECK ---
    st.subheader("Check Your Bearings 🧠")
    
    st.markdown("**Question 1:** What two things does a vector always have?")
    q1_ans = st.radio("Select the best answer:", ["X and Y components", "A start and an end point", "Magnitude and Direction"], key="c1_q1", index=None)
    if st.button("Check Q1"):
        if q1_ans == "Magnitude and Direction":
            st.success("Correct! That's the fundamental definition. The components are just one way to *describe* them.")
        else:
            st.error("Good try, but not the most fundamental answer. 'Magnitude and Direction' is the core concept.")

    st.markdown("**Question 2:** A bird is flying North at 3 km/h. A strong wind is blowing East at 4 km/h. What is the bird's actual ground path represented as a vector `[East, North]`?")
    q2_ans = st.radio("Select the correct vector:", ["`[3, 4]`", "`[4, 3]`", "`[0, 3]`", "`[4, 0]`"], key="c1_q2", index=None)
    if st.button("Check Q2"):
        if q2_ans == "`[4, 3]`":
            st.success("Exactly! The Eastward movement (4) is the first component, and the Northward movement (3) is the second.")
        else:
            st.error("Not quite. Remember the format is `[East/West, North/South]`. The wind is the East component.")