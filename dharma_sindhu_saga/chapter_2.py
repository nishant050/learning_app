# In dharma_sindhu_saga/chapter_2_mahabharata.py
# ---
# Integration Note for the Developer:
# 1. Place this file in the `dharma_sindhu_saga/` directory.
# 2. In `app.py`, import this chapter:
#    `from dharma_sindhu_saga import chapter_2_mahabharata as dharma_chapter_2`
# 3. Add it to the `dharma_chapters` dictionary in app.py:
#    `"Chapter 2: Echoes of the Mahabharata": dharma_chapter_2.render,`
# ---

import streamlit as st
from utils.plotting import image_search_button
import time

def render():
    """
    Renders Chapter 2 of the Dharma-Kshetra Saga, focusing on the Mahabharata.
    This chapter is a deep-dive, narrative-driven exploration following the 7-part guide.
    """

    # --- PART 1: THE CORE IDEA (THE ANALOGY) ---
    st.title("Chapter 2: Echoes of the Mahabharata")
    st.header("The Cosmic Family Feud on Sacred Ground")
    st.markdown("""
    ---
    Before we speak of armies, of divine weapons, or of kings and crowns, let us begin with something far more universal and relatable: a family dispute over ancestral property.

    Imagine a grand, sprawling ancestral home, built by revered forefathers, standing on the most fertile land in the entire region. This isn't just any home; it is the heart of the family's identity, a source of prosperity, and a symbol of their honour. For generations, it has been the silent witness to their shared joys and sorrows.

    Now, imagine the family has grown. Two branches of cousins now lay claim to this legacy. One branch, the elder, believes the entire estate is theirs by right of birth, even if that right is built on a foundation of moral blindness and greed. The other, younger branch, having been denied their rightful share through deceit and malice, asks for a just and fair division. They don't even ask for half; they plead for just five villages, a symbolic token of their heritage, a place to live with dignity.

    The elders refuse. Greed, like a cataract, has clouded their vision. They declare that they will not part with enough land to fit on the point of a needle without a fight.

    This simple, tragic story of a family breaking apart over inheritance is the seed of the Mahabharata. But here, the family is the Kuru clan. The ancestral property is the throne of Hastinapura, the very heart of the Indian subcontinent. And the conflict is not merely a legal or familial squabble; it is a **Dharma Sankat**—a crisis of righteousness so profound that it draws in gods, sages, and kings from every corner of the land.

    The battlefield, Kurukshetra in modern-day Haryana, transforms from a mere piece of land into a **Dharma-Kshetra**, a 'field of righteousness'. It becomes a cosmic stage where every action, every choice, and every arrow-loosed is weighed on the scales of Dharma. This is not just a war for a kingdom; it is a war to decide the very meaning of right and wrong for an entire epoch. The story of the Mahabharata, unfolding on Haryana's soil, is the ultimate exploration of human duty, sacrifice, grief, and the search for divine truth in the face of overwhelming despair. It’s the story of how a family feud became the bedrock of a civilization's moral philosophy.
    """)
    image_search_button("A symbolic representation of the Kuru Family Tree", "Kuru family tree abstract art")
    st.markdown("---")


    # --- PART 2: THE MECHANISM (INTERACTIVE DISCOVERY) ---
    st.header("The Mechanism: The Dharma Sankat Simulator")
    st.markdown("""
    The heart of the Mahabharata, the moment that elevates it from a mere war story to a timeless philosophical guide, is Arjuna's dilemma. On the brink of war, he sees his grand-uncles, his teachers, and his cousins arrayed against him. His warrior spirit collapses under the weight of his love and grief. Why must he kill his own kin for a kingdom?

    This is the **Dharma Sankat**, the crisis of duty. Krishna's answer to this crisis forms the **Bhagavad Gita**.

    Let's not just read about it. Let's *feel* the weight of this decision. Use the sliders below to experience the conflicting pulls of Dharma that tore Arjuna apart. As you adjust each one, the arguments presented to Arjuna will change, reflecting your chosen priorities.
    """)

    st.subheader("Arjuna's Dilemma: Adjust the Scales of Duty")

    col1, col2, col3 = st.columns(3)
    with col1:
        duty_family = st.slider("Attachment to Family (Kula Dharma)", 0, 100, 50, help="The duty to protect one's own family and avoid familial bloodshed.")
    with col2:
        duty_kshatriya = st.slider("Duty as a Warrior (Kshatriya Dharma)", 0, 100, 50, help="A warrior's sacred duty to fight against injustice and restore righteousness.")
    with col3:
        duty_personal = st.slider("Personal Grief & 'Sin' (Paap)", 0, 100, 50, help="The personal pain of killing loved ones and the fear of incurring sin.")

    total = duty_family + duty_kshatriya + duty_personal
    if total == 0: total = 1 # Avoid division by zero

    st.info("💡 **Krishna's Guidance:** Based on your current dilemma, here is the wisdom that might be offered.")

    # The logic here simulates different perspectives based on slider values.
    if duty_family > duty_kshatriya and duty_family > duty_personal:
        st.markdown(f"""
        **Focus: The Crime of Killing Kin**

        Your heart leans heavily towards your family. Like Arjuna, you cry out:

        > *"O Krishna, seeing my own kinsmen arrayed for battle, my limbs fail and my mouth is parched. I see no good in killing my own kith and kin in battle. I desire not victory, nor a kingdom, nor pleasures. What use is a kingdom, stained with the blood of my teachers and uncles?"* (Gita 1:28-32)

        This is a powerful and humane emotion. The argument is that the sin of destroying one's own lineage, the very fabric of society, is too great a price to pay for any worldly gain. The long-term chaos and societal collapse from such an act seem far worse than the injustice you currently face.
        """)
    elif duty_kshatriya > duty_family and duty_kshatriya > duty_personal:
        st.markdown(f"""
        **Focus: The Mandate to Uphold Righteousness**

        Your warrior-spirit dominates. You understand Krishna's core message:

        > *"O Arjuna, do not yield to this impotence. It does not befit you. Shake off this petty weakness of heart and arise, O vanquisher of foes! ... Considering your own specific duty as a Kshatriya, you should not waver. Indeed, for a warrior, there is no better engagement than fighting for a righteous cause."* (Gita 2:3, 2:31)

        The argument here is clear: injustice (Adharma), if left unchecked, poisons the entire world. Your personal feelings, however valid, are secondary to your sacred duty to protect society from the greed of the Kauravas. To walk away from this fight would be an act of cowardice and a failure of your Dharma, leading to greater suffering for millions.
        """)
    elif duty_personal > duty_family and duty_personal > duty_kshatriya:
        st.markdown(f"""
        **Focus: The Fear of Karmic Consequence**

        Your soul is troubled by the personal cost, the fear of `Paap` (sin). You resonate with Arjuna's fear:

        > *"Alas, how strange it is that we are preparing to commit a great sin. Driven by the desire for kingly pleasures, we are ready to slay our own kinsmen. It would be better for me if the sons of Dhritarashtra, with weapons in hand, were to kill me, unarmed and unresisting, on the battlefield."* (Gita 1:45-46)

        This perspective is about the soul's journey. The fear is that the karmic burden of this single act of violence will lead to suffering in this life and the next. The argument is that it is better to suffer injustice and even die than to stain one's own soul with the sin of such a terrible massacre.
        """)
    else:
        st.markdown(f"""
        **Focus: The Point of Equilibrium & The Path of Action**

        You are balanced in your conflict, feeling the pull of all duties equally. This is the very heart of the dilemma, and it is here that Krishna introduces the ultimate solution: **Nishkama Karma** (Action without attachment to the results).

        > *"You have a right to perform your prescribed duties, but you are not entitled to the fruits of your actions. Never consider yourself to be the cause of the results of your activities, and never be attached to not doing your duty."* (Gita 2:47)

        Krishna's genius is to reframe the entire problem. He tells Arjuna: "Do not fight for the kingdom. Do not fight out of anger. Do not shrink from it out of fear. Fight because it is your **Dharma**. Detach yourself from the outcome—victory or defeat, profit or loss, pleasure or pain. Act for the sake of the act itself, as an offering to the cosmic order." This is the path that allows one to navigate an impossible choice.
        """)
    st.markdown("---")


    # --- PART 3: THE GALLERY (SHOWCASING VARIETY) ---
    st.header("The Gallery: Sacred Sites of the Saga")
    st.markdown("""
    The Mahabharata is not just a story; it is etched into the very landscape of Haryana. These places are not mere tourist spots; they are centers of spiritual energy, resonating with the echoes of the epic. Explore the key locations where these cosmic events unfolded.
    """)

    tab1, tab2, tab3, tab4 = st.tabs(["**Kurukshetra**", "**Jyotisar**", "**Brahma Sarovar**", "**Thanesar**"])

    with tab1:
        st.subheader("Kurukshetra: The Field of Righteousness")
        st.markdown("""
        This is the grand stage. The name itself, `Dharma-Kshetra`, given in the very first verse of the Bhagavad Gita, defines its purpose. It was chosen, the stories say, because the soil of this land had a unique property: it would not let hatred and sin take root permanently, making it the perfect crucible to test Dharma. It was vast enough to hold the 18 `Akshauhini` (a battle formation) armies of the Kuru clan. Today, the city of Kurukshetra is a sprawling complex of temples, sacred water tanks, and memorials dedicated to the epic. It is a place where one can stand and imagine the thundering chariots and the great dilemma that faced Arjuna.
        """)
        image_search_button("The plains of Kurukshetra today", "Kurukshetra field")

    with tab2:
        st.subheader("Jyotisar: The Fount of Divine Wisdom")
        st.markdown("""
        If Kurukshetra is the stage, Jyotisar is the sacred spot where the divine script was revealed. It is revered as the exact place where Lord Krishna paused the chariot in the middle of the two armies and delivered the celestial sermon of the Bhagavad Gita to a despondent Arjuna. The name 'Jyotisar' means 'the essence of light' or 'the essence of knowledge'. A single, ancient Banyan tree stands here, believed to be a direct descendant of the silent, eternal witness to that profound moment of divine revelation. To visit Jyotisar is to seek the very source of the Gita's wisdom.
        """)
        image_search_button("The Banyan Tree at Jyotisar", "Jyotisar Kurukshetra")

    with tab3:
        st.subheader("Brahma Sarovar: The Waters of Creation and Liberation")
        st.markdown("""
        This vast, sacred water tank is one of the most breathtaking sites in Kurukshetra. Its origins are believed to predate the Mahabharata itself, linked to Lord Brahma, the creator of the universe. During the war, it served as a vital water source. Legend holds that on the final day of the war, the defeated Duryodhana, in a last, desperate act, used his mystical powers to hide in the depths of this Sarovar. It is a place deeply associated with both creation and the final, tragic end of the Kauravas. A dip in its waters during a solar eclipse is considered to be of immense spiritual merit.
        """)
        image_search_button("The sprawling Brahma Sarovar", "Brahma Sarovar Kurukshetra")

    with tab4:
        st.subheader("Thanesar: The Capital of a Preceding Era")
        st.markdown("""
        While Hastinapura was the Kuru capital, the city of Sthanishvara (modern Thanesar), was the capital of the preceding empire of Harsha Vardhana, and its history is deeply intertwined with Kurukshetra. The famous Shiva temple of Sthaneshwar Mahadev was a major pilgrimage site even during the Mahabharata era. It represents the continuity of Dharma in this region, a sacredness that existed before the great war and continued long after. It reminds us that the Mahabharata, while a pivotal event, was one chapter in the long spiritual history of this land.
        """)
        image_search_button("Sthaneshwar Mahadev Temple", "Sthaneshwar Mahadev Temple Thanesar")
    st.markdown("---")


    # --- PART 4: THE FORMALIZATION (THE GANITA SHASTRA) ---
    st.header("The Ganita Shastra: Deconstructing the Epic")
    st.markdown("""
    Our intuition now grounded, let us formalize our understanding. Just as a scientist needs precise terminology, we need to understand the structure of the conflict and the core tenets of the wisdom that emerged from it. This is the 'Ganita Shastra'—the science and system—behind the saga.
    """)

    st.subheader("The Kuru Family Tree: A House Divided")
    st.markdown("""
    At its core, the conflict was between two sets of cousins, the Pandavas and the Kauravas. Understanding this family tree is crucial to grasping the personal stakes of the war. Below is a simplified diagram of the central figures.

    *   **Pandavas:** The five sons of Pandu, guided by righteousness. Yudhishthira, Bhima, Arjuna, Nakula, and Sahadeva.
    *   **Kauravas:** The one hundred sons of the blind king Dhritarashtra, led by the eldest, the arrogant Duryodhana.
    """)
    st.graphviz_chart('''
    digraph kuru_family {
        rankdir=TB;
        node [shape=box, style=rounded];
        
        subgraph cluster_pandavas {
            label = "PANDAVAS (The Five Brothers)";
            style=filled;
            color=lightblue;
            Yudhishthira; Bhima; Arjuna; Nakula; Sahadeva;
            {rank=same; Yudhishthira; Bhima; Arjuna; Nakula; Sahadeva;}
            Pandu [label="King Pandu (Father)"];
            Pandu -> {Yudhishthira, Bhima, Arjuna, Nakula, Sahadeva} [label=" fathers"];
        }
        
        subgraph cluster_kauravas {
            label = "KAURAVAS (The Hundred Brothers)";
            style=filled;
            color=lightcoral;
            Duryodhana [label="Duryodhana (Eldest)"];
            Dushasana; "98 others";
            {rank=same; Duryodhana; Dushasana; "98 others";}
            Dhritarashtra [label="King Dhritarashtra (Blind King, Father)"];
            Dhritarashtra -> {Duryodhana, Dushasana, "98 others"} [label=" fathers"];
        }
        
        "King Shantanu (Ancestor)" -> {Pandu, Dhritarashtra} [label=" grandfather to sons"];
        
        Krishna [shape=ellipse, style=filled, color=gold, label="Lord Krishna (Guide & Avatar)"];
        Krishna -> Arjuna [label=" advises"];

        Bhishma [shape=ellipse, style=filled, color=lightgrey, label="Bhishma (Grand-Uncle)"];
        Drona [shape=ellipse, style=filled, color=lightgrey, label="Drona (Teacher)"];

        Bhishma -> {Pandavas, Kauravas} [style=dotted, label=" Fights for Kauravas"];
        Drona -> {Pandavas, Kauravas} [style=dotted, label=" Fights for Kauravas"];

    }
    ''')


    st.subheader("The Dharma of the Gita: Three Paths to the Divine")
    st.markdown("""
    The Bhagavad Gita, delivered amidst the chaos, is not just one teaching, but a synthesis of spiritual paths. It lays down three primary margas (paths) that an individual can take to achieve moksha (liberation), tailored to different human temperaments. These are the core 'laws' or 'dharma' of the philosophy that emerged from the war.
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Chapters in the Gita", value="18")
    with col2:
        st.metric(label="Days of the War", value="18")
    with col3:
        st.metric(label="Core Paths (Yogas)", value="3")

    st.markdown("#### 1. Karma Yoga: The Path of Selfless Action")
    st.markdown("""
    *   **For Whom:** The active, dynamic individual. The householder, the soldier, the leader, the professional.
    *   **Core Principle:** This is the path we explored in the interactive simulator. Its genius lies in its practicality. It does not ask you to renounce the world, but to renounce the *attachment to the fruits of your work*. You perform your duty to the best of your ability, not for personal gain, praise, or reward, but as an offering to a higher ideal (be it God, society, or Dharma itself).
    *   **Gita's Words (Gita 3.19):** *"Therefore, without being attached to the fruits of activities, one should act as a matter of duty, for by working without attachment one attains the Supreme."*
    *   **Example:** A doctor treating a patient with utmost dedication, irrespective of whether they will be paid or thanked. Their duty is simply to heal. That is Karma Yoga.

    """)

    st.markdown("#### 2. Jnana Yoga: The Path of Knowledge")
    st.markdown("""
    *   **For Whom:** The intellectual, the contemplative, the philosophical. Those who seek answers through inquiry and wisdom.
    *   **Core Principle:** This path involves a deep, intellectual inquiry into the nature of reality. It is the process of distinguishing the eternal from the temporary, the Self (Atman) from the non-Self (the body, the mind, the ego). Through study, reflection, and meditation, the Jnana Yogi comes to realize their true identity as the immortal soul, not the perishable body or fleeting thoughts.
    *   **Gita's Words (Gita 4.38):** *"In this world, there is nothing so sublime and pure as transcendental knowledge. Such knowledge is the mature fruit of all mysticism. And one who has become accomplished in the practice of devotional service enjoys this knowledge within himself in due course of time."*
    *   **Example:** A physicist pondering the fundamental laws of the universe to understand its true nature is treading a path parallel to the Jnana Yogi.

    """)

    st.markdown("#### 3. Bhakti Yoga: The Path of Devotion")
    st.markdown("""
    *   **For Whom:** The emotional, the relational, the artistic. Those who find fulfillment through love and surrender.
    *   **Core Principle:** This is considered the most direct path. It involves channeling all of one's emotional energy towards God. This love can take many forms: chanting His names, singing praises, seeing the divine in all beings, and surrendering one's will to the divine. The Bhakti Yogi builds a deep, personal, loving relationship with the Divine.
    *   **Gita's Words (Gita 9.34):** *"Engage your mind always in thinking of Me, become My devotee, offer obeisances to Me and worship Me. Being completely absorbed in Me, surely you will come to Me."*
    *   **Example:** A musician composing a song not for fame, but out of pure love for their chosen ideal, is practicing Bhakti Yoga.
    """)
    st.markdown("---")


    # --- PART 5: THE APPLICATION (THE GAMES & PUZZLES) ---
    st.header("The Application: Test Your Dharmic Wisdom")
    st.markdown("""
    Knowledge becomes wisdom only when it is applied. Let's move beyond theory and step into the arena. These challenges will test your understanding of the epic's characters, strategies, and philosophies in different contexts.
    """)

    game1, game2, game3 = st.tabs(["**Game 1: The Chakravyuha Challenge**", "**Game 2: Gita Verse Identifier**", "**Game 3: Who Am I?**"])

    with game1:
        st.subheader("The Chakravyuha Challenge: A Puzzle of Strategy and Sacrifice")
        st.markdown("""
        You are an advisor to the brave **Abhimanyu**, Arjuna's son, who knows how to enter the deadly Chakravyuha (discus formation) but not how to exit. Guide him through a series of choices. Your understanding of Dharma and strategy will determine his fate.
        """)
        
        st.info("The scenario is set. The Pandava army is being decimated. Only Abhimanyu can break the enemy formation. He has just entered.")

        choice1 = st.radio(
            "**Choice 1:** Inside the Vyuha, Abhimanyu faces Drona, his grand-teacher. How should he proceed?",
            ("Hesitate, showing respect to his teacher.", "Attack with full force, as his Kshatriya Dharma demands.", "Try to bypass him without a fight."),
            key="c1",
            index=None
        )
        if choice1 == "Attack with full force, as his Kshatriya Dharma demands.":
            st.success("Correct. In a Dharma Yuddha (righteous war), the duty of a warrior supersedes personal relationships. Drona himself would expect no less.")
            choice2 = st.radio(
                "**Choice 2:** Multiple Kaurava warriors, including Karna and Dushasana, are now surrounding him, breaking the established rules of engagement. What is the Dharmic response?",
                ("Surrender, as the fight is now unrighteous.", "Call out their Adharma (unrighteousness) and continue to fight with all his might.", "Focus on just one warrior to take down with him."),
                key="c2",
                index=None
            )
            if choice2 == "Call out their Adharma (unrighteousness) and continue to fight with all his might.":
                st.success("Excellent. Even when faced with Adharma, a warrior's duty is to fight on. His courageous stand, even in defeat, becomes a testament to Dharma.")
                st.balloons()
                st.markdown("🎉 **Victory in Spirit!** You guided Abhimanyu with wisdom. Though he achieved Veera Gati (a warrior's glorious death), he did so by upholding his Dharma to the very end. His sacrifice exposed the moral bankruptcy of the Kauravas and became a pivotal moment in the war.")
            elif choice2 is not None:
                st.error("Incorrect. Surrendering or focusing on revenge would be a lesser path. The highest Dharma is to continue fighting for the righteous cause, even when the opponent cheats, thereby highlighting their fall from grace.")

        elif choice1 is not None:
            st.error("Not quite. While respect for a teacher is a core value, in the context of a declared war for righteousness, the Kshatriya Dharma to fight injustice takes precedence. Hesitation on the battlefield is fatal.")

    with game2:
        st.subheader("Gita Verse Identifier: Match the Wisdom to the Moment")
        st.markdown("Read the modern-day scenario and choose the Bhagavad Gita teaching that provides the most relevant guidance.")

        scenarios = {
            "A student is terrified of failing a crucial exam. The fear is paralyzing them from studying effectively.": {
                "correct": "Act without attachment to the results. Focus on the duty (studying), not the fruit (the grade).",
                "wrong": ["The body is temporary, but the soul is eternal.", "Devote all your actions to a higher power."]
            },
            "A successful entrepreneur feels empty despite her wealth and achievements. She feels her work lacks meaning.": {
                "correct": "Perform actions as a devotion, a 'Yajna' (sacrifice), for the good of the world.",
                "wrong": ["Fight against injustice wherever you see it.", "Knowledge is the purest thing in this world."]
            },
            "Someone is grieving the loss of a loved one and is unable to comprehend the nature of life and death.": {
                "correct": "The soul is unborn, eternal, and indestructible. It does not die when the body dies.",
                "wrong": ["Do not give in to weakness.", "Act for the sake of duty alone."]
            }
        }
        
        scenario_list = list(scenarios.keys())
        selected_scenario = st.selectbox("Select a scenario:", scenario_list, index=0)

        if selected_scenario:
            options = scenarios[selected_scenario]["wrong"] + [scenarios[selected_scenario]["correct"]]
            import random
            random.shuffle(options)
            
            user_choice = st.radio(f"**Scenario:** *{selected_scenario}*\n\nWhich teaching applies best?", options, index=None, key=selected_scenario)

            if user_choice is not None:
                if user_choice == scenarios[selected_scenario]["correct"]:
                    st.success("Perfectly identified! That is the core teaching for this situation.")
                    st.balloons()
                else:
                    st.error(f"A good thought, but the more direct advice here would be: '{scenarios[selected_scenario]['correct']}'. Your choice might apply, but it's not the central theme for this specific problem.")
    
    with game3:
        st.subheader("Who Am I? - Kuru Kingdom Edition")
        st.markdown("Read the description and guess the character from the Mahabharata.")

        characters = {
            "Bhishma": "I took a terrible vow of celibacy and service to the throne of Hastinapura. I was the grand-uncle to both Pandavas and Kauravas, and fought for the latter out of duty, even though my heart was with the former. I could choose the time of my own death.",
            "Drona": "I was the royal teacher of archery and military arts to both sets of cousins. Arjuna was my favorite student. My loyalty to the throne forced me to fight against him in the great war.",
            "Karna": "I was the secret, abandoned son of Kunti, making me the eldest Pandava brother by birth. However, I was raised by a charioteer and became the closest friend of Duryodhana. I was known for my generosity and my skill in archery, which rivaled Arjuna's.",
            "Yudhishthira": "I was the eldest of the five Pandava brothers, known as 'Dharmaraja' for my unwavering commitment to righteousness. My one great weakness was the game of dice, which led to our exile."
        }
        
        char_name = st.selectbox("Choose a character to learn about:", list(characters.keys()))
        st.markdown("---")
        st.markdown(f"**Description:** *{characters[char_name]}*")
        st.markdown("---")

        guess = st.text_input("Type your guess here and press Enter:")

        if guess:
            if guess.strip().lower() == char_name.lower():
                st.success(f"Correct! You have a keen eye for the heroes and legends of the epic. It is indeed {char_name}.")
                time.sleep(1) # a small delay to let the user read
                st.balloons()
            else:
                st.error("Not quite. Read the description again carefully. The clues point to another major figure in the saga.")
    st.markdown("---")


    # --- PART 6: THE HORIZON (THE JNANA-CHAKSHU - EYE OF KNOWLEDGE) ---
    st.header("The Horizon: The Gita in the 21st Century")
    st.markdown("""
    The war ended. The Pandavas won the throne, but at a cost that haunted them forever. The fields of Kurukshetra fell silent. But the wisdom delivered on that battlefield—the Bhagavad Gita—became immortal. Why? Because it addresses the fundamental conflicts of the human condition.

    The key takeaway from this chapter is not just the story of a war, but the revelation of a timeless toolkit for decision-making and purposeful living. **The Gita teaches us how to act with purpose in a world of chaos, by transforming our work into worship and our duty into devotion.**

    *   **In the Office:** The principle of **Karma Yoga** is a powerful antidote to modern burnout. It encourages a programmer to code with excellence not just for a promotion, but for the sake of building something useful. It pushes a leader to manage a team with fairness not just for profit, but because it is their Dharma to nurture their people.

    *   **In Personal Life:** The concept of the eternal **Atman** (Self) from **Jnana Yoga** provides immense resilience. It helps us navigate loss, failure, and criticism by reminding us that our true worth is not tied to our temporary bodies, careers, or social status.

    *   **In Society:** The spirit of **Bhakti Yoga** inspires selfless service. It is the engine behind countless NGOs and individuals who work for the welfare of others, seeing a reflection of the divine in those they help.

    The Mahabharata, and the Gita within it, is not a relic of the past to be placed in a museum. It is a living, breathing guide. Its stage was the ancient soil of Haryana, but its message is for all humanity, for all time.

    **Teaser for the Next Chapter:** The great war, devastating as it was, created a massive power vacuum in northern India. The Kuru dynasty was shattered. This period of instability and recovery set the stage for the rise of new powers and great empires. In the next chapter, we will explore the **Rise of the Mahajanapadas and the stamp of Emperors like Ashoka**, who would try to unite the subcontinent not with the sword of war, but with the 'sword' of a different kind of Dharma.
    """)
    st.markdown("---")


    # --- PART 7: THE CHECK-UP (THE PARIKSHA) ---
    st.header("The Pariksha: Check Your Understanding")
    st.markdown("Let's consolidate what we've learned. Answer these questions to test your knowledge of the Mahabharata's core concepts.")

    questions = {
        "1. What is the central 'analogy' this chapter uses to describe the Mahabharata's conflict?": {
            "options": ["A natural disaster.", "A cosmic family feud over inheritance.", "A political election.", "A scientific experiment."],
            "correct": "A cosmic family feud over inheritance.",
            "explanation": "Correct! The chapter frames the epic as a relatable family dispute elevated to a cosmic scale, where the property is a kingdom and the conflict is about Dharma itself."
        },
        "2. What is the primary significance of 'Jyotisar'?": {
            "options": ["It was the main battlefield.", "It was the capital city of the Kauravas.", "It's where Krishna delivered the Bhagavad Gita to Arjuna.", "It's where the Pandavas lived in exile."],
            "correct": "It's where Krishna delivered the Bhagavad Gita to Arjuna.",
            "explanation": "Exactly! Jyotisar is revered as the precise location where the divine wisdom of the Gita was revealed, making it the 'fount of knowledge'."
        },
        "3. Which path (Yoga) from the Gita is most suited for an active person and emphasizes 'action without attachment to the results'?": {
            "options": ["Jnana Yoga (Path of Knowledge)", "Bhakti Yoga (Path of Devotion)", "Karma Yoga (Path of Action)", "Raja Yoga (Path of Meditation)"],
            "correct": "Karma Yoga (Path of Action)",
            "explanation": "Perfect! Karma Yoga is the path of selfless action, allowing one to engage with the world purposefully without being entangled by the desire for specific outcomes."
        },
        "4. In the Kuru family tree, who were the 'Pandavas'?": {
            "options": ["The hundred sons of the blind king Dhritarashtra.", "The advisors and ministers of the court.", "The five sons of King Pandu, including Arjuna.", "The gods who supported the Kauravas."],
            "correct": "The five sons of King Pandu, including Arjuna.",
            "explanation": "Correct. The Pandavas were the five brothers—Yudhishthira, Bhima, Arjuna, Nakula, and Sahadeva—who represented the side of Dharma."
        },
        "5. What is the key takeaway or 'Horizon' message of this chapter?": {
            "options": ["That wars should always be avoided.", "That family disputes are always destructive.", "That the Gita provides a timeless toolkit for purposeful action and decision-making.", "That Haryana has many historical sites."],
            "correct": "That the Gita provides a timeless toolkit for purposeful action and decision-making.",
            "explanation": "Yes! The ultimate point is that the wisdom from the epic is a practical and powerful guide for navigating the challenges of modern life by framing our actions within a context of Dharma."
        }
    }

    for i, (question, data) in enumerate(questions.items()):
        st.markdown(f"**{question}**")
        user_answer = st.radio("", data["options"], key=f"q{i}", index=None)
        
        if user_answer:
            if user_answer == data["correct"]:
                st.success(data["explanation"])
            else:
                st.error(f"Not quite. The correct answer is: **{data['correct']}**. {data['explanation']}")
        st.markdown("---")