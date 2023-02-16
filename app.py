from PIL import Image
import streamlit as st
from ai_improver import * 
from constants import * 
from cv_scanner import * 


def summary_result(string_data):
    st.write('Improving the summary for you! :rocket:')
    trimmed_text=get_fixedkey_text(FIXED_KEYS[1],string_data)
    text = summary_corrector(trimmed_text)
    return text
    
def experience_result(experience_text):
    st.write('Improving the work experience for you!')
    text=single_experience_corrector(experience_text)
    return text
    
if __name__=='__main__':
    image = Image.open('resume_image.jpeg')
    st.image(image, caption='Photo by Unseen Studio on Unsplash')
    st.header('Improving your CV in seconds using ChatGPT!')
    st.write('This app is meant to improve the quality of your CV by using Artificial Intelligence\n Start by downloading the template, fill the information, upload your CV and enjoy the magic! :smile:')
    st.write("\n Let's see what you got! Download the following template and fill it out with your information! :sunglasses:")
    download_template()
    uploaded_file = st.file_uploader("Upload your CV here! :point_down:") 
    reviewed_experiences = []
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)
        string_data = stringio.read()
        st.subheader('Lets discuss the summary :male-detective:')
        reviewed_summary = summary_result(string_data)
        st.subheader('Lets discuss the work experience :office:')
        experiences = experience_parser(string_data)
        st.write('We noticed that you added ' + str(len(experience_parser(string_data)))+ ' work experiences! :eyes:')
        for e in experiences:
            print('Experience:')
            print(e.split('[SEP]')[-2])
            review_experience = experience_result(e.split('[SEP]')[-2])
            reviewed_experiences.append(review_experience)
        new_file = open('cv_improved.txt','w+')
        new_file.write('SUMMARY:\n')
        new_file.write(reviewed_summary)
        for e in range(len(reviewed_experiences)):
            new_file.write('\nEXPERIENCE %i \n'%(e))
            new_file.write(reviewed_experiences[e])
        new_file.close()
        download_result()
        

    