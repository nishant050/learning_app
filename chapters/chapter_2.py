# chapters/chapter_2.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from utils.plotting import setup_plot
import urllib.parse

# --- HELPER FUNCTIONS ---

def image_search_button(label, search_term):
    """Creates a Streamlit link button that searches Google Images in a new tab."""
    encoded_term = urllib.parse.quote_plus(search_term)
    url = f"https://www.google.com/search?q={encoded_term}&tbm=isch"
    st.link_button(f"🖼️ See examples of: {label}", url, use_container_width=True)

def plot_warped_grid(ax, T, grid_range=10):
    """Helper function to plot the transformed grid lines."""
    for i in range(-grid_range, grid_range + 1):
        p1 = T @ np.array([i, -grid_range]); p2 = T @ np.array([i, grid_range])
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='gray', linestyle='--', linewidth=0.5, zorder=0)
    for i in range(-grid_range, grid_range + 1):
        p1 = T @ np.array([-grid_range, i]); p2 = T @ np.array([grid_range, i])
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='gray', linestyle='--', linewidth=0.5, zorder=0)

# --- MAIN RENDER FUNCTION ---

def render():
    st.header("Chapter 2: The Cosmic Warp Field 🌀")

    # --- 1. THE CORE IDEA (THE ANALOGY) ---
    st.markdown("""
    In the last chapter, we learned that vectors are like instructions. Now, imagine we stumble upon a strange cosmic anomaly: a **Warp Field**. This field distorts the very fabric of space itself. Everything changes in a consistent, predictable way.
    """)
    st.info("💡 **Aha! Moment:** Instead of changing one vector, what if we could apply a rule that changes *all* vectors in the universe at once?")
    st.divider()

    # --- 2. THE MECHANISM (INTERACTIVE DISCOVERY) ---
    st.subheader("Interactive Discovery: Steering the Universe")
    st.markdown("""
    To control the Warp Field, we only need to "steer" the two fundamental directions of space: **East** (`[1, 0]`) and **North** (`[0, 1]`).
    
    Instead of sliders, let's use a more intuitive control panel. For each fundamental direction, you will set its new **Angle** and **Magnitude (Length)**.
    """)

    # Initialize session state for our new controls
    if 'c2_ang_i' not in st.session_state:
        st.session_state.c2_ang_i = 0.0
        st.session_state.c2_mag_i = 1.0
        st.session_state.c2_ang_j = 90.0
        st.session_state.c2_mag_j = 1.0

    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("##### Warp Control Panel")
        with st.container(border=True):
            st.markdown("**1. New 'East' Vector Controls**")
            # We get the value from session state, which allows buttons to update it
            ang_i = st.slider("Angle (degrees)", 0.0, 360.0, st.session_state.c2_ang_i, 1.0, key="c2_sl_ang_i")
            mag_i = st.slider("Magnitude (Length)", 0.0, 2.5, st.session_state.c2_mag_i, 0.1, key="c2_sl_mag_i")
            # Update session state with the latest slider values
            st.session_state.c2_ang_i, st.session_state.c2_mag_i = ang_i, mag_i

        with st.container(border=True):
            st.markdown("**2. New 'North' Vector Controls**")
            ang_j = st.slider("Angle (degrees)", 0.0, 360.0, st.session_state.c2_ang_j, 1.0, key="c2_sl_ang_j")
            mag_j = st.slider("Magnitude (Length)", 0.0, 2.5, st.session_state.c2_mag_j, 0.1, key="c2_sl_mag_j")
            st.session_state.c2_ang_j, st.session_state.c2_mag_j = ang_j, mag_j

    # Convert our intuitive Angle/Magnitude controls to Cartesian (x,y) coordinates for the matrix
    rad_i = np.deg2rad(ang_i)
    new_i = np.array([mag_i * np.cos(rad_i), mag_i * np.sin(rad_i)])
    
    rad_j = np.deg2rad(ang_j)
    new_j = np.array([mag_j * np.cos(rad_j), mag_j * np.sin(rad_j)])
    
    T = np.array([new_i, new_j]).T # Each vector is a column

    with col2:
        house_points = np.array([[0,0], [0,2], [1.5, 3], [3,2], [3,0], [0,0], [1,0], [1,1], [2,1], [2,0]]).T
        transformed_house = T @ house_points
        fig, ax = plt.subplots(figsize=(8, 8))
        
        plot_warped_grid(ax, T)
        ax.plot(house_points[0, :6], house_points[1, :6], 'b-', label='Original House', alpha=0.3)
        ax.plot(house_points[0, 6:], house_points[1, 6:], 'b-', alpha=0.3)
        ax.plot(transformed_house[0, :6], transformed_house[1, :6], 'r-', label='Warped House', linewidth=2)
        ax.plot(transformed_house[0, 6:], transformed_house[1, 6:], 'r-', linewidth=2)
        
        # ERROR FIX: Removed the buggy `linestyle='--'` from the quiver calls. `alpha` is enough.
        ax.quiver(0, 0, 1, 0, color='orange', angles='xy', scale_units='xy', scale=1, alpha=0.3, label="Original 'East'")
        ax.quiver(0, 0, 0, 1, color='green', angles='xy', scale_units='xy', scale=1, alpha=0.3, label="Original 'North'")
        ax.quiver(0, 0, new_i[0], new_i[1], color='orange', angles='xy', scale_units='xy', scale=1, label="New 'East'")
        ax.quiver(0, 0, new_j[0], new_j[1], color='green', angles='xy', scale_units='xy', scale=1, label="New 'North'")
        
        setup_plot(ax, "Warping the Fabric of Space", xlim=(-4, 4), ylim=(-4, 4))
        ax.legend()
        st.pyplot(fig)
    st.divider()

    # --- 3. THE GALLERY (PRESETS & EXPLORATION) ---
    st.subheader("Gallery of Famous Transformations")
    st.markdown("See standard transformations in action! Click a preset button to configure the Warp Field, then see what happens. You can also search for more examples.")
    
    # Define Preset Callbacks
    def set_preset(mag_i, ang_i, mag_j, ang_j):
        st.session_state.c2_mag_i = mag_i
        st.session_state.c2_ang_i = ang_i
        st.session_state.c2_mag_j = mag_j
        st.session_state.c2_ang_j = ang_j

    g_col1, g_col2, g_col3, g_col4 = st.columns(4)
    with g_col1:
        st.button("Rotate 90°", on_click=set_preset, args=(1.0, 90.0, 1.0, 180.0), use_container_width=True)
        image_search_button("Rotation", "rotation matrix transformation gif")
    with g_col2:
        st.button("Shear Right", on_click=set_preset, args=(1.0, 0.0, 1.41, 45.0), use_container_width=True)
        image_search_button("Shear", "shear matrix transformation gif")
    with g_col3:
        st.button("Scale x2", on_click=set_preset, args=(2.0, 0.0, 2.0, 90.0), use_container_width=True)
        image_search_button("Scale", "scale matrix transformation gif")
    with g_col4:
        st.button("Reflect Y-Axis", on_click=set_preset, args=(1.0, 180.0, 1.0, 90.0), use_container_width=True)
        image_search_button("Reflection", "reflection matrix transformation")
    st.divider()
    
    # --- 4. THE FORMALIZATION ---
    st.subheader("The Machine's Secret Code: The Matrix")
    st.markdown(f"The 'settings' for the Warp Field are stored in a **Matrix**. A matrix simply stores the destination vectors for 'East' and 'North' as its columns:")
    st.latex(f"T = \\begin{{bmatrix}} {T[0,0]:.2f} & {T[0,1]:.2f} \\\\ {T[1,0]:.2f} & {T[1,1]:.2f} \\end{{bmatrix}}")
    st.divider()

    # --- 5. THE APPLICATION (THE GAME) ---
    st.subheader("Game Time: Shape Shifter 👽")
    # (The rest of the chapter from the previous version remains largely the same and fits well)
    st.markdown("""
    An alien client has sent you a blueprint (the **Target Shape** in green). Configure the Warp Field using the **Angle/Magnitude** controls above to match their blueprint.
    """)
    if 'c2_target_matrix' not in st.session_state:
        st.session_state.c2_target_name = "Shear"
        st.session_state.c2_target_matrix = np.array([[1, 0.5], [0, 1]])
    
    targets = { "Shear": np.array([[1, 0.5], [0, 1]]), "Rotate 45°": np.array([[0.707, -0.707], [0.707, 0.707]]), "Reflect & Stretch": np.array([[-1, 0], [0, 1.5]]), "Squish": np.array([[2.0, 0.5], [0.5, 0.5]]) }
    def new_challenge():
        current_name = st.session_state.c2_target_name
        possible_names = [name for name in targets if name != current_name]
        new_name = np.random.choice(possible_names)
        st.session_state.c2_target_name = new_name
        st.session_state.c2_target_matrix = targets[new_name]

    st.button("Give Me a New Challenge!", on_click=new_challenge)
    st.info(f"Current Challenge: **{st.session_state.c2_target_name}**")
    
    target_matrix = st.session_state.c2_target_matrix
    target_house = target_matrix @ house_points

    fig_game, ax_game = plt.subplots()
    ax_game.plot(transformed_house[0, :6], transformed_house[1, :6], 'r-', label='Your Warped House', linewidth=3)
    ax_game.plot(transformed_house[0, 6:], transformed_house[1, 6:], 'r-', linewidth=3)
    ax_game.plot(target_house[0, :6], target_house[1, :6], 'g--', label='Target Shape', linewidth=2)
    ax_game.plot(target_house[0, 6:], target_house[1, 6:], 'g--', linewidth=2)
    setup_plot(ax_game, "Match the Target Shape!", xlim=(-4,4), ylim=(-4,4))
    ax_game.legend()
    st.pyplot(fig_game)
    
    if np.allclose(T, target_matrix, atol=0.1): # Looser tolerance for slider fun
        st.balloons(); st.success("Perfect Match! The client is pleased!")
    st.divider()

    # --- 6. & 7. HORIZON & QUIZ ---
    final_tab1, final_tab2 = st.tabs(["What's Next? ✨", "Knowledge Check 🧠"])
    with final_tab1:
        st.subheader("A Puzzling Question... 🤔")
        st.markdown("""Some transformations make the house **bigger**, while others make it **smaller**. Is there a single "magic number" that tells us *how much a matrix scales area*? There is. It's called the **Determinant**, and it's the secret we'll uncover in **Chapter 3**.""")
    with final_tab2:
        st.subheader("Check Your Bearings")
        st.markdown("**Question 1:** The most fundamental way to define a 2x2 matrix transformation is by knowing...")
        q1_ans = st.radio("", ["Its four numbers: a, b, c, and d.", "Where the vectors `[1,0]` and `[0,1]` land after the transformation.", "Whether it rotates or stretches things."], key="c2_q1", index=None)
        if "Where the vectors" in str(q1_ans): st.write("✅ Correct! The four numbers just store that essential information.")

        st.markdown("**Question 2:** A matrix is defined as `T = [[2, 0], [0, 2]]`. What effect will this have?")
        q2_ans = st.radio("", ["Rotation", "Shear", "Scale twice as large", "No effect"], key="c2_q2", index=None)
        if "Scale twice as large" in str(q2_ans): st.write("✅ Correct! The 'East' vector `[1,0]` goes to `[2,0]`, and 'North' `[0,1]` goes to `[0,2]`.")