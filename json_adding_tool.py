import os
import glob
import json
import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
from datetime import datetime

# Specify the directory
folder_path = "Training"
df = pd.read_csv('processeddata/joined_df.csv')

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
            exec(data[e]["output"])
        except:
            #fails to run - don't add!
            success=False
        
        date = datetime.now()
        existing_rows.insert(0, f"{json_files_sorted[i]},{entry},{success},{date}")
        entry += 1
            
    i += 1
print(existing_rows)
    

    

    # If you need to write something, you can use file.write()
    # Example: file.write("New log entry\n")
    
    # You can now read from or write to the file

