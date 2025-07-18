import streamlit as st
from utils.plotting import image_search_button # Assuming this utility is in your utils folder

def render():
    """
    Renders Chapter 4 of the Streamlit Saga: Structuring Your App - Layouts & Containers.
    This chapter follows the 7-part "Blueprint 3.1" and the "Indian Feynman" philosophy.
    """

    # =================================================================================================
    # == PART 1: THE CORE IDEA (THE ANALOGY)
    # =================================================================================================
    st.markdown("## 🏛️ Chapter 4: The Architect's Vision - Structuring Your Digital Palace")
    st.markdown("---")
    st.markdown("""
    My dear apprentice, you have learned to gather the finest materials. You can carve beautiful text, you can display shimmering tables of data, and you can even craft interactive widgets that respond to a user's touch. But materials alone do not make a palace. A pile of marble is not the Taj Mahal. A stack of bricks is not a grand Haveli.

    Today, we move from being a craftsman to being an architect—a *Sthapati*. We learn the divine art of arranging space. An application, like a palace, must have structure. It must have public courtyards and private chambers, grand halls and hidden alcoves. This structure is what separates a simple script from a professional, intuitive application. It guides the visitor, tells them where to look, and creates a sense of order and purpose.

    Our guiding philosophy will be the design of a magnificent Rajasthani Haveli. Think of its sprawling structure. It isn't a single, long corridor. It has a grand entrance, leading to a central courtyard open to the sky, where many activities happen side-by-side. From this courtyard, you can enter different wings of the palace, each dedicated to a specific purpose—the Hall of Public Audience, the private quarters, the library. And within these rooms, you might find ornate chests that hold precious jewels, revealed only when you open them.

    This is the soul of app design. Our Streamlit commands for layout are the architectural blueprints for our own digital Haveli.
    - **`st.columns`** are our open-air **Courtyards**, allowing us to place elements side-by-side.
    - **`st.tabs`** are the different **Wings of the Palace**, letting users navigate between distinct sections without leaving the page.
    - **`st.expander`** is the ornate **Treasure Chest**, keeping detailed information neatly tucked away until the user wishes to see it.
    - **`st.container`** is the invisible **Foundation** or platform upon which a room is built, grouping elements together logically.

    Before we lay our first digital brick, let us visualize the inspiration for our work.
    """)
    
    image_search_button("Jaipur Haveli Architecture", "Jaipur Haveli Architecture")

    st.markdown("""
    So, take a deep breath. Clear your mind. Today, we don't just write code. We design an experience. We build our palace.
    """)


    # =================================================================================================
    # == PART 2: THE MECHANISM (INTERACTIVE DISCOVERY)
    # =================================================================================================
    st.markdown("## The Architect's Sandbox")
    st.markdown("---")
    st.markdown("""
    An architect does not begin by quarrying marble; they begin with a sketch, a model. This sandbox is our model. Here, you can experiment with the fundamental forces of layout and see the effect of your decisions instantly. Don't just read—*play*. Feel the structure taking shape under your command.

    **Your Task:** Use the controls on the left to build a small, dynamic layout in the space on the right. Ask yourself questions as you go:
    - What happens when you add columns inside a tab?
    - How does the `gap` setting change the feel of the layout?
    - Can you place an expander inside a column?
    
    This is your chance to build the intuition of a master Sthapati.
    """)

    sandbox_cols = st.columns((1, 2))

    with sandbox_cols[0]:
        st.subheader("Controls")
        use_tabs = st.checkbox("Create a Tabbed Layout?")
        tab_names_str = st.text_input("Enter Tab names (comma-separated)", "Profile,Dashboard,Settings")
        
        use_columns = st.checkbox("Add Columns inside the active section?")
        num_cols = st.slider("Number of Columns", min_value=2, max_value=5, value=2)
        gap_size = st.radio("Column Gap Size", ["small", "medium", "large"], index=1)

        use_expander = st.checkbox("Add an Expander (Treasure Chest)?")
        expander_label = st.text_input("Expander Label", "Show Advanced Details")


    with sandbox_cols[1]:
        st.subheader("Live Layout")
        
        if use_tabs:
            tab_names = [name.strip() for name in tab_names_str.split(',')]
            tabs = st.tabs(tab_names)
            
            for i, tab in enumerate(tabs):
                with tab:
                    st.write(f"This is the '{tab_names[i]}' Wing of our Palace.")
                    if use_columns:
                        cols = st.columns(num_cols, gap=gap_size)
                        for j, col in enumerate(cols):
                            with col:
                                st.info(f"Courtyard Column {j+1}")
                                if use_expander and j == 0: # Place expander in first column
                                    with st.expander(expander_label):
                                        st.success("You found the hidden treasure!")
                    elif use_expander:
                         with st.expander(expander_label):
                            st.success("You found the hidden treasure!")

        else: # No tabs
            st.info("This is the Main Hall of our Palace.")
            if use_columns:
                cols = st.columns(num_cols, gap=gap_size)
                for j, col in enumerate(cols):
                    with col:
                        st.info(f"Courtyard Column {j+1}")
                        if use_expander and j == 0:
                            with st.expander(expander_label):
                                st.warning("A secret revealed in the Main Hall!")
            elif use_expander:
                with st.expander(expander_label):
                    st.warning("A secret revealed in the Main Hall!")


    # =================================================================================================
    # == PART 3: THE GALLERY (SHOWCASING VARIETY)
    # =================================================================================================
    st.markdown("## The Blueprint Gallery")
    st.markdown("---")
    st.markdown("""
    Every grand palace is a collection of different architectural styles and components. Here, we will study the core blueprints individually. Each one has a specific purpose and feel. We'll give them thematic names to honor our analogy.
    """)

    gallery_tabs = st.tabs(["The Courtyard (`st.columns`)", "The Foundation (`st.container`)", "The Palace Wings (`st.tabs`)", "The Treasure Chest (`st.expander`)"])

    with gallery_tabs[0]:
        st.markdown("### The Courtyard: `st.columns`")
        st.markdown("""
        The courtyard is the heart of the Haveli. It's an open space where life unfolds in parallel. One person might be drawing water from a well, another might be sorting spices, and children might be playing a game—all visible at once, side-by-side. `st.columns` is our tool to create these digital courtyards.

        It's perfect for:
        - Displaying key metrics next to each other.
        - Showing a chart and its explanation side-by-side.
        - Creating a form on the left and showing results on the right.
        
        **Sub-analogy:** Think of a vibrant Indian marketplace. Each column is a different stall, offering its wares to you simultaneously.
        """)
        image_search_button("Indian Market Stall", "Indian Market Stall")
        
        st.markdown("#### Example: A Dashboard of the Kingdom")
        st.code("""
# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Treasury")
    st.metric(label="Gold Coins", value="1.2 Million", delta="+5%")
    image_search_button("Ancient Gold Coins", "Ancient Gold Coins")

with col2:
    st.subheader("Military Strength")
    st.metric(label="Active Soldiers", value="75,000", delta="-500")
    image_search_button("Rajput Soldiers", "Rajput Soldiers")
        """, language="python")

        col1_ex, col2_ex = st.columns(2)
        with col1_ex:
            st.subheader("Treasury")
            st.metric(label="Gold Coins", value="1.2 Million", delta="+5%")
            image_search_button("Ancient Gold Coins", "Ancient Gold Coins")
        with col2_ex:
            st.subheader("Military Strength")
            st.metric(label="Active Soldiers", value="75,000", delta="-500")
            image_search_button("Rajput Soldiers", "Rajput Soldiers")

    with gallery_tabs[1]:
        st.markdown("### The Foundation: `st.container`")
        st.markdown("""
        The container is the most subtle, yet one of the most powerful, layout elements. It's not about visual flair; it's about logical grouping. A container is like the raised stone platform (*jagati*) on which a temple is built. It creates a distinct boundary that says, "Everything on this platform belongs together."

        Its primary power is **controlling the order of rendering**. Normally, Streamlit runs from top to bottom. With a container, you can define a "box" and then add things to it from anywhere else in your code. This is essential for building complex layouts where you might want a summary at the top that is populated by calculations that happen later.

        **Sub-analogy:** A Thali tray. The tray itself (`st.container`) is created first. Then you place the different bowls of food (`st.write`, `st.metric`) onto it, in any order you please.
        """)
        
        st.markdown("#### Example: Building a Report Out of Order")
        st.code("""
with st.container():
    st.subheader("Final Report")
    # We are creating a placeholder for the results first
    results_placeholder = st.empty()
    st.write("This text appears above the results.")

# Now, we do some complex calculation...
import time
total_revenue = 520_000
growth = 0.15
time.sleep(2) # Simulate calculation

# ...and now we fill in the placeholder we created earlier!
results_placeholder.metric("Total Revenue", f"₹{total_revenue:,}", f"{growth:.0%}")
        """, language="python")
        st.info("The example above is a live demonstration. Note how the 'Final Report' header appeared before the metric was calculated and inserted.")


    with gallery_tabs[2]:
        st.markdown("### The Palace Wings: `st.tabs`")
        st.markdown("""
        As a visitor explores a grand palace, they don't see everything at once. They choose to enter the Hall of Mirrors, or the Armory, or the Library. Each wing has a distinct purpose and is self-contained. `st.tabs` gives our users this power of focused exploration. It's the best way to pack a huge amount of information into a small space without overwhelming the user.

        It's perfect for:
        - Separating a project into "Data," "Visualization," and "Model" sections.
        - Displaying user information under "Profile," "Settings," and "History" tabs.
        - Presenting different scenarios or case studies.

        **Sub-analogy:** The different galleries of the National Museum in Delhi. You choose whether you want to explore the Harappan Civilization or the Mughal Art gallery.
        """)
        image_search_button("National Museum New Delhi", "National Museum New Delhi")

        st.markdown("#### Example: The Royal Archives")
        st.code("""
dynasty_tabs = st.tabs(["Mauryan Empire", "Gupta Empire", "Chola Dynasty"])

with dynasty_tabs[0]:
    st.subheader("The Mauryan Empire (c. 322-185 BCE)")
    st.write("Founded by Chandragupta Maurya, it was the first empire to unify most of the Indian subcontinent. Its capital was Pataliputra (modern-day Patna).")
    image_search_button("Ashoka Pillar", "Ashoka Pillar")

with dynasty_tabs[1]:
    st.subheader("The Gupta Empire (c. 320-550 CE)")
    st.write("Known as the Golden Age of India, this period saw remarkable achievements in science, technology, art, and mathematics, including the concept of zero.")
    image_search_button("Gupta Period Coin", "Gupta Period Coin")

with dynasty_tabs[2]:
    st.subheader("The Chola Dynasty (c. 300s BCE - 1279 CE)")
    st.write("A southern Indian dynasty, the Cholas were masters of naval trade and temple architecture, building magnificent structures like the Brihadeeswarar Temple.")
    image_search_button("Brihadeeswarar Temple", "Brihadeeswarar Temple")
        """, language="python")
        dynasty_tabs_ex = st.tabs(["Mauryan Empire", "Gupta Empire", "Chola Dynasty"])
        with dynasty_tabs_ex[0]:
            st.subheader("The Mauryan Empire (c. 322-185 BCE)")
            st.write("Founded by Chandragupta Maurya, it was the first empire to unify most of the Indian subcontinent.")
        with dynasty_tabs_ex[1]:
            st.subheader("The Gupta Empire (c. 320-550 CE)")
            st.write("Known as the Golden Age of India, this period saw remarkable achievements.")
        with dynasty_tabs_ex[2]:
            st.subheader("The Chola Dynasty (c. 300s BCE - 1279 CE)")
            st.write("A southern Indian dynasty, the Cholas were masters of naval trade and temple architecture.")


    with gallery_tabs[3]:
        st.markdown("### The Treasure Chest: `st.expander`")
        st.markdown("""
        Every palace has its secrets. Not every piece of information needs to be visible at all times. Sometimes, you want to provide a clean, simple overview, but give the curious visitor a way to dig deeper. The expander is our digital treasure chest. It presents a simple label, and only reveals its rich contents when clicked.

        It's perfect for:
        - Hiding long code blocks.
        - Tucking away advanced settings or filters.
        - Providing "Show/Hide Explanation" sections for complex charts.

        **Sub-analogy:** An ancient scroll that is rolled up. You only see the title on the outside. You must consciously unroll it to read the wisdom contained within.
        """)
        image_search_button("Ancient Indian Scroll", "Ancient Indian scroll")

        st.markdown("#### Example: A Sage's Advice")
        st.code("""
st.info("A wise person once gave a simple piece of advice.")

with st.expander("📜 Click to unroll the scroll and read the sage's full explanation..."):
    st.markdown('''
    "The true measure of a developer," the sage explained, "is not in the complexity of the code they write, but in the simplicity of the experience they create. 
    
    A user who is lost is a user who will leave. Use layouts not to show off how much you can fit on a page, but to respectfully guide the user's attention to what is most important. 
    
    Clarity is the highest form of elegance."
    ''')
    st.success("Wisdom has been revealed!")
        """, language="python")

        with st.expander("📜 Click to unroll the scroll and read the sage's full explanation..."):
            st.markdown('"The true measure of a developer," the sage explained, "is not in the complexity of the code they write, but in the simplicity of the experience they create..."')
            st.success("Wisdom has been revealed!")


    # =================================================================================================
    # == PART 4: THE FORMALIZATION (THE GANITA SHASTRA / SHILPA SHASTRA)
    # =================================================================================================
    st.markdown("## The Shilpa Shastra of Layouts")
    st.markdown("---")
    st.markdown("""
    Our intuition is strong. We feel the flow of the Haveli. Now, let us learn the precise incantations—the formal syntax—that give our architectural visions form. This is our *Shilpa Shastra*, the sacred text on the science of building. Every parameter has a purpose.

    ### 1. `st.columns(spec, *, gap="small")`
    This is the command to create our side-by-side courtyards.

    - **`spec`**: This is the most important parameter. It defines the number of columns and their relative widths.
        - **Integer:** `st.columns(3)` creates three columns of equal width.
        - **List of Numbers (int or float):** `st.columns([2, 1, 1])` creates three columns. The first is twice as wide as the second and third. This is perfect for layouts with a main content area and two smaller sidebars. The numbers represent weights or ratios. `[0.5, 0.25, 0.25]` would produce the same result.
    - **`gap`**: An optional string that sets the size of the gap between columns. It can be `"small"`, `"medium"`, or `"large"`. This controls the "breathing room" in your app.

    **Code Deep Dive:**
    ```python
    # Two columns, the first being 3 times wider than the second
    col1, col2 = st.columns(, gap="large")

    with col1:
        st.header("Main Content Area")
        st.write("Because we used `[3, 1]`, this column gets 75% of the space.")
    
    with col2:
        st.header("Sidebar")
        st.write("This column gets the remaining 25% of the space.")
    ```

    ### 2. `st.tabs(list_of_strings)`
    This command creates the different wings of our palace.

    - **`list_of_strings`**: You must pass a list where each string is the label for one tab. The command returns a list of tab objects, one for each string you provided.
    - **Usage:** You must use a `with` statement to tell Streamlit which elements belong to which tab object.

    **Code Deep Dive:**
    ```python
    # Define the labels for your tabs
    tab_labels = ["Data Source", "Data Visualization", "ML Model Insights"]
    
    # Create the tab objects
    tab1, tab2, tab3 = st.tabs(tab_labels)

    with tab1:
        st.header("Data Source Details")
        st.write("Place your dataframe and data loading info here.")

    with tab2:
        st.header("Interactive Visualizations")
        st.write("Place your `st.pyplot` or `st.plotly_chart` calls here.")

    with tab3:
        st.header("Machine Learning Model Insights")
        st.write("Show model accuracy, feature importance, etc., here.")
    ```

    ### 3. `st.expander(label, expanded=False)`
    The command to create our treasure chests.

    - **`label`**: The string that will be visible on the expander when it is collapsed. It should invite the user to click.
    - **`expanded`**: An optional boolean. If `True`, the expander will be open by default when the app loads. If `False` (the default), it will be closed.

    **Code Deep Dive:**
    ```python
    st.write("Here is a summary of our project.")

    # The expander is closed by default
    with st.expander("See the full project methodology..."):
        st.write("This section was hidden.")
        st.write("It's a great place for verbose logs, detailed data dictionaries, or lengthy explanations that not every user needs to see immediately.")

    # This expander will be open when the page loads
    with st.expander("Credits and Acknowledgements", expanded=True):
        st.write("This project was made possible by...")
    ```

    ### 4. `st.container()`
    The command to lay our invisible foundation.

    - It takes no parameters. It simply creates a container object.
    - Its power comes from how it's used with a `with` statement to group elements, or by assigning it to a variable to insert elements out of order.

    **Code Deep Dive (Out-of-Order Rendering):**
    ```python
    # 1. Create a container variable at the top
    summary_container = st.container()

    st.write("This part of the app runs first.")
    # ... more code and calculations ...
    value_from_calculation = 10 * 5

    # 2. Now, use the container variable to add content back at the top!
    with summary_container:
        st.header("Executive Summary")
        st.write(f"The result of our important calculation is: {value_from_calculation}")
    ```
    """)


    # =================================================================================================
    # == PART 5: THE APPLICATION (THE GAMES & PUZZLES)
    # =================================================================================================
    st.markdown("## The Architect's Challenges")
    st.markdown("---")
    st.markdown("""
    Theory is the ink, but practice is the hand that builds the palace. You have studied the blueprints. Now, you must prove your skill. Here are three challenges. In each, you are given a scenario and must use the correct layout elements to solve the problem.
    """)
    
    challenge_tabs = st.tabs(["Challenge 1: The Maharaja's Dashboard", "Challenge 2: The Royal Archives", "Challenge 3: The Spy's Report"])

    with challenge_tabs[0]:
        st.subheader("Challenge 1: The Maharaja's Dashboard")
        st.markdown("""
        **The Scenario:** The Maharaja of Amer needs a daily dashboard. He is a very busy man and wants to see three key metrics side-by-side for a quick overview:
        1.  The kingdom's Food Supply.
        2.  The Treasury's balance.
        3.  The number of Trade Caravans currently active.

        **Your Task:** Use `st.columns` to create a three-column layout to display these metrics. Fill in the placeholder code below to complete the dashboard.
        """)
        
        st.code("""
import streamlit as st

st.header("Maharaja's Daily Briefing")

# YOUR CODE GOES HERE
# Create three columns. Use the variables col1, col2, and col3.
# ---
# col1, col2, col3 = ...
# ---

with col1:
    st.metric("Food Supply (Grains)", "82%", "+1.5%")

with col2:
    st.metric("Treasury (Asharfis)", "450,000", "+1,200")

with col3:
    st.metric("Trade Caravans", "32 Active", "-1")

# If your code is correct, you will see the three metrics below this line, side-by-side.
        """, language="python")

        st.markdown("---")
        st.subheader("Live Result")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Food Supply (Grains)", "82%", "+1.5%")
        with c2:
            st.metric("Treasury (Asharfis)", "450,000", "+1,200")
        with c3:
            st.metric("Trade Caravans", "32 Active", "-1")


    with challenge_tabs[1]:
        st.subheader("Challenge 2: The Royal Archives")
        st.markdown("""
        **The Scenario:** The Royal Librarian is digitizing the histories of India's great philosophical schools. The information is dense, and she wants to avoid a long, confusing page. She wants users to be able to click on a school's name to see its details.

        **Your Task:** Use `st.tabs` to organize the philosophies of Samkhya, Yoga, and Vedanta into three distinct, clean tabs.
        """)
        
        st.code("""
import streamlit as st

st.header("The Philosophical Archives")

# YOUR CODE GOES HERE
# Create three tabs with the labels "Samkhya", "Yoga", and "Vedanta".
# Use the variables tab1, tab2, and tab3.
# ---
# tab1, tab2, tab3 = st.tabs(...)
# ---

with tab1:
    st.subheader("Samkhya")
    st.write("One of the oldest schools, it is a dualistic philosophy that posits a fundamental difference between consciousness (Purusha) and matter (Prakriti).")

with tab2:
    st.subheader("Yoga")
    st.write("Closely linked to Samkhya, the Yoga school focuses on the practical methods and meditative disciplines to attain a state of liberation (Moksha).")

with tab3:
    st.subheader("Vedanta")
    st.write("Focusing on the Upanishads, Vedanta explores the nature of reality (Brahman). Its major sub-schools include Advaita (non-dualism) and Dvaita (dualism).")

# If your code is correct, you will see the archives organized into tabs below.
        """, language="python")
        st.markdown("---")
        st.subheader("Live Result")
        t1, t2, t3 = st.tabs(["Samkhya", "Yoga", "Vedanta"])
        with t1:
            st.subheader("Samkhya")
            st.write("One of the oldest schools, it is a dualistic philosophy that posits a fundamental difference between consciousness (Purusha) and matter (Prakriti).")
        with t2:
            st.subheader("Yoga")
            st.write("Closely linked to Samkhya, the Yoga school focuses on the practical methods and meditative disciplines to attain a state of liberation (Moksha).")
        with t3:
            st.subheader("Vedanta")
            st.write("Focusing on the Upanishads, Vedanta explores the nature of reality (Brahman). Its major sub-schools include Advaita (non-dualism) and Dvaita (dualism).")


    with challenge_tabs[2]:
        st.subheader("Challenge 3: The Spy's Report")
        st.markdown("""
        **The Scenario:** You are a spy in a foreign court. You need to send a report back to your spymaster. The report must look like a mundane summary of the court's daily proceedings, but it must contain a hidden section with the *real* intelligence. This hidden section should only be visible if the spymaster knows where to click.

        **Your Task:** Use `st.expander` to create a "secret" section within a seemingly normal report.
        """)
        
        st.code("""
import streamlit as st

st.header("Court Report: A Summary")
st.write("Today's session of the court was uneventful. Lord Bhim Singh discussed crop yields. The treasurer reported standard figures. All seems quiet.")
st.write("The weather is pleasant.")

# YOUR CODE GOES HERE
# Create an expander with the label "Show a detailed transcript of the treasurer's report...".
# ---
# with st.expander(...):
#     ...
# ---
    st.warning("SECRET INTEL:")
    st.write("The treasurer's numbers are fake! He is moving gold to a secret location in the Western Ghats. He mentioned a 'Tiger's Cave'. We must act now.")

# If your code is correct, you will see the innocuous report above, with the secret intel hidden inside an expander.
        """, language="python")

        st.markdown("---")
        st.subheader("Live Result")
        st.header("Court Report: A Summary")
        st.write("Today's session of the court was uneventful. Lord Bhim Singh discussed crop yields. The treasurer reported standard figures. All seems quiet.")
        st.write("The weather is pleasant.")
        with st.expander("Show a detailed transcript of the treasurer's report..."):
            st.warning("SECRET INTEL:")
            st.write("The treasurer's numbers are fake! He is moving gold to a secret location in the Western Ghats. He mentioned a 'Tiger's Cave'. We must act now.")


    # =================================================================================================
    # == PART 6: THE HORIZON (THE JNANA-CHAKSHU - EYE OF KNOWLEDGE)
    # =================================================================================================
    st.markdown("## The Jnana-Chakshu: Seeing with the Eye of Knowledge")
    st.markdown("---")
    st.markdown("""
    You have done it, architect. You have moved beyond laying single bricks and have now designed the very structure of the palace. This skill is the dividing line between a simple script and a sophisticated application.

    **Where This Power is Used:**
    - **Financial Dashboards:** Every stock trading app uses columns to show charts, news, and buy/sell orders on one screen.
    - **Data Science in Bengaluru:** A data scientist presents their findings to a client using tabs for "Data Exploration," "Model Performance," and "Business Impact."
    - **E-commerce Websites:** Product pages use expanders for "Product Details," "Specifications," and "Customer Reviews" to keep the main page clean.
    - **Internal Business Tools:** Companies build apps to track inventory, where different warehouses or product categories are separated into tabs.

    **The Key Takeaway:** The "Dharma" of this lesson is that **structure serves the user.** A well-organized app is an act of respect for the user's time and attention. Your goal is not to show everything at once, but to guide them to what they need, when they need it.

    You have built a beautiful, static palace. It is perfectly organized and a marvel to behold. But it is lifeless. It treats every visitor exactly the same. What if the palace could recognize you? What if it could remember what you were doing the last time you visited? What if it could change and adapt based on your choices?

    To do this, our palace needs a memory. It needs a soul. In our next chapter, we will bestow this gift upon it. We will learn about **Session State**, the magic that turns a static structure into a living, breathing, interactive experience.
    """)


    # =================================================================================================
    # == PART 7: THE CHECK-UP (THE PARIKSHA)
    # =================================================================================================
    st.markdown("## The Pariksha: Test Your Foundations")
    st.markdown("---")
    st.markdown("A master architect must know their blueprints by heart. Answer these questions to ensure your foundation is strong.")

    questions = {
        "1. In our Haveli analogy, what does `st.tabs` represent?": {
            "options": ["The open-air courtyards", "The different wings of the palace (e.g., library, armory)", "The hidden treasure chests", "The foundation platform"],
            "answer": "The different wings of the palace (e.g., library, armory)",
            "explanation": "Correct! `st.tabs` is used to create distinct, self-contained sections that the user can navigate between, just like the different wings of a large palace."
        },
        "2. How do you create two columns where the first is twice as wide as the second?": {
            "options": ["`st.columns(2, 1)`", "`st.columns([2, 1])`", "`st.columns(width=[2, 1])`", "`st.columns('2:1')`"],
            "answer": "`st.columns([2, 1])`",
            "explanation": "Excellent. The widths are defined by passing a list of numbers (integers or floats) representing the ratio of sizes."
        },
        "3. You have a lot of complex data processing code that you want to hide by default, but allow curious users to see. Which is the best element to use?": {
            "options": ["`st.container`", "`st.columns`", "`st.tabs`", "`st.expander`"],
            "answer": "`st.expander`",
            "explanation": "Precisely! `st.expander` is designed for this exact purpose—keeping detailed or non-essential information neatly tucked away until it's requested."
        },
        "4. What is the unique primary advantage of using `st.container`?": {
            "options": ["It adds a visible border around elements.", "It automatically creates columns.", "It allows you to insert elements into a specific spot on the page, even if your code for them appears later in the script.", "It is required for using `st.tabs`."],
            "answer": "It allows you to insert elements into a specific spot on the page, even if your code for them appears later in the script.",
            "explanation": "That's the key insight! While it also groups elements, its true power lies in enabling out-of-order or delayed rendering, which is crucial for complex app layouts."
        },
        "5. You want to make an `st.expander` visible as soon as the page loads. What parameter do you use?": {
            "options": ["`st.expander('Label', visible=True)`", "`st.expander('Label', default='open')`", "`st.expander('Label', expanded=True)`", "`st.expander('Label', open=True)`"],
            "answer": "`st.expander('Label', expanded=True)`",
            "explanation": "Correct. The `expanded=True` parameter tells the expander to be open by default, rather than the standard collapsed state."
        }
    }

    for i, (question, data) in enumerate(questions.items()):
        st.subheader(f"Question {i+1}")
        user_answer = st.radio(question, data["options"], key=f"q_{i}")
        
        if st.button(f"Check Answer for Question {i+1}", key=f"btn_{i}"):
            if user_answer == data["answer"]:
                st.success(data["explanation"])
            else:
                st.error(f"Not quite. The correct answer is **{data['answer']}**. {data['explanation']}")
        st.markdown("---")