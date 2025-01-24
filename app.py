import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
import numpy as np
import random

# Marvel character image URLs (working PNGs with transparent backgrounds)
MARVEL_AVATARS = [
    "https://w0.peakpx.com/wallpaper/668/674/HD-wallpaper-scarlett-johansson-as-black-widow-the-avengers-women-redhead-scarlett-johansson-black-widow-marvel-thumbnail.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmySF6TZ98dJkcdJ2AQz7fvNa0vFxMEWjL9A&s",
    "https://w0.peakpx.com/wallpaper/95/361/HD-wallpaper-ironman-ironman-2-superhero-thumbnail.jpg",
    "https://c4.wallpaperflare.com/wallpaper/107/848/913/spiderman-ps4-spiderman-games-hd-wallpaper-preview.jpg",
    "https://c4.wallpaperflare.com/wallpaper/289/711/826/elizabeth-olsen-women-actress-brunette-dark-hair-hd-wallpaper-preview.jpg",
    "https://wallpapercat.com/w/full/4/0/2/487820-3840x2160-desktop-4k-scarlet-witch-background-image.jpg",
]

# Custom CSS for marble movie vibe (improved layout)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@700&family=Montserrat:wght@400;700&display=swap');

* {
    font-family: 'Montserrat', sans-serif;
}

.stApp {
    background: linear-gradient(45deg, #2c3e50, #3498db);
    color: #ffffff;
}

h1 {
    font-family: 'Cinzel Decorative', cursive;
    color: #f1c40f !important;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    margin-bottom: 2rem;
}

.stTextInput>div>div>input, .stTextArea>div>div>textarea {
    background-color: rgba(255,255,255,0.1);
    color: white;
    border-radius: 8px;
}

.review-card {
    background: rgba(0,0,0,0.7);
    border-radius: 15px;
    padding: 2rem;
    margin: 2rem 0;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    border: 1px solid #f1c40f55;
}

.stars {
    font-size: 2.5rem;
    color: #f1c40f;
    text-shadow: 0 0 8px rgba(241,196,15,0.5);
    margin: 1rem 0;
}

.avatar-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2rem;
}

.marvel-avatar {
    width: 180px;
    height: 180px;
    border-radius: 50%;
    object-fit: cover;
    object-position: top; /* Ensures faces are centered */
    border: 3px solid #f1c40f;
    box-shadow: 0 0 25px rgba(241,196,15,0.4);
    margin-bottom: 1.5rem;
    overflow: hidden;
    transition: all 0.3s ease;
}

.marvel-avatar:hover {
    transform: scale(1.05);
    box-shadow: 0 0 35px rgba(241,196,15,0.6);
}

.critic-name {
    font-size: 1.4rem;
    font-weight: bold;
    color: #f1c40f;
}

.review-content {
    background: rgba(255,255,255,0.1);
    border-radius: 10px;
    padding: 1.5rem;
    margin: 1rem 0;
    color: #ffffff;
    line-height: 1.6;
}
</style>
""", unsafe_allow_html=True)

# Load model and word index
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model('simple_rnn_imdb.h5')
    word_index = tf.keras.datasets.imdb.get_word_index()
    return model, word_index

model, word_index = load_model()

# Helper functions
def preprocess_text(text):
    words = text.lower().replace('<br />', ' ').split()
    encoded = [word_index.get(word, 0) + 3 for word in words]
    padded = sequence.pad_sequences([encoded], maxlen=500)
    return padded

def get_stars(prediction):
    score = prediction * 10  # Convert to 0-10 scale
    if score < 2: return 1
    elif score < 4: return 2
    elif score < 6: return 3
    elif score < 8: return 4
    else: return 5

# App layout
st.title('🎬 Cinematic Review Analyzer')
st.markdown("### Experience the Magic of AI-Powered Movie Insights")

# Initialize session state for avatar persistence
if 'selected_avatar' not in st.session_state:
    st.session_state.selected_avatar = random.choice(MARVEL_AVATARS)

with st.form("review_form"):
    col1, col2 = st.columns([2, 1])
    
    with col1:
        name = st.text_input("Critic's Name", "Anonymous")
        text = st.text_area("Movie Review", height=200,
                          placeholder="Share your cinematic experience...",
                          help="Write your honest review about the movie")
        
    with col2:
        st.markdown(f"""
        <div class="avatar-container">
            <img src="{st.session_state.selected_avatar}" class="marvel-avatar">
            <div class="critic-name">{name}</div>
        </div>
        """, unsafe_allow_html=True)
    
    submitted = st.form_submit_button("✨ Generate Analysis")

if submitted and text:
    with st.spinner('Analyzing your review...'):
        # Preprocess and predict
        processed = preprocess_text(text)
        prediction = model.predict(processed)[0][0]
        stars = get_stars(prediction)
        sentiment = "Positive" if prediction > 0.5 else "Negative"
        
        # Display results
        st.markdown("<div class='review-card'>", unsafe_allow_html=True)
        
        # Display Marvel avatar and name
        st.markdown(f"""
        <div class="avatar-container">
            <img src="{st.session_state.selected_avatar}" class="marvel-avatar">
            <div class="critic-name">{name}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Review content
        st.markdown("<div class='review-content'>", unsafe_allow_html=True)
        st.write(text)
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Review analysis
        st.markdown(f"**📜 Verdict:** {sentiment} Experience")
        st.markdown(f"**📊 Confidence Score:** {prediction:.2%}")
        
        # Star display
        star_display = "★" * stars + "☆" * (5 - stars)
        st.markdown(f"<div class='stars'>{star_display}</div>", unsafe_allow_html=True)
        
        # Sentiment specific message
        if sentiment == "Positive":
            st.success("🌟 This film is a masterpiece! Highly recommended for cinephiles.")
        else:
            st.error("💤 This movie needs more cinematic magic. Proceed with caution.")
        
        st.markdown("</div>", unsafe_allow_html=True)

elif submitted and not text:
    st.warning("Please enter a movie review to analyze!")

# Add footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #bdc3c7; padding: 2rem 0;">
    ✨ Transforming Words into Cinematic Insights •
    © 2024 Ankit Pokhrel
</div>
""", unsafe_allow_html=True)