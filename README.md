![resume_image](https://user-images.githubusercontent.com/55837093/219502853-4aa23234-a086-460d-a9c2-db809fc43247.jpeg)



# CV Improver using Machine Learning
Hello :smiley: thank you for being here!

This is a Python project that will help you improving the CV using Artificial Intelligence. 
In particular, we will use the ChatGPT API to improve the __summary__ of  your CV and the AI will also review your work experience, making it more appealing for recruiters!

This project has two important applications. 
Let's  describe them

## 1. Application script

The application script uses the __streamlit__, that is an open-source app framework for Machine Learning and Data Science. 
In order to run it, once you download the folder and the ```pip install requirements.txt``` file, you have to change the ```constants.py``` file and change it with the Open AI API key †. (Unfortunately, OpenAI blocks your keys when they are shared online, so mine wont work and you have to put yours).

† If you do not have an Open AI API key, please follow the [Open AI blogpost](https://openai.com/blog/openai-api/).

Once that you have followed the procedure, what you'd have to do is to run the app using:

```streamlit run app.py```

and follow the procedure that the app will ask you. The app will provide you with a ```cv_template.txt``` file. Download it, fill it up with all your details. You can add __Experiences__, update the __summary__, delete __experiences__. 

The app will provide the details of everything that is happening, the summary and the work experience proposal will be printed and the result will be given in terms of a downloadable file that you can easily download with a button. :rocket:

## 2. main.py script

The application script uses the __streamlit__, that is an open-source app framework for Machine Learning and Data Science. 
In order to run it, once you download the folder and the ```pip install requirements.txt``` file, you have to change the ```constants.py``` file and change it with the Open AI API key †. (Unfortunately, OpenAI blocks your keys when they are shared online, so mine wont work and you have to put yours).

† If you do not have an Open AI API key, please follow the [Open AI blogpost](https://openai.com/blog/openai-api/).

Once that you have followed the procedure, what you'd have to do is to run the app using:

```python main.py```

In this file, change the 'cv_example.txt' file with the file that you want to be analyzed. Look for this line:

```uploaded_file = open('cv_example.txt','r')```

This script is less "user friendly", but very efficient. It doesn't print anything but it outputs a "cv_reviewed.txt" file that is the file with the proposal change in the summary and work experiences. 

## 3. Examples

This is an example using the script on my CV.

__Input SUMMARY:__ 

I’m a Physicist that has developed strong skills in Data Science and Deep Learning.Master’s Degree in Physics Of Complex Systems and Big Data (grade: 110/110 cum laude).

Currently working as a Research Assistant with the Aerospace Engineering and Engineering Mechanics Department of the University of Cincinnati while pursuing the PhD. 

The goal of my research is finding ways to optimize engineering experiments using Machine Learning and Data Science.Technical writer for Towards Data Science about trending Machine Learning applications and techniques to real world problems (60k+ monthly views). 

Course Creator and Teacher for Teens in AI. Developer of Image Processing I and Signal Processing I courses.

*** 
__AI Improved SUMMARY:__

I am an exceptionally talented Physicist with an impressive background in Data Science and Deep Learning. I have achieved an outstanding grade of 110/110 cum laude in my Master's Degree in Physics Of Complex Systems and Big Data. I am currently employed as a Research Assistant at the Aerospace Engineering and Engineering Mechanics Department of the University of Cincinnati, where I am optimizing engineering experiments through the use of Machine Learning and Data Science techniques. Additionally, I am a Technical Writer for Towards Data Science, with over 60k monthly views, and have created and instructed Courses in Image Processing I and Signal Processing I for Teens in AI.

***

__Input EXPERIENCES:__ 

_EXPERIENCE 1:_

Using Machine Learning to create surrogate modeling and increase the efficiency of Mechanical Engineering experiments. Hands on research in Traditional and Deep Machine Learning.[SEP]


_EXPERIENCE 2:_

50+ technical articles about using Machine Learning applications on real world problems. 50k+ monthly views.[SEP]

_EXPERIENCE 3:_

Developing Deep Learning techniques to decrease the scanning time of MRI scans[SEP]


_EXPERIENCE 4:_

Developing Deep Learning algorithms to classify Solar Flares based on magnetograms[SEP]

*** 
__AI Improved EXPERIENCES:__

_EXPERIENCE 1:_


I have extensive experience in utilizing Machine Learning to create surrogate modeling and optimize the efficiency of Mechanical Engineering experiments. My research background includes both Traditional and Deep Machine Learning, and I am eager to apply my knowledge and skills to a new role.

_EXPERIENCE 2:_


I have authored over 50 technical articles on the use of Machine Learning applications to solve real-world problems, garnering 50,000+ monthly views.

_EXPERIENCE 3:_


Developing Deep Learning techniques to dramatically reduce the scanning time of MRI scans

_EXPERIENCE 4:_


I recently completed a Bachelor's thesis exploring the potential of a Deep Neural Network to predict the next solar cycle. My research focused on the development of a model that could accurately forecast solar activity and provide insight into future solar behavior. I employed a variety of techniques, including data mining, statistical analysis, and machine learning, to create a model that achieved a high degree of accuracy. My findings have the potential to significantly improve our understanding of solar activity and provide valuable information for predicting future solar cycles.

***

### Contacts!

Thank you so much for reading this! If you want to stay in touch add me on 

[Linkedin](https://www.linkedin.com/in/pieropaialunga/)
[Medium](https://piero-paialunga.medium.com/)


