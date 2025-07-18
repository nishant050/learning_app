# In dharma_sindhu_saga/chapter_0_syllabus.py
import streamlit as st
from utils.plotting import image_search_button # Assuming you will use this utility

def render():
    """
    Renders the syllabus page for the Hindu Dharma & The Haryana Saga.
    This acts as the main index and introduction to this learning path.
    """

    # --- PAGE HEADER ---
    st.title("🕉️ The Dharma-Kshetra Saga")
    st.header("An Epic Journey Through Hindu Dharma and the History of Haryana")
    st.markdown("""
    Welcome, seeker, to a new learning saga. This is not just a history lesson; it is an exploration into the very soul of a land and its eternal principles. We will journey from the dawn of civilization on the banks of the Sarasvati to the modern-day dynamism of Haryana, all through the guiding lens of **Dharma**—the eternal code of conduct, righteousness, and cosmic order.

    This land, known as **Dharma-Kshetra** (the field of righteousness) in the Mahabharata, has been the stage for epic battles, profound philosophical revelations, and the rise and fall of great kingdoms. Understanding Haryana is to understand a core thread in the fabric of India's identity.

    Below is the grand syllabus for our journey. Each chapter is a stepping stone to a deeper understanding.
    """)

    image_search_button("Kurukshetra, the land of the Mahabharata", "Kurukshetra Mahabharata")
    st.divider()

    # --- CHAPTER LIST ---
    st.subheader("The Ten Chapters of Our Journey")

    with st.expander("Chapter 1: The Seed of Dharma & The Land of Beginnings", expanded=True):
        st.markdown("""
        *   **Core Idea:** We start at the very beginning, exploring the foundational concepts. What is Sanatana Dharma? Not as a religion, but as an eternal way of life. We then introduce the ancient geography of Haryana, the land watered by the mythical Sarasvati river.
        *   **Topics:** Introduction to the concepts of Dharma, Karma, and Samsara. The geography and climate of ancient Haryana. The legacy of the Indus-Sarasvati Civilization.
        """)

    with st.expander("Chapter 2: Echoes of the Mahabharata - The Field of Righteousness", expanded=True):
        st.markdown("""
        *   **Core Idea:** We dive deep into the world's longest epic poem, the Mahabharata, which unfolds on the soil of Kurukshetra. This chapter explores the historical and cultural significance of the great war and the divine wisdom of the Bhagavad Gita, delivered on this very land.
        *   **Topics:** The story of the Kuru Kingdom. Key sites like Kurukshetra and Jyotisar. The core teachings of the Gita as a guide to life.
        """)

    with st.expander("Chapter 3: The Rise of Kingdoms & The Stamp of Emperors", expanded=False):
        st.markdown("""
        *   **Core Idea:** After the epic age, new powers rose. We trace the lineage of the great Mahajanapadas and the mighty empires, like the Mauryas and Guptas, who left their indelible mark on the region's culture, administration, and trade routes.
        *   **Topics:** The Kuru and Panchala Mahajanapadas. The influence of the Mauryan and Gupta Empires. The rise of important ancient cities like Thanesar.
        """)

    with st.expander("Chapter 4: The Crucible of Conflict - The Battles of Panipat", expanded=False):
        st.markdown("""
        *   **Core Idea:** Haryana's strategic location made it the gateway to Delhi and the site of pivotal battles that reshaped India's destiny. We analyze the three legendary Battles of Panipat, understanding their context, strategy, and long-term consequences.
        *   **Topics:** Detailed analysis of the First (1526), Second (1556), and Third (1761) Battles of Panipat. The clash of empires: Mughals, Afghans, and Marathas.
        """)

    with st.expander("Chapter 5: The Voice of the People - Bhakti, Sufism, and Folk Traditions", expanded=False):
        st.markdown("""
        *   **Core Idea:** Beyond the courts of kings, a powerful spiritual wave swept through the land. We explore the Bhakti and Sufi movements in Haryana, listening to the voices of saints and poets who championed devotion and social equality, shaping the region's unique folk culture.
        *   **Topics:** The teachings of local saints like Garibdas and Nitanand. The synthesis of Hindu and Islamic mystical traditions. The birth of Haryanvi folk music (Ragini) and dance.
        """)

    with st.expander("Chapter 6: The Spark of Rebellion - The 1857 Uprising", expanded=False):
        st.markdown("""
        *   **Core Idea:** The first major cry for freedom from British rule found fervent support in Haryana. We uncover the stories of local heroes and communities who rose in the great revolt of 1857, paying a heavy price for their defiance.
        *   **Topics:** Key events of the 1857 Mutiny in Ambala, Rewari, and Hisar. The role of leaders like Rao Tula Ram. The aftermath and British retribution.
        """)

    with st.expander("Chapter 7: The Making of a Modern State - Identity and Formation", expanded=False):
        st.markdown("""
        *   **Core Idea:** We witness the birth of modern Haryana. This chapter covers the socio-political movements leading to the formation of Haryana as a separate state in 1966 and the challenges and triumphs of its early years.
        *   **Topics:** The Punjabi Suba movement and its impact. The role of the Arya Samaj in shaping regional identity. The linguistic and political reasons for statehood.
        """)

    with st.expander("Chapter 8: The Green Revolution & The Rise of Gurugram", expanded=False):
        st.markdown("""
        *   **Core Idea:** From fields of green to towers of glass. We explore the two great transformations that define modern Haryana: the agricultural boom of the Green Revolution and the meteoric rise of Gurugram as a global corporate and technological hub.
        *   **Topics:** The impact of new farming techniques on Haryana's economy. The story of Maruti Udyog. The urban planning and economic policies that created Gurugram.
        """)

    with st.expander("Chapter 9: The Cultural Fabric - Language, Sports, and Society", expanded=False):
        st.markdown("""
        *   **Core Idea:** We immerse ourselves in the vibrant culture of contemporary Haryana. This chapter celebrates the Haryanvi language, the region's dominance in sports (especially wrestling and boxing), its unique social structure, and its rich traditions.
        *   **Topics:** An introduction to the Haryanvi dialect. The "Akhara" culture and sporting legends. The social system of "Khaps." Traditional attire and cuisine.
        """)

    with st.expander("Chapter 10: Dharma for the 21st Century - The Timeless Principle", expanded=False):
        st.markdown("""
        *   **Core Idea:** In our final chapter, we bring our journey full circle. We reflect on how the eternal principles of Dharma, which we saw unfold across millennia of Haryanvi history, remain profoundly relevant in navigating the complexities of modern life, technology, and global society.
        *   **Topics:** Applying Dharmic principles to modern ethics. The role of tradition in a globalized world. The future of Haryana as a synthesis of the ancient and the ultra-modern.
        """)