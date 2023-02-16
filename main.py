from PIL import Image
import streamlit as st
from ai_improver import * 
from constants import * 
from cv_scanner import * 


def summary_result_main(string_data):
    trimmed_text=get_fixedkey_text(FIXED_KEYS[1],string_data)
    text = summary_corrector_main(trimmed_text)
    return text
    
def experience_result_main(experience_text):
    text=single_experience_corrector_main(experience_text)
    return text
    
if __name__=='__main__':
    uploaded_file = open('cv_example.txt','r')
    reviewed_experiences = []
    if uploaded_file is not None:
        string_data = uploaded_file.read()
        reviewed_summary = summary_result_main(string_data)
        experiences = experience_parser(string_data)
        for e in experiences:
            review_experience = experience_result_main(e.split('[SEP]')[-2])
            reviewed_experiences.append(review_experience)
        new_file = open('cv_improved_main.txt','w+')
        new_file.write('SUMMARY:\n')
        new_file.write(reviewed_summary)
        for e in range(len(reviewed_experiences)):
            new_file.write('\n EXPERIENCE %i \n'%(e))
            new_file.write(reviewed_experiences[e])
        new_file.close()
        

    