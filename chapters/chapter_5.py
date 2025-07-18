# chapters/chapter_5.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import urllib.parse
import time

# ======================================================================================
# 3.3. Mandatory Helper Function & Best Practices
# This function should be in a shared file like `utils/helpers.py` as per the guide,
# but is included here for this self-contained example.
# ======================================================================================
def image_search_button(label, search_term):
    """Creates a Streamlit link button that searches Google Images in a new tab."""
    encoded_term = urllib.parse.quote_plus(search_term)
    url = f"https://www.google.com/search?q={encoded_term}&tbm=isch"
    st.link_button(f"🖼️ See images of: {label}", url, use_container_width=True)

# ======================================================================================
# 3.2. The render() Contract
# The entire chapter is encapsulated within this single function.
# ======================================================================================
def render():
    """
    Renders Chapter 5 of the Eigen-Verse Explorer, focusing on the application of
    Eigenvectors and Eigenvalues to population dynamics, following the Design Guide 3.1.
    """
    st.title("Chapter 5: Eigen-Destiny — The Oracle of Population 🔮")

    # ==================================================================================
    # Part 1: The Core Idea (The Analogy)
    # Goal: Build profound, culturally-grounded intuition using a powerful analogy.
    # ==================================================================================
    st.header("Part 1: The Analogy — Dharma and the Karmic Matrix", divider="rainbow")
    st.markdown("""
    In the grand theatre of the universe, every entity, from the smallest firefly to the largest star, follows a certain path, a certain law of being. The ancient seers of India called this **Dharma** (धर्म) — the intrinsic nature or the fundamental principle that governs existence. A population of living beings also has a Dharma: a natural, stable structure it tends to settle into. This is its **stable age distribution**.

    But what shapes this destiny? It is **Karma** (कर्म) — the law of cause and effect, the sum of actions that lead to future consequences. For a population, Karma is the set of rules that governs its life: birth rates, survival rates, the harshness of the environment. These rules, when applied year after year, determine the population's fate.

    In this chapter, we will see that the language of Linear Algebra provides a breathtakingly precise way to model this cosmic dance.
    
    *   The population's **Dharma**, its stable structure, is perfectly described by an **Eigenvector**.
    *   The laws of **Karma**, the rules of life and death, are encapsulated in a special **Matrix**.
    *   The ultimate outcome, the long-term growth or decline, is revealed by the **Eigenvalue**.

    Imagine the majestic tigers of the Ranthambore forest. Their population has an inherent rhythm. There is a natural balance of cubs, juveniles, and adults. This balance is their Dharma. The 'rules' of the forest—how many cubs are born to each tigress, how many cubs survive to adulthood, and how long adults live—are the Karma. By understanding these rules as a matrix, we can predict the future of the tiger population. We can become oracles, using the power of eigenvectors to foresee their destiny.
    """)
    image_search_button("Ranthambore Tigers", "ranthambore tigers")
    st.markdown("Let us now build the Karmic engine that drives this destiny.")
    st.info("💡 **Analogy Recap:**\n\n*   **The Matrix:** The rules of life (birth/survival rates). The *Karma*.\n*   **The Eigenvector:** The stable population structure. The *Dharma*.\n*   **The Eigenvalue:** The long-term growth/decay rate. The *Fruit of Karma*.")


    # ==================================================================================
    # Part 2: The Mechanism (Interactive Discovery)
    # Goal: Allow the user to "feel" the cause-and-effect relationship.
    # ==================================================================================
    st.header("Part 2: The Karmic Engine — An Interactive Simulation", divider="rainbow")
    st.markdown("""
    Here is our oracle. We will model a simple population of 'Young' and 'Adult' creatures. You control the laws of their universe. You set their Karma. Observe how the population evolves and, more importantly, watch as its internal structure (**the ratio of young to old**) magically converges to the predicted Dharma (the eigenvector).
    """)

    # Initialize session state for the simulation
    if 'c5_pop_history' not in st.session_state:
        st.session_state.c5_pop_history = []
        st.session_state.c5_initial_pop = np.array([20.0, 80.0]) # Start with an unbalanced population

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("The Rules of Life (Karma)")
        birth_rate = st.slider("Adult Birth Rate (new young per adult)", 0.0, 2.5, 0.8, 0.1, key="c5_br", help="How many young are born per adult each year?")
        survival_y = st.slider("Young Survival Rate (to become adult)", 0.0, 1.0, 0.5, 0.05, key="c5_sy", help="What percentage of young survive to become adults in the next year?")
        survival_a = st.slider("Adult Survival Rate (to stay adult)", 0.0, 1.0, 0.9, 0.05, key="c5_sa", help="What percentage of adults survive to the next year?")

        # This is a Leslie Matrix, a core concept in mathematical ecology
        L = np.array([[0, birth_rate], [survival_y, survival_a]])

        st.markdown("##### The Karmic Matrix (L):")
        st.latex(f"L = \\begin{{bmatrix}} 0 & {birth_rate:.2f} \\\\ {survival_y:.2f} & {survival_a:.2f} \\end{{bmatrix}}")

        eigenvalues, eigenvectors = np.linalg.eig(L)
        dominant_eigenvalue = np.max(np.real(eigenvalues))
        dominant_idx = np.argmax(np.real(eigenvalues))
        stable_dist_vec = np.real(eigenvectors[:, dominant_idx])
        
        # Ensure the eigenvector components are positive for interpretation
        stable_dist_vec = np.abs(stable_dist_vec)
        stable_ratio = stable_dist_vec[0] / np.sum(stable_dist_vec)

        st.metric("Oracle's Prediction: Long-term Growth Rate (λ)", f"{dominant_eigenvalue:.4f}")
        
        if dominant_eigenvalue > 1.0:
            st.success("The prophecy is growth! 📈 The population will expand.", icon="🌿")
        elif dominant_eigenvalue < 1.0:
            st.warning("The prophecy is decline. 📉 The population will shrink.", icon="🍂")
        else:
            st.info("The prophecy is balance. ⚖️ The population will stabilize.", icon="🙏")

        st.metric("Oracle's Prediction: Stable 'Young' Ratio (Dharma)", f"{stable_ratio:.3f}")

        st.subheader("Simulation Controls")
        if st.button("Advance One Year →", use_container_width=True):
            if not st.session_state.c5_pop_history:
                st.session_state.c5_pop_history.append(st.session_state.c5_initial_pop)
            last_pop = st.session_state.c5_pop_history[-1]
            # Here is the core calculation: new_population = L * old_population
            new_pop = L @ last_pop
            st.session_state.c5_pop_history.append(new_pop)

        if st.button("Reset Simulation", use_container_width=True):
            st.session_state.c5_pop_history = []
            st.rerun()

    with col2:
        st.subheader("The Unfolding Destiny")
        if not st.session_state.c5_pop_history:
            st.info("Press 'Advance One Year' to begin the simulation and witness destiny unfold.")
            fig, ax = plt.subplots()
            ax.bar(['Young', 'Adults'], st.session_state.c5_initial_pop, color=['#3498db', '#e67e22'])
            ax.set_title("Initial Population State (Year 0)")
            ax.set_ylabel("Population Count")
            st.pyplot(fig)

        else:
            history = np.array(st.session_state.c5_pop_history)
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, gridspec_kw={'height_ratios': [2, 1]})
            
            years = range(len(history))
            ax1.bar(years, history[:, 0], label='Young', color='#3498db')
            ax1.bar(years, history[:, 1], bottom=history[:, 0], label='Adults', color='#e67e22')
            ax1.set_ylabel("Population Count")
            ax1.set_title("Population History")
            ax1.legend()
            ax1.grid(True, axis='y', linestyle=':')

            total_pop = np.sum(history, axis=1)
            # Avoid division by zero if population dies out
            safe_total_pop = np.where(total_pop == 0, 1, total_pop)
            ratio_young = history[:, 0] / safe_total_pop
            
            ax2.plot(years, ratio_young, 'g-', marker='o', label='Actual Ratio of Young')
            ax2.axhline(stable_ratio, color='r', linestyle='--', label=f'Predicted Stable Ratio (Dharma) ≈ {stable_ratio:.3f}')
            ax2.set_ylim(0, 1)
            ax2.set_xlabel("Years")
            ax2.set_ylabel("Proportion")
            ax2.set_title("Convergence to Dharma (The Stable Eigenvector)")
            ax2.legend()
            ax2.grid(True, linestyle=':')

            plt.tight_layout()
            st.pyplot(fig)
            
    st.markdown("""
    **Experiment and Observe:**
    1.  **Convergence:** Notice how even if you start with a very unbalanced population, the *ratio* of young to adults (the bottom graph) quickly converges to the red dotted line—the Dharma predicted by the eigenvector. The raw numbers may grow or shrink, but the *structure* stabilizes.
    2.  **The Growth Rate:** If the dominant eigenvalue (λ) is 1.1, the total population will eventually grow by about 10% each year. Test this!
    3.  **The Tipping Point:** Find the settings that make the eigenvalue exactly 1.0. This is the sacred point of balance where the population neither grows nor shrinks. It has achieved perfect sustainability.
    """)

    # ==================================================================================
    # Part 3: The Gallery (Showcasing Variety)
    # Goal: Demonstrate the breadth and different "flavors" of the concept.
    # ==================================================================================
    st.header("Part 3: The Gallery of Destinies", divider="rainbow")
    st.markdown("The fate of a population can take many forms. Let's explore some classic scenarios. Each is a different set of Karmic rules, leading to a different destiny.")
    
    tab1, tab2, tab3 = st.tabs(["📈 The Thriving Metropolis", "⚖️ The Ancient Forest", "📉 The Ghost Village"])

    with tab1:
        st.subheader("The Thriving Metropolis: A Story of Growth")
        st.markdown("""
        Imagine a booming city like Bengaluru, attracting talent from all over. The 'birth rate' (new people arriving or being born) is high, and the 'survival rate' (people staying) is also high. This creates a powerful Karmic Matrix where the dominant eigenvalue is significantly greater than 1.
        
        This is the signature of exponential growth. The city's population and economy expand relentlessly year after year. The eigenvector, in this case, would describe the stable ratio of students, young professionals, and established families that the city's structure supports.
        """)
        image_search_button("Bengaluru Skyline at Night", "bengaluru skyline night")
        st.latex(r"L_{growth} = \begin{bmatrix} 0 & 2.0 \\ 0.6 & 0.95 \end{bmatrix} \implies \lambda_{dominant} \approx 1.48 > 1")

    with tab2:
        st.subheader("The Ancient Forest: A Story of Balance")
        st.markdown("""
        Consider a self-sustaining ecosystem, like the sacred groves of Meghalaya, undisturbed for centuries. Here, the cycle of life and death is in perfect harmony. For every ancient tree that falls, a sapling rises to take its place. The number of births is finely tuned to the number of deaths.
        
        This is a system where the dominant eigenvalue is almost exactly 1. The total population remains constant. The Dharma, or eigenvector, represents the perfect, stable balance of seedlings, young trees, and ancient giants, a structure that has proven resilient for generations. This is ecological equilibrium.
        """)
        image_search_button("Sacred Groves of Meghalaya", "sacred groves of meghalaya")
        st.latex(r"L_{balance} = \begin{bmatrix} 0 & 0.5 \\ 0.8 & 0.8 \end{bmatrix} \implies \lambda_{dominant} = 1.0")

    with tab3:
        st.subheader("The Ghost Village: A Story of Decline")
        st.markdown("""
        Think of a remote village facing depopulation. The young generation moves to the cities for work (low young survival rate in the village context), and the birth rate is low. Even if the adults have a high survival rate, the lack of new blood creates a Karmic Matrix of decay.
        
        The dominant eigenvalue is less than 1, signaling a slow, inevitable decline. Each year, the total population shrinks by a fixed percentage. The stable age distribution (eigenvector) would likely be skewed heavily towards the elderly, the last witnesses to the village's former life.
        """)
        image_search_button("Abandoned Indian Village", "abandoned indian village")
        st.latex(r"L_{decline} = \begin{bmatrix} 0 & 0.4 \\ 0.3 & 0.9 \end{bmatrix} \implies \lambda_{dominant} \approx 0.97 < 1")


    # ==================================================================================
    # Part 4: The Formalization (The Ganita Shastra)
    # Goal: Bridge intuitive understanding to formal mathematical language.
    # ==================================================================================
    st.header("Part 4: The Ganita Shastra — The Mathematics of Destiny", divider="rainbow")
    st.markdown("""
    What we have called 'Karma' and 'Dharma' has a precise and beautiful mathematical foundation. Let's formalize our oracle's knowledge.
    """)
    
    with st.expander("📜 Defining the Leslie Matrix"):
        st.markdown("""
        The 'Karmic Matrix' we've been using is a specific type called a **Leslie Matrix**. For a population divided into *n* age classes, it's an *n x n* matrix that describes the transitions between them. In our 2x2 case (Young, Adult):

        $L = \\begin{bmatrix} f_1 & f_2 \\ s_1 & p_2 \\end{bmatrix}$

        *   $f_1$ and $f_2$ are **fecundity** rates. $f_1$ is the birth rate from the 'Young' class, and $f_2$ is from the 'Adult' class. In our simple model, we assumed only adults give birth, so $f_1=0$.
        *   $s_1$ is the **survival rate** of the 'Young' class to become members of the 'Adult' class in the next time step.
        *   $p_2$ is the **survival rate** of the 'Adult' class to remain in the 'Adult' class.

        If our population vector at time *t* is $P_t = \\begin{bmatrix} \text{Young}_t \\ \text{Adult}_t \\end{bmatrix}$, then the population at time *t+1* is simply:

        $P_{t+1} = L \cdot P_t$

        Applying the matrix is like turning the wheel of Karma one full cycle.
        """)

    with st.expander("🔮 The Eigen-Equation of Population"):
        st.markdown(r"""
        The core of our entire chapter lies in the fundamental eigenvector equation:

        $L \cdot v = \lambda \cdot v$
        
        Let's translate this from pure math into the language of life:
        
        *   "When the Karmic Matrix ($L$) acts upon a very special population structure—the Dharma vector ($v$)..."
        *   "...the resulting population ($L \cdot v$) is not a chaotic mess. It is an exact copy of the original Dharma vector ($v$), just scaled by a single number, $\lambda$."

        This is profound. It means that once a population reaches this 'Dharma' state (the eigenvector's proportions), it has found its destiny. From then on, the structure will never change. The entire population will just grow or shrink as a whole, governed by the scaling factor $\lambda$, the dominant eigenvalue.

        This is why the ratio on our interactive chart becomes a flat line. It has locked onto the eigenvector.
        """)

    with st.expander("💡 The Perron-Frobenius Theorem: The Oracle's Guarantee"):
        st.markdown("""
        How do we know there will always be one, unique, positive eigenvalue that is larger than all others and dictates the long-term behavior? Can we be sure our oracle isn't lying?

        For matrices with all non-negative entries, like our Leslie Matrix, a powerful result called the **Perron-Frobenius Theorem** guarantees it. It states that there will be a unique, real, and positive eigenvalue which is the largest in magnitude. This is our dominant eigenvalue. Furthermore, the corresponding eigenvector will have all positive components.

        This is the mathematical guarantee that a single "growth rate" and a single "stable age distribution" will always emerge in such systems. The Dharma is not a matter of chance; it is a mathematical certainty.
        
        Let's see it in code. No matter the inputs, `numpy` will find this dominant value for us:
        """)
        st.code(f"""
import numpy as np

# Our Karmic Matrix from the simulation
L = np.array([
    [0, {birth_rate:.2f}], 
    [{survival_y:.2f}, {survival_a:.2f}]
])

eigenvalues, eigenvectors = np.linalg.eig(L)

# Find the dominant eigenvalue (the one with the largest real part)
dominant_eigenvalue = np.max(np.real(eigenvalues))
dominant_idx = np.argmax(np.real(eigenvalues))

# Find the corresponding eigenvector (the Dharma)
stable_distribution_vector = np.real(eigenvectors[:, dominant_idx])

# Normalize it to see the ratios
stable_distribution_vector = np.abs(stable_distribution_vector / np.sum(stable_distribution_vector))

print(f"Dominant Eigenvalue (Growth Rate): {{dominant_eigenvalue:.4f}}")
print(f"Stable Distribution (Dharma): {{stable_distribution_vector}}")
        """, language="python")


    # ==================================================================================
    # Part 5: The Application (The Games & Puzzles)
    # Goal: Solidify understanding through active, goal-oriented problem-solving.
    # ==================================================================================
    st.header("Part 5: The Puzzles of the Oracle", divider="rainbow")
    st.markdown("Knowledge must be tested to become wisdom. Here are three challenges to prove your mastery over the oracle's secrets.")

    game1, game2, game3 = st.tabs(["🐅 The ISRO Tiger Project", "🎣 The Fisherman's Dilemma", "🏺 The Archaeologist's Riddle"])

    with game1:
        st.subheader("Challenge 1: The ISRO Satellite-Aided Tiger Conservation Project")
        st.markdown("""
        You are a conservation officer using ISRO satellite data to monitor a new tiger reserve. Your goal is to ensure the tiger population thrives. The target is a stable growth rate of **5% per year** (an eigenvalue of **1.05**).
        
        You cannot change the adult tigers' natural lifespan (survival is fixed at 92%), but you *can* run conservation programs that affect cub survival.
        
        **Your task: Adjust the 'Cub Survival Rate' until you achieve the target growth rate of 1.05.**
        """)
        
        adult_survival_game1 = 0.92
        birth_rate_game1 = 0.6 # Low birth rate for tigers
        
        cub_survival_game1 = st.slider("Cub Survival Rate", 0.0, 1.0, 0.4, 0.01, key="game1_slider")
        
        L_game1 = np.array([[0, birth_rate_game1], [cub_survival_game1, adult_survival_game1]])
        eigvals_g1, _ = np.linalg.eig(L_game1)
        current_growth = np.max(np.real(eigvals_g1))
        
        st.metric("Current Population Growth Rate (λ)", f"{current_growth:.4f}")
        
        if np.isclose(current_growth, 1.05, atol=0.005):
            st.balloons()
            st.success("🎯 Target Achieved! The tiger population is now on a stable 5% growth path. Your conservation efforts have paid off!")
        elif current_growth > 1.05:
            st.warning("Overshot! Growth is too high, which might strain the ecosystem. Lower the survival rate slightly.")
        else:
            st.info("Keep trying! The population isn't growing fast enough. You need to improve the cub survival rate.")

    with game2:
        st.subheader("Challenge 2: The Chilika Lake Fisherman's Dilemma")
        st.markdown("""
        You are managing the fish population in the magnificent Chilika Lake. The natural system is stable, with a birth rate of 1.2 and survival rates of 40% for young and 80% for adults.
        
        You need to harvest fish to support the local community, which reduces the survival rates. Your goal is to **maximize your total harvest percentage** while ensuring the fishery remains **sustainable** (i.e., the growth rate λ must be ≥ 1.0).
        
        **Your task: Adjust the harvest sliders to find the maximum possible harvest that doesn't doom the population.**
        """)
        image_search_button("Chilika Lake fishing boats", "chilika lake fishing boats")
        
        col_g2_1, col_g2_2 = st.columns(2)
        with col_g2_1:
            harvest_y = st.slider("Harvest Rate of Young (%)", 0, 100, 10, key="g2_hy")
        with col_g2_2:
            harvest_a = st.slider("Harvest Rate of Adults (%)", 0, 100, 10, key="g2_ha")
            
        base_survival_y, base_survival_a = 0.4, 0.8
        
        final_survival_y = base_survival_y * (1 - harvest_y/100)
        final_survival_a = base_survival_a * (1 - harvest_a/100)
        
        L_game2 = np.array([[0, 1.2], [final_survival_y, final_survival_a]])
        eigvals_g2, _ = np.linalg.eig(L_game2)
        current_growth_g2 = np.max(np.real(eigvals_g2))
        
        st.metric("Resulting Population Growth Rate (λ)", f"{current_growth_g2:.4f}")
        total_harvest = harvest_y + harvest_a
        st.metric("Your Total Harvest Score", f"{total_harvest}%")

        if current_growth_g2 < 1.0:
            st.error(" unsustainable! The fish population will collapse over time. Reduce your harvest.", icon="💔")
        else:
            st.success("Sustainable! The fishery will survive. Can you increase your harvest score further?", icon="✅")

    with game3:
        st.subheader("Challenge 3: The Harappan Archaeologist's Riddle")
        st.markdown(r"""
        You are an archaeologist excavating a site from the Indus Valley Civilization. You've found ancient texts describing the 'Dharma' of their sacred cattle population. The texts state that, at equilibrium, **for every 10 adult cattle, there were exactly 7 young calves.**
        
        This means the stable age distribution (the Dharma vector) was proportional to $\begin{bmatrix} 7 \\ 10 \end{bmatrix}$.

        Your team has narrowed down the possible 'Karmic laws' (Leslie Matrices) to three options based on climate models.
        
        **Your task: Identify which of the following three matrices would produce the sacred 7:10 ratio.**
        """)

        # The target ratio of young is 7 / (7+10) = 7/17 ≈ 0.4117
        st.info("Hint: Calculate the dominant eigenvector for each matrix and see which one matches the ratio.")
        
        options = {
            "Matrix A": np.array([[0, 1.0], [0.8, 0.6]]),
            "Matrix B": np.array([[0, 0.9], [0.7, 0.7]]),
            "Matrix C": np.array([[0, 1.2], [0.5, 0.8]])
        }
        
        choice = st.radio("Which matrix governed the Harappan cattle?", options.keys(), index=None)

        if choice:
            chosen_matrix = options[choice]
            eigvals, eigvecs = np.linalg.eig(chosen_matrix)
            dom_idx = np.argmax(np.real(eigvals))
            vec = np.abs(np.real(eigvecs[:, dom_idx]))
            ratio = vec[0] / vec[1] # young / adult ratio
            
            st.write(f"You chose {choice}. Let's analyze it:")
            st.latex(f"L = {str(chosen_matrix).replace(' [', '[').replace('[ ', '[')}")
            st.write(f"The calculated Young:Adult ratio for this matrix is approximately **{ratio:.2f} : 1**, which is {vec[0]:.2f} : {vec[1]:.2f}.")
            
            if choice == "Matrix B":
                st.balloons()
                st.success(f"Correct! The ratio for Matrix B is {ratio:.2f}, which is very close to the sacred 7:10 (0.7) ratio. You've solved the riddle!")
            else:
                st.error("Incorrect. This matrix does not produce the 7:10 Dharma. The ratio is wrong. Please try another.")


    # ==================================================================================
    # Part 6: The Horizon (The Jnana-Chakshu - Eye of Knowledge)
    # Goal: Motivate the user by revealing the concept's true power.
    # ==================================================================================
    st.header("Part 6: The Jnana-Chakshu — The Eye of Knowledge", divider="rainbow")
    st.markdown("""
    The oracle of population is but one application of this profound idea. The principle of finding the 'stable state' or 'most important feature' of a system governed by a matrix is one of the most powerful in all of science and technology.

    *   **Google's PageRank:** In the beginning, Google didn't rank pages by keywords alone. It modeled the entire internet as a giant matrix, where a link from page A to page B was a 'vote'. The eigenvector of this colossal matrix gave a 'rank' to every page on the internet. The pages with the highest values in the eigenvector were, by 'Dharma', the most important. You used an eigenvector every time you searched the web.
    
    *   **Vibrational Analysis:** When engineers at ISRO design a rocket, they model it as a structural system. The eigenvalues of this system's matrix represent the natural frequencies at which the rocket will vibrate. To avoid catastrophic failure, they must ensure the engine's vibrations do not match these eigenvalues.
    
    *   **Economics (Leontief Model):** An entire national economy can be modeled with an input-output matrix, showing how industries rely on each other. The eigenvector of this matrix reveals a stable state of economic equilibrium, for which the government can solve to set production targets.
    
    *   **Quantum Mechanics:** In the quantum world, every observable property (like energy or momentum) is represented by an operator (a matrix). The eigenvalues of that matrix are the only possible values that can be measured. The universe itself is governed by eigen-logic!

    **The Grand Takeaway:** Eigenvectors and eigenvalues reveal the hidden, stable soul of a system that undergoes repeated transformation. They are the 'Dharma' within the 'Karma'.

    **Teaser for the Next Chapter:** We have seen how a matrix transforms a vector and what its stable states are. But what if the matrix isn't square? What if it represents a transformation between completely different worlds, like from a high-dimensional space of movie ratings to a low-dimensional space of movie genres? For this, we need a tool even more powerful, a 'universal decomposition' that can handle any matrix. Prepare to meet the master of all matrix transformations: the **Singular Value Decomposition (SVD)**.
    """)

    # ==================================================================================
    # Part 7: The Check-up (The Pariksha)
    # Goal: Provide a robust self-assessment.
    # ==================================================================================
    st.header("Part 7: The Pariksha — A Check-up of Your Wisdom", divider="rainbow")
    st.markdown("Answer these questions to solidify your understanding.")

    questions = {
        "1. In our population model, what does the dominant eigenvalue (λ) fundamentally represent?": {
            "options": ["The starting population", "The stable age distribution (the ratio of young to old)", "The long-term annual growth or decline rate", "The number of years until the population doubles"],
            "correct": 2,
            "feedback": "Correct! The dominant eigenvalue λ tells us the rate at which the total population will scale each year. If λ > 1, it grows. If λ < 1, it shrinks."
        },
        "2. The stable age distribution, our 'Dharma', corresponds to which mathematical object?": {
            "options": ["The Leslie Matrix itself", "The dominant eigenvector", "The smallest eigenvalue", "The initial population vector"],
            "correct": 1,
            "feedback": "Exactly! The dominant eigenvector defines the proportional structure (e.g., ratio of young to old) that the population will naturally converge to over time."
        },
        "3. In our 'Dharma and Karma' analogy, the rules of life (birth and survival rates) were represented by what?": {
            "options": ["The Eigenvector", "The Eigenvalue", "A vector of population counts", "The Leslie Matrix"],
            "correct": 3,
            "feedback": "Perfect. The matrix is the engine of 'Karma' that takes the population from one state to the next according to a fixed set of rules."
        },
        "4. An ecologist finds that a certain bird population has a dominant eigenvalue of exactly 1.0. What can you conclude?": {
            "options": ["The population is growing rapidly.", "The population will die out.", "The population is in a state of perfect equilibrium and will remain stable in size.", "There are no adult birds left."],
            "correct": 2,
            "feedback": "Correct. An eigenvalue of 1 means the population size is multiplied by 1 each year, meaning it remains constant. This is the definition of sustainability."
        },
        "5. Why is Google's PageRank algorithm a famous application of eigenvectors?": {
            "options": ["It uses eigenvalues to decide the color of the Google logo.", "It finds the 'stable importance' of web pages in the vast network of links.", "It calculates how fast the internet is growing.", "It uses eigenvectors to compress images on web pages."],
            "correct": 1,
            "feedback": "That's right! PageRank treats the internet as a massive matrix of links and finds the dominant eigenvector. The components of this vector assign an 'importance' score to every webpage, representing the stable state of navigating that link network."
        }
    }

    for i, (q, data) in enumerate(questions.items()):
        st.subheader(f"Question {i+1}")
        user_answer = st.radio(q, data["options"], index=None, key=f"q{i}")
        
        if user_answer:
            if data["options"].index(user_answer) == data["correct"]:
                st.success(data["feedback"])
            else:
                st.error(f"Not quite. The correct answer is: **{data['options'][data['correct']]}**. \n\n*Why:* {data['feedback']}")
        st.markdown("---")