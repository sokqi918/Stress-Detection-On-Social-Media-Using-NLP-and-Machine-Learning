# library

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav','rb'))

# creating a function for prediction

def stress_detection(input_data):
    import joblib

    import gensim
    from gensim.parsing.preprocessing import STOPWORDS

    import nltk
    from nltk.corpus import stopwords
    nltk.download('stopwords')
    nltk.download('wordnet')
    from nltk.stem import WordNetLemmatizer

    # data preprocessing
    stop_words = stopwords.words('english')
    lemmatizer = WordNetLemmatizer()

    def preprocess(text):
        result = []
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 2 and token not in stop_words:
                result.append(lemmatizer.lemmatize(token))
        return result

    # Preprocess and transform the input data using the loaded vectorizer
    processed_data = preprocess(input_data)
    joined_text = [" ".join(processed_data)]

    # save model
    saved_tfidf = joblib.load('tfidf.joblib')

    X_train_tfidf = saved_tfidf.transform(joined_text)

    prediction = loaded_model.predict(X_train_tfidf)
    print(prediction)

    if prediction == 0:
        return "**Stress-Free!** Based on your responses, it seems that the words may not be contributing to stress. If you need further assistance, please visit our pages for additional resources and guidance."
    else:
        return "**Stress!** Based on your responses, it seems that certain words may be **contributing to stress**. If you need further assistance, please visit our pages for additional resources and guidance."


def main():
    
    # giving a title
    st.title('What is Stress?')
    
    #insert photo
    from PIL import Image
    img = Image.open("what is stress.png")
    st.image(img)
    
    st.header("Share Your Story")
    st.write("*Life can be challenging, and we believe that sharing your experiences can be a powerful step towards understanding stress. Your story matters, and by opening up, you not only contribute to a supportive community but also take the first step towards a healthier, more resilient you.*")
    
    st.header("Our Stress Detector")
    st.write("Our advanced stress detection system will analyze your story to identify potential stressors and patterns. Based on this, we will provide personalized insights and coping strategies to help you navigate through difficult times.")
    st.info("Ready to share? Write your story below and take first step towards a stress-free future.")
    
    # getting the input data from user
    Stress_Content = st.text_input('Content')
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    if st.button('Detect'):
        diagnosis = stress_detection(Stress_Content)
        
        
    st.success(diagnosis)
    
    
# if __name__ == '__main__':
#    main()

def introduction():
    st.title("Stress Self-Guide Web")
    st.header("Welcome to Stress Self-Guide!")
    st.write("In the hustle and bustle of our daily lives, stress has become an unwelcome companion for many. At Stress Self-Guide Web, we understand the impact that stress can have on your well-being, and we're to help you navigate through it.")
    
    # what is this apps?
    st.header("What is Stress Self-Guide Web?")
    st.write("Stress Self-Guide is a dedicate platform designed to provide you with valuable insights into stress, its causes, and most importantly, effective strategies to manage and overcome it. Whether you're dealing with the pressures of work, relationships, or other life challenges, our goals is to empower you with the knowledge and tools to lead a more balanced and fulfilling life.")
    
    # key feature
    st.header("Key Features of Stress Self-Guide Web")
    st.markdown("""
    - **Educational Resources:** We will provide stress information for you to understand stress and what symptoms when the people are having stress.
    - **Interactive Stress Detector:** Share your story with us, and our stress detector will analyze your narrative to help you identify stress-related patterns and triggers.
    - **Stress Management:** Receive tailored suggestions to maange stress effectively.
    - **Supportive Community:** Connect with others who are on similar journey.
        """)
    
    #insert photo
    from PIL import Image
    img3 = Image.open("youcan.jpg")
    st.image(img3)
    
    
    # join us
    st.header("Join Us on the Journey to Stress-Free Living")
    st.write("Embark on a journey towards a healthier and more balanced life. At Stress Self-Guide, we're here to provide knowledge, support, and tools you need to conquer stress and thrive.")
    st.write("**Ready to take the first step?**")
    st.write("*Share your story, explore our resources, and let's navigate the path to a stress-free future together.*")
    
# Page: Sypmtoms
def symptom():
    
    # insert photo
    from PIL import Image
    img1 = Image.open("how it feels to have stress.jpg")
    st.image(img1)
    
# Page: Stress Management
def Stress_Manage():
    
    # insert photo
    from PIL import Image
    img2 = Image.open("C:Stress management.jpg")
    st.image(img2)

def needhelp():
    st.title("Contact Us")

    # Contact form
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    story = st.text_area("Your Story:")

    # Submit button
    if st.button("Submit"):
        # Process the form data (you can add your logic here)
        # For simplicity, we'll just print the information
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Story: {story}")

        # Thank the user and mention that you'll contact them soon
        st.success("Thank you for reaching out! We'll contact you soon.")
        
    # Include a phone number for immediate assistance
    st.info("If you need immediate assistance or are in crisis, please call **[1800 88 8888]**.")

# Sidebar navigation
pages = {"Introduction":introduction,"Stress Detector": main, "How It Feels to Have Stress?": symptom, "How Can I Manage Stress?": Stress_Manage,"Contact Us!":needhelp}
page = st.sidebar.radio("Pages", list(pages.keys()))

# Run the selected page
pages[page]()       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







