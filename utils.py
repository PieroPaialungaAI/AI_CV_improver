from constants import * 


def get_fixedkey_text(key,text):
    key_order = ORDERED_KEYS.index(key)
    next_key = ORDERED_KEYS[key_order+1]
    start_text =  text.split(key+':')[1]
    find_stop = start_text.find(next_key)
    trimmed_text = start_text[0:find_stop]
    trimmed_text = trimmed_text.replace('\n','')
    return trimmed_text

def extract_content(name_of_file):
    file = open(name_of_file,'r')
    content = file.read()
    file.close()
    return content

if __name__=='__main__':
    trimmed_text=get_fixedkey_text(FIXED_KEYS[1],extract_content('cv_example.txt'))
    print(trimmed_text)