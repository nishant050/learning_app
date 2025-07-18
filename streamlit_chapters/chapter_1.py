# streamlit_chapters/chapter_1.py

import streamlit as st
import urllib.parse
from time import sleep

# Per the design guide, this helper function should be in a central utils file.
# It is included here for completeness of this single-file example.
def image_search_button(label, search_term):
    """Creates a Streamlit link button that searches Google Images in a new tab."""
    encoded_term = urllib.parse.quote_plus(search_term)
    url = f"https://www.google.com/search?q={encoded_term}&tbm=isch"
    st.link_button(f"🖼️ See images of: {label}", url, use_container_width=True)

def render():
    """
    This function renders Chapter 1 of the Streamlit Saga, meticulously following
    the LESSON_DESIGN_GUIDE.md (Version 3.1).
    """

    # ======================================================================================
    # PART 1: THE CORE IDEA (THE ANALOGY)
    # Goal: Build profound, culturally-grounded intuition for Streamlit.
    # Analogy: The Indian Thali - a complete, satisfying meal from simple, distinct parts.
    # ======================================================================================

    st.header("Part 1: The Core Idea - Your First App as a Digital Thali", divider="rainbow")
    st.markdown("""
    Imagine you are tasked with preparing a grand feast, a *Bhoj*, for a respected guest. Your guest is a data scientist, a historian, a poet—someone with a hunger for knowledge. You could spend days, even weeks, mastering complex culinary arts, learning intricate recipes from ancient texts, and sourcing exotic ingredients. That is the path of traditional web development—powerful, yes, but immensely time-consuming, like preparing a formal, multi-course French meal.

    But what if there was another way? A path of elegant simplicity and rapid creation?

    Think of preparing a magnificent Indian Thali.

    A Thali is a masterpiece of composition. It’s a full, balanced, and deeply satisfying meal presented on a single platter. You have a central serving of rice or roti. Surrounding it are small bowls, the *katoris*, each holding a different, delicious preparation: a dal, a sabzi, a raita, a pickle, and a sweet dish. Each *katori* holds something simple, prepared with a clear purpose. The dal is comforting, the pickle is sharp, the sabzi is nutritious, the sweet is celebratory. Individually, they are simple. Together, they form a complete, harmonious experience that is far greater than the sum of its parts. The guest can enjoy a little of everything, moving from one flavor to another, creating their own unique culinary journey.

    **This is the soul of Streamlit.**

    Streamlit is your digital Thali platter. It allows you to take your individual "dishes"—a piece of data, a plot, a nugget of text, a user input—and arrange them effortlessly into a beautiful, interactive web application. You don't need to be a master chef (a traditional web developer) to do this. If you know Python, you already know how to prepare the individual dishes.

    - Your data analysis script is the **Dal Tadka**—hearty and fundamental.
    - Your Matplotlib or Plotly chart is the vibrant **Vegetable Jalfrezi**—colorful and insightful.
    - A simple text explanation is the comforting **Jeera Rice**—the base that holds everything together.
    - A button or a slider for user interaction is the tangy **Aam ka Achaar** (mango pickle)—it adds a kick and changes the experience of the other dishes.
    - A title for your app is the formal invitation to the feast itself.

    With just a few simple commands, you place each of these prepared items onto your platter. `st.title()` draws the invitation. `st.write()` serves the rice. `st.pyplot()` presents the colorful sabzi. `st.button()` offers the pickle. Before you know it, you have arranged a full, interactive experience for your guest. You've built a web app not in weeks, but in minutes. You have served a digital Thali.

    This chapter is your invitation to become a master of the digital kitchen. We will start with the simplest of platters and the most basic of dishes. By the end, you will know how to arrange your own simple Thali, a complete web application, ready to serve to the world.
    """)
    image_search_button("A traditional Indian Thali", "indian thali meal")
    st.markdown("---")


    # ======================================================================================
    # PART 2: THE MECHANISM (INTERACTIVE DISCOVERY)
    # Goal: Allow the user to "feel" how simple commands build a script.
    # Method: An interactive "code builder" that generates a script based on user toggles.
    # ======================================================================================

    st.header("Part 2: The Mechanism - Assembling Your Thali", divider="rainbow")
    st.markdown("""
    Let's move from philosophy to practice. How do you actually place a *katori* on the Thali? In Streamlit, this is done with simple, intuitive commands. Each command is like a specific instruction to your kitchen staff: "Place the title here," "Serve the chart now."

    Here, we have a simple interactive "Code Kitchen." As you select different elements for your app, you will see the corresponding Python code being assembled in real-time. This isn't a working app *yet*—it's a dynamic recipe being written before your eyes.

    **Your Task:** Experiment by turning these switches on and off. Observe how each selection adds a clean, readable line to the script. Notice the pattern. This is your first taste of the cause-and-effect at the heart of Streamlit.
    """)

    st.subheader("Interactive Code Kitchen")
    c1, c2 = st.columns([1, 1.2])

    with c1:
        st.markdown("##### Choose Your App's Ingredients:")
        use_title = st.toggle("Add a Title", value=True)
        use_header = st.toggle("Add a Header")
        use_text = st.toggle("Add some descriptive text", value=True)
        use_button = st.toggle("Add a button")
        use_balloons = st.toggle("Make the button celebratory!")

    with c2:
        st.markdown("##### Your Dynamically Generated Script:")
        code_body = "import streamlit as st\n\n"
        if use_title:
            code_body += '# This command adds a big, bold title at the top.\nst.title("My Grand Feast App")\n\n'
        if use_header:
            code_body += '# A header is like a section title.\nst.header("The Main Course")\n\n'
        if use_text:
            code_body += '# Use st.write() for most text, like an explanation.\nst.write("Welcome to my Thali! Here are the delicious items.")\n\n'
        if use_button:
            code_body += '# st.button() creates a button. It returns True when clicked.\nif st.button("Celebrate!"):\n'
            if use_balloons:
                code_body += '    # This line runs ONLY when the button is clicked.\n    st.balloons()\n'
            else:
                code_body += '    # This line runs ONLY when the button is clicked.\n    st.write("Hooray!")\n'

        st.code(code_body, language="python")

    st.markdown("""
    **Observations to Guide You:**
    1.  **Readability:** Can you read the generated code and guess what it does, even without knowing Python deeply? This is a core principle of Streamlit. The function names (`title`, `header`, `write`) are self-explanatory.
    2.  **Simplicity:** Notice how it's just one line for one element. There's no complex setup, no "boilerplate" code to copy-paste. You ask for a title, you get a title.
    3.  **The 'if' statement:** Look closely at the button code. The action (`st.balloons()` or `st.write("Hooray!")`) is *inside* an `if` block. This is the fundamental mechanism of interactivity in Streamlit. The code literally says: "**if** the user clicks the 'Celebrate!' button, **then** do the fun thing." Your app is a script that re-runs from top to bottom every time you interact with it. We will explore this profound idea more in the next sections.
    """)
    st.markdown("---")


    # ======================================================================================
    # PART 3: THE GALLERY (SHOWCASING VARIETY)
    # Goal: Demonstrate the different "flavors" of basic Streamlit widgets.
    # Method: Interactive tabs for key components, with sub-analogies and image buttons.
    # ======================================================================================

    st.header("Part 3: The Gallery - The Katoris of Your Digital Thali", divider="rainbow")
    st.markdown("""
    A good Thali has variety. A bland meal with five bowls of the same dal would be terribly boring! Streamlit offers a rich variety of 'widgets'—the interactive elements—to serve your content in. Let's explore the most fundamental ones. Each is a different *katori* you can place on your platter.
    """)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📜 st.write()",
        "👑 st.title()",
        "💬 st.text_input()",
        "✅ st.checkbox()",
        "🎚️ st.slider()"
    ])

    with tab1:
        st.subheader("The All-Purpose Katori: `st.write()`")
        st.markdown("""
        **Sub-Analogy:** Think of `st.write()` as the bowl of **Dal or Plain Rice**. It's the versatile, foundational element. You can put almost anything in it, and it will present it sensibly.

        The `st.write()` command is the swiss-army knife of Streamlit. It's intelligent. You can give it text, numbers, DataFrames (like spreadsheets), and even charts, and it will do its best to render it correctly. It is your default choice for displaying information.
        """)
        st.code('import streamlit as st\n\nst.write("Hello, world! This is the start of my app.")\nst.write(42)\nst.write("You can mix text and numbers.")', language="python")
        image_search_button("A comforting bowl of Dal", "dal fry bowl")


    with tab2:
        st.subheader("The Grand Entrance: `st.title()` & `st.header()`")
        st.markdown("""
        **Sub-Analogy:** These are the **Grand Archway and Welcome Banner** at the entrance of your feast. They announce the purpose of the event in a bold and unmissable way.

        Every app needs a clear beginning. `st.title()` creates the main, top-level title for your page. It should be used only once per page. `st.header()` is used to break your app into logical sections, like chapters in a book.
        """)
        st.code('import streamlit as st\n\nst.title("The Ultimate Cricket Analysis Dashboard")\nst.header("Section 1: Virat Kohli\'s Performance")\nst.write("In this section, we analyze the run-scoring patterns...")\n\nst.header("Section 2: Jasprit Bumrah\'s Bowling Magic")\nst.write("Here, we focus on the bowler\'s economy and wicket-taking ability...")', language="python")
        image_search_button("A decorated Indian wedding archway", "indian wedding archway")

    with tab3:
        st.subheader("The Conversation Starter: `st.text_input()`")
        st.markdown("""
        **Sub-Analogy:** This is like asking your guest, **"What is your name?"** or "What city are you from?". It's a way to get information *from* them to personalize their experience.

        Interactivity begins when the user can give something back to the app. `st.text_input()` displays a box where the user can type. Whatever they type is stored in a variable in your Python script, which you can then use.
        """)
        st.code('import streamlit as st\n\nst.title("Personalized Greeting App")\n\nuser_name = st.text_input("Please enter your name:", "Guest")\n\nst.write(f"Namaste, {user_name}!")', language="python")
        image_search_button("A friendly conversation", "two people talking india")

    with tab4:
        st.subheader("The Simple Choice: `st.checkbox()`")
        st.markdown("""
        **Sub-Analogy:** This is like asking your guest a simple yes/no question, like **"Would you like extra ghee on your roti?"**. Their choice is a clear, binary decision.

        A checkbox is perfect for turning a feature on or off. When the box is checked, the function returns `True`; otherwise, it returns `False`. You can use this in an `if` statement to conditionally show or hide other elements in your app.
        """)
        st.code('import streamlit as st\n\nst.title("Data Explorer")\n\nif st.checkbox("Show raw data table"):\n    st.write("Here is the raw data you requested...")\n    # (code to display a data table would go here)', language="python")
        image_search_button("A simple checkbox", "checkbox icon")


    with tab5:
        st.subheader("The Spice Meter: `st.slider()`")
        st.markdown("""
        **Sub-Analogy:** This is like a **Spice Meter** where your guest can choose how spicy they want their food, on a scale from 'Mild' to 'Extra Hot'. It allows for a nuanced choice within a defined range.

        A slider is a fantastic way to let users select a number from a range. You can define the minimum value, the maximum value, and a starting point. The chosen value is stored in a variable for you to use in calculations or to filter data.
        """)
        st.code('import streamlit as st\n\nst.title("Loan Calculator")\n\ninvestment_years = st.slider(\n    "How many years do you want to invest for?",\n    min_value=1, \n    max_value=30, \n    value=10, # The default starting position\n    step=1\n)\n\nst.write(f"Calculating returns for an investment period of {investment_years} years.")', language="python")
        image_search_button("A variety of Indian spices", "indian spices variety")

    st.markdown("---")


    # ======================================================================================
    # PART 4: THE FORMALIZATION (THE GANITA SHASTRA)
    # Goal: Bridge intuition to formal language, providing significant depth.
    # Method: Explain the core concepts (run command, script flow, import) and the "dharma."
    # ======================================================================================

    st.header("Part 4: The Formalization - The 'Ganita Shastra' of Streamlit", divider="rainbow")
    st.markdown("""
    We have seen the analogy (the Thali) and felt the mechanism (the Code Kitchen). Now it is time to understand the *Shastra*—the formal rules and principles that govern the world of Streamlit. This is the 'Dharma' of the framework, the fundamental truth that makes it all work.

    ### The Sacred Invocation: `import streamlit as st`
    Every Python script that wishes to use the power of Streamlit must begin with this line:
    ```python
    import streamlit as st
    ```
    Think of this as chanting a mantra to invoke a deity. You are telling Python, "I wish to invoke the library named `streamlit`, and I will refer to it by the shorter, conventional name `st`." Every Streamlit command you issue will be prefixed with `st.`, like `st.title()`, `st.write()`, and so on. This is a non-negotiable first step.

    ### The Ritual of Execution: `streamlit run`
    A Python script is just a text file. A Streamlit app is a living, interactive experience. The magic that transforms one into the other is a command you type not in Python, but in your computer's terminal (like Command Prompt or PowerShell on Windows, or Terminal on Mac/Linux).

    If you save your script as a file, for example `my_first_app.py`, you would navigate to that file's directory in your terminal and execute the following command:
    ```bash
    streamlit run my_first_app.py
    ```
    This command does two things:
    1.  It starts a local web server on your computer.
    2.  It opens a new tab in your web browser pointing to that server, where your app is now running.

    This command is the ceremonial act that brings your creation to life.

    ### The Core Dharma: The Top-to-Bottom Rerun
    This is the most important concept to grasp. It is the central law of the Streamlit universe.

    **Every time a user interacts with a widget (like clicking a button or moving a slider), your entire Python script runs again from top to bottom.**

    Let's reflect on this. It seems inefficient, doesn't it? Why rerun everything?

    This is the genius of Streamlit's design. By embracing this simple model, it eliminates the immense complexity of "state management," "callbacks," and "event handlers" that plague traditional web frameworks. You don't have to write complex logic to decide *what part* of the app needs to update. You simply write your script as if it's a single, straight-line report.

    Consider this code:
    ```python
    import streamlit as st

    name = st.text_input("Enter your name", "Bhuvan")
    st.write(f"Hello, {name}")

    if st.checkbox("Show celebration"):
        st.balloons()
    ```
    **Execution Flow:**
    1.  **Initial Run:** The script runs. It shows a text box with "Bhuvan" and prints "Hello, Bhuvan". It shows a checkbox.
    2.  **User types "Priya" in the box:** The script **re-runs from the top**.
        - `name = st.text_input(...)`: This time, `st.text_input` knows the user just typed "Priya", so it assigns the string `"Priya"` to the `name` variable.
        - `st.write(f"Hello, {name}")`: This line now executes as `st.write("Hello, Priya")`. The output on the screen updates automatically.
        - The checkbox is checked, and the script ends.
    3.  **User clicks the checkbox:** The script **re-runs from the top**.
        - `name = st.text_input(...)`: The value is still "Priya", so `name` becomes `"Priya"`.
        - `st.write(...)`: It prints "Hello, Priya" again.
        - `if st.checkbox(...)`: This time, the checkbox function returns `True`. The `if` block executes, and `st.balloons()` makes balloons appear on the screen.

    This top-to-bottom rerun is the "dharma" you must internalize. Your script is not a static thing; it's a dynamic recipe that is re-cooked with fresh ingredients (user inputs) every single time there's an interaction. This makes coding feel like simple scripting, which is Streamlit's superpower.
    """)
    st.markdown("---")

    # ======================================================================================
    # PART 5: THE APPLICATION (THE GAMES & PUZZLES)
    # Goal: Solidify understanding through active, goal-oriented problem-solving.
    # Method: Three distinct mini-games in tabs, wrapped in relatable scenarios.
    # ======================================================================================

    st.header("Part 5: The Application - Puzzles from the Digital Kitchen", divider="rainbow")
    st.markdown("""
    Knowledge becomes wisdom only through practice. It's time to get your hands dirty and apply the principles you've learned. Here are three small challenges. The goal is not just to get them right, but to understand *why* the solution works. Each puzzle is presented with the expected output. Your task is to write the code that produces it.
    """)

    game1, game2, game3 = st.tabs([
        "📜 The Shopkeeper's Welcome Sign",
        "🗳️ The Village Election Poll",
        "🌶️ The Chef's Spice Selector"
    ])

    with game1:
        st.subheader("Challenge 1: The Shopkeeper's Welcome Sign")
        st.markdown("""
        **Scenario:** A local artisan in Jaipur wants a simple app for her shop entrance. She wants it to greet customers by name.

        **Task:** Create an app that displays a title, asks for the customer's name, and then prints a personalized welcome message.

        **Expected Output:**
        """)
        st.info("""
        **Jaipur Gems & Crafts**

        (A text box appears here asking for a name)

        *Welcome to our shop, [Customer's Name]!*
        """)
        with st.expander("Show Solution"):
            st.code("""
import streamlit as st

st.title("Jaipur Gems & Crafts")

customer_name = st.text_input("What is your name?", "Friend")

st.write(f"*Welcome to our shop, {customer_name}!*")
            """, language="python")


    with game2:
        st.subheader("Challenge 2: The Village Election Poll")
        st.markdown("""
        **Scenario:** The village of Ramgarh is holding a mock election to see which development project is more popular: a new School or a new Hospital.

        **Task:** Create an app with a header and two buttons, one for each option. When a button is clicked, it should display a confirmation message.

        **Expected Output:**
        """)
        st.info("""
        **Ramgarh Development Poll**

        What should we build next?

        [Button: "Vote for School"] [Button: "Vote for Hospital"]

        *(When a button is clicked, a message like "Thank you for voting for the School!" appears)*
        """)
        with st.expander("Show Solution"):
            st.code("""
import streamlit as st

st.header("Ramgarh Development Poll")
st.write("What should we build next?")

col1, col2 = st.columns(2)

with col1:
    if st.button("Vote for School"):
        st.success("Thank you for voting for the School!")

with col2:
    if st.button("Vote for Hospital"):
        st.success("Thank you for voting for the Hospital!")
# Note: Using st.columns is a neat way to place buttons side-by-side!
            """, language="python")


    with game3:
        st.subheader("Challenge 3: The Chef's Spice Selector")
        st.markdown("""
        **Scenario:** A chef at a famous Bengaluru restaurant wants to let customers choose the spice level of their curry using a digital menu. The spice level can range from 1 (very mild) to 10 (extremely spicy).

        **Task:** Create an app with a slider to select a spice level. The app should display the chosen level.

        **Expected Output:**
        """)
        st.info("""
        **Curry Spice Level**

        (A slider appears here, from 1 to 10)

        *You have selected a spice level of: [Selected Level]*
        """)
        with st.expander("Show Solution"):
            st.code("""
import streamlit as st

st.subheader("Curry Spice Level")

spice_level = st.slider("Select your desired spice level:", 1, 10, 5)

st.write(f"**You have selected a spice level of: {spice_level}**")
            """, language="python")

    st.markdown("---")


    # ======================================================================================
    # PART 6: THE HORIZON (THE JNANA-CHAKSHU - EYE OF KNOWLEDGE)
    # Goal: Motivate by revealing the concept's power and teasing the next chapter.
    # ======================================================================================

    st.header("Part 6: The Horizon - The 'Jnana-Chakshu' (Eye of Knowledge)", divider="rainbow")
    st.markdown("""
    You have successfully assembled your first Digital Thali. You started with a simple idea, arranged your components, and served a complete, interactive experience. Do not underestimate the power of what you have learned. While these examples are simple, they are the fundamental building blocks of applications that are changing industries.

    **Where this Power is Used:**
    *   **The ISRO Scientist:** An engineer quickly builds a dashboard to visualize telemetry data from a satellite launch, using sliders to scrub through time and checkboxes to toggle different data streams. This isn't for the public; it's a quick, internal tool that helps them understand complex data in minutes, not days.
    *   **The Fin-Tech Analyst in Mumbai:** A financial analyst who knows Pandas (a data analysis library) but not web development can wrap her latest stock market model in a Streamlit app. She can add text inputs for stock tickers and sliders for risk tolerance, turning her static analysis into an interactive tool for her team.
    *   **The Aspiring Data Scientist in Bengaluru:** A student builds a personal project to showcase their skills to recruiters. Instead of just showing a Jupyter Notebook on GitHub, they deploy a Streamlit app where the recruiter can interact with their machine learning model, instantly demonstrating the real-world value of their work.

    **The Key Takeaway:** The profound insight of this chapter is that **you can now build a web application.** It might be simple, but the barrier between your Python script and an interactive web experience has been shattered. You no longer need to wait for a "web developer" to show your work to the world. You can do it yourself.

    You have learned to arrange the *katoris* on the Thali. You can serve text, get input, and react to simple choices. But what about the main course? How do you display complex data tables? How do you create beautiful, interactive plots and charts? How do you structure your app into multiple pages?

    That is the journey for our next chapter. We will move beyond the basic dishes and learn to prepare the feast's centerpiece: **Data and Visuals**. Prepare to unlock the true power of Streamlit by making your data dance.
    """)
    st.markdown("---")


    # ======================================================================================
    # PART 7: THE CHECK-UP (THE PARIKSHA)
    # Goal: Provide a robust self-assessment covering the lesson's full depth.
    # Method: 5-7 concise multiple-choice questions with clear feedback.
    # ======================================================================================

    st.header("Part 7: The Check-up - The 'Pariksha'", divider="rainbow")
    st.markdown("Time to test your understanding. Choose the best answer for each question.")

    questions = [
        {
            "q": "1. What is the core analogy used to describe Streamlit's philosophy in this chapter?",
            "options": ["A complex multi-course French meal", "Building a house brick by brick", "Assembling a balanced and modular Indian Thali", "Writing a long epic poem"],
            "answer": "Assembling a balanced and modular Indian Thali",
            "feedback": "Correct! The Thali analogy represents how Streamlit lets you quickly assemble a complete app from simple, individual components (`st.write`, `st.button`, etc.), just like arranging different dishes in a thali."
        },
        {
            "q": "2. What is the command you type in your terminal to bring your Streamlit script to life?",
            "options": ["`python my_app.py`", "`start streamlit my_app.py`", "`streamlit run my_app.py`", "`render app my_app.py`"],
            "answer": "`streamlit run my_app.py`",
            "feedback": "Exactly. The `streamlit run` command is the special instruction that starts the Streamlit server and executes your Python script as an interactive web application."
        },
        {
            "q": "3. What is the 'Core Dharma' or the most fundamental principle of how a Streamlit app works?",
            "options": ["Only the changed element on the page is updated.", "The script runs once and then waits for events.", "The entire script re-runs from top to bottom on every user interaction.", "You must manually define which functions to call for each widget."],
            "answer": "The entire script re-runs from top to bottom on every user interaction.",
            "feedback": "This is the most critical concept. This top-to-bottom rerun model is what makes Streamlit so simple. You don't manage state or callbacks; you just write a script that reacts to the latest user inputs on each run."
        },
        {
            "q": "4. If you want to add a main, top-level title to your app, which command is most appropriate?",
            "options": ["`st.write('My Title')`", "`st.header('My Title')`", "`st.title('My Title')`", "`st.markdown('# My Title')`"],
            "answer": "`st.title('My Title')`",
            "feedback": "Correct. While other commands can create large text, `st.title()` is specifically designed for the main, single title of an application, conveying semantic importance."
        },
        {
            "q": "5. A user interacts with a slider in your app. What happens to a variable assigned from a `st.text_input` that the user already filled out?",
            "options": ["It is reset to its default value.", "It keeps the value the user typed because the script re-runs and `st.text_input` preserves its state.", "The script crashes because two widgets cannot have state.", "It becomes empty."],
            "answer": "It keeps the value the user typed because the script re-runs and `st.text_input` preserves its state.",
            "feedback": "That's right. During the rerun, Streamlit is smart. `st.text_input` (and other widgets) remembers its last state (the text the user typed) and will assign that same value to your variable on subsequent reruns, unless the user changes it."
        }
    ]

    for i, item in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.markdown(item["q"])
        user_answer = st.radio(f"Select your answer for question {i+1}:", item["options"], key=f"q{i}", label_visibility="collapsed")

        if f"submitted_q{i}" in st.session_state and st.session_state[f"submitted_q{i}"]:
            if st.session_state[f"user_answer_q{i}"] == item["answer"]:
                st.success(f"**Correct!** {item['feedback']}")
            else:
                st.error(f"**Not quite.** The correct answer is: **{item['answer']}**. \n\n*Reasoning:* {item['feedback']}")

    # Use a single button to check all answers
    if st.button("Submit My Answers", use_container_width=True):
        for i, item in enumerate(questions):
            # Retrieve the answer from the radio button's state
            user_answer = st.session_state[f"q{i}"]
            # Store it in the session state to persist after the rerun
            st.session_state[f"user_answer_q{i}"] = user_answer
            st.session_state[f"submitted_q{i}"] = True
        st.rerun()