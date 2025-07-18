# streamlit_chapters/chapter_5.py

import streamlit as st
import time

# Assuming the image_search_button is in utils/plotting.py as per the guide
# from utils.plotting import image_search_button 
# For this self-contained example, we'll define it here.
import urllib.parse

def image_search_button(label, search_term, use_container_width=True):
    """Creates a Streamlit link button that searches Google Images in a new tab."""
    encoded_term = urllib.parse.quote_plus(search_term)
    url = f"https://www.google.com/search?q={encoded_term}&tbm=isch"
    st.link_button(f"🖼️ See images of: {label}", url, use_container_width=use_container_width)

def render():
    """
    Renders Chapter 5: The App's Memory - Understanding Session State.
    This chapter is a deep, narrative-driven exploration designed to be a cornerstone
    of the Streamlit learning journey, following the rigorous LESSON_DESIGN_GUIDE.md.
    """

    #================================================================================
    # METADATA & HEADER
    #================================================================================
    st.title("🧠 Chapter 5: The App's Memory - Understanding Session State")
    st.markdown("---")


    #================================================================================
    # PART 1: THE CORE IDEA (THE ANALOGY)
    #================================================================================
    st.markdown("## Part 1: The Brahma-Kamala of Memory - Our Akshaya Patra")

    st.markdown("""
    Before we write a single line of code, let us embark on a story. A story from the grand epic, the Mahabharata, that holds the very essence of the concept we are about to master.

    Imagine the Pandavas, living in exile in the forest. They are noble princes, but now they are humble hermits. They have guests, learned sages and rishis, who visit them. But how does one host a guest in a forest with no kingdom, no treasury, no granary? A deep worry creases Yudhisthira's brow. To fail to show hospitality is a great adharma.

    Seeing his plight, Yudhisthira prays to Surya, the Sun God. Pleased with his devotion, Surya grants him a divine vessel: the **Akshaya Patra**, the *Inexhaustible Vessel*.
    """)

    image_search_button("Akshaya Patra Mahabharata", "Akshaya Patra Mahabharata story")

    st.markdown("""
    This vessel was not ordinary. It had a magical property. Every day, Draupadi could serve food from it to any number of guests. The vessel would never become empty. It would continuously produce food until she herself had taken her meal for the day. Once she ate, the vessel would be exhausted until the next sunrise.

    Now, think about this beautiful concept. Each day is a new beginning, a 'reset'. And yet, the Akshaya Patra is there, ready to provide. It *remembers* its duty. It *holds* its bounty across the day, no matter how many sages come and go.

    **This is the very heart of Streamlit's Session State.**

    Every time a user clicks a button or moves a slider in your app, Streamlit does something that might surprise you: **it re-runs your entire Python script from top to bottom.** It's like a new sunrise. Every variable you created is wiped clean and re-initialized. Your `count = 0` is always `count = 0` at the start of each run. Your app, by default, has the memory of a goldfish. It's perpetually a new day, with an empty kitchen.

    This is where `st.session_state` comes in. It is our Akshaya Patra.

    `st.session_state` is a special, magical container that Streamlit gives us. It is **not** wiped clean on every re-run. It persists. It endures. It holds whatever we put inside it, safe from the constant cycle of script re-runs. It allows our app to have a *memory within a single user session*. It's how our app can remember the user's name, the items in their shopping cart, or their score in a game, even as they click around and cause the script to re-run dozens of times.

    In this chapter, we will learn how to receive this divine vessel. We will learn how to store our data within it, how to retrieve that data, and how to use it to build applications that are not just interactive, but intelligent, responsive, and truly stateful. We are about to give our app a memory, a consciousness. We are about to give it its own Akshaya Patra.
    """)
    st.markdown("---")


    #================================================================================
    # PART 2: THE MECHANISM (INTERACTIVE DISCOVERY)
    #================================================================================
    st.markdown("## Part 2: Feeling the Forgetting, Seeing the Remembering")
    st.markdown("""
    Words and analogies can take us far, but to truly understand, we must feel. Let's build two simple worlds side-by-side. The first world is a standard Streamlit app with no memory. The second world has been gifted the Akshaya Patra of `st.session_state`.

    Your goal is simple: try to make the counter in each world go up.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("World 1: The Land of Forgetfulness")
        st.markdown("In this world, we create a variable `count = 0` and increment it when you click the button. Observe what happens.")

        # The "forgetful" counter
        count_no_state = 0
        if st.button("Increment in the Forgetful World", use_container_width=True):
            count_no_state += 1
        st.metric("Counter Value", count_no_state)
        st.info("Notice that no matter how many times you click, the counter never gets past 1. This is because every click re-runs the script, and the line `count_no_state = 0` is executed every single time. The app forgets its past instantly.")
        
        with st.expander("Show me the code for the Forgetful World"):
            st.code("""
import streamlit as st

st.subheader("The Land of Forgetfulness")

# This line runs EVERY single time you interact with the app
count_no_state = 0 

if st.button("Increment"):
    count_no_state += 1

st.metric("Counter Value", count_no_state)
            """, language="python")

    with col2:
        st.subheader("World 2: The Land of the Akshaya Patra")
        st.markdown("Here, we will use `st.session_state` to hold our counter. Watch the difference.")

        # Initialize the state, this is the "prayer to Surya"
        if 'count_with_state' not in st.session_state:
            st.session_state.count_with_state = 0

        if st.button("Increment in the Rememberful World", use_container_width=True):
            st.session_state.count_with_state += 1
        
        st.metric("Counter Value", st.session_state.count_with_state)
        st.success("It works! The `st.session_state` object persists across re-runs. The initialization line is inside an `if` block, so it only runs ONCE at the very beginning of the session. The memory is preserved.")

        with st.expander("Show me the code for the Rememberful World"):
            st.code("""
import streamlit as st

st.subheader("The Land of the Akshaya Patra")

# This `if` block runs its contents only ONCE per session!
# This is how we place the 'food' in our vessel for the first time.
if 'count_with_state' not in st.session_state:
    st.session_state.count_with_state = 0

if st.button("Increment"):
    # We read from and write to the session_state object
    st.session_state.count_with_state += 1

st.metric("Counter Value", st.session_state.count_with_state)
            """, language="python")

    st.markdown("### The Grand Reveal: Look Inside the Akshaya Patra")
    st.markdown("What *is* this `st.session_state` object? Let's peek inside. It's just like a Python dictionary! Below, we print the entire `st.session_state` object. Watch how it changes as you interact with the widgets above and others we will add.")
    
    st.write("---")
    st.subheader("Contents of `st.session_state`:")
    st.json(st.session_state)
    st.caption("Try clicking the 'Rememberful World' button and see the `count_with_state` value update here in real-time.")
    st.markdown("---")

    #================================================================================
    # PART 3: THE GALLERY (SHOWCASING VARIETY)
    #================================================================================
    st.markdown("## Part 3: The Many Rooms of the Palace of Memory")
    st.markdown("""
    The Akshaya Patra can hold more than just one dish. `st.session_state` can hold many different pieces of information, each with its own purpose. Let's explore some common patterns, like walking through the different rooms of a grand palace, each with its own treasure.
    """)

    gallery_tabs = st.tabs([
        "Room 1: The Personal Greeter", 
        "Room 2: The Multi-Step Wizard", 
        "Room 3: The Toggled View"
    ])

    with gallery_tabs[0]:
        st.subheader("The Personal Greeter: Remembering the User")
        st.markdown("A great host remembers their guest's name. A great app remembers its user. This is one of the most common and powerful uses of session state: personalization.")
        st.markdown("In this example, we ask for the user's name once. If they haven't told us their name yet, we show them a text box. Once they enter it, we store it in `st.session_state` and greet them personally on every subsequent re-run.")

        if 'user_name' not in st.session_state:
            st.session_state.user_name = ""

        if st.session_state.user_name == "":
            st.text_input("What is your name, traveler?", key="user_name_input")
            if st.button("Submit Name"):
                # Transfer from the widget's state key to our desired state key
                st.session_state.user_name = st.session_state.user_name_input
                st.rerun() # Rerun to update the UI immediately
        else:
            st.success(f"### Welcome back, {st.session_state.user_name}!")
            st.write("Notice how the input box is gone. The app *remembers* you now.")
            if st.button("Forget My Name"):
                del st.session_state.user_name # We can delete keys too!
                st.rerun()
        
        image_search_button("Traditional Indian Welcome 'Namaste'", "Namaste welcome")


    with gallery_tabs[1]:
        st.subheader("The Multi-Step Wizard: A Journey, Not a Race")
        st.markdown("Have you ever filled out a long form online? A good one takes you step-by-step. This prevents overwhelm and feels like a guided journey. `st.session_state` is the thread that connects these steps.")
        st.markdown("Here, we simulate a 3-step user registration. The information from Step 1 and 2 must be remembered to complete Step 3.")
        
        # Initialize the step and the data storage
        if 'wizard_step' not in st.session_state:
            st.session_state.wizard_step = 1
            st.session_state.user_data = {}

        if st.session_state.wizard_step == 1:
            st.info("Step 1: Personal Details")
            with st.form("step1_form"):
                name = st.text_input("Name")
                submitted = st.form_submit_button("Next")
                if submitted and name:
                    st.session_state.user_data['name'] = name
                    st.session_state.wizard_step = 2
                    st.rerun()
        
        elif st.session_state.wizard_step == 2:
            st.info("Step 2: Contact Information")
            with st.form("step2_form"):
                email = st.text_input("Email")
                submitted = st.form_submit_button("Next")
                if submitted and email:
                    st.session_state.user_data['email'] = email
                    st.session_state.wizard_step = 3
                    st.rerun()

        elif st.session_state.wizard_step == 3:
            st.info("Step 3: Confirmation")
            st.success("Registration Complete!")
            st.write("We have gathered the following information, remembered across multiple steps:")
            st.json(st.session_state.user_data)
        
        if st.button("Start Over"):
            st.session_state.wizard_step = 1
            st.session_state.user_data = {}
            st.rerun()

        image_search_button("Saptapadi seven steps Hindu wedding", "Saptapadi ritual")
        st.caption("Just like the seven sacred steps of the Saptapadi, each step in our wizard builds upon the last, held together by a sacred bond - in our case, `st.session_state`.")


    with gallery_tabs[2]:
        st.subheader("The Toggled View: Remembering a Choice")
        st.markdown("Often, you want to give the user a choice and have the app respect that choice throughout their session. For example, 'Dark Mode vs Light Mode', or in our case, 'Simple View vs Detailed View'.")
        st.markdown("We'll use a boolean (True/False) flag in `st.session_state` to remember this preference.")

        if 'detailed_view' not in st.session_state:
            st.session_state.detailed_view = False
        
        st.write("Current View Mode:", "**Detailed**" if st.session_state.detailed_view else "**Simple**")

        if st.button("Toggle View Mode"):
            st.session_state.detailed_view = not st.session_state.detailed_view
            st.rerun()

        st.markdown("---")
        st.subheader("Your Data Report")
        st.write("This is the simple summary of the report.")
        
        if st.session_state.detailed_view:
            st.warning("Displaying Detailed View because the memory flag is set to True.")
            st.write("Here is some extra, super-detailed information that you requested:")
            st.dataframe({
                'Metric': ['User Engagement', 'Bounce Rate', 'Conversion'],
                'Value': ['85%', '23%', '4.5%'],
                'Trend': ['+5%', '-2%', '+0.5%']
            })
        
        image_search_button("Ardhanarishvara half male half female", "Ardhanarishvara")
        st.caption("Like Ardhanarishvara, who holds two forms in one, our app holds two states (Simple/Detailed) and can switch between them, remembering which one to display.")
    
    st.markdown("---")


    #================================================================================
    # PART 4: THE FORMALIZATION (THE GANITA SHASTRA)
    #================================================================================
    st.markdown("## Part 4: The Ganita Shastra - The Laws and Language of Memory")
    st.markdown("""
    We have felt the power of the Akshaya Patra. Now, let us become its master. We must learn the formal language, the *sutras* and principles that govern its behavior. This is the 'Ganita Shastra' (the Science of Calculation, or in our case, the Science of State).

    `st.session_state` behaves almost exactly like a standard Python dictionary. If you know how to use a dictionary, you are 90% of the way there. It is an object that stores key-value pairs.
    """)

    st.subheader("1. The Sutra of Initialization: The First Offering")
    st.markdown("""
    You cannot take food from an empty vessel. The first and most critical rule is: **you must initialize a key before you can use it.**

    The problem is that your script re-runs from top to bottom. A simple `st.session_state.my_variable = 0` will reset your variable on every single interaction. This defeats the purpose!

    The solution is the sacred initialization block we saw earlier. This is the single most important pattern in state management:
    """)
    st.code("""
# The Canonical Initialization Block
if 'my_key' not in st.session_state:
    st.session_state.my_key = 'my_initial_value'
    """, language="python")
    st.markdown("""
    **The Dharma (The Law):** This code says, "Look into the Akshaya Patra. Is there a dish called 'my_key'? If there isn't, and *only* if there isn't, create it and give it an initial value." Since this check happens on every re-run, the inner block is executed only on the very first run of the session, before 'my_key' exists. After that, the key is present, and the block is skipped, preserving the value within.
    """)

    st.subheader("2. The Sutra of Access: Reading and Writing")
    st.markdown("Once initialized, interacting with the state is beautifully simple. You can access values using two styles:")

    st.markdown("**Attribute Notation (The 'dot' method):**")
    st.code("""
# Reading
name = st.session_state.user_name

# Writing / Updating
st.session_state.counter += 1 
    """, language="python")

    st.markdown("**Dictionary Notation (The 'square bracket' method):**")
    st.code("""
# Reading
name = st.session_state['user_name']

# Writing / Updating
st.session_state['counter'] += 1
    """, language="python")
    st.info("While both work, the **attribute notation (`.key`) is more common** in Streamlit code for its cleanliness. However, if your key is a variable itself or contains spaces, you must use the dictionary notation.")

    st.subheader("3. The Sutra of Deletion: Emptying the Vessel")
    st.markdown("Sometimes, you need to make the app forget. We did this in the 'Personal Greeter' example. You can delete a key from the state, which is useful for resetting parts of your application.")
    st.code("""
# Using the 'del' keyword, just like with a dictionary
if st.button("Logout"):
    del st.session_state.user_name
    del st.session_state.logged_in
    """, language="python")

    st.subheader("4. The Hidden Magic: Widget Keys")
    st.markdown("""
    This is a subtle but powerful feature. **Every interactive widget in Streamlit can be connected directly to session state using the `key` argument.**

    When you write `st.text_input("Your name", key="my_input")`, Streamlit does two things automatically:
    1.  The value of the text input is now stored in `st.session_state.my_input`.
    2.  If `st.session_state.my_input` already has a value, the text input widget will initialize with that value.

    It's a two-way street! The widget updates the state, and the state sets the widget.
    """)
    st.code("""
import streamlit as st

# Initialize
if 'name' not in st.session_state:
    st.session_state.name = "Siddhartha"

# This text input is now directly linked to st.session_state.name
# It will display "Siddhartha" by default. If you type something
# new, st.session_state.name will be updated automatically!
st.text_input("Enter your name:", key="name")

st.write("The current value in session state is:", st.session_state.name)
    """, language="python")

    st.warning("**A Common Pitfall:** Be careful not to have two interactive widgets with the same `key` on the same page. This will cause an error, as Streamlit won't know which widget is the true source of the value.")
    st.markdown("---")


    #================================================================================
    # PART 5: THE APPLICATION (THE GAMES & PUZZLES)
    #================================================================================
    st.markdown("## Part 5: The Khel-Mandala - The Playground of Memory")
    st.markdown("""
    Knowledge, when not applied, is like a lamp that is not lit. Let's enter the *Khel-Mandala* (the playground or circle of games) to truly test our mastery of `st.session_state`. Each game is a unique puzzle that can only be solved with memory.
    """)

    game_tabs = st.tabs([
        "Game 1: The Spice Merchant's Inventory", 
        "Game 2: The Ashrama Escape Puzzle", 
        "Game 3: The Festive Shopping Cart"
    ])

    with game_tabs[0]:
        st.subheader("The Spice Merchant's Inventory")
        st.markdown("You are a spice merchant in a bustling bazaar. Customers are buying and you are restocking. Your reputation depends on not running out of your precious spices! **Your goal is to manage your inventory using `st.session_state` and fulfill an order.**")
        image_search_button("Indian Spice Market", "Khari Baoli spice market Delhi")

        # Initialize inventory
        if 'inventory' not in st.session_state:
            st.session_state.inventory = {'Cardamom': 20, 'Cloves': 50, 'Turmeric': 100}

        st.write("Your Current Inventory:")
        st.json(st.session_state.inventory)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("**Restock**")
            spice_to_add = st.selectbox("Select Spice to Restock", options=list(st.session_state.inventory.keys()), key="add_spice")
            qty_to_add = st.number_input("Quantity to Add", min_value=1, step=1, key="add_qty")
            if st.button("Add to Inventory"):
                st.session_state.inventory[spice_to_add] += qty_to_add
                st.success(f"Added {qty_to_add} units of {spice_to_add}!")
                st.rerun()
        
        with col_b:
            st.markdown("**Sell**")
            spice_to_sell = st.selectbox("Select Spice to Sell", options=list(st.session_state.inventory.keys()), key="sell_spice")
            qty_to_sell = st.number_input("Quantity to Sell", min_value=1, step=1, key="sell_qty")
            if st.button("Sell from Inventory"):
                if st.session_state.inventory[spice_to_sell] >= qty_to_sell:
                    st.session_state.inventory[spice_to_sell] -= qty_to_sell
                    st.success(f"Sold {qty_to_sell} units of {spice_to_sell}!")
                else:
                    st.error(f"Not enough {spice_to_sell}! You only have {st.session_state.inventory[spice_to_sell]}.")
                st.rerun()

        if st.button("Reset Inventory"):
            del st.session_state.inventory
            st.rerun()
        st.caption("This game tests your ability to manage a dictionary in state, performing updates based on user input.")

    with game_tabs[1]:
        st.subheader("The Ashrama Escape Puzzle")
        st.markdown("You are a student in an ancient ashrama, and you've been locked in the library by your mischievous guru to test your wits. You must interact with the room to find your way out. **Your goal is to perform a sequence of actions, with each action changing the state of the room, to unlock the door.**")
        image_search_button("Ancient Indian Library Nalanda", "Nalanda university library")

        # Initialize the state of the escape room
        if 'room_state' not in st.session_state:
            st.session_state.room_state = {
                'chest_locked': True,
                'has_key': False,
                'door_locked': True
            }
        
        st.write("**Your Situation:**")
        if st.session_state.room_state['door_locked']:
            st.info("You are in a quiet library. The main door is locked. You see a large wooden chest in the corner and a scroll on a table.")
        else:
            st.success("You unlocked the door! You are free. Your guru is impressed. You have won the game!")

        st.write("**What do you do?**")
        
        col_c, col_d = st.columns(2)
        with col_c:
            if st.button("Examine Scroll"):
                st.write("> The scroll has a riddle: 'I have no voice, but I hold the key to freedom. What am I?'")
            if st.button("Try to Open Door"):
                if st.session_state.room_state['door_locked']:
                    st.warning("The door is firmly locked.")
                else: # Should not happen if game is won
                    st.success("The door is already open!")
        
        with col_d:
            if st.button("Try to Open Chest"):
                if st.session_state.room_state['chest_locked']:
                    st.session_state.room_state['chest_locked'] = False
                    st.session_state.room_state['has_key'] = True
                    st.write("> You force the chest open! It was unlocked all along. Inside, you find a small, ornate key. You take it.")
                    st.balloons()
                else:
                    st.write("> The chest is already open.")
            
            if st.session_state.room_state['has_key']:
                 if st.button("Use Key on Door"):
                    if st.session_state.room_state['door_locked']:
                        st.session_state.room_state['door_locked'] = False
                        st.write("> You insert the key into the lock. It turns with a satisfying click! The door is now unlocked.")
                        st.rerun()
                    else:
                        st.write("> The door is already unlocked.")

        if st.button("Reset Puzzle"):
            del st.session_state.room_state
            st.rerun()
        st.caption("This game tests your ability to use boolean flags in state to control the logic and narrative flow of an application.")


    with game_tabs[2]:
        st.subheader("The Festive Shopping Cart")
        st.markdown("It's Diwali season! You are building a simple e-commerce page for a sweet shop. Customers should be able to add items to their cart and see the cart update instantly. **Your goal is to add at least one of each item to the cart.**")
        image_search_button("Indian Sweets for Diwali", "Diwali sweets mithai")

        products = {
            "Jalebi": 250,
            "Kaju Katli": 500,
            "Laddu": 300,
            "Soan Papdi": 200,
        }

        # Initialize cart
        if 'cart' not in st.session_state:
            st.session_state.cart = []

        st.write("Available Sweets:")
        for item, price in products.items():
            st.write(f"- **{item}**: ₹{price}/kg")
        
        st.markdown("---")

        item_to_add = st.selectbox("Choose a sweet to add:", options=list(products.keys()))
        if st.button(f"Add {item_to_add} to Cart"):
            st.session_state.cart.append(item_to_add)
            st.rerun()

        st.markdown("---")
        st.subheader("Your Shopping Cart")
        if not st.session_state.cart:
            st.warning("Your cart is empty.")
        else:
            total_cost = 0
            cart_items_count = {item: st.session_state.cart.count(item) for item in set(st.session_state.cart)}
            for item, count in cart_items_count.items():
                cost = count * products[item]
                total_cost += cost
                st.write(f"- {item} (x{count}) - ₹{cost}")
            st.markdown("---")
            st.header(f"Total: ₹{total_cost}")

        if st.button("Empty Cart"):
            st.session_state.cart = []
            st.rerun()

        st.caption("This game tests your ability to manage a list in state, adding items and then reading from the list to perform calculations.")

    st.markdown("---")

    #================================================================================
    # PART 6: THE HORIZON (THE JNANA-CHAKSHU - EYE OF KNOWLEDGE)
    #================================================================================
    st.markdown("## Part 6: The Jnana-Chakshu - The Eye of Future Knowledge")
    st.markdown("""
    You have mastered the Akshaya Patra. You have tamed the ephemeral nature of the web. `st.session_state` is more than a feature; it is a fundamental shift in what you can build. It is the boundary between a simple script that displays data and a true, stateful *application*.

    With this skill, you have unlocked the door to creating:
    *   **Personalized Dashboards:** Apps that remember a user's preferences, their favorite stocks, or the cities they track for weather.
    *   **Complex Forms and Wizards:** Any process that requires multiple steps, like creating a user profile, booking a train ticket, or configuring a machine learning model.
    *   **Interactive Games:** Any game, from a simple quiz to a complex puzzle, requires state to track score, progress, and inventory.
    *   **User Login Systems:** The most fundamental state of all: is this user logged in or not? This is controlled by a simple boolean flag in `st.session_state`.

    Think of the apps you use every day. They all have memory. Your email client remembers who you are. Your favorite shopping app remembers your cart. Your music app remembers your playlists. This is the power you now wield.

    ### The Next Horizon: The Gift of Speed

    We have bestowed the gift of **Memory** upon our app. It can remember what happened in the past. But what if a part of our app is very, very slow? What if we need to download a large file, query a huge database, or run a complex calculation that takes 30 seconds?

    Right now, if that calculation is part of our script, it will re-run every single time, even if the inputs haven't changed! Our app may have a good memory, but it has no patience. It does the same hard work over and over again, needlessly.

    This is the next challenge on our journey. We must give our app the gift of **Speed**. We must teach it not to re-calculate what it already knows.

    In the next chapter, we will learn about **Caching** (`st.cache_data` and `st.cache_resource`). We will learn how to perform a slow operation just once and then store the result in a high-speed memory, giving our applications the instantaneous, magical feel of a truly professional tool. The journey from apprentice to master builder continues!
    """)
    st.markdown("---")


    #================================================================================
    # PART 7: THE CHECK-UP (THE PARIKSHA)
    #================================================================================
    st.markdown("## Part 7: The Pariksha - A Test of Your New Memory")
    st.markdown("Let's solidify our understanding. Answer these questions to ensure the knowledge of the Akshaya Patra is truly yours.")

    questions = {
        "1. What is the fundamental problem that `st.session_state` solves in Streamlit?": {
            "options": [
                "It makes the app look more beautiful with CSS.",
                "It allows the app to remember data even when the script re-runs after an interaction.",
                "It helps draw faster charts and graphs.",
                "It automatically deploys the app to the cloud."
            ],
            "answer": "It allows the app to remember data even when the script re-runs after an interaction.",
            "explanation": "Correct! Streamlit's default behavior is to re-run the entire script from top-to-bottom on every widget interaction. `st.session_state` provides a persistent, dictionary-like object that survives these re-runs, giving your app a memory."
        },
        "2. In our core analogy, `st.session_state` is the Akshaya Patra. What does Draupadi taking her meal for the day represent?": {
            "options": [
                "The user clicking a button.",
                "The user closing their browser tab, ending the session.",
                "An error happening in the script.",
                "The user adding an item to their cart."
            ],
            "answer": "The user closing their browser tab, ending the session.",
            "explanation": "Excellent insight! Just as the vessel became exhausted for the day once Draupadi ate, `st.session_state` is cleared and the memory is wiped when the user's session ends (i.e., they close the browser tab or the server times out)."
        },
        "3. What is the correct and safest way to initialize a counter named `my_counter` in session state?": {
            "options": [
                "`st.session_state.my_counter = 0`",
                "`if not st.session_state.my_counter: st.session_state.my_counter = 0`",
                "`if 'my_counter' not in st.session_state: st.session_state.my_counter = 0`",
                "`my_counter = st.session_state.get('my_counter', 0)`"
            ],
            "answer": "`if 'my_counter' not in st.session_state: st.session_state.my_counter = 0`",
            "explanation": "Perfect! This is the canonical pattern. Placing the initialization `st.session_state.my_counter = 0` by itself would reset the counter on every run. Checking for the key's existence with `if 'my_counter' not in st.session_state:` ensures the initialization code runs only once per session."
        },
        "4. You have a widget: `st.slider('Choose a value', key='my_slider')`. How do you access the slider's current value from session state?": {
            "options": [
                "`st.my_slider`",
                "`st.session_state.get('my_slider')`",
                "`st.session_state.my_slider`",
                "Both B and C are correct."
            ],
            "answer": "Both B and C are correct.",
            "explanation": "Correct! When you assign a `key` to a widget, its value is directly available in `st.session_state`. You can access it using either attribute notation (`st.session_state.my_slider`) or dictionary-style access (`st.session_state.get('my_slider')` or `st.session_state['my_slider']`)."
        },
        "5. Which of the following application features would be IMPOSSIBLE to build correctly without `st.session_state` or a similar mechanism?": {
            "options": [
                "A page that displays a welcome message and a static image.",
                "An app that takes a number as input and displays its square.",
                "A multi-page quiz that keeps track of your score as you answer questions.",
                "A page with a button that shows or hides a data table."
            ],
            "answer": "A multi-page quiz that keeps track of your score as you answer questions.",
            "explanation": "Exactly! Tracking a score across multiple interactions (answering questions) requires memory that persists between script re-runs. The other options can be handled with simple re-runs, though the show/hide button would also typically use state for a better user experience."
        }
    }
    
    st.markdown("---")
    
    for i, (q, data) in enumerate(questions.items()):
        st.subheader(f"Question {i+1}")
        st.markdown(f"**{q}**")
        user_answer = st.radio("Select your answer:", data["options"], key=f"q_{i}")

        if st.button("Check Answer", key=f"check_{i}"):
            if user_answer == data["answer"]:
                st.success("Correct! Well done.")
                st.info(f"**Explanation:** {data['explanation']}")
            else:
                st.error("Not quite. Here's a hint:")
                st.info(f"**Explanation:** {data['explanation']}")
            st.markdown("---")