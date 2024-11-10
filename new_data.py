#importing all vars

import json
import csv
import random
import black
import code_scrambler
import warnings
import traceback
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
import numpy as np
from tqdm import tqdm


# warnings.simplefilter(action='ignore')

#loading custom font

manjari_bold_path = 'font/Manjari-Bold.ttf'
manjari_regular_path = 'font/Manjari-Regular.ttf'
manjari_thin_path = 'font/Manjari-thin.ttf'
logo_img = mpimg.imread('Media/horizontal-logo.png')
manjari_bold = fm.FontProperties(fname=manjari_bold_path)
manjari_regular = fm.FontProperties(fname=manjari_regular_path)
manjari_thin = fm.FontProperties(fname=manjari_thin_path)

#loading all different variations

with open('values.json','r') as file:
    vars = json.load(file)

colours = vars['colours']
start_date = vars['start date']
end_date = vars['end date']
period = vars['period']
names = vars['names']
mat_plot_lib_all_plots = vars['mat_plot_lib_all_plots']


#things to modulate:
#colour #COLOUR#
#date 
#title
#axis
#coding format
#columns/names

#steps:
#provide base format
#replace date, colour, title, axis with tags #DATE#, #COLOUR#, #TITLE#, #AXIS#
#replace appropriate columns with tags 
#scramble code after tags replaced
#change coding format DONE

#instruction class

class instruction():
    def __init__(self, instruction, xaxis="", yaxis="", title=""):
        self.instruction = instruction #instruction with tags
        self.xaxis = xaxis
        self.yaxis = yaxis
        self.title = title

    def __str__(self):
        return str({'instruction': self.instruction, 'x-axis': self.xaxis, 'y-axis': self.yaxis,'title': self.title})

#each data entry represents a row of data

class data_entry():
    def __init__(self,label,instructions, graph: str, output_raw: str):
        self.instructions = instructions #instruction class
        self.output_raw = output #string
        self.graph = graph
        self.label = label

def assess_graph_type(code): #IMPROVE THIS!!

    for graph in mat_plot_lib_all_plots:
        if f'ax.{graph}' in code or f'ax.{graph}' in code:
            return graph
    return 'other'


