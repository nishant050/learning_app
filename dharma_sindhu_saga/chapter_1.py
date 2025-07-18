# In dharma_sindhu_saga/chapter_1.py
import streamlit as st
import time
from utils.plotting import image_search_button

def render():
    """
    Renders Chapter 1 of the Dharma-Kshetra Saga, following the 7-part design guide.
    Topic: The Seed of Dharma & The Land of Beginnings.
    """

    # =================================================================================================
    # METADATA & HEADER
    # =================================================================================================
    st.title("Chapter 1: The Seed of Dharma & The Land of Beginnings")
    st.markdown("---")


    # =================================================================================================
    # PART 1: THE CORE IDEA (THE ANALOGY)
    # Goal: Build profound, culturally-grounded intuition for Sanatana Dharma.
    # Method: Use the analogy of a Great Banyan Tree (Vata Vriksha).
    # =================================================================================================

    st.header("Part 1: The Great Banyan Tree of Being")
    st.markdown("""
    Before we speak of kings, battles, or even gods, we must first sit in the shade of a very old tree. It is not just any tree. Imagine a colossal Banyan, a *Vata Vriksha*, so vast its branches seem to kiss the clouds and so ancient its roots have burrowed into the very memory of the Earth. This tree has no single trunk, no simple origin you can point to and say, "Here, this is where it began." Instead, it sends down new roots from its branches, which then become trunks themselves, creating a living, breathing forest that is a single, interconnected organism.

    This Great Banyan is our analogy for **Sanatana Dharma**.
    """)

    image_search_button("The Great Banyan Tree (Vata Vriksha)", "Great Banyan Tree India")

    st.markdown("""
    The term ‘religion’ is too small, too contained for what this tree represents. Think of it not as a structure built by human hands, but as a natural law of the universe, like gravity or the rising of the sun. ‘Sanatana’ means eternal, perennial, that which has no beginning and no end. ‘Dharma’ is a word so rich it defies a single translation; it is righteousness, duty, cosmic law, virtue, the very 'way of being' of a thing. The Dharma of fire is to burn; the Dharma of water is to flow. What, then, is the Dharma of a human being? Our entire saga is an attempt to answer this question.

    Let's explore our Great Banyan, this tree of Sanatana Dharma:

    *   **The Unseen Roots (The Core Principles):** Deep beneath the soil, anchoring this entire universe, are the foundational truths. These are concepts like *Brahman* (the ultimate, formless reality), the oneness of existence, and the eternal nature of the soul (*Atman*). You don't see them every day, but the entire tree—the entire cosmos—draws its nourishment from them. They are the source code of reality.

    *   **The Trunks & Branches (The Many Paths):** Look at the Banyan. Which one is the 'main' trunk? It's impossible to tell. Some are thick and ancient, others are young and vigorous. Each trunk is a valid path to the same core nourishment. These represent the diverse traditions within Dharma—Shaivism, Vaishnavism, Shaktism, and countless other schools of thought and regional practices. They may look different, use different names and forms for the divine, but they are all part of the same tree, sharing the same roots. There is no single "correct" path up the tree; there is only *your* path.

    *   **The Leaves (Individual Lives):** Every single leaf on this colossal tree is a life, a soul on its journey. Each leaf is unique—some are large, some small, some in the bright sun, some in the shade. Each one performs its duty: engaging in photosynthesis, sustaining the branch, and playing its part in the life of the whole. The leaf's personal dharma (*Svadharma*) is to be the best leaf it can be, right where it is. It doesn't envy the leaf on the higher branch or pity the one below. It simply *is*, contributing to the whole and fulfilling its purpose.

    *   **The Cycle of Seasons (Karma and Samsara):** The leaves sprout, live, and eventually wither and fall, returning to the earth to nourish the roots. This is the cycle of life, death, and rebirth—**Samsara**. The quality of a leaf's life—how well it absorbed sunlight, how much it contributed—influences the soil. This is **Karma**, the law of cause and effect. Actions in one season (one life) determine the conditions for the next. The soil becomes richer or poorer based on the collective actions of the leaves.

    This tree is not a static monument. It is alive, growing, and ever-changing, yet its core principles—its roots—are eternal. It provides shade and shelter for all, regardless of who they are. This is the grand, open, and profound idea we begin with. Before we can understand the history of Haryana, the Land of Dharma, we must first understand the Dharma itself: not as a set of rules, but as this sprawling, life-giving, eternal Banyan of Being.
    """)
    st.markdown("---")


    # =================================================================================================
    # PART 2: THE MECHANISM (INTERACTIVE DISCOVERY)
    # Goal: Allow the user to "feel" the cause-and-effect of Karma and Samsara.
    # Method: A simple "Karma & Samsara Simulator".
    # =================================================================================================

    st.header("Part 2: The Cosmic Account Book - A Karma Simulator")
    st.markdown("""
    The ideas of Karma and Samsara can feel abstract. Let's make them tangible. Karma is not a reward/punishment system from a celestial judge; it is a universal, impersonal law of cause and effect, like a cosmic ledger. Every action, thought, and intention is a transaction that shifts your balance. Samsara is the grand cycle of existence this ledger is part of.

    Here is a simple interactive simulator. Imagine you are guiding a soul through several lifetimes. Your goal isn't to 'win', but to observe how different types of actions shape the soul's journey and the conditions of its next birth.
    """)

    st.info("💡 **How to Use:** Adjust the sliders to represent the dominant actions in a lifetime. Then click 'Live a Lifetime' to see the effect. Observe how the 'Karmic Balance' and 'Conditions for Next Life' change. Do this for several lifetimes to see the long-term trend.")

    # Initialize session state for the simulator
    if 'karmic_balance' not in st.session_state:
        st.session_state.karmic_balance = 0
        st.session_state.lifetime_number = 1
        st.session_state.log = []

    col1, col2 = st.columns([1, 1.5])

    with col1:
        st.subheader("Actions in This Lifetime")
        selfless_actions = st.slider("🌱 Selfless Actions (Nishkama Karma)", 0, 10, 5, help="Actions done without expecting personal gain, for the good of the whole.")
        good_actions = st.slider("😊 Good/Kind Actions (Punya)", 0, 10, 5, help="Acts of kindness, charity, honesty. These create positive karmic credits.")
        selfish_actions = st.slider("🔥 Selfish/Harmful Actions (Papa)", 0, 10, 2, help="Acts of greed, anger, harm, dishonesty. These create karmic debts.")

        if st.button("⏳ Live a Lifetime"):
            # Simple algorithm for karmic effect
            karmic_change = (selfless_actions * 1.5) + good_actions - (selfish_actions * 1.2)
            st.session_state.karmic_balance += karmic_change
            st.session_state.lifetime_number += 1

            log_entry = f"**Lifetime {st.session_state.lifetime_number - 1}:** Balance changed by {karmic_change:.1f}. New Balance: {st.session_state.karmic_balance:.1f}"
            st.session_state.log.insert(0, log_entry)
            if len(st.session_state.log) > 5:
                st.session_state.log.pop()

    with col2:
        st.subheader("The Soul's Journey")
        st.metric(label=f"🔄 Lifetime Number", value=st.session_state.lifetime_number)

        balance = st.session_state.karmic_balance
        st.metric(label="⚖️ Cumulative Karmic Balance", value=f"{balance:.1f}")

        conditions = "Neutral"
        if balance > 30:
            conditions = "🌱 Favorable (Health, wisdom, opportunity)"
        elif balance > 10:
            conditions = "🙂 Slightly Favorable"
        elif balance < -30:
            conditions = "🔥 Challenging (Hardship, obstacles)"
        elif balance < -10:
            conditions = "😕 Slightly Challenging"

        st.markdown("**Conditions for Next Life:**")
        st.success(conditions) if balance > 0 else st.warning(conditions)

        with st.expander("Show Karmic Ledger"):
            if not st.session_state.log:
                st.write("Your journey has not yet begun. Live a lifetime to see the log.")
            for entry in st.session_state.log:
                st.markdown(entry)

        if st.button("Reset Journey"):
            st.session_state.karmic_balance = 0
            st.session_state.lifetime_number = 1
            st.session_state.log = []
            st.rerun()

    st.markdown("""
    **Guiding Questions for Your Discovery:**
    1.  What happens if you only perform 'Good Actions' but also many 'Selfish Actions'? Does one cancel the other out perfectly?
    2.  Notice the impact of 'Selfless Actions'. Why do you think they have a slightly higher weight in our model?
    3.  Try to drive your balance as low as possible. Then, see how many lifetimes of positive action it takes to recover. What does this tell you about the journey of a soul?
    4.  This is a vast oversimplification. In reality, Karma is not a simple score. It's more like a complex web of tendencies, opportunities, and psychological patterns. How would you improve this model to make it more realistic?
    """)
    st.markdown("---")


    # =================================================================================================
    # PART 3: THE GALLERY (SHOWCASING VARIETY)
    # Goal: Demonstrate the breadth of "Dharma".
    # Method: Interactive tabs for different "flavors" of Dharma.
    # =================================================================================================

    st.header("Part 3: The Flavors of Dharma - A Gallery of Duties")
    st.markdown("""
    Dharma is not a one-size-fits-all instruction manual. Remember our Banyan tree? The duty of a leaf is different from the duty of a root. The concept is multi-layered, adapting to the person, their stage in life, their society, and their time. Let's explore some of these essential "flavors."
    """)

    tab1, tab2, tab3 = st.tabs(["**Svadharma** (Personal Duty)", "**Samaja Dharma** (Societal Duty)", "**Rashtra Dharma** (National Duty)"])

    with tab1:
        st.subheader("Svadharma: Your Unique Melody")
        st.markdown("""
        *Sva* means 'own' or 'self'. *Svadharma* is one's own unique, personal duty and nature. It is the path that aligns with your innate tendencies, talents, and stage in life. It's the role you were born to play in the cosmic drama.

        **Sub-Analogy: The Orchestra**
        Imagine a grand orchestra. There is a violinist, a drummer, a flutist. The Dharma of the violinist is to play the violin beautifully. If the violinist, yearning to be the drummer, drops their bow and tries to bang the drums, they create chaos. They not only fail at being a good drummer but also neglect their own unique gift. Svadharma is about discovering your instrument and playing it with all your heart for the harmony of the whole orchestra. It is better to perform your own Dharma imperfectly than to perform another's Dharma perfectly.

        This is the message Arjuna receives in the Bhagavad Gita, on the battlefield of Kurukshetra. He, a warrior (*Kshatriya*), is overcome with doubt about fighting his own kin. Krishna reminds him of his Svadharma: as a warrior, his duty is to fight for righteousness and protect order, however painful it may be.
        """)
        image_search_button("Arjuna and Krishna on the battlefield", "Arjuna Krishna chariot Bhagavad Gita")

    with tab2:
        st.subheader("Samaja Dharma: The Web of Society")
        st.markdown("""
        *Samaja* means 'society'. *Samaja Dharma* refers to the duties and ethics that govern a community. It's the collective code of conduct that allows people to live together in harmony, trust, and mutual prosperity.

        **Sub-Analogy: Traffic Rules**
        Think about the traffic in a busy Indian city. It can seem chaotic, but underlying it is a shared understanding—a Samaja Dharma. We agree to (mostly) stop at red lights, drive on one side of the road, and give way to ambulances. These aren't profound spiritual laws, but they are a form of Dharma. Without this shared code, the system would collapse into gridlock and accidents.

        Samaja Dharma includes traditions, ethics, laws, and customs that maintain social order. It is the Dharma of a doctor to heal, the Dharma of a teacher to educate, and the Dharma of a citizen to be responsible. It's the ethical web that holds the community together, ensuring its health and continuity.
        """)
        image_search_button("Busy Indian city street traffic", "Mumbai street traffic")

    with tab3:
        st.subheader("Rashtra Dharma: The Soul of the Nation")
        st.markdown("""
        *Rashtra* means 'nation' or 'state'. *Rashtra Dharma* is the highest duty to protect the integrity, culture, and well-being of the nation. It transcends personal and even community interests when the nation itself is at stake.

        **Sub-Analogy: The Ship of State**
        A nation is like a great ship sailing through the ocean of time. Every citizen is a member of the crew. When a mighty storm threatens to sink the ship, the personal preferences of the crew become secondary. The cook, the navigator, the engineer—all must work together with a single purpose: to save the ship. This unified, selfless duty to the collective vessel is Rashtra Dharma.

        Throughout Indian history, this concept has been invoked. From Chanakya's teachings on statecraft in the *Arthashastra* to the sacrifices of freedom fighters, the idea that the nation's Dharma is a sacred responsibility has been a powerful force. In the context of Haryana, the land that has so often been the guardian of the throne of Delhi, this concept is particularly resonant.
        """)
        image_search_button("Indian Parliament building (Sansad Bhavan)", "New Parliament of India")
    st.markdown("---")


    # =================================================================================================
    # PART 4: THE FORMALIZATION (THE GANITA SHASTRA)
    # Goal: Bridge intuition to formal language, providing significant depth.
    # Method: A comprehensive dive into the core terms and the ancient geography.
    # =================================================================================================

    st.header("Part 4: The Ganita Shastra - Naming What We Now Know")
    st.markdown("""
    We have felt the rhythm of Karma and explored the many flavors of Dharma through analogies. Now, let us do what the ancient Indian sages, the *Rishis*, did. Let us give these concepts their proper names and examine them with rigor. This section is our 'Ganita Shastra' (Science of Calculation/Formalization), where we transition from intuition to formal knowledge.
    """)

    with st.expander("📜 The Lexicon of Being: Dharma, Karma, Samsara, Moksha", expanded=True):
        st.subheader("Dharma (धर्म)")
        st.markdown("""
        *   **Etymology:** From the Sanskrit root *'dhri'*, which means 'to hold', 'to maintain', or 'to support'.
        *   **Deep Meaning:** Dharma is literally that which 'upholds' reality. It is the foundational law that prevents the cosmos from collapsing into chaos. It is the intrinsic nature of a thing. The Dharma of sugar is to be sweet. The Dharma of a human is far more complex, encompassing duty, ethics, law, and purpose, all aimed at upholding both personal and cosmic order. It is not a command from a god, but a principle woven into the fabric of existence.
        """)

        st.subheader("Karma (कर्म)")
        st.markdown("""
        *   **Etymology:** From the Sanskrit root *'kri'*, which means 'to do' or 'to act'.
        *   **Deep Meaning:** Karma literally means 'action'. The law of Karma states that every action has a corresponding reaction. It is a universal law of cause and effect. It's crucial to understand that Karma is not 'fate'. Fate implies a predetermined destiny you cannot escape. Karma implies a destiny you are *currently creating* through your actions, thoughts, and words. You are the architect of your own experience. There are three types:
            1.  **Sanchita Karma:** The total sum of all past karmas from previous lives that have yet to bear fruit. It's like a vast storehouse of seeds.
            2.  **Prarabdha Karma:** The portion of Sanchita Karma that has 'sprouted' and is shaping your current life. It's the hand of cards you've been dealt in this lifetime (your body, family, innate talents, and major life events). You cannot change this portion.
            3.  **Kriyamana Karma:** The new Karma you are creating right now, in this moment. This is where your free will lies. The actions you take now will determine your future experiences and become part of your Sanchita Karma.
        """)

        st.subheader("Samsara (संसार)")
        st.markdown("""
        *   **Etymology:** From Sanskrit, meaning 'to flow on', 'to wander through', or 'a passing through'.
        *   **Deep Meaning:** Samsara is the cycle of birth, death, and rebirth to which all beings are subject as long as they are bound by Karma. It is often visualized as a wheel or a river. It is not seen as inherently good or bad, but as a state of perpetual wandering driven by desire, attachment, and ignorance of one's true nature (the *Atman*). The goal is not to get a 'better' birth within the cycle, but to break free from the cycle altogether.
        """)

        st.subheader("Moksha (मोक्ष)")
        st.markdown("""
        *   **Etymology:** From the Sanskrit root *'muc'*, which means 'to liberate', 'to free', 'to release'.
        *   **Deep Meaning:** Moksha is the ultimate goal of the Dharmic paths: liberation. It is the release from the cycle of Samsara. It is the state where one's individual consciousness (*Atman*) realizes its oneness with the ultimate reality (*Brahman*). It is the end of striving, the extinguishing of the karmic ledger, and the attainment of a state of absolute freedom, peace, and bliss. It is the final destination of the soul's long journey home.
        """)

    with st.expander("🌏 The Land of Beginnings: Ancient Haryana and the Sarasvati River", expanded=False):
        st.subheader("The Cradle of Civilization: Sapta Sindhu")
        st.markdown("""
        To understand Haryana's title as 'Dharma-Kshetra', we must travel back in time, to an era when the geography of North India was vastly different. The most ancient Hindu scriptures, the Vedas, don't speak of the Ganga as their most sacred river. They sing praises of a mighty, life-giving river called the **Sarasvati**. The land they describe, the heartland of early Vedic culture, was called **Sapta Sindhu**—the land of seven rivers.

        This region, located in the Punjab and its surroundings, was a fertile, green paradise. Along with the Indus (Sindhu) and its tributaries, the Sarasvati was the central artery of this civilization. It was on the banks of this river that the Rishis are said to have composed the Vedas, contemplating the very concepts of Dharma and Karma we have just discussed.
        """)
        image_search_button("Map of the Sapta Sindhu region", "Sapta Sindhu map vedic")

        st.subheader("The Lost River: The Sarasvati")
        st.markdown("""
        For centuries, the Sarasvati was considered a myth, a poetic imagination. But modern science—satellite imagery, geological surveys, and archaeology—has confirmed its existence. What is today the seasonal Ghaggar-Hakra riverbed, flowing through parts of Haryana, Rajasthan, and into Pakistan, is the remnant of that once-mighty Sarasvati. Tectonic shifts and climate change caused its tributaries to be captured by other river systems (the Yamuna and Sutlej), and the great river dried up around 1900 BCE.

        The drying of the Sarasvati was a catastrophic ecological event that likely led to the eastward migration of populations, contributing to the decline of the urban phase of the Indus Valley Civilization and the shift of Indian civilization's center of gravity towards the Gangetic plain.
        """)

        st.subheader("The Legacy: The Indus-Sarasvati Civilization")
        st.markdown("""
        The civilization that flourished in this basin from roughly 3300 BCE to 1900 BCE is known as the Indus Valley Civilization (IVC), or more accurately, the Indus-Sarasvati Civilization, as a majority of its sites have been found along the paleochannel of the Sarasvati.

        Haryana is home to some of the most significant sites of this ancient culture. The largest known city of the entire civilization, **Rakhigarhi**, is located in Hisar district, Haryana. It is even larger than the famous sites of Harappa and Mohenjo-daro.
        """)
        image_search_button("Rakhigarhi archaeological site", "Rakhigarhi excavation")

        st.markdown("""
        What does the legacy of Rakhigarhi and other sites like Banawali and Kunal (also in Haryana) tell us?
        *   **Advanced Urban Planning:** They had grid-like street layouts, sophisticated drainage and water management systems, and multi-story brick houses.
        *   **Trade and Commerce:** Seals found from these sites indicate a vast trade network extending to Mesopotamia (modern Iraq).
        *   **Early Culture:** While we cannot decipher their script, their art, pottery, and ritual objects (like 'fire altars' found at Kalibangan, nearby in Rajasthan) suggest a culture deeply concerned with order, cleanliness, and ritual—early forms of what would evolve into Dharmic practices.

        Therefore, when we say Haryana is the 'Land of Beginnings', it is no exaggeration. It is the soil where the seeds of Indian civilization were first sown, where urban life flourished, and where the foundational concepts of Dharma were first contemplated along the banks of a now-lost sacred river.
        """)
    st.markdown("---")


    # =================================================================================================
    # PART 5: THE APPLICATION (THE GAMES & PUZZLES)
    # Goal: Solidify understanding through active, goal-oriented problem-solving.
    # Method: Three distinct mini-games housed in tabs.
    # =================================================================================================

    st.header("Part 5: The Workshop - Sharpening Your Understanding")
    st.markdown("""
    Knowledge is not truly ours until we can apply it. This section is a workshop for your mind. Let's move beyond theory and engage with these ideas through puzzles and scenarios.
    """)

    game_tab1, game_tab2, game_tab3 = st.tabs(["**Game 1: The Farmer's Dilemma**", "**Game 2: Trace the Sarasvati**", "**Game 3: The Sage's Lexicon**"])

    with game_tab1:
        st.subheader("The Farmer's Dilemma: A Test of Dharma")
        st.markdown("""
        **Scenario:** You are a poor farmer in ancient Haryana. A severe drought has ruined your crops. Your family is hungry. One night, you discover that your neighbor, who is also your cousin, has managed to save a small portion of his harvest and has stored it in his shed. He has refused to share it with anyone, saying he must protect his own family first. What is the most 'Dharmic' action to take?
        """)
        st.markdown("Read the options and choose the one that best reflects the complex nature of Dharma. There is no single 'perfect' answer, but one choice reflects a deeper understanding.")

        dharma_choice = st.radio(
            "What will you do?",
            (
                "A) My Svadharma is to protect my family. I will secretly take a small amount of grain from my neighbor's shed at night. My family's survival comes first.",
                "B) My Samaja Dharma is to respect property. I will not steal. I will go to the village elder or council and plead for them to intervene and encourage my neighbor to share, upholding the community's well-being.",
                "C) I will do nothing and accept my fate. This suffering is my Prarabdha Karma, and I must endure it without complaint.",
                "D) I will confront my neighbor aggressively and demand he share, for hoarding is against Dharma."
            ),
            index=None,
            key="dharma_game"
        )

        if dharma_choice:
            st.markdown("---")
            if dharma_choice.startswith("B"):
                st.success("**Wise Reflection:** You chose option B. This is arguably the most Dharmic choice. You acknowledged your personal duty (Svadharma) but sought a solution that upholds the social order (Samaja Dharma) without resorting to theft (Adharma) or passive resignation. It balances personal need with community ethics, showing a mature understanding of Dharma's many layers.")
            elif dharma_choice.startswith("A"):
                st.warning("**A Complicated Path:** You chose option A. This highlights the intense conflict between Svadharma (duty to family) and Samaja Dharma (duty to not steal). While understandable from a survival standpoint, it breaks the social contract and creates negative Karma. Dharma often presents us with such difficult choices.")
            elif dharma_choice.startswith("C"):
                st.info("**A Misunderstanding of Karma?:** You chose option C. While accepting one's situation is a virtue, passivity in the face of injustice or hardship isn't necessarily Dharma. Kriyamana Karma (current action) allows us to respond to our Prarabdha Karma (current situation). Your duty is to act, not just to endure.")
            elif dharma_choice.startswith("D"):
                st.warning("**Righteous but Risky:** You chose option D. Your intention to call out hoarding is good, but aggression can lead to more conflict and negative Karma. The path of Dharma often favors skillful, calm, and community-oriented action over angry confrontation.")

    with game_tab2:
        st.subheader("Trace the Sarasvati: An Archaeologist's Quiz")
        st.markdown("You are an archaeologist working to map the ancient Indus-Sarasvati Civilization. Based on what you learned in Part 4, which of these ancient sites is the **largest** known city of that civilization and is located in modern-day Haryana?")

        archaeo_choice = st.radio(
            "Select the correct site:",
            ("Mohenjo-daro", "Harappa", "Rakhigarhi", "Lothal"),
            index=None,
            key="archaeo_game"
        )
        if archaeo_choice:
            st.markdown("---")
            if archaeo_choice == "Rakhigarhi":
                st.success(f"**Correct!** You've found it! Rakhigarhi, in the Hisar district of Haryana, is indeed the largest known urban center of the Indus-Sarasvati Civilization. This places Haryana at the absolute heart of that ancient world.")
            else:
                st.error(f"**Not quite.** While {archaeo_choice} is a very important site from that civilization, the largest one currently known, located in Haryana, is Rakhigarhi. Mohenjo-daro and Harappa are in modern-day Pakistan, and Lothal is a port city in Gujarat.")

    with game_tab3:
        st.subheader("The Sage's Lexicon: A Matching Game")
        st.markdown("The old sage of the village has written down the core concepts, but the definitions have been jumbled! Match the concept to its correct meaning to restore the sage's text.")

        concepts = {
            "Karma": "The universal law of cause and effect; every action has a reaction.",
            "Samsara": "The cycle of birth, death, and rebirth; the 'wandering' of the soul.",
            "Moksha": "Liberation from the cycle of rebirth; the ultimate goal.",
            "Dharma": "The cosmic law that upholds reality; one's duty, nature, and purpose."
        }
        options = list(concepts.keys())

        user_choice = st.selectbox("Choose a concept:", options, index=None)
        if user_choice:
            st.markdown(f"**The correct meaning of `{user_choice}` is:**")
            st.info(f"*{concepts[user_choice]}*")
    st.markdown("---")


    # =================================================================================================
    # PART 6: THE HORIZON (THE JNANA-CHAKSHU - EYE OF KNOWLEDGE)
    # Goal: Motivate by revealing the concept's true power and its role in future lessons.
    # Method: Explain where this skill is used and explicitly tease the next chapter.
    # =================================================================================================

    st.header("Part 6: The Horizon - The Field of Dharma")
    st.markdown("""
    You have now sat under the Great Banyan Tree, simulated the cosmic ledger of Karma, and walked the ancient banks of the Sarasvati. You have begun to grasp the foundational principles that underpin not just a religion, but a whole worldview.

    **So where does this lead? Why is this the *first* chapter?**

    Because what we have discussed—Dharma, Karma, Svadharma—are not just abstract philosophical ideas. They are the operating system for the epic story that comes next. They are the very questions that drive the greatest heroes and villains of Indian lore to their destinies.

    The concepts you've learned are the **rules of the game**. Now, you are ready to watch the players.
    """)
    st.success("""
    **Key Takeaway (The Jnana-Chakshu - Eye of Knowledge):**
    Sanatana Dharma is not a set of commands, but a framework for understanding your place in the cosmos. Your life is a constant interplay between your unchangeable past (*Prarabdha Karma*), your present choices (*Kriyamana Karma*), and your unique purpose (*Svadharma*). Understanding this is the first step to navigating life with wisdom.
    """)
    st.markdown("""
    **The Next Chapter Awaits...**

    The land of Haryana, this ancient cradle, is not just a place of quiet beginnings. It is destined to become a stage for the most profound and terrible conflict imaginable. A conflict where families will be torn apart, where the greatest warriors of an age will assemble, and where the very meaning of Dharma will be questioned, tested, and ultimately defined in a baptism of fire.

    We are heading to **Kurukshetra**. We are heading to the **Mahabharata**.

    In the next chapter, we will leave the age of myth and memory and enter the age of the epic. We will see how these principles of Dharma become the central conflict in a war that will shape the destiny of India forever. The questions will no longer be theoretical. They will be matters of life and death on the grandest scale.
    """)
    st.markdown("---")


    # =================================================================================================
    # PART 7: THE CHECK-UP (THE PARIKSHA)
    # Goal: Provide a robust self-assessment.
    # Method: 5-7 concise multiple-choice questions with feedback.
    # =================================================================================================

    st.header("Part 7: The Check-up - How Firm is Your Foundation?")
    st.markdown("Let's test the foundations we've built. Answer these questions to see how well you've grasped the core ideas of Chapter 1.")

    questions = {
        "1. In our 'Great Banyan Tree' analogy for Sanatana Dharma, what do the unseen roots represent?": {
            "options": ["The many different paths and traditions", "The lives of individual people", "The core, foundational principles like Brahman and Atman", "The cycle of cause and effect"],
            "correct": "The core, foundational principles like Brahman and Atman",
            "feedback": "Correct! The roots are the deep, unseen, eternal principles that nourish the entire system."
        },
        "2. What is the most accurate description of the Law of Karma?": {
            "options": ["A system of reward and punishment from God", "A predetermined fate that you cannot change", "The law of cause and effect, where your current actions shape your future", "A social custom of ancient India"],
            "correct": "The law of cause and effect, where your current actions shape your future",
            "feedback": "Exactly! Karma is not fate. It is the empowering idea that you are the architect of your destiny through your present actions (Kriyamana Karma)."
        },
        "3. Svadharma refers to...": {
            "options": ["The laws of the nation", "One's own personal duty, nature, and path in life", "The rules of society", "The duty to one's parents"],
            "correct": "One's own personal duty, nature, and path in life",
            "feedback": "Perfect. Svadharma is about finding your unique role in the cosmic orchestra and playing your part to the best of your ability."
        },
        "4. Modern science suggests the mythical Sarasvati River corresponds to the...": {
            "options": ["Modern-day Yamuna River", "Ghaggar-Hakra river system", "Ganges River", "Narmada River"],
            "correct": "Ghaggar-Hakra river system",
            "feedback": "Correct. Satellite imagery has traced the ancient paleochannel of the Sarasvati to the path of the seasonal Ghaggar-Hakra river, confirming the geographical accuracy of the Vedas."
        },
        "5. What is the ultimate goal of the soul's journey in the Dharmic worldview?": {
            "options": ["To be reborn in a wealthy family", "To achieve Moksha, or liberation from the cycle of rebirth", "To perform as many good deeds as possible to have a good afterlife", "To become a powerful ruler"],
            "correct": "To achieve Moksha, or liberation from the cycle of rebirth",
            "feedback": "Yes! The ultimate goal is not just a better position within the cycle (Samsara), but to transcend the cycle entirely and achieve liberation (Moksha)."
        }
    }

    for i, (question, details) in enumerate(questions.items()):
        st.subheader(f"Question {i+1}")
        user_answer = st.radio(question, details["options"], index=None, key=f"pariksha_{i}")
        if user_answer:
            if user_answer == details["correct"]:
                st.success(f"**Correct:** {details['feedback']}")
            else:
                st.error(f"**Not quite.** The correct answer is '{details['correct']}'. {details['feedback']}")
            st.markdown("---")