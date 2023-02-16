

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