total_over_time = """sales_data = df.groupby('Date')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(sales_data['Date'], sales_data['#TOTAL#'], color=dark, linewidth=2)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Total Sales Over Time', color=dark, font_properties=manjari_bold)
ax.set_xlim(df['Date'].min() - pd.Timedelta(days=3), df['Date'].max() + pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

total_over_time_july = """sales_data = df[(df['#ACTION#']>='2024-07-01') & (df['#ACTION#']<='2024-07-31')].groupby('Date')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(sales_data['Date'], sales_data['#TOTAL#'], color=medium)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.set_xlim(pd.to_datetime('2024-07-01')-pd.Timedelta(days=1), pd.to_datetime('2024-07-31')+pd.Timedelta(days=1))
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.set_title('Total Sales Over Time (July)', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

total_over_time_august = """sales_data = df[(df['#ACTION#']>='2024-08-01') & (df['#ACTION#']<='2024-08-31')].groupby('Date')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(sales_data['Date'], sales_data['#TOTAL#'], color=medium)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_xlim(pd.to_datetime('2024-08-01')-pd.Timedelta(days=1), pd.to_datetime('2024-08-31')+pd.Timedelta(days=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.set_title('Total Sales Over Time (August)', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

total_over_time_machines = """machine_sales_only = df[df['#CATEGORY#']=='Photo']
sales_data = machine_sales_only.groupby('Date')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(sales_data['Date'], sales_data['#TOTAL#'], color=dark, linewidth=2)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Total Sales Over Time', color=dark, font_properties=manjari_bold)
ax.set_xlim(df['Date'].min() - pd.Timedelta(days=3), df['Date'].max() + pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

total_over_time_machines_august = """machine_sales_only = df[(df['#CATEGORY#']=='Photo') & (df['#ACTION#']>='2024-08-01') & (df['#ACTION#']<='2024-08-31')]
sales_data = machine_sales_only.groupby('Date')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(sales_data['Date'], sales_data['#TOTAL#'], color=dark, linewidth=2)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Total Sales Over Time', color=dark, font_properties=manjari_bold)
ax.set_xlim(df['Date'].min() - pd.Timedelta(days=1), df['Date'].max() + pd.Timedelta(days=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

total_over_time_machines_july = """machine_sales_only = df[(df['#CATEGORY#']=='Photo') & (df['#ACTION#']>='2024-07-01') & (df['#ACTION#']<='2024-07-31')]
sales_data = machine_sales_only.groupby('Date')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(sales_data['Date'], sales_data['#TOTAL#'], color=dark, linewidth=2)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Total Sales Over Time', color=dark, font_properties=manjari_bold)
ax.set_xlim(df['Date'].min() - pd.Timedelta(days=1), df['Date'].max() + pd.Timedelta(days=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

by_people = """staff_data = df.groupby('#STAFF#')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(staff_data['#STAFF#'], staff_data['#TOTAL#'], color=medium)
ax.set_xlabel('Staff', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Total Sales per Employee', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

peak_hours_quantity = """df['hour'] = df['#ACTION#'].dt.hour
peak_hours = df.groupby('hour')['#QUANTITY#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(peak_hours['hour'], peak_hours['#QUANTITY#'], color=medium)
ax.set_xlabel('Hour', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Quantity', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Quantity of Sales at each hour', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

peak_hours_total = """df['hour'] = df['#ACTION#'].dt.hour
peak_hours = df.groupby('hour')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(peak_hours['hour'], peak_hours['#TOTAL#'], color=medium)
ax.set_xlabel('Hour', color=dark, font_properties=manjari_bold)
ax.set_ylabel('#TOTAL#', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Total Sales at each hour', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

total_0_sale_transactions_over_time = """zero_total = df[df['#TOTAL#']==0]
zero_sale_summary = zero_total.groupby('Date')['#TOTAL#'].count().reset_index()
zero_sale_summary.columns = ['Date','#TOTAL#']
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(zero_sale_summary['Date'], zero_sale_summary['#TOTAL#'], color=dark, linewidth=2)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Transactions', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Total of Sales with $0 over time', color=dark, font_properties=manjari_bold)
ax.set_xlim(df['Date'].min() - pd.Timedelta(days=3), df['Date'].max() + pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

photo_vs_copy = """photos_vs_copies = df[df['#CATEGORY#']=='Photo']
photos_vs_copies['next_purchase'] = photos_vs_copies.groupby('#MACHINE#')['#DETAIL#'].shift(-1)
photos_vs_copies.loc[(photos_vs_copies['#DETAIL#'] == 'Photo') & (photos_vs_copies['next_purchase'] == 'Photo'), 'purchase_category'] = 'Only Photo'
photos_vs_copies.loc[(photos_vs_copies['#DETAIL#'] == 'Photo') & (photos_vs_copies['next_purchase'] == 'Copy'), 'purchase_category'] = 'Copy'
photos_vs_copies_summary = photos_vs_copies.groupby('purchase_category').size().reset_index(name='count')
photos_vs_copies_summary.columns=['Purchase Category','Count']
fix, ax = plt.subplots(figsize=(10, 8))
ax.bar(photos_vs_copies_summary['Purchase Category'], photos_vs_copies_summary['Count'], color=light)
ax.set_xlabel('Purchase Category', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Count', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Do Customers Only Buy Photos?', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

weekend_vs_weekday_table = """df['day_type'] = df['Date'].dt.dayofweek.apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
total_sales_per_type = df.groupby('day_type')['#TOTAL#'].sum().reset_index()
total_sales_per_type.columns = ['Day Type', 'Total Sales']
total_sales_per_type['Total Sales'] = total_sales_per_type['Total Sales'].apply(lambda x: f'${x:,.2f}')

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=total_sales_per_type.values, 
    colLabels=total_sales_per_type.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Total Sales: Weekdays vs Weekends', weight='bold', font_properties=manjari_bold)

"""

weekend_vs_weekday = """df['day_type'] = df['Date'].dt.dayofweek.apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
total_sales_per_type = df.groupby('day_type')['#TOTAL#'].sum().reset_index()
total_sales_per_type.columns = ['Day Type', 'Total Sales']
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(total_sales_per_type['Day Type'], total_sales_per_type['Total Sales'], color=medium)
ax.set_xlabel('Day Type', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Total Sales: Weekdays vs Weekends', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""


table_albums_month = """albumn_data = df[df['#CATEGORY#']=='Album']
monthly_sales = albumn_data.groupby(pd.Grouper(key='#ACTION#', freq='M'))['#QUANTITY#'].sum().reset_index()
monthly_sales.columns = ['Month','Total Albums']
monthly_sales['Month']=monthly_sales['Month'].dt.strftime('%B %Y')

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=monthly_sales.values, 
    colLabels=monthly_sales.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Album Sales per Month', weight='bold', font_properties=manjari_bold)

"""

replacement_count = """staff_replacement_days = df.groupby('#REPLACED#')['Date'].nunique().reset_index(name='Days')
staff_replacement_days = staff_replacement_days.dropna()
all_staff = df['#STAFF#'].unique()
all_staff_df = pd.DataFrame(all_staff, columns=['#STAFF#'])
staff_replacement_days_complete = all_staff_df.merge(staff_replacement_days, left_on='#STAFF#', right_on='#REPLACED#', how='left')
staff_replacement_days_complete['Days'] = staff_replacement_days_complete['Days'].fillna(0)
staff_replacement_days_complete = staff_replacement_days_complete.drop(columns=['#REPLACED#'])
staff_replacement_days_complete = staff_replacement_days_complete.sort_values(by='Days', ascending=False)

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(staff_replacement_days_complete['#STAFF#'], staff_replacement_days_complete['Days'], color=medium)
ax.set_xlabel('Staff', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Days', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Count of Shifts that Needed Replacing', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

replacement_count_table = """staff_replacement_days = df.groupby('#REPLACED#')['Date'].nunique().reset_index(name='Days')
staff_replacement_days = staff_replacement_days.dropna()
all_staff = df['#STAFF#'].unique()
all_staff_df = pd.DataFrame(all_staff, columns=['#STAFF#'])
staff_replacement_days_complete = all_staff_df.merge(staff_replacement_days, left_on='#STAFF#', right_on='#REPLACED#', how='left')
staff_replacement_days_complete['Days'] = staff_replacement_days_complete['Days'].fillna(0)
staff_replacement_days_complete = staff_replacement_days_complete.drop(columns=['#REPLACED#'])
staff_replacement_days_complete = staff_replacement_days_complete.sort_values(by='Days',ascending=False)

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=staff_replacement_days_complete.values, 
    colLabels=staff_replacement_days_complete.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Table of all Employees that needed Replacements', weight='bold', font_properties=manjari_bold)

"""

album_distribution_sales = """physical_sales_df = df[(df['#CATEGORY#']=='Album') & (~pd.isna(df['#TOTAL#']))]
physical_sales_per_product = physical_sales_df.groupby('#ARTIST#')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(12,12))
ax.pie(physical_sales_per_product['#TOTAL#'], labels=physical_sales_per_product['#ARTIST#'], autopct='%1.1f%%', textprops={'fontproperties': manjari_bold})
ax.set_title('Distribution of Album Sales ber Artist', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

"""

album_distribution_sales_actual = """def format_autopct(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f"${absolute} ({pct:.1f}%)"

fig, ax = plt.subplots(figsize=(9,9))
physical_sales_df = df[(df['#CATEGORY#']=='Album') & (~pd.isna(df['#TOTAL#']))]
physical_sales_per_product = physical_sales_df.groupby('#ARTIST#')['#TOTAL#'].sum().reset_index()
ax.pie(physical_sales_per_product['#TOTAL#'], labels=physical_sales_per_product['#ARTIST#'], autopct=lambda pct: format_autopct(pct, physical_sales_per_product['#TOTAL#']), textprops={'fontproperties': manjari_bold})
ax.set_title('Distribution of Album Sales by Artist', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

"""

machine_sales = """total_sales = df[df['#CATEGORY#']=='Photo']
total_sales_grouped = total_sales.groupby('#MACHINE#')['#TOTAL#'].sum().reset_index()
total_sales_grouped.columns = ['Machine','Total Sales']

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=total_sales_grouped.values, 
    colLabels=total_sales_grouped.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Total Machine Sales', weight='bold', font_properties=manjari_bold)

"""

machine_count = """count_sales = df[df['#CATEGORY#']=='Photo']
count_sales_grouped = count_sales.groupby('#MACHINE#')['#TOTAL#'].count().reset_index()
count_sales_grouped.columns = ['Album','Total Sales']

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=count_sales_grouped.values, 
    colLabels=count_sales_grouped.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Machine Sales', weight='bold', font_properties=manjari_bold)

"""

total_sales_per_day_of_week = """df['Day'] = df['#ACTION#'].dt.day_name()
total_sales_per_day = df.groupby('Day')['#TOTAL#'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
).reset_index()
total_sales_per_day.columns = ['Day of Week', 'Total Sales']
total_sales_per_day['Total Sales'] = total_sales_per_day['Total Sales'].apply(lambda x: f'${x:,.2f}')

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=total_sales_per_day.values, 
    colLabels=total_sales_per_day.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Total Sales per Day of Week', weight='bold', font_properties=manjari_bold)

"""

total_sales_per_day_of_week_bar = """df['Day'] = df['#ACTION#'].dt.day_name()
total_sales_per_day = df.groupby('Day')['#TOTAL#'].sum().reset_index()
total_sales_per_day.columns = ['Day of Week', 'Total Sales ($)']
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(total_sales_per_day['Day of Week'], total_sales_per_day['Total Sales ($)'], color=medium)
ax.set_xlabel('Day of Week', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Total Sales by Day of Week', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

avg_sales_by_day_of_week = """df_grouped = df.groupby('Date')['#TOTAL#'].sum().reset_index()
df_grouped['Day'] = pd.to_datetime(df_grouped['Date']).dt.day_name()
avg_sales_per_day = df_grouped.groupby('Day')['#TOTAL#'].mean().reset_index()
avg_sales_per_day.columns = ['Day of Week', 'Total Sales ($)']
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(avg_sales_per_day['Day of Week'], avg_sales_per_day['Total Sales ($)'], color=medium)
ax.set_xlabel('Day of Week', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45, colors=dark)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Average Sales by Day of Week', color=dark, font_properties=manjari_bold)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

bts_sales = """filtered_df = df[df['#ARTIST#']=='BTS']
count_sales = filtered_df.groupby('#ARTIST#')['#QUANTITY#'].sum().reset_index()
count_sales.columns = ['Group', 'Count of Sales']

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=count_sales.values, 
    colLabels=count_sales.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Count of Sales for BTS Albums', weight='bold', font_properties=manjari_bold)

"""

album_photo_sales = """fig, ax = plt.subplots(figsize=(9,9))
album_photo_comparison = df[(df['#CATEGORY#'] != 'Miscellaneous') & (~pd.isna(df['#TOTAL#']))]
album_photo_comparison_grouped = album_photo_comparison.groupby('#CATEGORY#')['#TOTAL#'].sum().reset_index()
ax.pie(album_photo_comparison_grouped['#TOTAL#'], labels=album_photo_comparison_grouped['#CATEGORY#'], autopct='%1.1f%%', textprops={'fontproperties': manjari_bold})
ax.set_title('Album and Photo Sales Comparison', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

"""

karmel_sales = """filtered_df = df[(df['#STAFF#']=='Karmel') & (df['#CATEGORY#']=='Album')]
count_sales = filtered_df.groupby('#STAFF#')['#QUANTITY#'].sum().reset_index()
count_sales.columns = ['Staff', 'Count of Sales']

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=count_sales.values, 
    colLabels=count_sales.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title("Count of Karmel's Album Sales", weight='bold', font_properties=manjari_bold)

"""

jess_total_sales="""filtered_df = df[(df['#STAFF#']=='Jess') & (df['#CATEGORY#']=='Photo')]
count_sales = filtered_df.groupby('#STAFF#')['#TOTAL#'].sum().reset_index()
count_sales.columns = ['Staff', 'Total Sales']
count_sales['Total Sales'] = count_sales['Total Sales'].apply(lambda x: f'${x:,.2f}')

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=count_sales.values, 
    colLabels=count_sales.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title("Total Photo Sales for Jess", weight='bold', font_properties=manjari_bold)

"""

machine_by_month_comparison = """photo_df = df[df['#CATEGORY#']=='Photo']
photo_df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M')
monthly_sales = photo_df.groupby(['Month', '#MACHINE#'])['#TOTAL#'].sum().reset_index()
monthly_sales['Month']=monthly_sales['Month'].dt.strftime('%B %Y')
pivot_sales = monthly_sales.pivot(index='Month', columns='#MACHINE#', values='#TOTAL#').fillna(0)
months = pivot_sales.index.astype(str)
machines = pivot_sales.columns
num_machines = len(machines)
x = np.arange(len(months))
bar_width = 0.8 / num_machines  # Adjust the width based on the number of machines
fig, ax = plt.subplots(figsize=(10, 8))

for i, product in enumerate(machines):
    if i % 2 == 0:
        ax.bar(x + i * bar_width, pivot_sales[product], width=bar_width, label=product,color=blue)
    else:
        ax.bar(x + i * bar_width, pivot_sales[product], width=bar_width, label=product,color=medium)

ax.set_xlabel('Month', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sale ($)', color=dark, font_properties=manjari_bold)
ax.set_xticks(x + bar_width * (num_machines - 1) / 2, months)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Total Photo Sales by #MACHINE# and Month', color=dark, font_properties=manjari_bold)
ax.legend(title='Machine')
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

"""

album_sales="""sales_data = df[df['#CATEGORY#']=='Album']
sales_data = sales_data.groupby('Date')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(sales_data['Date'], sales_data['#TOTAL#'], color=dark, linewidth=2)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
ax.set_xlim(df['Date'].min() - pd.Timedelta(days=3), df['Date'].max() + pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
ax.tick_params(axis='x', labelrotation=45, colors=dark)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Album Sales Over Time', color=dark, font_properties=manjari_bold)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

shift_count_per_staff="""staff_shift_count = df.groupby('#STAFF#')['Date'].nunique().reset_index()
staff_shift_count.columns = ['Staff','Shift Count']

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(staff_shift_count['Staff'], staff_shift_count['Shift Count'], color=medium)
ax.set_xlabel('Staff', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Shift Count', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Shift Count per Staff', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

average_sales_per_shift="""total_per_employee_day = df.groupby(['#STAFF#','Date'])['#TOTAL#'].sum().reset_index()
avg_per_employee = total_per_employee_day.groupby(['#STAFF#'])['#TOTAL#'].mean().reset_index()
avg_per_employee.columns=['Staff','Average']

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(avg_per_employee['Staff'], avg_per_employee['Average'], color=medium)
ax.set_xlabel('Staff', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Average Sales', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Average Sales per Shift', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

average_sales_per_shift_table="""total_per_employee_day = df.groupby(['#STAFF#','Date'])['#TOTAL#'].sum().reset_index()
avg_per_employee = total_per_employee_day.groupby(['#STAFF#'])['#TOTAL#'].mean().round(2).reset_index()
avg_per_employee.columns=['Staff','Average']
avg_per_employee['Average'] = avg_per_employee['Average'].apply(lambda x: f'${x:,.2f}')

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=avg_per_employee.values, 
    colLabels=avg_per_employee.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title("Staff Average Sales per Shift", weight='bold', font_properties=manjari_bold)

"""

top_day_sales="""sales_by_date = df.groupby(['Date'])['#TOTAL#'].sum().reset_index()
top_10_sales_by_date = sales_by_date.sort_values(by='#TOTAL#', ascending=False).head(10)
top_10_sales_by_date.columns = ['Date','Total Sales']
top_10_sales_by_date['Total Sales'] = top_10_sales_by_date['Total Sales'].apply(lambda x: f'${x:,.2f}')
top_10_sales_by_date['Date'] = top_10_sales_by_date['Date'].dt.strftime('%d/%m/%Y')

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=top_10_sales_by_date.values, 
    colLabels=top_10_sales_by_date.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off')

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title("Top 10 Best Day Sales", weight='bold', font_properties=manjari_bold)

"""

employee_sales_pie_chart = """def format_autopct(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f"${absolute} ({pct:.1f}%)"

fig, ax = plt.subplots(figsize=(9,9))
total_sales_per_employee = df[~pd.isna(df['#TOTAL#'])]
total_sales_per_employee_grouped = total_sales_per_employee.groupby('#STAFF#')['#TOTAL#'].sum().reset_index()
ax.pie(total_sales_per_employee_grouped['#TOTAL#'], labels=total_sales_per_employee_grouped['#STAFF#'], autopct=lambda pct: format_autopct(pct, total_sales_per_employee_grouped['#TOTAL#']), textprops={'fontproperties': manjari_bold})
ax.set_title('Distribution of Sales per Employee', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

"""

boxplot_per_employee="""grouped_by_day = df.groupby(['#STAFF#','Date'])['#TOTAL#'].sum().reset_index()
staff_names = grouped_by_day['#STAFF#'].unique()
grouped_by_staff = [grouped_by_day[grouped_by_day['#STAFF#'] == staff]['#TOTAL#'].values for staff in staff_names]
fig, ax = plt.subplots(figsize=(9,6))
box = ax.boxplot(grouped_by_staff, labels=staff_names, patch_artist=True)
ax.set_title('Plot of Sales per Employee', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
ax.set_xlabel('Staff', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Sales ($)', color=dark, font_properties=manjari_bold)
colors=[yellow, orange, green, blue, light, medium, dark]
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)

for patch, colour in zip(box['boxes'],colors):
    patch.set_facecolor(colour)


"""

daily_statistics="""daily_statistics = df.groupby('Date')['#TOTAL#'].sum().reset_index()
daily_statistics_agg = daily_statistics['#TOTAL#'].agg(['mean','median','std','max','min']).round(2).reset_index()
daily_statistics_agg.columns = ['Measurement','Value']
daily_statistics_agg['Measurement']=daily_statistics_agg['Measurement'].str.title()

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=daily_statistics_agg.values, 
    colLabels=daily_statistics_agg.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)

logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title("Overview of Daily Sales", weight='bold', font_properties=manjari_bold)

"""

moving_avg_week = """total_sales_per_day = df.groupby('Date')['#TOTAL#'].sum().reset_index()
total_sales_per_day.set_index('Date', inplace=True)
total_sales_per_day['Weekly Moving Average'] = total_sales_per_day['#TOTAL#'].rolling(window=7).mean()
total_sales_per_day.columns=['Total Sales ($)', 'Weekly Moving Average ($)']

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(total_sales_per_day.index, total_sales_per_day['Total Sales ($)'], color=medium)
ax.plot(total_sales_per_day.index, total_sales_per_day['Weekly Moving Average ($)'], color=dark, linewidth=3, linestyle=':')
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=90)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Sales over Time', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
ax.set_xlim(df['Date'].min()-pd.Timedelta(days=3),df['Date'].max()+pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

tally_days_less_than_50="""total_sales_per_day = df.groupby('Date')['#TOTAL#'].sum().reset_index()
low_sales = total_sales_per_day[total_sales_per_day['#TOTAL#']<50]
low_sales['Day'] = pd.to_datetime(low_sales['Date']).dt.day_name()
low_sales_grouped = low_sales.groupby('Day')['Date'].nunique().reset_index()
low_sales_grouped.columns=['Day','Tally']

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=low_sales_grouped.values, 
    colLabels=low_sales_grouped.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)

logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title("Tally of Days with less than $50 in sales", weight='bold', font_properties=manjari_bold)

"""

area_chart_albums_sold_over_time="""album_sales = df[df['#CATEGORY#']=='Album']
total_album_sales = album_sales.groupby(['Date','#CATEGORY#'])['#QUANTITY#'].sum().reset_index()
pivot_df = total_album_sales.pivot(index='Date', columns='#CATEGORY#', values='#QUANTITY#').fillna(0)
x = pivot_df.index  
y = pivot_df.values.T 
fig, ax = plt.subplots(figsize=(10, 8))
ax.stackplot(x, y, labels=pivot_df.columns, alpha=0.8)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Albums Sold', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Album Sales over Time', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
ax.set_xlim(df['Date'].min()-pd.Timedelta(days=3),df['Date'].max()+pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
ax.legend(loc='center right',bbox_to_anchor=(1.35, 0.5))
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

"""

quantity_albums_over_time="""album_sales = df[df['#CATEGORY#']=='Album']
total_album_sales = album_sales.groupby(['Date'])['#QUANTITY#'].sum().reset_index()
total_album_sales['Date']=pd.to_datetime(total_album_sales['Date'])
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(total_album_sales['Date'], total_album_sales['#QUANTITY#'], color=medium)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Albums Sold', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Album Count over Time', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
ax.set_xlim(df['Date'].min()-pd.Timedelta(days=3),df['Date'].max()+pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

copies_over_time="""copy_sales = df[(df['#DETAIL#']=='Copy')]
total_copy_sales = copy_sales.groupby(['Date'])['#QUANTITY#'].sum().reset_index()
total_copy_sales['Date']=pd.to_datetime(total_copy_sales['Date'])
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(total_copy_sales['Date'], total_copy_sales['#QUANTITY#'], color=medium)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Copies Printed', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Copies over Time', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
ax.set_xlim(df['Date'].min()-pd.Timedelta(days=3),df['Date'].max()+pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

copies_july="""copy_sales = df[(df['#DETAIL#']=='Copy')]
total_copy_sales = copy_sales.groupby(['Date'])['#QUANTITY#'].sum().reset_index()
total_copy_sales['Date']=pd.to_datetime(total_copy_sales['Date'])
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(total_copy_sales['Date'], total_copy_sales['#QUANTITY#'], color=medium)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Copies Printed', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Copies over July', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
ax.set_xlim(pd.to_datetime('2024-07-01')-pd.Timedelta(days=1), pd.to_datetime('2024-07-31')+pd.Timedelta(days=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

correlation_between_album_photo = """photos_df = df[df['#CATEGORY#']=='Photo']
albums_df = df[df['#CATEGORY#']=='Album']
photo_sales = photos_df.groupby('Date')['#TOTAL#'].sum().reset_index(name='photo_sales')
album_sales = albums_df.groupby('Date')['#TOTAL#'].sum().reset_index(name='album_sales')
merged_sales = pd.merge(photo_sales, album_sales, on='Date', how='inner')

fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(merged_sales['photo_sales'], merged_sales['album_sales'], color=medium)
ax.set_xlabel('Photo Sales', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Album Sales', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Correlation between Photo and Album Sales', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

correlation_between_copy_photo="""photos_df = df[df['#CATEGORY#']=='Photo']
copy_df = df[df['#DETAIL#']=='Copy']
photo_sales = photos_df.groupby('Date')['#TOTAL#'].sum().reset_index(name='photo_sales')
copy_df = copy_df.groupby('Date')['#TOTAL#'].sum().reset_index(name='copy_sales')
merged_sales = pd.merge(photo_sales, copy_df, on='Date', how='inner')

fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(merged_sales['photo_sales'], merged_sales['copy_sales'], color=medium)
ax.set_xlabel('Photo Sales', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Copy Sales', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Correlation between Photo and Copy Sales', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

total_sales_per_day_of_week_barh = """df['Day'] = df['#ACTION#'].dt.day_name()
total_sales_per_day = df.groupby('Day')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(total_sales_per_day['Day'],total_sales_per_day['#TOTAL#'],color=medium)
ax.set_xlabel('Day of Week', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=90)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Total Sales by Day of Week', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

staff_copy =  """copy_sales = df[df['#DETAIL#']=='Copy']
copy_sales_per_staff = copy_sales.groupby('#STAFF#')['#TOTAL#'].sum().reset_index()
copy_sales_per_staff.columns = ['Staff', 'Total Sales ($)']
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(copy_sales_per_staff['Staff'],copy_sales_per_staff['Total Sales ($)'],color=medium)
ax.set_xlabel('Staff', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=90)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Total Sales in Copies per #STAFF#', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

#total revenue generated per album

total_revenue_generated_per_album = """album_sales = df[df['#CATEGORY#']=='Album']
album_sales_summary = album_sales.groupby('#DETAIL#')['#TOTAL#'].sum().reset_index()
album_sales_summary.columns = ['Album', 'Total Sales ($)']
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(album_sales_summary['Album'],album_sales_summary['Total Sales ($)'],color=medium)
ax.set_xlabel('Album', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=90)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Total Sales in Copies per Album', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""

#average sales per transaction

average_sale_per_transaction = """transaction_total = df.groupby(['#CATEGORY#','#ORDER_ID#'])['#TOTAL#'].sum().reset_index()
average_transaction = transaction_total.groupby('#CATEGORY#')['#TOTAL#'].mean().reset_index()
average_transaction.columns=['Category','Average']
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=average_transaction.values, 
    colLabels=average_transaction.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Average Sale per Transaction', weight='bold', font_properties=manjari_bold)

"""

#average quantity per transaction

average_quantity_per_transaction = """transaction_total = df.groupby(['#CATEGORY#','#ORDER_ID#'])['#QUANTITY#'].sum().reset_index()
average_transaction = transaction_total.groupby('#CATEGORY#')['#QUANTITY#'].mean().reset_index()
average_transaction.columns=['Category','Average']
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=average_transaction.values, 
    colLabels=average_transaction.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Average Quantity per Transaction', weight='bold', font_properties=manjari_bold)

"""

#which product had highest total revenue

product_highest_revenue = """total_revenue = df.groupby('#DETAIL#')['#TOTAL#'].sum().reset_index()
total_revenue = total_revenue.sort_values(by='#TOTAL#',ascending=False)
total_revenue = total_revenue.iloc[:5]
total_revenue['#TOTAL#'] = total_revenue['#TOTAL#'].apply(lambda x: f'${x:,.2f}')
total_revenue.columns=['Product','Revenue']

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=total_revenue.values, 
    colLabels=total_revenue.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Products with Highest Revenue', weight='bold', font_properties=manjari_bold)

"""

#average transaction value per staff

average_transaction_value_per_staff="""transaction_total = df.groupby(['#STAFF#','#ORDER_ID#'])['#TOTAL#'].sum().reset_index()
average_transaction = transaction_total.groupby('#STAFF#')['#TOTAL#'].mean().reset_index()
average_transaction.columns=['Staff','Average']
fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=average_transaction.values, 
    colLabels=average_transaction.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1.2, 4)

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Average Revenue per Transaction (Staff)', weight='bold', font_properties=manjari_bold)

"""

#number of times each album sold

album_quantity_sales = """album_sales = df[df['#CATEGORY#']=='Album']
quantity_albumns_sold = album_sales.groupby('#DETAIL#')['#QUANTITY#'].sum().reset_index()
quantity_albumns_sold['#QUANTITY#'] = quantity_albumns_sold['#QUANTITY#'].apply(lambda x: f'${x:,.2f}')
quantity_albumns_sold.columns=['Product','Revenue']

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=quantity_albumns_sold.values, 
    colLabels=quantity_albumns_sold.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Quantity of Album Sales', weight='bold', font_properties=manjari_bold)

"""

#top 5 albumns sold

top_5_albums_sold = """album_sales = df[df['#CATEGORY#']=='Album']
total_album_revenue = df.groupby('#DETAIL#')['#TOTAL#'].sum().reset_index()
total_album_revenue = total_album_revenue.sort_values(by='#TOTAL#',ascending=False)
total_album_revenue = total_album_revenue.iloc[:5]
total_album_revenue['#TOTAL#'] = total_album_revenue['#TOTAL#'].apply(lambda x: f'${x:,.2f}')
total_album_revenue.columns=['Product','Revenue']

fig, ax = plt.subplots(figsize=(10, 8))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=total_album_revenue.values, 
    colLabels=total_album_revenue.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Top 5 Albumns in Sales ($)', weight='bold', font_properties=manjari_bold)

"""

#bottom 5 albumns sold

bottom_5_albums = """album_sales = df[df['#CATEGORY#']=='Album']
total_album_revenue = df.groupby('#DETAIL#')['#TOTAL#'].sum().reset_index()
total_album_revenue = total_album_revenue.sort_values(by='#TOTAL#',ascending=True)
total_album_revenue = total_album_revenue.iloc[:5]
total_album_revenue['#TOTAL#'] = total_album_revenue['#TOTAL#'].apply(lambda x: f'${x:,.2f}')
total_album_revenue.columns=['Product','Revenue']

fig, ax = plt.subplots(figsize=(10, 8))
fig.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=total_album_revenue.values, 
    colLabels=total_album_revenue.columns, 
    cellLoc='center',
    bbox=[0.05, 0.1, 0.9, 0.8]
)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

for (i, j), cell in table.get_celld().items():
    if i == 0:  
        cell.set_text_props(weight='bold', color='white',font=manjari_bold)
        cell.set_facecolor(dark) 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor(medium) if i % 2 == 0 else cell.set_facecolor(light)

ax.set_title('Bottom 5 Albumns in Sales ($)', weight='bold', font_properties=manjari_bold)

"""







#instruction
#input
#output
#graph type
#category
#error


base_data = [
{
    "instruction": "show me total sales over time",
    "input": '',
    "output": total_over_time
},
{
    "instruction": "give me sales results based off employee as a bar graph",
    "input": '',
    "output": by_people
},
{
    "instruction": "give me a table of total albumns sold per month",
    "input": '',
    "output": table_albums_month
},
{
    "instruction": "give me total sales over time for july?",
    "input": '',
    "output": total_over_time_july
},
{
    "instruction": "Can I have total sales over time for august?",
    "input": '',
    "output": total_over_time_august
},
{
    "instruction": "Hi, can you show me in a table the number of times employees needed to be replaced on a shift",
    "input": '',
    "output": replacement_count_table
},
{
    "instruction": "Show how many employees needed to be replaced on a shift",
    "input": '',
    "output": replacement_count
},
{
    "instruction": "give distribution of album sales",
    "input": '',
    "output": album_distribution_sales
},
{
    "instruction": "Generate the distribution of album sales as a pie graph with actual numbers",
    "input": '',
    "output": album_distribution_sales_actual
},
{
    "instruction": "Can you sum up the sales on both machines",
    "input": '',
    "output": machine_sales
},
{
    "instruction": "How many times has each machine been used?",
    "input": '',
    "output": machine_count
},
{
    "instruction": "total sales per day of week",
    "input": '',
    "output": total_sales_per_day_of_week
},
{
    "instruction": "give me the total sales per day of week as a barchart",
    "input": '',
    "output": total_sales_per_day_of_week_bar
},
{
    "instruction": "avg sales per day of week",
    "input": '',
    "output": avg_sales_by_day_of_week
},
{
    "instruction": "how many BTS albums have we sold so far?",
    "input": '',
    "output": bts_sales
},
{
    "instruction": "album sales vs photo sales?",
    "input": '',
    "output": album_photo_sales
},
{
    "instruction": "how many album sales did Karmel have?",
    "input": '',
    "output": karmel_sales
},
{
    "instruction": "total of photobooth sales on Jess' shifts?",
    "input": '',
    "output": jess_total_sales
},
{
    "instruction": "total sales per month blue vs purple machine",
    "input": '',
    "output": machine_by_month_comparison
},
{
    "instruction": "album sales over time",
    "input": '',
    "output": album_sales
},
{
    "instruction": "can you count how many shifts each staff have been on",
    "input": '',
    "output": shift_count_per_staff
},
{
    "instruction": "can you give me the average sales per shift per staff",
    "input": '',
    "output": average_sales_per_shift
},
{
    "instruction": "What is the average sales each employee gets",
    "input": '',
    "output": average_sales_per_shift_table
},
{
    "instruction": "Hi! What are our best selling days?",
    "input": '',
    "output": top_day_sales
},
{
    "instruction": "pie chart of total sales per employee",
    "input": '',
    "output": employee_sales_pie_chart
},
{
    "instruction": "Generate a visual showing a boxplot each employee sale",
    "input": '',
    "output": boxplot_per_employee
},
{
    "instruction": "Give me a rundown of daily sales statistics",
    "input": '',
    "output": daily_statistics
},
{
    "instruction": "get me the moving average of sales per week",
    "input": '',
    "output": moving_avg_week
},
{
    "instruction": "tally the days with less than $50 in sales",
    "input": '',
    "output": tally_days_less_than_50
},
{
    "instruction": "area chart of albums sold over time",
    "input": '',
    "output": area_chart_albums_sold_over_time
},
{
    "instruction": "make me a plot of albums sold over time",
    "input": '',
    "output": quantity_albums_over_time
},
{
    "instruction": "how many copies of photos were printed over time?",
    "input": '',
    "output":  copies_over_time
},
{
    "instruction": "Can you produce a bar graph which shows number of copies printed in July",
    "input": '',
    "output":  copies_july
},
{
    "instruction": "Can you show me the correlation between album sales and photo sales",
    "input": '',
    "output":  correlation_between_album_photo
},
{
    "instruction": "Are sales of copies related to sales of photos",
    "input": '',
    "output":  correlation_between_copy_photo
},
{
    "instruction": "can you give me a horizontal bar chart of the count of sales per day?",
    "input": '',
    "output":  total_sales_per_day_of_week_barh

},
{
    "instruction": "can you summarise the number of sales per hour?",
    "input": '',
    "output":  peak_hours_quantity

},
{
    "instruction": "Tell me the total sales per hour?",
    "input": '',
    "output":  peak_hours_total

},
{
    "instruction": "How many transactions have been $0",
    "input": '',
    "output":  total_0_sale_transactions_over_time

},
{
    "instruction": "Do customers only buy photos, or do they buy copies too?",
    "input": '',
    "output":  photo_vs_copy

},
{
    "instruction": "inform me which staff sells more copies",
    "input": '',
    "output":  staff_copy

},
{
    "instruction": "tell me in table the total sales on weekends vs weekdays",
    "input": '',
    "output":  weekend_vs_weekday_table

},
{
    "instruction": "tell me the total sales on weekends vs weekdays",
    "input": '',
    "output":  weekend_vs_weekday

},
{
    "instruction": "what is the revenue of each unique album",
    "input": '',
    "output":  total_revenue_generated_per_album

},
{
    "instruction": "what is the average sale per transactions",
    "input": '',
    "output":  average_sale_per_transaction

},
{
    "instruction": "what is the average quantity per transaction",
    "input": '',
    "output":  average_quantity_per_transaction

},
{
    "instruction": "which items in store sold the most",
    "input": '',
    "output":  product_highest_revenue

},
{
    "instruction": "what is the average revenue per transaction per staff?",
    "input": '',
    "output":  average_transaction_value_per_staff

},
{
    "instruction": "count of album sales?",
    "input": '',
    "output":  album_quantity_sales

},
{
    "instruction": "top 5 albums sold",
    "input": '',
    "output":  top_5_albums_sold

},
{
    "instruction": "bottom 5 albums sold",
    "input": '',
    "output":  bottom_5_albums

},


]

#LOADING ALL DATASETS

all_dfs = {}
for i in range(200):
    data = pd.read_csv(f'ProcessedData/Joined_DF_{i}.csv')
    try:
        data['action_time'] = pd.to_datetime(data['action_time'])
    except KeyError:
        data['action'] = pd.to_datetime(data['action'])
    data['Date']=pd.to_datetime(data['Date'])
    all_dfs[f'ProcessedData/Joined_DF_{i}.csv'] = data

#SCRAMBLE

print(len(base_data))

graph_types = {}




new_code_list = []

for i,_ in enumerate(base_data):
    random.seed(i)
    index_arr = [random.randint(0,len(code_scrambler.df_columns_list)-1) for _ in range(5)]
    for index in index_arr:
        filename = code_scrambler.df_columns_list[index]['filename']
        output= base_data[i]['output'].replace('#STAFF#',code_scrambler.df_columns_list[index]['staff'])
        output = output.replace('#REPLACED#',code_scrambler.df_columns_list[index]['replaced'])
        output = output.replace('#ACTION#',code_scrambler.df_columns_list[index]['action'])
        output = output.replace('#QUANTITY#',code_scrambler.df_columns_list[index]['quantity'])
        output = output.replace('#ORDER_ID#',code_scrambler.df_columns_list[index]['order_id'])
        output = output.replace('#TOTAL#',code_scrambler.df_columns_list[index]['total'])
        output = output.replace('#CATEGORY#',code_scrambler.df_columns_list[index]['category'])
        output = output.replace('#ARTIST#',code_scrambler.df_columns_list[index]['artist'])
        output = output.replace('#MACHINE#',code_scrambler.df_columns_list[index]['machine'])
        output = output.replace('#DETAIL#',code_scrambler.df_columns_list[index]['detail'])
        new_code_list.append({
            "instruction": base_data[i]['instruction'],
            'input': filename,
            'output': output
        })

#RESTRUCTURE

restructured_code = []

for i in range(len(new_code_list)):

    new_code = code_scrambler.rewrite_ast_to_plot(new_code_list[i]['output'])
    restructured_code.append({
        "instruction": new_code_list[i]["instruction"],
        "input": new_code_list[i]["input"],
        "output": new_code
    })

new_code_list.extend(restructured_code)
errors = 0

final_list = []

for i in tqdm(range(len(new_code_list))):
    
    graph = assess_graph_type(new_code_list[i]['output'])
    graph_types[graph] = graph_types.get(graph,0)+1
    short_error = ''
    image_location = ''
    df = all_dfs[new_code_list[i]['input']]
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            exec(new_code_list[i]['output']+ f"\nplt.savefig('TrainingImages/{i}_{graph}.png', bbox_inches='tight')")
        image_location = f'TrainingImages/{i}_{graph}.png'

    except Warning as w:
        _, _, tb = traceback.sys.exc_info()
        full_error = traceback.format_exc()
        short_error = f'{type(w).__name__ }({tb.tb_lineno}): for {str(w)}'

    except Exception as e:
        
        _, _, tb = traceback.sys.exc_info()
        full_error = traceback.format_exc()
        short_error = f'{type(e).__name__ }({tb.tb_lineno}): for {str(e)}'
        print(full_error)
        errors += 1
    finally:
        exec("plt.close()")
        final_output = black.format_str(new_code_list[i]["output"], mode=black.FileMode())
        final_list.append({
            "instruction": new_code_list[i]["instruction"].replace("\n", "").replace("\r", "").strip(),
            "input": new_code_list[i]["input"].replace("\n", "").replace("\r", "").strip(),
            "output": final_output,
            "graph": graph,
            "error": short_error,
            "image_location": image_location
        })


#making readable file

with open('Training/final_file_readable.txt','w+') as txt_file:
    for item in final_list:
        txt_file.write("Instruction: " + item['instruction']+'\n')
        txt_file.write("Input: " + item['input']+'\n')
        txt_file.write("Graph: " + item['graph']+'\n')
        txt_file.write("Output: " + item['output']+'\n')
        txt_file.write("Error: " + item['error']+'\n\n')
        

with open('Training/final_file.json', 'w+') as json_file:
   
    json.dump(final_list, json_file, indent=4) 

print(f'SUMMARY OF DATA:\n{graph_types}\n')


print(f'COMPILE ERRORS: {errors}/{len(final_list)}')

