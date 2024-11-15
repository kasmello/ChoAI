import json
import code_scrambler
import re
import os
import random
import warnings
import traceback
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
from tqdm import tqdm

manjari_bold_path = 'font/Manjari-Bold.ttf'
manjari_regular_path = 'font/Manjari-Regular.ttf'
manjari_thin_path = 'font/Manjari-thin.ttf'
logo_img = mpimg.imread('Media/horizontal-logo.png')
manjari_bold = fm.FontProperties(fname=manjari_bold_path)
manjari_regular = fm.FontProperties(fname=manjari_regular_path)
manjari_thin = fm.FontProperties(fname=manjari_thin_path)

with open('values.json','r') as file:
    vars = json.load(file)

colours = vars['colours']
date = vars['date']
periods = vars['period']
names = vars['names']
staff_names = vars['staff_name']
band_names = vars['band_name']
machine_names = vars['machine_name']
staff_names = vars['staff_name']
category_names = vars['category_name']
mat_plot_lib_all_plots = vars['mat_plot_lib_all_plots']

def remove_all_files_in_training_folder():

    # List all files in the folder
    for filename in os.listdir("TrainingImages"):
        file_path = os.path.join("TrainingImages", filename)
        
        # Check if it's a file before removing
        if os.path.isfile(file_path):
            os.remove(file_path)

remove_all_files_in_training_folder()


class instruction():
    def __init__(self, instruction, xaxis="", yaxis="", title=""):
        self.instruction = instruction #instruction with tags
        self.xaxis = xaxis
        self.yaxis = yaxis
        self.title = title

    def __str__(self):
        return str({'instruction': self.instruction, 'x-axis': self.xaxis, 'y-axis': self.yaxis,'title': self.title})
    
    def __repr__(self):
        return str({'instruction': self.instruction, 'x-axis': self.xaxis, 'y-axis': self.yaxis,'title': self.title})
    
class data_entry():
    def __init__(self,label: str,instructions, output_raw):
        self.instructions = instructions #instruction class
        self.output_raw = output_raw #list of outputs
        self.graph = self.assess_graph_type()
        self.label = label

    def assess_graph_type(self): #IMPROVE THIS!!

        for graph in mat_plot_lib_all_plots:
            if f'ax.{graph}' in self.output_raw[0] or (graph == 'table' and graph in self.output_raw[0]):
                return graph
        return 'other'
    
    def __str__(self):
        return self.output_raw[0]

    def __repr__(self):
        return self.output_raw[0]
    
#function 1: mix instructions with query

def mix(base_data): #sampling?
    #input: list of data entry
    #output: list of dictionaries
    new_list = []
    print('Mixing')
    for data_entry in tqdm(base_data):
        #first stage: pairing all inputs and outputs
        for instruction, output in zip(data_entry.instructions, data_entry.output_raw):
            if not instruction.xaxis:
                output = re.sub(r'ax\.set_xlabel\([^\)]*\)\n?', '', output)
            else:
                output = output.replace('#XAXIS#',instruction.xaxis)
            if not instruction.yaxis:
                output = re.sub(r'ax\.set_ylabel\([^\)]*\)\n?', '', output)
            else:
                output = output.replace('#YAXIS#',instruction.yaxis)
            if not instruction.title:
                output = re.sub(r'ax\.set_title\([^\)]*\)\n?', '', output)
            else:
                output = output.replace('#TITLE#',instruction.title)
            new_list.append({
                "label": data_entry.label,
                "instruction": instruction.instruction,
                "input": None,
                "output": output,
                "graph": data_entry.graph,
                "error": None,
                "image_location": None
            })
    return new_list

# function 2: replacing random variables

def colour_replace(dict_list):
    temp_list = []
    for i in tqdm(range(len(dict_list))):
        entry = dict_list[i]
        if '#COLOUR#' in entry['instruction']:
            random.seed(i)
            temp_list2 = [
            {
                "label": entry["label"].replace('#COLOUR#', colour.title()),
                "instruction": entry['instruction'].replace('#COLOUR#', colour.title()),
                "input": entry["input"],
                "output": entry['output'].replace('#COLOUR#', colours[colour]),
                "graph": entry["graph"],
                "error": entry['error'],
                "image_location": entry["image_location"]
            }

            for colour in random.sample(list(colours.keys()),10)]
        else:
            temp_list2 = [{
                "label": entry["label"],
                "instruction": entry['instruction'],
                "input": entry["input"],
                "output": entry['output'],
                "graph": entry["graph"],
                "error": entry['error'],
                "image_location": entry["image_location"]
            }]
        temp_list.extend(temp_list2)

    return temp_list

