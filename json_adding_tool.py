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

existing_rows=[]

def on_exit():
    print("Script has ended, saving progress.")
    with open('json_log.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['File','Entry','Success','Date'])
        writer.writerows(existing_rows)

# Register the exit function
atexit.register(on_exit)

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

# Get all .json files from the folder
json_files = [f for f in glob.glob(os.path.join(folder_path, "*.json")) if 'manual_add.json' not in f]

# Sort files by creation date
json_files_sorted = sorted(json_files, key=os.path.getctime, reverse=True)
i = 0
entry = 0
with open('json_log.csv', 'a+') as file:
    reader = csv.reader(file)
    # Move the cursor to the beginning of the file
    # Read the current content (if needed)
    existing_rows = list(reader)
        

if len(existing_rows)>0:
    existing_rows = existing_rows[1:]
    first_line = existing_rows[0]
    file_name = first_line.split(',')[0]
    entry = first_line.split(',')[1]+1
    for json in json_files_sorted:
        if os.path.basename(json)==file_name:
            break
        i += 1

while i < len(json_files_sorted):
    with open(json_files_sorted[i], 'r') as json_file:
        data = json.load(json_file) 
    for e in range(entry,len(data)):
        success=True
        try:
            print(f'\n===============================\n{data[e]["instruction"]}\n===============================\n')
            fixed_output = data[e]["output"].replace("plt.show()","plt.show(block=False)")
            exec(fixed_output)
            option = input('(Y)es if input matches graph, (N) if input does not match:\t')
            while option.upper() not in ['Y','N']:
                print('Invalid option!')
                option = input('(Y)es if input matches graph, (N) if input does not match:\t')
            if option == 'N':
                success=False
            exec("plt.close(fig)")
        except:
            #fails to run - don't add!
            success=False
            print(f'{data[e]["instruction"]} - Fail')
        
        date = datetime.now()
        existing_rows.insert(0, [json_files_sorted[i],entry,success,date])
        entry += 1
            
    i += 1
exit(0)
    

    

    # If you need to write something, you can use file.write()
    # Example: file.write("New log entry\n")
    
    # You can now read from or write to the file

