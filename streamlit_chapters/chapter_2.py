# streamlit_chapters/chapter_2.py

import streamlit as st
import pandas as pd
import numpy as np
from utils.plotting import image_search_button

def render():
    """
    Renders Chapter 2: The Art of Display - Text & Data.
    This chapter follows the 7-part lesson design guide.
    """
    st.title("📊 Chapter 2: The Art of Display")
    st.markdown("---")

    # =================================================================================================
    # Part 1: The Core Idea (The Analogy)
    # =================================================================================================
    st.header("Part 1: The Editor's Desk - From Raw News to a Gripping Story")
    st.markdown("""
    Imagine you are the chief editor of a bustling digital newspaper, let's call it *'The Daily Darpan'* (The Daily Mirror). Every morning, reporters send you raw, unformatted text and data: election results, the latest cricket scores, stock market numbers, and festival announcements.

    Is this raw information a story? Not yet. It's just... data.

    Your job, as the editor, is to *present* this information so it tells a compelling story. You don't just dump the text on the page.
    - You create a powerful **Headline** that grabs attention.
    - You highlight the most **Critical Numbers** in bold, eye-catching boxes.
    - You organize the detailed results into clean, easy-to-read **Tables**.

    This is precisely what you do in Streamlit. You are the editor of your web application. The tools we'll learn in this chapter—`st.markdown`, `st.metric`, and `st.dataframe`—are your editorial tools. They are the ink, the printing press, and the layout grid that transform your raw data into a clear, insightful, and beautiful narrative for your users.

    This chapter is about learning the art of presentation. It’s about taking the numbers and words from your code and arranging them with such clarity that they create meaning and insight.
    """)
    image_search_button("Vintage Indian Newspaper", "vintage indian newspaper")
    st.markdown("---")


    # =================================================================================================
    # Part 2: The Mechanism (Interactive Discovery)
    # =================================================================================================
    st.header("Part 2: The Live Newsroom - Your Interactive Editing Tools")
    st.markdown("""
    Let's step into the live newsroom. Here, you can experiment with your editorial tools in real-time and see the immediate effect.

    #### The Markdown Composer
    Markdown is the language you use to write headlines, create lists, and emphasize text. It's like choosing the font and style for your newspaper's articles. Type in the box below and see how your text transforms instantly.

    **Challenge:** Try to create a bold headline, an italicized sub-heading, and a bulleted list.
    (Hint: Use `**Bold Text**`, `*Italic Text*`, and `- List Item`)
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Your Composer")
        markdown_input = st.text_area("Write your markdown here:", 
"""### Main Headline!
**Date: Today**

This is an *important* update.

- First point
- Second point
- Third point

> A quote worth remembering.""", height=300)
    with col2:
        st.subheader("Live Preview")
        st.markdown(markdown_input)

    st.markdown("---")
    st.markdown("""
    #### The Data Desk
    Now, let's handle the numbers. A table of data can be overwhelming. As an editor, you guide the reader's eye. Use the checkboxes below to see how you can style a table to highlight key information, just like circling the winning numbers in a lottery report.
    """)

    # Sample DataFrame for the data desk
    df_data_desk = pd.DataFrame({
        'Salesperson': ['Arjun', 'Priya', 'Rohan', 'Sneha'],
        'Units Sold': [150, 210, 120, 300],
        'Region': ['North', 'South', 'West', 'South'],
        'Profit (in ₹ Lakhs)': [1.2, 1.8, 0.9, 2.5]
    })

    highlight_max_profit = st.checkbox("Highlight Top Profit")
    highlight_min_units = st.checkbox("Highlight Lowest Units Sold")

    st.write("#### Quarterly Sales Report")
    
    styled_df = df_data_desk.style
    if highlight_max_profit:
        styled_df = styled_df.highlight_max(subset=['Profit (in ₹ Lakhs)'], color='lightgreen')
    if highlight_min_units:
        styled_df = styled_df.highlight_min(subset=['Units Sold'], color='#ffcccb') # Light red

    st.dataframe(styled_df)
    st.markdown("Notice how a simple highlight makes the data instantly easier to interpret. You've just guided your reader to the most important insights without them having to search.")
    st.markdown("---")


    # =================================================================================================
    # Part 3: The Gallery (Showcasing Variety)
    # =================================================================================================
    st.header("Part 3: The Newspaper Sections - Different Tools for Different Stories")
    st.markdown("Every section of a newspaper has a different style. The headline is different from the stock market ticker, which is different from the classifieds. Let's explore the different 'sections' you can create.")

    gallery_tabs = st.tabs(["📜 The Front Page (Markdown)", "🏏 The Scoreboard (Metric)", "📈 The Business Ledger (DataFrames)"])

    with gallery_tabs[0]:
        st.subheader("The Front Page: `st.markdown()`")
        st.markdown("""
        `st.markdown()` is your tool for all narrative content. It's not just for text; it's for structure. You can create headers, lists, links, and more. It's the equivalent of typesetting your main articles.
        """)
        image_search_button("Indian language calligraphy", "devanagari script calligraphy")
        st.code("""
# Different levels of headlines
st.markdown("# This is a headline (H1)")
st.markdown("## This is a sub-headline (H2)")
st.markdown("### This is a smaller sub-headline (H3)")

# Text formatting
st.markdown("This is **bold text**.")
st.markdown("This is *italic text*.")

# Lists
st.markdown("- A bullet point")
st.markdown("- Another bullet point")

# Blockquote
st.markdown("> To be, or not to be, that is the question.")
        """, language='python')


    with gallery_tabs[1]:
        st.subheader("The Scoreboard: `st.metric()`")
        st.markdown("""
        `st.metric()` is designed for one thing: displaying a Key Performance Indicator (KPI) in a big, bold, beautiful way. It's perfect for a cricket scorecard, a stock price, or website visitors. The 'delta' shows the change from a previous value, instantly telling the user if the trend is positive or negative.
        """)
        image_search_button("Live cricket scoreboard", "live cricket scoreboard")
        st.code("""
st.metric(label="India's Score", value="357/5", delta="Overs: 48.2")
st.metric(label="Sensex", value="74,227", delta="-81.54", delta_color="inverse")
st.metric(label="New Signups", value="1,200", delta="150", delta_color="normal")
        """, language='python')
        st.success("**Pro-Tip:** `delta_color='inverse'` makes negative numbers appear red and positive ones green. `'normal'` does the opposite.")


    with gallery_tabs[2]:
        st.subheader("The Business Ledger: `st.dataframe()` & `st.table()`")
        st.markdown("""
        When you have rows and columns of data, you need a table. Streamlit gives you two choices:
        1.  **`st.dataframe()`**: This is the default choice. It's interactive! Users can scroll, sort by columns, and expand the table. It's best for displaying large datasets from sources like Pandas DataFrames.
        2.  **`st.table()`**: This is a static table. It displays the entire dataset at once without scroll bars. It's best for small, simple tables where you want to show all the data at a glance.

        Think of `st.dataframe` as an interactive digital ledger and `st.table` as a printed summary in a report.
        """)
        df_ledger = pd.DataFrame({
            'Item': ['Samosa', 'Jalebi', 'Chai'],
            'Price (₹)': [15, 25, 10],
            'Quantity': [100, 50, 200]
        })
        st.write("Interactive DataFrame (`st.dataframe`):")
        st.dataframe(df_ledger)

        st.write("Static Table (`st.table`):")
        st.table(df_ledger)
    st.markdown("---")


    # =================================================================================================
    # Part 4: The Formalization (The Ganita Shastra - The Science of Presentation)
    # =================================================================================================
    st.header("Part 4: The 'Ganita Shastra' - The Science of Presentation")
    st.markdown("""
    Let's formalize our understanding. In ancient India, 'Ganita Shastra' referred to the science of calculation. Here, we adapt it to mean the 'Science of Presentation'. Let's look at the precise rules and powers of our new tools.

    ### `st.markdown(body, unsafe_allow_html=False)`
    -   **`body`**: The string to be rendered as Markdown.
    -   **`unsafe_allow_html`**: A powerful but dangerous parameter. If `True`, you can inject raw HTML (`<p>`, `<font>`, etc.). Use it with extreme caution, as it can break your app's layout or create security risks if the HTML comes from a user.

    ### `st.metric(label, value, delta=None, delta_color="normal")`
    -   **`label`**: A short, descriptive title for the metric.
    -   **`value`**: The main number or text to display.
    -   **`delta`**: An optional string indicating the change from a previous value. It's displayed below the main value.
    -   **`delta_color`**: Controls the color of the delta.
        -   `"normal"`: Green for positive delta, red for negative.
        -   `"inverse"`: Red for positive, green for negative (useful for things like 'rank' where a lower number is better).
        -   `"off"`: The delta is always gray.

    ### `st.dataframe(data, width=None, height=None)`
    -   **`data`**: The data to display. Usually a Pandas DataFrame, but can be many other types.
    -   **`width`** / **`height`**: Set the dimensions of the table in pixels. If not set, it will try to fit its container.
    -   Its real power comes from being able to display **styled** DataFrames. You can pre-process a DataFrame with functions like `.style.background_gradient()` to create heatmaps directly in your table.

    ### `st.table(data)`
    -   **`data`**: The data to display.
    -   It's simple and static. What you see is what you get. No scrolling, no sorting. Best for small, summary tables.
    """)
    st.markdown("---")

    # =================================================================================================
    # Part 5: The Application (The Games & Puzzles)
    # =================================================================================================
    st.header("Part 5: On-the-Job Training - Puzzles from the Newsroom")
    st.markdown("Theory is one thing, but an editor learns on the job. Let's tackle a few real-world scenarios.")

    game_tabs = st.tabs(["🏏 The Cricket Commentator", "📈 The Startup Analyst", "📦 The Inventory Manager"])

    with game_tabs[0]:
        st.subheader("The Cricket Commentator")
        st.markdown("You've just received live data from an ongoing T20 match. Your task is to build a visually clear scoreboard using `st.metric`.")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="Team Score", value="182/3", delta="18.5 Overs")
        with c2:
            st.metric(label="Current Run Rate", value="9.75", delta="Required: 8.5")
        with c3:
            st.metric(label="Star Batsman Runs", value="85* (42 balls)")
        
        st.markdown("**Your Challenge:** In the code below, which metric would you give a `delta_color` of `'inverse'`? Why?")
        st.info("Answer: The 'Required Run Rate'. If the current rate is higher than the required rate, that's good! But if you just subtract them, the *difference* might be positive, which should be green. `st.metric`'s delta is for showing *change*, so here, we just use the text field. But if you were tracking a player's rank (where #1 is best), a change from 5 to 3 is a *drop* of 2, but it's a *good* thing. That's where `delta_color='inverse'` shines!")

    with game_tabs[1]:
        st.subheader("The Startup Analyst")
        st.markdown("You're creating a real-time dashboard for a Bengaluru-based food delivery startup. You need to present the daily KPIs. Use a mix of `st.markdown` for headers and `st.metric` for the numbers.")

        st.markdown("### Daily Performance Dashboard")
        g1, g2, g3 = st.columns(3)
        g1.metric("Orders Today", "2,456", "+12%")
        g2.metric("Avg. Delivery Time", "28 Mins", "-2 Mins")
        g3.metric("Customer Rating", "4.8 ★", "+0.1")

        st.markdown("**Your Challenge:** Write the Streamlit code to produce the dashboard above. Pay close attention to the `delta` values.")
        with st.expander("Show Solution"):
            st.code("""
st.markdown("### Daily Performance Dashboard")
col1, col2, col3 = st.columns(3)
col1.metric("Orders Today", "2,456", "+12%")
col2.metric("Avg. Delivery Time", "28 Mins", "-2 Mins")
col3.metric("Customer Rating", "4.8 ★", "+0.1")
            """, language="python")

    with game_tabs[2]:
        st.subheader("The Inventory Manager")
        st.markdown("You are managing the inventory for a sweet shop during Diwali. You need to display the stock levels. Use `st.dataframe` and its styling to highlight which item needs to be restocked urgently (less than 20 units).")
        
        inventory_df = pd.DataFrame({
            "Sweet Name": ["Kaju Katli", "Jalebi", "Ladoo", "Gulab Jamun", "Rasgulla"],
            "Stock (kg)": [50, 45, 18, 60, 12]
        })

        def highlight_low_stock(s):
            return ['background-color: #ffcccb' if v < 20 else '' for v in s]
        
        st.dataframe(inventory_df.style.apply(highlight_low_stock, subset=['Stock (kg)']))
        st.markdown("**Your Challenge:** Can you modify the styling function to highlight items with *high* stock (> 50kg) in green?")
        with st.expander("Show Solution"):
            st.code("""
# Define the data
inventory_df = pd.DataFrame({
    "Sweet Name": ["Kaju Katli", "Jalebi", "Ladoo", "Gulab Jamun", "Rasgulla"],
    "Stock (kg)": [50, 45, 18, 60, 12]
})

# Define the styling function
def highlight_stock(s):
    styles = []
    for v in s:
        if v < 20:
            styles.append('background-color: #ffcccb') # Low stock in red
        elif v > 50:
            styles.append('background-color: lightgreen') # High stock in green
        else:
            styles.append('')
    return styles

# Apply the style and display
st.dataframe(inventory_df.style.apply(highlight_stock, subset=['Stock (kg)']))
            """, language='python')
    st.markdown("---")


    # =================================================================================================
    # Part 6: The Horizon (The Jnana-Chakshu - Eye of Knowledge)
    # =================================================================================================
    st.header("Part 6: The 'Jnana-Chakshu' - The Power of Clear Presentation")
    st.markdown("""
    You now hold the tools of the editor. This might seem simple—just displaying text and numbers—but it is the foundation of every data application ever built.

    -   **Business Intelligence Dashboards** used by startups in Mumbai and Bengaluru are built on these principles. They use `st.metric` for KPIs and `st.dataframe` for deep dives.
    -   **Machine Learning Engineers** use `st.markdown` to explain their models and `st.dataframe` to show prediction results.
    -   **Financial Analysts** tracking the Nifty 50 use these tools to build live reports that are easier to understand than any spreadsheet.

    **The Key Takeaway:** Raw data is noise. Well-presented data is information. Information that guides decisions is knowledge. Your job as a Streamlit developer is to facilitate this journey from data to knowledge.

    **The Next Chapter:** So far, our newspaper is static. We, the editors, decide what the reader sees. But what if the reader could talk back? What if they could ask questions, filter the news, and create their own view?

    In the next chapter, we will hand the controls to the user. We will explore **Interactive Widgets**, turning our one-way broadcast into a two-way conversation.
    """)
    st.markdown("---")


    # =================================================================================================
    # Part 7: The Check-up (The Pariksha)
    # =================================================================================================
    st.header("Part 7: The 'Pariksha' - Check Your Understanding")

    questions = {
        "1. How do you create a level 2 headline in Markdown?": {
            "options": ["`## Headline`", "`**Headline**`", "`<h2>Headline</h2>`", "`st.header('Headline')`"],
            "correct": "`## Headline`",
            "explanation": "In Markdown, the number of '#' symbols determines the header level. `##` corresponds to an H2 headline."
        },
        "2. You are displaying a company's financial loss. The delta is `+50 Lakhs` (meaning the loss increased). How do you make this delta appear red?": {
            "options": ["`delta_color='normal'`", "`delta_color='red'`", "`delta_color='inverse'`", "`delta_color='off'`"],
            "correct": "`delta_color='inverse'`",
            "explanation": "Normally, a positive delta is green. Since an increased loss is a negative outcome, `delta_color='inverse'` flips the colors, making the positive number appear red."
        },
        "3. When should you prefer `st.table` over `st.dataframe`?": {
            "options": ["For very large datasets", "When you want users to sort the data", "For small, static tables where all data should be visible at once", "When you need to add colors and styles"],
            "correct": "For small, static tables where all data should be be visible at once",
            "explanation": "`st.table` is static and renders the entire table, making it ideal for small summaries. `st.dataframe` is interactive and better for large, sortable, and styleable datasets."
        },
        "4. What does the `unsafe_allow_html=True` parameter in `st.markdown` do?": {
            "options": ["It makes the text bold.", "It allows you to render raw HTML code within your app.", "It connects to the internet to check for unsafe content.", "It automatically corrects spelling errors."],
            "correct": "It allows you to render raw HTML code within your app.",
            "explanation": "This parameter lets you pass HTML tags directly, but it should be used with caution as it can affect your app's security and layout if not handled carefully."
        }
    }

    for i, (question, data) in enumerate(questions.items()):
        st.subheader(f"Question {i+1}")
        user_answer = st.radio(question, data["options"], key=f"q_{i}")
        
        if st.button("Check Answer", key=f"check_{i}"):
            if user_answer == data["correct"]:
                st.success("Correct! 🎉")
                st.markdown(data["explanation"])
            else:
                st.error("Incorrect. Here's the explanation:")
                st.markdown(data["explanation"])