def period_replace(dict_list):
    temp_list = []
    for i in tqdm(range(len(dict_list))):
        entry = dict_list[i]
        if "#PERIOD#" in entry['instruction'] or "#START#" in entry['instruction'] or "#END#" in entry['instruction']:
            random.seed(i+5)
            temp_list2 = [{
                "label": entry["label"].replace('#PERIOD#', period),
                "instruction": entry['instruction'].replace('#PERIOD#', period).replace('#START#', periods[period][0]).replace('#END#', periods[period][1]),
                "input": entry["input"],
                "output": entry['output'].replace('#PERIOD#', period).replace('#START#', periods[period][0]).replace('#END#', periods[period][1]),
                "graph": entry["graph"],
                "error": entry['error'],
                "image_location": entry["image_location"]
            }
            for period in random.sample(list(periods.keys()),10)]
        else:
            temp_list2 = [{
                "label": entry["label"],
                "instruction": entry['instruction'],
                "input": entry["input"],
                "output": entry['output'],
                "graph": entry["graph"],
                "error": entry['error'],
                "image_location": entry["image_location"]
            }]

        temp_list.extend(temp_list2)

    return temp_list

def staff_replace(dict_list):
    temp_list = []
    for i in tqdm(range(len(dict_list))):
        entry = dict_list[i]
        if '#STAFF_NAME#' in entry['instruction']:
            random.seed(i**2)
            temp_list2 = [
            {
                "label": entry["label"].replace('#STAFF_NAME#', staff_name.title()),
                "instruction": entry['instruction'].replace('#STAFF_NAME#', staff_name.title()),
                "input": entry["input"],
                "output": entry['output'].replace('#STAFF_NAME#', staff_name.title()),
                "graph": entry["graph"],
                "error": entry['error'],
                "image_location": entry["image_location"]
            }

            for staff_name in random.sample(staff_names,4)]
        else:
            temp_list2 = [{
                "label": entry["label"],
                "instruction": entry['instruction'],
                "input": entry["input"],
                "output": entry['output'],
                "graph": entry["graph"],
                "error": entry['error'],
                "image_location": entry["image_location"]
            }]
        temp_list.extend(temp_list2)

    return temp_list

def band_replace(dict_list):
    temp_list = []
    for i in tqdm(range(len(dict_list))):
        entry = dict_list[i]
        if '#BAND_NICKNAME#' in entry['instruction']:
            random.seed(i**3)
            bands = random.sample(list(band_names.keys()),6)
            for band in bands:
            
                temp_list2 = [
                {
                    "label": entry["label"].replace('#BAND_NICKNAME#', nickname.title()),
                    "instruction": entry['instruction'].replace('#BAND_NICKNAME#', nickname.title()),
                    "input": entry["input"],
                    "output": entry['output'].replace('#BAND_NAME#', band).replace('#BAND_NICKNAME#', nickname.title()),
                    "graph": entry["graph"],
                    "error": entry['error'],
                    "image_location": entry["image_location"]
                }

                for nickname in band_names[band]]
                temp_list.extend(temp_list2)
        else:
            temp_list2 = [{
                "label": entry["label"],
                "instruction": entry['instruction'],
                "input": entry["input"],
                "output": entry['output'],
                "graph": entry["graph"],
                "error": entry['error'],
                "image_location": entry["image_location"]
            }]
            temp_list.extend(temp_list2)

    return temp_list

def category_replace(dict_list):
    temp_list = []
    for i in tqdm(range(len(dict_list))):
        entry = dict_list[i]
        if '#CATEGORY_ALTNAME#' in entry['instruction']:
            for category in category_names.keys():
            
                temp_list2 = [
                {
                    "label": entry["label"].replace('#CATEGORY_ALTNAME#', alt_name.title()),
                    "instruction": entry['instruction'].replace('#CATEGORY_ALTNAME#', alt_name.title()),
                    "input": entry["input"],
                    "output": entry['output'].replace('#CATEGORY_NAME#', category).replace('#CATEGORY_ALTNAME#', alt_name.title()),
                    "graph": entry["graph"],
                    "error": entry['error'],
                    "image_location": entry["image_location"]
                }

                for alt_name in category_names[category]]
                temp_list.extend(temp_list2)
        else:
            temp_list2 = [{
                "label": entry["label"],
                "instruction": entry['instruction'],
                "input": entry["input"],
                "output": entry['output'],
                "graph": entry["graph"],
                "error": entry['error'],
                "image_location": entry["image_location"]
            }]
            temp_list.extend(temp_list2)

    return temp_list

