import streamlit as st
import time
# We are assuming the image_search_button is in a shared utility file
from utils.plotting import image_search_button

def render():
    """
    Renders Chapter 3 of the Streamlit Saga: Making it Talk - Interactive Widgets.
    This chapter is a deep dive into the core interactive elements that transform a
    static page into a dynamic application. It follows the 7-part structure
    of the Lesson Design Guide.
    """

    # =================================================================================================
    # == PART 1: THE CORE IDEA (THE ANALOGY)
    # =================================================================================================
    st.title("🎛️ Chapter 3: Making it Talk")
    st.subheader("From a Silent Sign to a Bustling Bazaar Stall")
    st.markdown("---")

    st.markdown("""
    Imagine you are walking through a vibrant Indian market. You see two stalls side-by-side.

    The first stall has a beautifully painted, static wooden sign. It reads: **"Superb Samosas - Crispy, Hot, and Delicious."** It's informative, yes. You know what they sell. But it's a one-way street. The sign talks *at* you. It cannot listen. It cannot answer your questions. It cannot change.

    The second stall has a cheerful vendor. As you approach, they make eye contact and smile. They don't just have a sign; they start a conversation.

    *"Namaste! Welcome! Looking for a snack?"* they ask.
    
    You ask, *"How spicy are your samosas?"*
    
    They reply, *"We have three levels! Mild, for the gentle soul; Medium, for the adventurous spirit; and Fire, for the truly brave! Which one calls to you?"*

    You point and ask, *"How much for four?"*

    They respond, *"For you, a special price! Move this marker,"* they say, pointing to a sliding scale, *"to a price you feel is fair, and we have a deal!"*

    This second stall is **interactive**. It responds to you. It reconfigures itself based on your questions and choices. It pulls you into an experience.

    Until now, our Streamlit apps have been like that first wooden sign: beautiful, perhaps, but silent. We used `st.write` and `st.markdown` to display information. In this chapter, we will learn how to become the second vendor. We will give our app a voice and ears. We will learn to use **widgets**—the tools of conversation in Streamlit. These are the magical elements like buttons, sliders, and dropdown menus that allow your user to "talk" to your app, and your app to listen and respond.
    """)

    st.info("💡 **The Big Idea:** Static apps present information. Interactive apps have a conversation. Widgets are the building blocks of that conversation.")

    st.markdown("---")


    # =================================================================================================
    # == PART 2: THE MECHANISM (INTERACTIVE DISCOVERY)
    # =================================================================================================
    st.header("The Vendor's Toolkit: Our First Interactive Playground")
    st.markdown("""
    Let's set up our own digital stall and experiment with the tools of the trade. Below is our "Control Panel." As you interact with each widget, pay close attention to the **"App's Brain"** section. This shows you exactly what the widget is "telling" our Python script.

    This is the most crucial concept to grasp: **every time you click, slide, or select, Streamlit reruns your entire Python script from top to bottom.** The widget the user just changed simply reports its new value, which your script can then use to change what it displays. It's a continuous, dynamic loop.
    """)

    # Create a two-column layout for the interactive playground
    col1, col2 = st.columns([1, 1.5], gap="large")

    with col1:
        st.subheader("Your Control Panel")
        st.markdown("---")
        
        # 1. Text Input
        user_name = st.text_input("First, what is your name?", "Explorer")
        
        # 2. Selectbox
        spice_level = st.selectbox(
            "Choose your spice level:",
            ("Mild 🌶️", "Medium 🌶️🌶️", "Fire 🌶️🌶️🌶️")
        )
        
        # 3. Slider
        quantity = st.slider("How many samosas would you like?", 1, 20, 4)
        
        # 4. Button
        confirm_button = st.button("Confirm Your Order", use_container_width=True)

    with col2:
        st.subheader("The App's Brain (What Your Script Sees)")
        st.markdown("---")
        st.markdown(f"Hello, **{user_name}**! Let's analyze your choices.")
        
        st.write("`st.text_input` is currently telling our script:")
        st.code(f'user_name = "{user_name}"', language="python")

        st.write("`st.selectbox` is telling our script:")
        st.code(f'spice_level = "{spice_level}"', language="python")

        st.write("`st.slider` is telling our script:")
        st.code(f'quantity = {quantity}', language="python")
        
        st.write("`st.button` is a special case. It acts like a trigger.")
        st.code(f'confirm_button = {confirm_button}', language="python")

        # Logic that depends on the button press
        if confirm_button:
            st.success(f"**Order Confirmed!** Preparing {quantity} '{spice_level}' samosas for {user_name}. Thank you!")
            st.balloons()
        else:
            st.warning("Your order is not yet confirmed. Please press the button to proceed.")

    st.markdown("---")

    # =================================================================================================
    # == PART 3: THE GALLERY (SHOWCASING VARIETY)
    # =================================================================================================
    st.header("A Gallery of Conversations")
    st.markdown("""
    While the four widgets above are our workhorses, each has its own personality and is suited for different kinds of conversations. Let's explore them in more detail, like a craftsperson studying their tools.
    """)

    button_tab, select_tab, slider_tab, text_tab = st.tabs([
        "🔘 The Trigger (Button)", 
        "👇 The Choice (Selectbox)", 
        "↔️ The Dial (Slider)", 
        "✍️ The Blank Slate (Text Input)"
    ])

    with button_tab:
        st.subheader("🔘 The Trigger: `st.button`")
        st.markdown("""
        **Sub-Analogy:** The "Go!" signal in a race.
        
        The button is the simplest form of interaction. It does not store a value like the others; it simply reports whether it was pressed *on this specific script run*. Its value is `True` for the single run immediately after it's clicked, and `False` on all subsequent runs until clicked again.
        
        This makes it perfect for actions: starting a calculation, submitting a form, or triggering an animation. It's the "Do this now!" command.
        """)
        image_search_button("Website 'Submit' button", "submit button ui")
        st.code("""
# When to use it: For actions and confirmations.
if st.button("Launch the Rocket"):
    st.write("🚀 Liftoff!")
else:
    st.write("The rocket is waiting for your command.")
        """, language="python")

    with select_tab:
        st.subheader("👇 The Choice: `st.selectbox`")
        st.markdown("""
        **Sub-Analogy:** A menu at a restaurant.
        
        The selectbox is for when you have a limited, pre-defined set of options for the user. It's clean, simple, and prevents the user from entering an invalid choice. You give it a list of options, and it returns the single option the user has currently selected.
        
        It's ideal for categories, modes, or any situation where the user must pick one from many.
        """)
        image_search_button("Dropdown menu on a website", "web dropdown menu ui")
        st.code("""
# When to use it: For selecting from a list of defined options.
city = st.selectbox(
    "Which city's weather report would you like?",
    ("Mumbai", "Delhi", "Bengaluru", "Chennai", "Kolkata")
)
st.write(f"Fetching the weather for {city}...")
        """, language="python")

    with slider_tab:
        st.subheader("↔️ The Dial: `st.slider`")
        st.markdown("""
        **Sub-Analogy:** The volume knob on a stereo.
        
        The slider is the king of numerical input over a range. It allows the user to select a value by dragging a handle along a continuum. This is far more intuitive for quantities than typing a number, as it gives a visual sense of scale.
        
        It can select a single value, or with an extra argument, it can select a *range* (a start and end value).
        """)
        image_search_button("Price range filter on e-commerce", "price range slider ui")
        st.code("""
# When to use it: For selecting numbers within a known range.

# Single value slider
age = st.slider("What is your age?", 0, 100, 25)
st.write(f"You are {age} years old.")

# Range slider
price_range = st.slider(
    "Select a price range (in ₹):",
    0, 10000, (1000, 5000) # (min, max, default_tuple)
)
st.write(f"You selected items between ₹{price_range[0]} and ₹{price_range[1]}.")
        """, language="python")

    with text_tab:
        st.subheader("✍️ The Blank Slate: `st.text_input`")
        st.markdown("""
        **Sub-Analogy:** A blank form field for your name.
        
        When you need information that you cannot pre-define—like a name, a search query, or a password—`st.text_input` is your tool. It provides a simple text box and returns whatever the user types into it as a string. You can also have a multi-line version called `st.text_area` for longer feedback or comments.
        """)
        image_search_button("Web search bar", "search bar ui")
        st.code("""
# When to use it: For freeform text, like names, IDs, or search terms.
user_query = st.text_input("What would you like to search for?", "Eigenvalues")
st.write(f"Searching for articles about: {user_query}")
        """, language="python")

    st.markdown("---")


    # =================================================================================================
    # == PART 4: THE FORMALIZATION (THE GANITA SHASTRA)
    # =================================================================================================
    st.header("The Ganita Shastra: Formalizing the Conversation")
    st.markdown("""
    Our intuition is strong, but to be true masters, we must understand the precise rules of our tools—their *dharma*. Let's formalize the Streamlit execution model and the key parameters that give us fine-grained control over our widgets.
    """)

    st.subheader("The Golden Rule: The Script Reruns")
    st.markdown("""
    This is the law that governs all of Streamlit. It is so important, we will state it again:

    > **Every time a user interacts with a widget, the entire Python script is re-executed from top to bottom.**

    This seems strange at first. Why not just update the part of the page that changed? This "rerun" model is what makes Streamlit so simple and powerful. Your script is always a direct reflection of your app's state. You don't need to write complex "callback" logic to handle what changes when. You just write a simple, linear script.
    
    1.  A user moves a slider.
    2.  The browser tells Streamlit the slider's new value.
    3.  Streamlit says, "Aha! A change!" and **reruns `your_script.py` from the very first line.**
    4.  When the execution reaches the slider's line of code (e.g., `value = st.slider(...)`), Streamlit doesn't use the default value. It substitutes the new value it received from the browser.
    5.  The rest of your script executes naturally, using this new value.

    This mental model is your key to unlocking everything. Your code isn't a one-time setup; it's a recipe that is re-cooked fresh every single time an ingredient changes.
    """)

    st.subheader("Essential Widget Parameters: The Art of Control")
    st.markdown("""
    While the basic usage of widgets is simple, their true power is unlocked by using optional parameters. Here are the most vital ones you will use constantly.
    """)

    st.markdown("#### 1. The `label` (The Question)")
    st.markdown("""
    - **What it is:** The first argument to any widget. It's the text that's displayed to the user.
    - **Syntax:** `st.widget("This is the label", ...)`
    - **Dharma:** A good label is a clear, concise question. It is the most important piece of user interface design. Never have a widget without a clear label. Your user should never have to guess what a widget is for.
    """)

    st.markdown("#### 2. The `key` (The Name Tag)")
    st.markdown("""
    - **What it is:** An optional string parameter that gives the widget a unique internal name.
    - **Syntax:** `st.slider("My Slider", key="my_unique_slider")`
    - **Dharma:** The `key` is essential for two reasons. First, if you have two widgets of the same type with the exact same label, Streamlit will throw an error unless you give them unique keys. Second, and more importantly, the widget's value is stored in `st.session_state` under its key. We will explore `st.session_state` in a future chapter, but know that the `key` is the secret to making your app remember things.
    """)
    st.code("""
# This will cause an error without keys!
st.text_input("Enter your value:")
st.text_input("Enter your value:") # Duplicate widget

# This is the correct way, using keys
st.text_input("Enter your value:", key="value1")
st.text_input("Enter your value:", key="value2")
    """, language="python")

    st.markdown("#### 3. The `help` (The Guidebook)")
    st.markdown("""
    - **What it is:** An optional string that provides a tooltip—a small help text that appears when the user hovers over a small `(?)` icon next to the widget.
    - **Syntax:** `st.slider("Age", help="Drag the slider to your current age.")`
    - **Dharma:** Use the `help` parameter to provide extra context or instructions without cluttering your main UI. If a widget's purpose isn't immediately obvious from its label, add a `help` tooltip. It's a sign of a thoughtful developer.
    """)

    st.slider("My slider with a tooltip", 0, 100, 50, help="Hover over the (?) to see me! This is useful for giving users more context.")


    st.markdown("---")

    # =================================================================================================
    # == PART 5: THE APPLICATION (THE GAMES & PUZZLES)
    # =================================================================================================
    st.header("The Workshop: Puzzles to Sharpen Your Skills")
    st.markdown("""
    Theory is one thing, but mastery is earned through practice. Let's apply our knowledge in a few fun, goal-oriented scenarios. Each tab is a self-contained challenge.
    """)

    game1, game2, game3 = st.tabs(["🎨 The ISRO Satellite Painter", "🎵 The Mood Music Curator", "👨‍🍳 The Digital Dosa Maker"])

    with game1:
        st.subheader("🎨 The ISRO Satellite Painter")
        st.markdown("""
        **Mission:** You are in charge of designing the color scheme for India's next communication satellite, the 'Bharat-SAT'. Use the widgets to select a primary color, a secondary color, and the intensity of the metallic sheen. The button will generate the design specification.
        """)
        
        st.markdown("---")
        
        primary_color = st.selectbox(
            "Select the Primary Hull Color:",
            ("ISRO Gold", "Deep Space Blue", "Solar Flare Orange", "Lunar Grey"),
            key="primary_color_sat"
        )
        
        secondary_color = st.selectbox(
            "Select the Secondary Accent Color:",
            ("Tricolour Trim", "GSLV White", "Mission Control Silver"),
            key="secondary_color_sat"
        )
        
        sheen_intensity = st.slider(
            "Select Metallic Sheen Intensity (%):",
            0, 100, 75,
            help="Determines how reflective the satellite's surface is."
        )
        
        if st.button("Generate Design Specification", use_container_width=True):
            st.write("Generating Design Spec...")
            with st.spinner('Calculating orbital paint trajectories...'):
                time.sleep(2)
            st.success("Specification Generated!")
            st.markdown(f"""
            - **Satellite:** Bharat-SAT
            - **Primary Color:** `{primary_color}`
            - **Secondary Color:** `{secondary_color}`
            - **Sheen Intensity:** `{sheen_intensity}%`
            - **Status:** Approved for fabrication.
            """)

    with game2:
        st.subheader("🎵 The Mood Music Curator")
        st.markdown("""
        **Mission:** You are designing a smart music player for a cafe. The user needs to select their current mood, and the app will suggest a genre of music and a volume level.
        """)
        st.markdown("---")
        
        mood = st.selectbox(
            "What is the mood of the cafe right now?",
            ("Peaceful Morning ☀️", "Busy Afternoon 🏃", "Relaxed Evening 🌙")
        )

        if mood == "Peaceful Morning ☀️":
            genre = "Instrumental Sitar"
            volume = 30
            emoji = "🧘"
        elif mood == "Busy Afternoon 🏃":
            genre = "Upbeat Bollywood Pop"
            volume = 70
            emoji = "🕺"
        else: # Relaxed Evening
            genre = "Classic Ghazals"
            volume = 50
            emoji = "🌃"
            
        st.write(f"For a **{mood}** mood, we suggest:")
        st.markdown(f"### **Genre:** {genre} {emoji}")
        
        suggested_volume = st.slider(
            "Adjust Volume:",
            0, 100, volume
        )

        st.info(f"The music player is now set to play **{genre}** at volume **{suggested_volume}**.")


    with game3:
        st.subheader("👨‍🍳 The Digital Dosa Maker")
        st.markdown("""
        **Mission:** Create an order form for a modern Dosa restaurant. Take the customer's name, let them choose a dosa, and confirm their order.
        """)
        st.markdown("---")

        customer_name = st.text_input("Please enter your name for the order:", "Guest")
        
        dosa_type = st.selectbox(
            "Choose your Dosa:",
            ("Classic Masala Dosa", "Spicy Mysore Masala Dosa", "Rich Paneer Dosa", "Modern Cheese Burst Dosa")
        )
        
        is_crispy = st.toggle("Make it extra crispy?", value=True)
        
        if st.button("Place My Dosa Order!", use_container_width=True):
            crispy_text = "extra crispy" if is_crispy else "regular"
            st.success(f"Order received for **{customer_name}**!")
            st.balloons()
            st.write(f"One **{crispy_text} {dosa_type}** is being prepared. Your order will be ready shortly!")

    st.markdown("---")

    # =================================================================================================
    # == PART 6: THE HORIZON (THE JNANA-CHAKSHU - EYE OF KNOWLEDGE)
    # =================================================================================================
    st.header("The Horizon: The Power of Conversation")
    st.markdown("""
    You have now mastered the fundamental building blocks of user interaction. These simple widgets are the atoms from which almost all complex web applications are built.
    
    - A **data science dashboard** uses `selectbox` to choose a dataset and `slider` to filter a date range.
    - A **machine learning tool** uses `st.text_input` for a user to enter a sentence for analysis and a `button` to run the model.
    - A **financial modeling app** uses multiple `st.slider` widgets for users to input their assumptions about market growth and inflation.

    **The Key Takeaway:** Interactivity separates a report from a tool. By allowing users to input their own context, questions, and data, you transform your script from a piece of code into a collaborative partner.

    However, as you were playing with the games, did you notice a small inconvenience? In the satellite painter, every time you changed a color, the whole app re-ran before you were ready. You couldn't set the primary color, then the secondary, and *then* generate the spec. You had to do it all at once with the button.
    
    What if we want to fill out multiple fields *before* submitting? How do we group widgets together? And how do we build apps that have completely separate pages, like a real website?

    This brings us to the next steps in our journey...
    """)
    st.success("🚀 **Next Chapter Tease:** In our upcoming chapters, we will learn how to structure our apps with **Layouts and Containers** to create clean, professional designs, and how to use **Forms** to batch multiple inputs together for a more seamless user experience.")

    st.markdown("---")

    # =================================================================================================
    # == PART 7: THE CHECK-UP (THE PARIKSHA)
    # =================================================================================================
    st.header("The Pariksha: Check Your Understanding")
    st.markdown("Test your knowledge of the core concepts of interactivity.")

    questions = {
        "1. What is the 'Golden Rule' of Streamlit's execution model?": {
            "options": [
                "Only the widget that was changed gets updated.",
                "The entire Python script reruns from top to bottom on every interaction.",
                "You must write a callback function for every widget.",
                "Widgets can only be updated once per second."
            ],
            "answer": "The entire Python script reruns from top to bottom on every interaction.",
            "explanation": "This is the fundamental model. Every interaction causes a full, top-to-bottom rerun of the script, making the code simple and declarative."
        },
        "2. You have created a button: `is_pressed = st.button('Click me')`. If a user clicks the button, what is the value of `is_pressed` on the *very next* script run after the click?": {
            "options": [
                "True, and it stays True until another widget is used.",
                "False.",
                "True, but only for the one script run immediately following the click.",
                "1"
            ],
            "answer": "True, but only for the one script run immediately following the click.",
            "explanation": "`st.button` is a momentary trigger. It returns True only for the single rerun caused by its click, and then it reverts to False."
        },
        "3. Which widget would be the most appropriate for allowing a user to select one of five predefined machine learning models?": {
            "options": [
                "st.slider",
                "st.text_input",
                "st.selectbox",
                "st.button"
            ],
            "answer": "st.selectbox",
            "explanation": "`st.selectbox` is ideal for situations where a user must choose one option from a predefined list, preventing typos and invalid entries."
        },
        "4. What is the primary purpose of the `key` parameter (e.g., `st.slider('My Slider', key='my_key')`)?": {
            "options": [
                "To set the widget's default value.",
                "To provide a help tooltip for the user.",
                "To change the color of the widget.",
                "To give the widget a unique, stable identifier, especially for use with Session State."
            ],
            "answer": "To give the widget a unique, stable identifier, especially for use with Session State.",
            "explanation": "The `key` is crucial for uniquely identifying a widget. This prevents errors when multiple widgets might have the same label and is the mechanism by which its value can be accessed via `st.session_state`."
        },
        "5. You want to let a user enter their full street address. Which widget is the best choice?": {
            "options": [
                "st.text_area",
                "st.selectbox",
                "st.slider",
                "st.text_input"
            ],
            "answer": "st.text_area",
            "explanation": "While `st.text_input` is for single lines of text, `st.text_area` is designed for multi-line freeform text, making it perfect for addresses or longer comments."
        }
    }

    for i, (question, details) in enumerate(questions.items()):
        st.subheader(f"Question {i+1}")
        st.markdown(f"**{question}**")
        user_answer = st.radio(
            "Select your answer:",
            details["options"],
            key=f"q_{i}",
            label_visibility="collapsed"
        )

        if st.button(f"Check Answer for Question {i+1}", key=f"check_{i}"):
            if user_answer == details["answer"]:
                st.success(f"**Correct!** {details['explanation']}")
            else:
                st.error(f"**Incorrect.** The correct answer is: **'{details['answer']}'.** {details['explanation']}")
        st.markdown("---")