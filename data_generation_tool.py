import os
import glob
import json
import csv
import pandas as pd
import atexit


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
from datetime import datetime
from random import choice


from transformers import pipeline, T5ForConditionalGeneration, RobertaTokenizer, PreTrainedTokenizerFast, AutoModelForCausalLM, AutoTokenizer 

# Load a paraphrasing pipeline using pegasus-xsum
# paraphraser = pipeline("text2text-generation", model="facebook/bart-base")
paraphraser = pipeline("text2text-generation", model="tuner007/pegasus_paraphrase")
# paraphraser = pipeline("text2text-generation", model="sentence-transformers/paraphrase-MiniLM-L6-v2")
code_rephraser = AutoModelForCausalLM.from_pretrained("NTQAI/Nxcode-CQ-7B-orpo",torch_dtype="auto",
    device_map="mps")
tokenizer = AutoTokenizer.from_pretrained("NTQAI/Nxcode-CQ-7B-orpo")

# Generate paraphrases
def generate_paraphrase(input):
    return paraphraser(f"{input}", max_length=60, num_return_sequences=10, num_beams = 10)

def generate_paraphrase_code(output):
    random_phrase = ["translate Python to Python: "]
    input_ids = tokenizer(choice(random_phrase) + output, return_tensors="pt").input_ids
    outputs = code_rephraser.generate(input_ids, max_length=2048)
    breakpoint()
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def generate_code_ntqai(output):
    messages = [
        {"role": "user", "content": output}
    ]
    inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(code_rephraser.device)
    outputs = code_rephraser.generate(inputs, max_new_tokens=2048, do_sample=False, top_k=50, top_p=0.95, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)
    res = tokenizer.decode(outputs[0][len(inputs[0]):], skip_special_tokens=True)
    return res


existing_rows=[]

# def on_exit():
#     print("Script has ended, saving progress.")
#     with open('json_log.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['File','Entry','Success','Date'])
#         writer.writerows(existing_rows)

# Register the exit function
# atexit.register(on_exit)

# Specify the directory
folder_path = "Training"
df = pd.read_csv('processeddata/joined_df.csv')
df['action_time'] = pd.to_datetime(df['action_time'])
df['Date']=pd.to_datetime(df['Date'])

manjari_bold_path = 'font/Manjari-Bold.ttf'
manjari_regular_path = 'font/Manjari-Regular.ttf'
manjari_thin_path = 'font/Manjari-thin.ttf'

dark = "#3B3365"
medium = "#8F81DD"
light = "#BCADFF"
peach = "#FFEEDD"

logo_img = mpimg.imread('Media/horizontal-logo.png')

# Load the custom font
manjari_bold = fm.FontProperties(fname=manjari_bold_path)
manjari_regular = fm.FontProperties(fname=manjari_regular_path)
manjari_thin = fm.FontProperties(fname=manjari_thin_path)

new = []

with open('Training/manual_add.json', 'r') as json_file:
    data = json.load(json_file) 
    for e in range(0,len(data)):
        instruction = data[e]["instruction"]
        output = data[e]["output"]
        try:
            
            new_instruction = generate_paraphrase(instruction)
            print(f'\n===============================\n{new_instruction}\n===============================\n')
            new_output = generate_code_ntqai(output)
            print(new_output)
            exec(new_output)
            option = input('(Y)es if input matches graph, (N) if input does not match:\t')
            while option.upper() not in ['Y','N']:
                print('Invalid option!')
                option = input('(Y)es if input matches graph, (N) if input does not match:\t')
                
            exec("plt.close(fig)")
        except Exception as e:
            #fails to run - don't add!
            success=False
            print(f'{instruction} - Fail')
            print(e)
        
            

# exit(0)
    