def machine_replace(dict_list):
    temp_list = []
    for i in tqdm(range(len(dict_list))):
        entry = dict_list[i]
        if '#MACHINE_ALTNAME#' in entry['instruction']:
            for machine in machine_names.keys():
                random.seed(len(machine)**i)
                temp_list2 = [
                {
                    "label": entry["label"],
                    "instruction": entry['instruction'].replace('#MACHINE_ALTNAME#', alt_name.title()),
                    "input": entry["input"],
                    "output": entry['output'].replace('#MACHINE_NAME#', machine).replace('#MACHINE_ALTNAME#', alt_name.title()),
                    "graph": entry["graph"],
                    "error": entry['error'],
                    "image_location": entry["image_location"]
                }

                for alt_name in random.sample(machine_names[machine],2)]
                temp_list.extend(temp_list2)
        else:
            temp_list2 = [{
                "label": entry["label"],
                "instruction": entry['instruction'],
                "input": entry["input"],
                "output": entry['output'],
                "graph": entry["graph"],
                "error": entry['error'],
                "image_location": entry["image_location"]
            }]
            temp_list.extend(temp_list2)

    return temp_list



def flag_replace(dict_list): #need to add randomness
    #input: dict list
    #output: dict list
    new_list = []
    print('Replacing Colour Flag')
    new_list = colour_replace(dict_list)
    print('Replacing Period Flag')
    new_list = period_replace(new_list)
    print('Replacing Staff Flag')
    new_list = staff_replace(new_list)
    print('Replacing Band Flag')
    new_list = band_replace(new_list)
    print('Replacing Category Flag')
    new_list = category_replace(new_list)
    print('Replacing Machine Flag')
    new_list = machine_replace(new_list)
    
    return new_list
                    
# function 3: scramble

def scramble(dict_list):
    #input: dict list
    #output: dict list
    new_list = []
    print('Scrambling columns')
    for i in tqdm(range(len(dict_list))):
        entry = dict_list[i]
        random.seed(i)
        index_arr = [random.randint(0,len(code_scrambler.df_columns_list)-1) for _ in range(5)]
        for index in index_arr:
            filename = code_scrambler.df_columns_list[index]['filename']
            output= dict_list[i]['output'].replace('#STAFF#',code_scrambler.df_columns_list[index]['staff'])
            output = output.replace('#REPLACED#',code_scrambler.df_columns_list[index]['replaced'])
            output = output.replace('#ACTION#',code_scrambler.df_columns_list[index]['action'])
            output = output.replace('#QUANTITY#',code_scrambler.df_columns_list[index]['quantity'])
            output = output.replace('#ORDER_ID#',code_scrambler.df_columns_list[index]['order_id'])
            output = output.replace('#TOTAL#',code_scrambler.df_columns_list[index]['total'])
            output = output.replace('#CATEGORY#',code_scrambler.df_columns_list[index]['category'])
            output = output.replace('#ARTIST#',code_scrambler.df_columns_list[index]['artist'])
            output = output.replace('#MACHINE#',code_scrambler.df_columns_list[index]['machine'])
            output = output.replace('#DETAIL#',code_scrambler.df_columns_list[index]['detail'])
            new_list.append({
                "label": entry["label"],
                "instruction": entry['instruction'],
                'input': filename,
                'output': output,
                'graph': entry['graph'],
                "error": entry['error'],
                "image_location": entry["image_location"]
            })
    return new_list



# function 4: oo-to-state
    
def oo_to_state(dict_list):
    #input is dict
    #output is dict 
    new_list = dict_list
    print('OO to State')
    for i in tqdm(range(len(dict_list))):
        entry = dict_list[i]
        output = code_scrambler.rewrite_ast_to_plot(entry['output'])
        new_list.append({
                "label": entry["label"],
                "instruction": entry['instruction'],
                'input': entry['input'],
                'output': output,
                'graph': entry['graph'],
                "error": entry['error'],
                "image_location": entry["image_location"]
            })
    return new_list

#function 5: test

