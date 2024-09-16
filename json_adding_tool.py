import os
import glob
import json
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.image as mpimg

# Specify the directory
folder_path = "Training"
df = pd.read_csv('processeddata/joined_df.csv')
df

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
# Move the cursor to the beginning of the file
    file.seek(0)
    # Read the current content (if needed)
    first_line = file.readline().strip()

    if first_line:
        file_name = first_line.split(',')[0]
        entry_number = first_line.split(',')[1]
        for json in json_files_sorted:
            if os.path.basename(json)==file_name:
                break
            i += 1
while i < len(json_files_sorted):
    with open(json_files_sorted[i], 'r') as json_file:
        data = json.load(json_file) 
        eof = False
        for e in range(entry,len(data)):
            try:
                exec(data[e]["output"])
            except:
                #fails to run - don't add!
    i += 1
    

    

    # If you need to write something, you can use file.write()
    # Example: file.write("New log entry\n")
    
    # You can now read from or write to the file

