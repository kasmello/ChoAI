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
from classes_and_functions import *

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

#FLAGS IN CODE OUTPUT:
    #REPLACED#
        #ACTION#
        #QUANTITY#
        #ORDER_ID#
        #TOTAL#
        #CATEGORY#
        #ARTIST#
        #MACHINE#
        #DETAIL#
        #COLOUR#
        #START#
        #END#
        #YAXIS#
        #XAXIS#
        #TITLE#
    
base_data = [
    data_entry(
        label = "total_over_time",
        instructions=[
            instruction("show me total sales over time", "Date","Total Sales ($)","Total Sales over Time"),
            instruction("What is the total value of sales each day?", "Date","Total Sales ($)","Total Value of Sales Each Day"),
            instruction("Hi, give me the total in revenue as a timeline", "Date", "Total Revenue ($)", "Total Revenue over Time"),
            instruction("how much money made over time", "Date", "Total Revenue ($)", "Total Revenue over Time"),
            instruction("Make me a graph of total sales over time. And hide all axes and titles", "", "", ""),
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
        label = "total_over_time_#PERIOD#",
        instructions=[
            instruction("give me total sales over time for #PERIOD#?", "Date","Total Sales ($)", "Total Sales over Time (#PERIOD#)"),
            instruction("how much money was made over #PERIOD#?", "Date","Total Sales ($)", "Total Sales over Time (#PERIOD#)"),
            instruction("Give me a graph of profit over #PERIOD#? without any labels", "", "",""),
            instruction("Give me a graph of total sales were made over timeline #PERIOD# without an X Axis or Y Axis?", "", "", "Total Sales over Time")
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
        label = "total_over_time_machines",
        instructions=[
            instruction("how much money have the machines made over time?", "Date","Total Sales ($)", "Total Machine Sales over Time"),
            instruction("money profit for photobooth over time", "Date","Profit ($)", "Total Profit over Time for Photobooth"),
            
        ],
        output_raw = [
"""machine_sales_only = df[df['#CATEGORY#']=='Photo']
sales_data = machine_sales_only.groupby('Date')['#TOTAL#'].sum().reset_index()
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
logo_ax.axis('off')"""

        ]
    ),
    data_entry(
        label = "total_over_time_machines_#PERIOD#",
        instructions=[
            instruction("how much money have the machines made over time between #START# and #END#?", "Date","Total Machine Sales ($)", "Total Machine Sales between #START# and #END#"),
            instruction("photobooth sales between #START# and #END#", "Date","Total Machine Sales ($)", "Total Machine Sales between #START# and #END#"),
        ],
        output_raw = [
"""machine_sales_only = df[(df['#CATEGORY#']=='Photo') & (df['#ACTION#']>='#START#') & (df['#ACTION#']<='#END#')]
sales_data = machine_sales_only.groupby('Date')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(sales_data['Date'], sales_data['#TOTAL#'], color="#3B3365", linewidth=2)
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title("#TITLE#", font_properties=manjari_bold)
ax.set_xlim(df['Date'].min() - pd.Timedelta(days=1), df['Date'].max() + pd.Timedelta(days=1))
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
        label = "by_people",
        instructions=[
            instruction("give me sales results based off employee as a bar graph", "Employee","Total Sales ($)", "Total Sales ($) per Employee"),
            instruction("total revenue per staff", "Staff","Total Revenue ($)", "Total Revenue ($) per Employee"),
            instruction("How much money did each worker pull in? Make me a bar graph", "Worker","Total Sales ($)", "Total Sales ($) per Employee"),
        ],
        output_raw = [
"""staff_data = df.groupby('#STAFF#')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(staff_data['#STAFF#'], staff_data['#TOTAL#'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS# Sales ($)', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "peak_hours_quantity",
        instructions=[
            instruction("can you summarise the number of sales per hour?", "Hour","Quantity", "Quantity of Sales at Each Hour"),
            instruction("Quantity of Sales per hour as a bar graph", "Hour","Quantity", "Quantity of Sales at Each Hour"),
        ],
        output_raw = [
"""df['hour'] = df['#ACTION#'].dt.hour
peak_hours = df.groupby('hour')['#QUANTITY#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(peak_hours['hour'], peak_hours['#QUANTITY#'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "peak_hours_total",
        instructions=[
            instruction("Tell me the total revenue each hour of the day?", "Hour","Revenue", 'Total Revenue ($) at each hour'),
            instruction("How much money is made in each hour the store is open", "Hour","Sales", 'Total Sales ($) at each hour'),
        ],
        output_raw = [
"""df['hour'] = df['#ACTION#'].dt.hour
peak_hours = df.groupby('hour')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(peak_hours['hour'], peak_hours['#TOTAL#'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "total_0_sale_transactions_over_time",
        instructions=[
            instruction("How many transactions have been $0 over time", "Date","Transactions", 'Total of Sales with $0 Over Time'),
            instruction("Can you plot all transactions at $0 as a timeline", "Date","Transactions", 'Total of Sales with $0 Over Time'),
        ],
        output_raw = [
"""zero_total = df[df['#TOTAL#']==0]
zero_sale_summary = zero_total.groupby('Date')['#TOTAL#'].count().reset_index()
zero_sale_summary.columns = ['#XAXIS#','#YAXIS#']
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(zero_sale_summary['#XAXIS#'], zero_sale_summary['#YAXIS#'], color="#3B3365", linewidth=2)
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "photo_vs_copy",
        instructions=[
            instruction("Do customers only buy photos, or do they buy copies too?", 'Purchase Category',"Customers", 'Customers Photo Purchase Analysis'),
            instruction("Can you give me a bar graph of customers that buy photos vs customers that also get copies", "Category","Customers", 'Photo and Copy Purchase Analysis'),
        ],
        output_raw = [
"""photos_vs_copies = df[df['#CATEGORY#']=='Photo']
photos_vs_copies['next_purchase'] = photos_vs_copies.groupby('#MACHINE#')['#DETAIL#'].shift(-1)
photos_vs_copies.loc[(photos_vs_copies['#DETAIL#'] == 'Photo') & (photos_vs_copies['next_purchase'] == 'Photo'), 'purchase_category'] = 'Only Photo'
photos_vs_copies.loc[(photos_vs_copies['#DETAIL#'] == 'Photo') & (photos_vs_copies['next_purchase'] == 'Copy'), 'purchase_category'] = 'Copy'
photos_vs_copies_summary = photos_vs_copies.groupby('purchase_category').size().reset_index(name='#YAXIS#')
photos_vs_copies_summary.columns=['#XAXIS#','#YAXIS#']
fix, ax = plt.subplots(figsize=(10, 8))
ax.bar(photos_vs_copies_summary['#XAXIS#'], photos_vs_copies_summary['#YAXIS#'], color="#BCADFF")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "weekend_vs_weekday_table",
        instructions=[
            instruction("tell me in table the total sales on weekends vs weekdays", 'Day Type',"Total Sales ($)", 'Total Sales: Weekdays vs Weekends'),
            instruction("Make a table comparing sales on weekends vs weekdays", "Day","Total Sales ($)", 'Total Sales: Weekdays vs Weekends'),
            instruction("analysis of revenue: weekends and weekdays", "Day","Total Revenue ($)", 'Total Revenue: Weekdays vs Weekends'),
        ],
        output_raw = [
"""df['day_type'] = df['Date'].dt.dayofweek.apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
total_sales_per_type = df.groupby('day_type')['#TOTAL#'].sum().reset_index()
total_sales_per_type.columns = ['#XAXIS#', '#YAXIS#']
total_sales_per_type['#YAXIS#'] = total_sales_per_type['#YAXIS#'].apply(lambda x: f'${x:,.2f}')

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)
"""
        ]
    ),
    data_entry(
        label = "weekend_vs_weekday",
        instructions=[
            instruction("with a bar graph - tell me total sales on weekends vs weekdays", 'Day Type',"Total Sales ($)", 'Total Sales: Weekdays vs Weekends'),
            instruction("Give me an analysis on sales on weekends vs weekdays", "Day","Total Sales ($)", 'Analysis: Weekdays vs Weekends'),
            instruction("Can you give me the total revenue on weekdays and weekends?", "Day Category","Total Revenue ($)", 'Total Revenue: Weekdays vs Weekends'),
        ],
        output_raw = [
"""df['day_type'] = df['Date'].dt.dayofweek.apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
total_sales_per_type = df.groupby('day_type')['#TOTAL#'].sum().reset_index()
total_sales_per_type.columns = ['#XAXIS#', '#YAXIS#']
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(total_sales_per_type['#XAXIS#'], total_sales_per_type['#YAXIS#'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "table_albums_month",
        instructions=[
            instruction("give me a table of total albumns sold per month", 'Month',"Total Albums", 'Albums Sold per Month'),
            instruction("count how many albums were sold each month", 'Month',"Total Albums", 'Albums Sold per Month'),
            instruction("album monthly sales count", 'Month',"Total Albums", 'Quantity of Albums Sold per Month'),

        ],
        output_raw = [
"""albumn_data = df[df['#CATEGORY#']=='Album']
monthly_sales = albumn_data.groupby(pd.Grouper(key='#ACTION#', freq='M'))['#QUANTITY#'].sum().reset_index()
monthly_sales.columns = ['#XAXIS#',"#YAXIS#"]
monthly_sales['#XAXIS#']=monthly_sales['#XAXIS#'].dt.strftime('%B %Y')

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)

"""
        ]
    ),
    data_entry(
        label = "replacement_count",
        instructions=[
            instruction("Show how many employees needed to be replaced on a shift", 'Employee',"Shifts", 'Employees Who Needed Replacement Shifts'),
            instruction("How many shifts needed to be replaced", 'Staff',"Shifts", 'Count of Replacement Shifts'),
            instruction("Was there any workers that could not make it to work", 'Worker',"Shifts", 'Workers Who Needed Replacement Shifts'),

        ],
        output_raw = [
"""staff_replacement_days = df.groupby('#REPLACED#')['Date'].nunique().reset_index(name='Days')
staff_replacement_days = staff_replacement_days.dropna()
all_staff = df['#STAFF#'].unique()
all_staff_df = pd.DataFrame(all_staff, columns=['#STAFF#'])
staff_replacement_days_complete = all_staff_df.merge(staff_replacement_days, left_on='#STAFF#', right_on='#REPLACED#', how='left')
staff_replacement_days_complete['Days'] = staff_replacement_days_complete['Days'].fillna(0)
staff_replacement_days_complete = staff_replacement_days_complete.drop(columns=['#REPLACED#'])
staff_replacement_days_complete = staff_replacement_days_complete.sort_values(by='Days', ascending=False)
staff_replacement_days_complete.columns = ['#XAXIS#','#YAXIS#']

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(staff_replacement_days_complete['#XAXIS#'], staff_replacement_days_complete['#YAXIS#'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "replacement_count_table",
        instructions=[
            instruction("Hi, can you show me in a table the number of times employees needed to be replaced on a shift", 'Employee',"Shifts", 'Employees Who Needed Replacement Shifts'),
            instruction("In table format - print staff that needed replacement shifts", 'Staff',"Shifts", 'Quantity of Replacement Shifts for Staff')

        ],
        output_raw = [
"""staff_replacement_days = df.groupby('#REPLACED#')['Date'].nunique().reset_index(name='Days')
staff_replacement_days = staff_replacement_days.dropna()
all_staff = df['#STAFF#'].unique()
all_staff_df = pd.DataFrame(all_staff, columns=['#STAFF#'])
staff_replacement_days_complete = all_staff_df.merge(staff_replacement_days, left_on='#STAFF#', right_on='#REPLACED#', how='left')
staff_replacement_days_complete['Days'] = staff_replacement_days_complete['Days'].fillna(0)
staff_replacement_days_complete = staff_replacement_days_complete.drop(columns=['#REPLACED#'])
staff_replacement_days_complete = staff_replacement_days_complete.sort_values(by='Days',ascending=False)
staff_replacement_days_complete.columns = ['#XAXIS#','#YAXIS#']

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)

"""
        ]
    ),
    data_entry(
        label = "album_distribution_sales",
        instructions=[
            instruction("give distribution of album sales per Artist as a pir graph", '',"", 'Distribution of Album Sales ber Artist'),
            instruction("what is the total revenue of album sales per artist", '',"", 'Distribution of Album Revenue ber Artist')

        ],
        output_raw = [
"""physical_sales_df = df[(df['#CATEGORY#']=='Album') & (~pd.isna(df['#TOTAL#']))]
physical_sales_per_product = physical_sales_df.groupby('#ARTIST#')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10,8))
ax.pie(physical_sales_per_product['#TOTAL#'], labels=physical_sales_per_product['#ARTIST#'], autopct='%1.1f%%', textprops={'fontproperties': manjari_bold})
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
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
"""def absolute_and_percentage(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f"${absolute} ({pct:.1f}%)"

fig, ax = plt.subplots(figsize=(10,8))
physical_sales_df = df[(df['#CATEGORY#']=='Album') & (~pd.isna(df['#TOTAL#']))]
physical_sales_per_product = physical_sales_df.groupby('#ARTIST#')['#TOTAL#'].sum().reset_index()
ax.pie(physical_sales_per_product['#TOTAL#'], labels=physical_sales_per_product['#ARTIST#'], autopct=lambda pct: absolute_and_percentage(pct, physical_sales_per_product['#TOTAL#']), textprops={'fontproperties': manjari_bold})
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
        ]
    ),
    data_entry(
        label = "machine_sales",
        instructions=[
            instruction("Can you sum up the sales on both machines", 'Machine',"Total Sales ($)", 'Total Machine Sales'),
            instruction("In both the blue and pink Photobooths, what is the total revenue?", 'Photobooth',"Revenue ($)", 'Total Machine Revenue')

        ],
        output_raw = [
"""total_sales = df[df['#CATEGORY#']=='Photo']
total_sales_grouped = total_sales.groupby('#MACHINE#')['#TOTAL#'].sum().reset_index()
total_sales_grouped.columns = ['#XAXIS#','#YAXIS#']

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)

"""
        ]
    ),
    data_entry(
        label = "total_sales_per_day_of_week",
        instructions=[
            instruction("total sales per day of week", 'Day of Week',"Total Sales ($)", 'Total Sales per Day of Week'),
            instruction("How much money is made? Split by day", 'Day of Week',"Revenue ($)", 'Total Revenue per Day of Week'),
            instruction("What is the total profit per weekday? Make a Table", 'Day of Week',"Profit ($)", 'Total Profit per Day of Week')

        ],
        output_raw = [
"""df['Day'] = df['#ACTION#'].dt.day_name()
total_sales_per_day = df.groupby('Day')['#TOTAL#'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
).reset_index()
total_sales_per_day.columns = ['#XAXIS#', '#YAXIS#']
total_sales_per_day['#YAXIS#'] = total_sales_per_day['#YAXIS#'].apply(lambda x: f'${x:,.2f}')

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)

"""
        ]
    ),
    data_entry(
        label = "total_sales_per_day_of_week_bar",
        instructions=[
            instruction("give us the total sales per day of week as a barchart", 'Day of Week',"Total Sales ($)", 'Total Sales per Day of Week'),
            instruction("Sales split by day", 'Day of Week',"Sales ($)", 'Total Sales per Day of Week'),
            instruction("Plot the cumulative sales per day as a vertical bar plot", 'Day of Week',"Cumulative Sales ($)", 'Cumulative per Day of Week')

        ],
        output_raw = [
"""df['Day'] = df['#ACTION#'].dt.day_name()
total_sales_per_day = df.groupby('Day')['#TOTAL#'].sum().reset_index()
total_sales_per_day.columns = ['#XAXIS#', '#YAXIS#']
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(total_sales_per_day['#XAXIS#'], total_sales_per_day['#YAXIS#'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "avg_sales_by_day_of_week",
        instructions=[
            instruction("avg sales per day of week", 'Day of Week',"Average Sales ($)", 'Average Sales per Day of Week'),
            instruction("mean sales per day of week", 'Day of Week',"Mean Sales ($)", 'Mean Sales per Day of Week'),
            instruction("Produce a plot which shows the average value of sales for each weekday", 'Day', "Average Value of Sales ($)", 'Averave Value of Sales per Day')

        ],
        output_raw = [
"""df_grouped = df.groupby('Date')['#TOTAL#'].sum().reset_index()
df_grouped['Day'] = pd.to_datetime(df_grouped['Date']).dt.day_name()
avg_sales_per_day = df_grouped.groupby('Day')['#TOTAL#'].mean().reset_index()
avg_sales_per_day.columns = ['#XAXIS#', '#YAXIS#']
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(avg_sales_per_day['#XAXIS#'], avg_sales_per_day['#YAXIS#'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45, colors="#3B3365")
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
        ]
    ),
    data_entry(
        label = "#BAND_NICKNAME#_sales",
        instructions=[
            instruction("how many #BAND_NICKNAME# albums have we sold so far?", 'Group',"Albums Sold", 'Albums Sold by #BAND_NAME#'),
            instruction("did #BAND_NICKNAME# sell a lot of albums", 'Group',"Albums Sold", 'Albums Sold by #BAND_NAME#'),
            instruction("Can you tell me how many albums #BAND_NICKNAME# sold?", 'Band', "Albums Sold", 'Albums Sold by #BAND_NAME#')

        ],
        output_raw = [
"""
filtered_df = df[df['#ARTIST#']=='#BAND_NAME#']
count_sales = filtered_df.groupby('#ARTIST#')['#QUANTITY#'].sum().reset_index()
count_sales.columns = ['#XAXIS#', '#YAXIS#']

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)
"""
        ]
    ),
    data_entry(
        label = "album_photo_sales",
        instructions=[
            instruction("album sales vs photo sales?", '',"", 'Album vs Photo Sales ($)'),
            instruction("compare album and photo sales", '',"", 'Album vs Photo Sales Comparison ($)'),
            instruction("how much money sold for albums and photos", '', "", 'Album and Photo Sales ($)')

        ],
        output_raw = [
"""fig, ax = plt.subplots(figsize=(10,8))
album_photo_comparison = df[(df['#CATEGORY#'] != 'Miscellaneous') & (~pd.isna(df['#TOTAL#']))]
album_photo_comparison_grouped = album_photo_comparison.groupby('#CATEGORY#')['#TOTAL#'].sum().reset_index()
ax.pie(album_photo_comparison_grouped['#TOTAL#'], labels=album_photo_comparison_grouped['#CATEGORY#'], autopct='%1.1f%%', textprops={'fontproperties': manjari_bold})
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off')
""",
"""fig, ax = plt.subplots(figsize=(10,8))
album_photo_comparison = df[df['#CATEGORY#'] != 'Miscellaneous']
album_photo_comparison_grouped = album_photo_comparison.groupby('#CATEGORY#')['#TOTAL#'].sum().reset_index()
ax.pie(album_photo_comparison_grouped['#TOTAL#'], labels=album_photo_comparison_grouped['#CATEGORY#'], autopct='%1.1f%%', textprops={'fontproperties': manjari_bold})
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off')
"""
        ]
    ),
    data_entry(
        label = "#STAFF_NAME#_#CATEGORY_ALTNAME#_sales",
        instructions=[
            instruction("how many #CATEGORY_ALTNAME# sales did #STAFF_NAME# have?", 'Staff',"Quantity of Sales", "Quantity of #STAFF_NAME#'s #CATEGORY_ALTNAME# Sales"),
            instruction("count how many #CATEGORY_ALTNAME#s #STAFF_NAME# sold?", 'Staff',"Albums Sold", "#STAFF_NAME#'s #CATEGORY_ALTNAME# Sales"),
            instruction("Calculate #STAFF_NAME#'s #CATEGORY_ALTNAME# sales", 'Staff', "Number of #CATEGORY_ALTNAME#s", "#STAFF_NAME#'s #CATEGORY_ALTNAME# Sales"),
            instruction("#STAFF_NAME# #CATEGORY_ALTNAME# sales", 'Staff', "#CATEGORY_ALTNAME# Sales", "#STAFF_NAME# #CATEGORY_ALTNAME# Sales"),
            instruction("Hello, please show number of #CATEGORY_ALTNAME#s sold for #STAFF_NAME#", 'Staff', "#CATEGORY_ALTNAME#s Sold", "#CATEGORY_ALTNAME#s Sold for #STAFF_NAME#"),

        ],
        output_raw = [
"""
def sum_category(list_of_values):
    #CATEGORY_NAME#_column = list_of_values['#CATEGORY#']
    #QUANTITY#_column = list_of_values['#QUANTITY#']
    return np.where(#CATEGORY_NAME#_column=='#CATEGORY_NAME#', #QUANTITY#_column, 0).sum()

filtered_df = df[df['#STAFF#']=='#STAFF_NAME#']
count_sales = filtered_df.groupby('#STAFF#').apply(sum_category).reset_index()
count_sales.columns = ['#XAXIS#', '#YAXIS#']

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title("#TITLE#", weight='bold', font_properties=manjari_bold)

"""
        ]
    ),
    data_entry(
        label = "machine_by_month_comparison",
        instructions=[
            instruction("total sales per month blue vs purple machine", 'Month',"Sales ($)", "Total Sales for Each Machine per Month"),
            instruction("sales per month for both machines machine", 'Month',"Sales ($)", "Total Sales for All Machines per Month"),
            instruction("Profit per month for photobooths", 'Month', "Profit ($)", "Profit per Month for All Photobooths"),
            instruction("Can we please count money made per photobooth per month without a title", 'Month', "Money Made ($)", "")

        ],
        output_raw = [
"""photo_df = df[df['#CATEGORY#']=='Photo']
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
        ax.bar(x + i * bar_width, pivot_sales[product], width=bar_width, label=product,color="#0000FF")
    else:
        ax.bar(x + i * bar_width, pivot_sales[product], width=bar_width, label=product,color="#8F81DD")

ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_xticks(x + bar_width * (num_machines - 1) / 2, months)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
ax.legend(title='Machine')
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

"""
        ]
    ),
    data_entry(
        label = "machine_by_month_comparison",
        instructions=[
            instruction("total sales per month blue vs purple machine", 'Month',"Sales ($)", "Total Sales for Each Machine per Month"),
            instruction("sales per month for both machines machine", 'Month',"Sales ($)", "Total Sales for All Machines per Month"),
            instruction("Profit per month for photobooths", 'Month', "Profit ($)", "Profit per Month for All Photobooths"),
            instruction("Can we please count money made per photobooth per month without a title", 'Month', "Money Made ($)", "")

        ],
        output_raw = [
"""photo_df = df[df['#CATEGORY#']=='Photo']
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
        ax.bar(x + i * bar_width, pivot_sales[product], width=bar_width, label=product,color="#0000FF")
    else:
        ax.bar(x + i * bar_width, pivot_sales[product], width=bar_width, label=product,color="#8F81DD")

ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_xticks(x + bar_width * (num_machines - 1) / 2, months)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
ax.legend(title='Machine')
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 

"""
        ]
    ),
    data_entry(
        label = "#CATEGORY_ALTNAME#_sales_timeline",
        instructions=[
            instruction("#CATEGORY_ALTNAME# sales over time", 'Date',"Total Sales ($)", "#CATEGORY_ALTNAME# Sales Over Time"),
            instruction("#CATEGORY_ALTNAME# revenue over time", 'Date',"Revenue ($)", "Total Revenue for #CATEGORY_ALTNAME# Over Time"),
            instruction("Show me money made for #CATEGORY_ALTNAME#. Hide the X axis", '', "Money Made ($)", "Money Made for #CATEGORY_ALTNAME# Over Time"),
            instruction("Make graph for #CATEGORY_ALTNAME# profit. Hide X and Y axis, only show title. Make it 'Profit for #CATEGORY_ALTNAME#'", '', "", "Profit for #CATEGORY_ALTNAME#")

        ],
        output_raw = [
"""sales_data = df[df['#CATEGORY#']=='#CATEGORY_NAME#']
sales_data = sales_data.groupby('Date')['#TOTAL#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(sales_data['Date'], sales_data['#TOTAL#'], color="#3B3365", linewidth=2)
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_xlim(df['Date'].min() - pd.Timedelta(days=3), df['Date'].max() + pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
ax.tick_params(axis='x', labelrotation=45, colors="#3B3365")
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
        ]
    ),
    data_entry(
        label = "shift_count_per_staff",
        instructions=[
            instruction("can you count how many shifts each staff have been on", 'Staff',"Shift Count", "Shift Count per Staff"),
            instruction("make bar graph that totals all employee shifts", 'Employee',"Shifts","Total Employee Shifts"),
            instruction("Do we know how many shifts each worker been on?", 'Worker', "Shifts", "Shifts per Worker"),
        ],
        output_raw = [
"""staff_shift_count = df.groupby('#STAFF#')['Date'].nunique().reset_index()
staff_shift_count.columns = ["#XAXIS#","#YAXIS#"]

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(staff_shift_count["#XAXIS#"], staff_shift_count["#YAXIS#"], color="#8F81DD")
ax.set_xlabel("#XAXIS#", color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel("#YAXIS#", color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "average_sales_per_shift",
        instructions=[
            instruction("can you give me the average sales per shift per staff", 'Staff',"Average Sales ($)", "Average Sales per Shift for each Staff"),
            instruction("mean profit per shift per staff, no xaxis, yaxis, or title", '',"",""),
            instruction("Give me as a bar graph the mean revenue per staff each time they work", 'Staff', "Mean Revenue ($)", "Mean Revenue per Day"),
        ],
        output_raw = [
"""total_per_employee_day = df.groupby(['#STAFF#','Date'])['#TOTAL#'].sum().reset_index()
avg_per_employee = total_per_employee_day.groupby(['#STAFF#'])['#TOTAL#'].mean().reset_index()
avg_per_employee.columns=["#XAXIS#",'#YAXIS#']

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(avg_per_employee["#XAXIS#"], avg_per_employee['#YAXIS#'], color="#8F81DD")
ax.set_xlabel("#XAXIS#", color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "average_sales_per_shift_table",
        instructions=[
            instruction("What is the average sales each employee gets each day they work", 'Staff',"Average Sales ($)", "Average Sales per Day for each Staff"),
            instruction("Calculate average revenue staff brings in 1 day. X axis = 'Staff of PicCho', Y axis = 'Revenue ($)', title = 'AVG Revenue!'", 'Staff of PicCho',"Revenue ($)","AVG Revenue!"),
            instruction("Calculate in a table mean sales per worker in a single day", 'Worker', "Mean Sales ($)", "Mean Sales per Day"),
        ],
        output_raw = [
"""total_per_employee_day = df.groupby(['#STAFF#','Date'])['#TOTAL#'].sum().reset_index()
avg_per_employee = total_per_employee_day.groupby(['#STAFF#'])['#TOTAL#'].mean().round(2).reset_index()
avg_per_employee.columns=["#XAXIS#","#YAXIS#"]
avg_per_employee["#YAXIS#"] = avg_per_employee["#YAXIS#"].apply(lambda x: f'${x:,.2f}')

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title("Staff Average Sales per Shift", weight='bold', font_properties=manjari_bold)
"""
        ]
    ),
    data_entry(
        label = "top_10_day_sales",
        instructions=[
            instruction("Hi! What are our best selling dates?", 'Date',"Total Sales", "Top 10 Best Day Sales"),
            instruction("Visualise in a table the best selling dates since opening. Make title 'Best Selling Days in Order'", "Date","Sales","Best Selling Days in Order"),
            instruction("Give a top 10 days of most revenue bright in. Ignore X Axis", '', "Revenue", "Top 10 Days of Revenue"),
        ],
        output_raw = [
"""sales_by_date = df.groupby(['Date'])['#TOTAL#'].sum().reset_index()
top_10_sales_by_date = sales_by_date.sort_values(by='#TOTAL#', ascending=False).head(10)
top_10_sales_by_date.columns = ['#XAXIS#','#YAXIS#']
top_10_sales_by_date['#YAXIS#'] = top_10_sales_by_date['#YAXIS#'].apply(lambda x: f'${x:,.2f}')
top_10_sales_by_date['#XAXIS#'] = top_10_sales_by_date['#XAXIS#'].dt.strftime('%d/%m/%Y')

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title("#TITLE#", weight='bold', font_properties=manjari_bold)

"""
        ]
    ),
    data_entry(
        label = "employee_sales_pie_chart",
        instructions=[
            instruction("pie chart of total sales per employee", '',"", "Distribution of Sales per Employe"),
            instruction("Make a visualisation showing distribution of sales per employee. No title", "","",""),
            instruction("Proportion of revenue per staff. Make a Pie chart", '', "", "Proportion of Revenue per Staff"),
        ],
        output_raw = [
"""def actual_percentage(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f"${absolute} ({pct:.1f}%)"

fig, ax = plt.subplots(figsize=(10,8))
total_sales_per_employee = df[~pd.isna(df['#TOTAL#'])]
total_sales_per_employee_grouped = total_sales_per_employee.groupby('#STAFF#')['#TOTAL#'].sum().reset_index()
ax.pie(total_sales_per_employee_grouped['#TOTAL#'], labels=total_sales_per_employee_grouped['#STAFF#'], autopct=lambda pct: actual_percentage(pct, total_sales_per_employee_grouped['#TOTAL#']), textprops={'fontproperties': manjari_bold})
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
        ]
    ),
    data_entry(
        label = "boxplot_per_employee",
        instructions=[
            instruction("Generate a visual showing a boxplot each employee sale", 'Employee',"Sales ($)", "Plot of Sales per Employee"),
            instruction("Boxplot of total revenue per employee. No employee axis. Title = 'Calculated Revenue oer Employee'", "","Revenue ($)","Calculated Revenue oer Employee"),
            instruction("Box Plot Staff Sales in $. No Labels or axes", '', "", ""),
            instruction("worker sales - see median in box plot", 'Worker', "Sales ($)", "Worker Sales"),
        ],
        output_raw = [
"""grouped_by_day = df.groupby(['#STAFF#','Date'])['#TOTAL#'].sum().reset_index()
staff_names = grouped_by_day['#STAFF#'].unique()
grouped_by_staff = [grouped_by_day[grouped_by_day['#STAFF#'] == staff]['#TOTAL#'].values for staff in staff_names]
fig, ax = plt.subplots(figsize=(10,8))
box = ax.boxplot(grouped_by_staff, labels=staff_names, patch_artist=True)
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
colors=["#800000", "#FF7F50", "#90EE90", "#0000FF", "#BCADFF", "#8F81DD", "#3B3365"]
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)

for patch, colour in zip(box['boxes'],colors):
    patch.set_facecolor(colour)
"""
        ]
    ),
    data_entry(
        label = "daily_statistics",
        instructions=[
            instruction("Give me a rundown of daily sales statistics", 'Statistic',"Value", "Overview of Daily Sales"),
            instruction("Display Summary Statistics. Hide Title", "Summary Statistic","Value",""),
        ],
        output_raw = [
"""daily_statistics = df.groupby('Date')['#TOTAL#'].sum().reset_index()
daily_statistics_agg = daily_statistics['#TOTAL#'].agg(['mean','median','std','max','min']).round(2).reset_index()
daily_statistics_agg.columns = ['#XAXIS#','#YAXIS#']
daily_statistics_agg['#XAXIS#']=daily_statistics_agg['#XAXIS#'].str.title()

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title("#TITLE#", weight='bold', font_properties=manjari_bold)

"""
        ]
    ),
    data_entry(
        label = "moving_avg_week",
        instructions=[
            instruction("get me the moving average of sales per week!", 'Date', "Total Sales ($)", 'Sales over Time'),
            instruction("Bar chart of revenue vs moving average with rolling window of 7 days", 'Date', "Revenue ($)", 'Sales over Time'),
        ],
        output_raw = [
"""total_sales_per_day = df.groupby('Date')['#TOTAL#'].sum().reset_index()
total_sales_per_day['Weekly Moving Average'] = total_sales_per_day['#TOTAL#'].rolling(window=7).mean()
total_sales_per_day.columns=['#XAXIS#','#YAXIS#', 'Weekly Moving Average ($)']

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(total_sales_per_day['#XAXIS#'], total_sales_per_day['#YAXIS#'], color="#8F81DD")
ax.plot(total_sales_per_day['#XAXIS#'], total_sales_per_day['Weekly Moving Average ($)'], color="#3B3365", linewidth=3, linestyle=':')
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=90)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(colors="#3B3365")
ax.set_xlim(df['Date'].min()-pd.Timedelta(days=3),df['Date'].max()+pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
        ]
    ),
    data_entry(
        label = "tally_days_less_than_50",
        instructions=[
            instruction("tally the days with less than $50 in sales", 'Day', "Tally", "Tally of Days with less than $50 in sales"),
        ],
        output_raw = [
"""total_sales_per_day = df.groupby('Date')['#TOTAL#'].sum().reset_index()
low_sales = total_sales_per_day[total_sales_per_day['#TOTAL#']<50]
low_sales['Day'] = pd.to_datetime(low_sales['Date']).dt.day_name()
low_sales_grouped = low_sales.groupby('Day')['Date'].nunique().reset_index()
low_sales_grouped.columns=['#XAXIS#','#YAXIS#']

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title("#TITLE#", weight='bold', font_properties=manjari_bold)

"""
        ]
    ),
    data_entry(
        label = "area_chart_albums_sold_over_time",
        instructions=[
            instruction("area chart of albums sold over time", 'Date', "Albums Sold", "Quantity of Albums Sold over Time"),
            instruction("Make an area chart about album sales in timeline", 'Date', "Albums Sold", "Albums Sold over Time"),
        ],
        output_raw = [
"""album_sales = df[df['#CATEGORY#']=='Album']
total_album_sales = album_sales.groupby(['Date','#CATEGORY#'])['#QUANTITY#'].sum().reset_index()
pivot_df = total_album_sales.pivot(index='Date', columns='#CATEGORY#', values='#QUANTITY#').fillna(0)
x = pivot_df.index  
y = pivot_df.values.T 
fig, ax = plt.subplots(figsize=(10, 8))
ax.stackplot(x, y, labels=pivot_df.columns, alpha=0.8)
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(colors="#3B3365")
ax.set_xlim(df['Date'].min()-pd.Timedelta(days=3),df['Date'].max()+pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
ax.legend(loc='center right',bbox_to_anchor=(1.35, 0.5))
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
        ]
    ),
    data_entry(
        label = "quantity_albums_over_time",
        instructions=[
            instruction("make me a plot of albums sold over time", 'Date', "Albums Sold", "Quantity of Albums Sold over Time"),
        ],
        output_raw = [
"""album_sales = df[df['#CATEGORY#']=='Album']
total_album_sales = album_sales.groupby(['Date'])['#QUANTITY#'].sum().reset_index()
total_album_sales['Date']=pd.to_datetime(total_album_sales['Date'])
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(total_album_sales['Date'], total_album_sales['#QUANTITY#'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(colors="#3B3365")
ax.set_xlim(df['Date'].min()-pd.Timedelta(days=3),df['Date'].max()+pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
        ]
    ),
    data_entry(
        label = "copies_over_time",
        instructions=[
            instruction("how many copies of photos were printed over time", 'Date', "Copies Printed", "Copied Over Time"),
        ],
        output_raw = [
"""copy_sales = df[(df['#DETAIL#']=='Copy')]
total_copy_sales = copy_sales.groupby(['Date'])['#QUANTITY#'].sum().reset_index()
total_copy_sales['Date']=pd.to_datetime(total_copy_sales['Date'])
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(total_copy_sales['Date'], total_copy_sales['#QUANTITY#'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(colors="#3B3365")
ax.set_xlim(df['Date'].min()-pd.Timedelta(days=3),df['Date'].max()+pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
        ]
    ),
    data_entry(
        label = "copies_#PERIOD#",
        instructions=[
            instruction("copies between #START# and #END#", 'Date', "Copies", "Quantity of Sold Copies between #START# and #END#"),
        ],
        output_raw = [
"""copy_sales = df[(df['#DETAIL#']=='Copy')]
total_copy_sales = copy_sales.groupby(['Date'])['#QUANTITY#'].sum().reset_index()
total_copy_sales['Date']=pd.to_datetime(total_copy_sales['Date'])
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(total_copy_sales['Date'], total_copy_sales['#QUANTITY#'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS# Printed', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('#TITLE#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(colors="#3B3365")
ax.set_xlim(pd.to_datetime('2024-07-01')-pd.Timedelta(days=1), pd.to_datetime('2024-07-31')+pd.Timedelta(days=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
"""
    ]
    ),
    data_entry(
        label = "correlation_between_album_photo",
        instructions=[
            instruction("Can you show me the correlation between album sales and photo sales", 'Photo Sales ($)', "Album Sales ($)", "Correlation between Photo and Album Sales"),
            instruction("Show relationship between album and film sales", 'Film Sales ($)', "Album Sales ($)", "Relationship between Film and Album Sales"),
        ],
        output_raw = [
"""photos_df = df[df['#CATEGORY#']=='Photo']
albums_df = df[df['#CATEGORY#']=='Album']
photo_sales = photos_df.groupby('Date')['#TOTAL#'].sum().reset_index(name='photo_sales')
album_sales = albums_df.groupby('Date')['#TOTAL#'].sum().reset_index(name='album_sales')
merged_sales = pd.merge(photo_sales, album_sales, on='Date', how='inner')

fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(merged_sales['photo_sales'], merged_sales['album_sales'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "correlation_between_copy_photo",
        instructions=[
            instruction("Are sales of copies related to sales of photos", 'Photo Sales ($)', "Copy Sales ($)", "Relationship between Photo and Copy Sales"),
            instruction("show correlation between Copy and Film", 'Copy Sales ($)', "Film Sales ($)", "Correlation between Copy and Film Sales"),
        ],
        output_raw = [
"""photos_df = df[df['#CATEGORY#']=='Photo']
copy_df = df[df['#DETAIL#']=='Copy']
photo_sales = photos_df.groupby('Date')['#TOTAL#'].sum().reset_index(name='photo_sales')
copy_df = copy_df.groupby('Date')['#TOTAL#'].sum().reset_index(name='copy_sales')
merged_sales = pd.merge(photo_sales, copy_df, on='Date', how='inner')

fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(merged_sales['photo_sales'], merged_sales['copy_sales'], color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "total_sales_per_day_of_week_barh",
        instructions=[
            instruction("give me a horizontal bar chart of the count of sales per weekday", 'Count of Sales', "Day of Week", "Sales Count by Day of Week"),
            instruction("Show the quantity of sales on unique day of week", 'Quantity of Sales', "Day of Week", "Sales Quantity by Day of Week"),
        ],
        output_raw = [
"""df['Day'] = df['#ACTION#'].dt.day_name()
total_sales_per_day = df.groupby('Day')['#QUANTITY#'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(total_sales_per_day['Day'],total_sales_per_day['#QUANTITY#'],color="#8F81DD")
ax.set_xlabel('#XAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('#YAXIS#', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=90)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "staff_copy",
        instructions=[
            instruction("inform which staff sells more copies", 'Staff', "Total Copy Sales", "Ordering Staff by Copy Sales"),
            instruction("Show order of employee by quantity of copy sales", 'Employee', "Quantity of Copy Sales", "Employees Ordered by Copy Sales"),
        ],
        output_raw = [
"""copy_sales = df[df['#DETAIL#']=='Copy']
copy_sales_per_staff = copy_sales.groupby('#STAFF#')['#TOTAL#'].sum().reset_index()
copy_sales_per_staff.columns = ['#XAXIS#', '#YAXIS#']
copy_sales_per_staff = copy_sales_per_staff.sort_values(by='#YAXIS#', ascending=False)
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(copy_sales_per_staff["#XAXIS#"],copy_sales_per_staff['#YAXIS#'],color="#8F81DD")
ax.set_xlabel("#XAXIS#", color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=90)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "total_revenue_generated_per_album",
        instructions=[
            instruction('revenue of each unique album. Make into bar plot, make title "total revenue of all albums"', 'Album', "Total Revenue ($)", "Total Revenue of All Albums"),
            instruction('give sales of each album', 'Album', "Total Sales ($)", "Total Sales of All Albums"),
        ],
        output_raw = [
"""album_sales = df[df['#CATEGORY#']=='Album']
album_sales_summary = album_sales.groupby('#DETAIL#')['#TOTAL#'].sum().reset_index()
album_sales_summary.columns = ["#XAXIS#", '#YAXIS#']
fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(album_sales_summary["#XAXIS#"],album_sales_summary['#YAXIS#'],color="#8F81DD")
ax.set_xlabel("#XAXIS#", color="#3B3365", font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color="#3B3365", font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=90)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
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
        label = "average_sale_per_transaction",
        instructions=[
            instruction('what is the average sale per transaction', 'Category', "AVG Value ($)", "Average Sale per Transaction Type"),
            instruction('mean value of revenue per type of transaction', 'Type', "Mean Revenue ($)", "Mean Revenue per Transaction Type"),
        ],
        output_raw = [
"""transaction_total = df.groupby(['#CATEGORY#','#ORDER_ID#'])['#TOTAL#'].sum().reset_index()
average_transaction = transaction_total.groupby('#CATEGORY#')['#TOTAL#'].mean().reset_index()
average_transaction.columns=['#XAXIS#','#YAXIS#']
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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)

"""
    ]
    ),
    data_entry(
        label = "average_quantity_per_transaction",
        instructions=[
            instruction('what is the avg quantity per transaction? Make horizontal axis "Type of Transaction", vertical axis "AVG", title = "Average Quantity per Transaction"', 'Type of Transaction', "AVG", "Average Quantity per Transaction"),
            instruction('what is the mean count of items per transaction? Make x axis "Transaction", y axis "AVG", title is "Average Count each Transaction"', 'Transaction', "AVG", "Average Count each Transaction"),
            instruction('draw mean items per transaction in table', 'Category', "Mean Items", "Mean Items per Transaction"),
        ],
        output_raw = [
"""transaction_total = df.groupby(['#CATEGORY#','#ORDER_ID#'])['#QUANTITY#'].sum().reset_index()
average_transaction = transaction_total.groupby('#CATEGORY#')['#QUANTITY#'].mean().reset_index()
average_transaction.columns=['#XAXIS#','#YAXIS#']
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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)

"""
    ]
    ),
    data_entry(
        label = "product_highest_revenue",
        instructions=[
            instruction('which items in store sold the most', 'Product', "Revenue ($)", "Products with Highest Revenue"),
        ],
        output_raw = [
"""total_revenue = df.groupby('#DETAIL#')['#TOTAL#'].sum().reset_index()
total_revenue = total_revenue.sort_values(by='#TOTAL#',ascending=False)
total_revenue = total_revenue.iloc[:5]
total_revenue['#TOTAL#'] = total_revenue['#TOTAL#'].apply(lambda x: f'${x:,.2f}')
total_revenue.columns=['#XAXIS#','#YAXIS#']

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)

"""
    ]
    ),
    data_entry(
        label = "average_transaction_value_per_staff",
        instructions=[
            instruction('what is the average revenue per transaction per staff?', 'Staff', "AVG Revenue ($)", "Average Revenue per Transaction (Staff)"),
        ],
        output_raw = [
"""transaction_total = df.groupby(['#STAFF#','#ORDER_ID#'])['#TOTAL#'].sum().reset_index()
average_transaction = transaction_total.groupby('#STAFF#')['#TOTAL#'].mean().reset_index()
average_transaction.columns=['#XAXIS#','#YAXIS#']
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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)
"""
    ]
    ),
    data_entry(
        label = "album_quantity_sales",
        instructions=[
            instruction('count of album sales?', 'Album', "Count", "Count of Album Sales"),
        ],
        output_raw = [
"""album_sales = df[df['#CATEGORY#']=='Album']
quantity_albumns_sold = album_sales.groupby('#DETAIL#')['#QUANTITY#'].sum().reset_index()
quantity_albumns_sold['#QUANTITY#'] = quantity_albumns_sold['#QUANTITY#'].apply(lambda x: f'${x:,.2f}')
quantity_albumns_sold.columns=['#XAXIS#','#YAXIS#']

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)

"""
    ]
    ),
    data_entry(
        label = "top_5_albums_sold",
        instructions=[
            instruction('top 5 albums sold', 'Album', "Sales ($)", "Top 5 Albums in Sales"),
        ],
        output_raw = [
"""album_sales = df[df['#CATEGORY#']=='Album']
total_album_revenue = album_sales.groupby('#DETAIL#')['#TOTAL#'].sum().reset_index()
total_album_revenue = total_album_revenue.sort_values(by='#TOTAL#',ascending=False)
total_album_revenue = total_album_revenue.iloc[:5]
total_album_revenue['#TOTAL#'] = total_album_revenue['#TOTAL#'].apply(lambda x: f'${x:,.2f}')
total_album_revenue.columns=['#XAXIS#','#YAXIS#']

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)

"""
    ]
    ),
    data_entry(
        label = "bottom_5_albums",
        instructions=[
            instruction('bottom 5 albums in Revenue as a table', 'Album', "Revenue ($)", "Bottom 5 Albums in Revenue"),
        ],
        output_raw = [
"""album_sales = df[df['#CATEGORY#']=='Album']
total_album_revenue = album_sales.groupby('#DETAIL#')['#TOTAL#'].sum().reset_index()
total_album_revenue = total_album_revenue.sort_values(by='#TOTAL#',ascending=True)
total_album_revenue = total_album_revenue.iloc[:5]
total_album_revenue['#TOTAL#'] = total_album_revenue['#TOTAL#'].apply(lambda x: f'${x:,.2f}')
total_album_revenue.columns=['#XAXIS#','#YAXIS#']

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
        cell.set_facecolor("#3B3365") 
    else:
        cell.set_text_props(weight='bold', color='black',font=manjari_bold)
        cell.set_facecolor("#8F81DD") if i % 2 == 0 else cell.set_facecolor("#BCADFF")

ax.set_title('#TITLE#', weight='bold', font_properties=manjari_bold)

"""
    ]
    )
    


]

new_data = mix(base_data)
new_data = flag_replace(new_data)
new_data = scramble(new_data)
new_data = oo_to_state(new_data)
new_data = test(new_data)

#making readable file

with open('Training/final_file_readable.txt','w+') as txt_file:
    for item in new_data:
        txt_file.write("ID: " + str(item['ID'])+'\n')
        txt_file.write("Label: " + str(item['label'])+'\n')
        txt_file.write("Instruction: " + item['instruction']+'\n')
        txt_file.write("Input: " + item['input']+'\n')
        txt_file.write("Graph: " + item['graph']+'\n')
        txt_file.write("Output: " + item['output']+'\n')
        txt_file.write("Error: " + item['error']+'\n\n')
        

with open('Training/final_file.json', 'w+') as json_file:
   
    json.dump(new_data, json_file, indent=4) 