def test(dict_list):
    #LOADING ALL DATASETS
    new_list = []
    all_dfs = {}
    graph_types = {}
    errors = 0
    warnings_s = 0
    short_error = ''
    image_location = ''
    print('Testing')
    for i in range(200):
        data = pd.read_csv(f'ProcessedData/Joined_DF_{i}.csv')
        try:
            data['action_time'] = pd.to_datetime(data['action_time'])
        except KeyError:
            data['action'] = pd.to_datetime(data['action'])
        data['Date']=pd.to_datetime(data['Date'])
        all_dfs[f'ProcessedData/Joined_DF_{i}.csv'] = data

    for i in tqdm(range(len(dict_list))):
        entry = dict_list[i]

        df = all_dfs[entry['input']]
        try:
            with warnings.catch_warnings(record=True) as caught_warnings:
                warnings.simplefilter("always")
                exec(f"{dict_list[i]['output']}\nplt.savefig('TrainingImages/{i}_{entry['graph']}_{entry['label']}.png', bbox_inches='tight')")
                for w in caught_warnings:
                    _, _, tb = traceback.sys.exc_info()
                    full_error = traceback.format_exc()
                    short_error = f'{type(w).__name__ }({tb.tb_lineno}): for {str(w)}'
                    print(full_error)
                    warnings_s += 1
            image_location = f"TrainingImages/{i}_{entry['graph']}_{entry['label']}.png"

        except AttributeError as e:
            continue

        except Exception as e:
            _, _, tb = traceback.sys.exc_info()
            full_error = traceback.format_exc()
            short_error = f'{type(e).__name__ }({tb.tb_lineno}): for {str(e)}'
            print(full_error)
            errors += 1
            
        finally:
            exec("plt.close()")
            # final_output = black.format_str(dict_list[i]["output"], mode=black.FileMode())
            new_list.append({
                "ID": i,
                "label": entry["label"],
                "instruction": entry["instruction"].replace("\n", "").replace("\r", "").strip(),
                "input": entry["input"].replace("\n", "").replace("\r", "").strip(),
                "output": entry["output"].strip(),
                "graph": entry["graph"],
                "error": short_error,
                "image_location": image_location
            })
            graph_types[entry["graph"]] = graph_types.get(entry["graph"],0)+1
            # print(f'SUMMARY OF DATA:\n{graph_types}\n')
    print(f'SUMMARY OF DATA:\n{graph_types}\n')
    print(f'COMPILE ERRORS: {errors}/{len(new_list)}')
    print(f'COMPILE WARNINGS: {warnings_s}/{len(new_list)}')
    return new_list

#TRANFORM FUNCTIONS:
# def format_autopct(pct, allvalues):
#     absolute = int(pct / 100. * sum(allvalues))
#     return f"${absolute} ({pct:.1f}%)"
    
if __name__ == '__main__':
    base_data = [
    data_entry(
        label = "total_over_time",
        instructions=[
            instruction("show me total sales over time", "Date","Total Sales ($)","Total Sales over Time"),
            instruction("What is the total value of sales each day?", "Date","Total Sales ($)","Total Value of Sales Each Day"),
            instruction("Hi, give me the total in revenue over time", "Date", "Total Sales ($)", "Total Revenue over Time")
        ],
        output_raw = [
"""sales_data = df.groupby('Date')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(sales_data['Date'], sales_data['#TOTAL#'], color="#3B3365", linewidth=2)
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
ax.set_xlim(df['Date'].min() - pd.Timedelta(days=3), df['Date'].max() + pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.tick_params(colors="#3B3365")
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
            ]

    ),
    data_entry(
        label = "total_over_time_custom",
        instructions=[
            instruction("give me total sales over time for #PERIOD#?", "Date","Total Sales ($)", "Total Sales over Time (#PERIOD#)"),
        ],
        output_raw = [
"""sales_data = df[(df['#ACTION#']>='#START#') & (df['#ACTION#']<='#END#')].groupby('Date')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(sales_data['Date'], sales_data['#TOTAL#'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_xlim(pd.to_datetime('#START#')-pd.Timedelta(days=1), pd.to_datetime('#END#')+pd.Timedelta(days=1))
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(colors="#3B3365")
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
        ]
    ),
    data_entry(
        label = "album_distribution_sales_actual",
        instructions=[
            instruction("Generate the distribution of album sales as a pie graph with actual numbers", '',"", 'Distribution of Album Sales ber Artist'),
            instruction("Give me Sales Total of Albums sold categorized by Artist", '',"", 'Distribution of Album Revenue ber Artist')

        ],
        output_raw = [
"""def format_autopct(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f"${absolute} ({pct:.1f}%)"

fig, ax = plt.subplots(figsize=(10,8))
physical_sales_df = df[(df['#CATEGORY#']=='Album') & (~pd.isna(df['#TOTAL#']))]
physical_sales_per_product = physical_sales_df.groupby('#ARTIST#')['#TOTAL#'].sum().reset_index()
ax.pie(physical_sales_per_product['#TOTAL#'], labels=physical_sales_per_product['#ARTIST#'], autopct=lambda pct: format_autopct(pct, physical_sales_per_product['#TOTAL#']), textprops={'fontproperties': manjari_bold})
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
        ]
    )
    ]

    new_data = mix(base_data)
    new_data = flag_replace(new_data)
    new_data = scramble(new_data)
    new_data = oo_to_state(new_data)
    new_data = test(new_data)