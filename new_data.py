import json
import csv
import random
import code_scrambler
import pandas as pd


def turn_df_into_input(data_file):
    with open(data_file, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile, quotechar='"', delimiter=',')
        headers = next(csvreader)
        combined_data = ['"' + '","'.join(headers) + '"']

        for row in csvreader:
            combined_row = '"' + '","'.join(row) + '"'  # Add quotes around each cell
            combined_data.append(combined_row)

    # Join all rows into a single string separated by newlines
    training_data = '\n'.join(combined_data)
    return training_data

data_file = 'ProcessedData/Joined_DF.csv'
data_str = turn_df_into_input(data_file)



# def replace_database


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


#what we need data of


machine_over_time = """sales_data = df.groupby('Date')['total'].sum().reset_index()
fig, ax = plt.subplots()
ax.plot(sales_data['Date'], sales_data['total'], color=dark, linewidth=2)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Machine Sales Over Time', color=dark, font_properties=manjari_bold)
ax.set_xlim(df['Date'].min() - pd.Timedelta(days=3), df['Date'].max() + pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show(block=False)"""

machine_over_time_july = """sales_data = df[(df[#ACTION#]>='2024-07-01') & (df[#ACTION#]<='2024-07-31')].groupby('Date')['total'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(sales_data['Date'], sales_data['total'], color=medium)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.set_xlim(pd.to_datetime('2024-07-01')-pd.Timedelta(days=1), pd.to_datetime('2024-07-31')+pd.Timedelta(days=1))
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.set_title('Machine Sales Over Time (July)', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show(block=False)"""

machine_over_time_august = """sales_data = df[(df[#ACTION#]>='2024-08-01') & (df[#ACTION#]<='2024-08-31')].groupby('Date')['total'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(sales_data['Date'], sales_data['total'], color=medium)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_xlim(pd.to_datetime('2024-08-01')-pd.Timedelta(days=1), pd.to_datetime('2024-08-31')+pd.Timedelta(days=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y')) 
ax.set_title('Machine Sales Over Time', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show(block=False)"""

by_people = """staff_data = df.groupby(#STAFF#)['total'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(staff_data[#STAFF#], staff_data['total'], color=medium)
ax.set_xlabel('Staff', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales ($)', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Machine Sales per Employee', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show(block=False)"""

peak_hours_quantity = """df['hour'] = df[#ACTION#].dt.hour
peak_hours = df.groupby('hour')[#QUANTITY#].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(peak_hours['hour'], peak_hours[#QUANTITY#], color=medium)
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
plt.show(block=False)"""

peak_hours_total = """df['hour'] = df[#ACTION#].dt.hour
peak_hours = df.groupby('hour')['total'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(peak_hours['hour'], peak_hours['total'], color=medium)
ax.set_xlabel('Hour', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total', color=dark, font_properties=manjari_bold)
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
plt.show(block=False)"""

total_0_sale_transactions_over_time = """zero_total = df[df['total']==0]
zero_sale_summary = zero_total.groupby('Date')['total'].count().reset_index()
zero_sale_summary.columns = ['Date','Total']
fig, ax = plt.subplots()
ax.plot(zero_sale_summary['Date'], zero_sale_summary['Total'], color=dark, linewidth=2)
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
plt.show(block=False)"""

photo_vs_copy = """photos_vs_copies = df[df['product'].isin(['Blue Machine','Purple Machine'])]
photos_vs_copies['next_purchase'] = photos_vs_copies.groupby('product')['type'].shift(-1)
photos_vs_copies.loc[(photos_vs_copies['type'] == 'Photo') & (photos_vs_copies['next_purchase'] == 'Photo'), 'purchase_category'] = 'Only Photo'
photos_vs_copies.loc[(photos_vs_copies['type'] == 'Photo') & (photos_vs_copies['next_purchase'] == 'Copy/Print'), 'purchase_category'] = 'Copy'
photos_vs_copies_summary = photos_vs_copies.groupby('purchase_category').size().reset_index(name='count')
photos_vs_copies_summary.columns=['Purchase Category','Count']
fix, ax = plt.subplots()
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
plt.show(block=False)"""

weekend_vs_weekday_table = """df['day_type'] = df['Date'].dt.dayofweek.apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
total_sales_per_type = df.groupby('day_type')['total'].sum().reset_index()
total_sales_per_type.columns = ['Day Type', 'Total Sales']
total_sales_per_type['Total Sales'] = total_sales_per_type['Total Sales'].apply(lambda x: f'${x:,.2f}')

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=total_sales_per_type.values, 
    colLabels=total_sales_per_type.columns, 
    cellLoc='center'
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

ax.set_title('Total Sales: Weekdays vs Weekends', fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

weekend_vs_weekday = """df['day_type'] = df['Date'].dt.dayofweek.apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')
total_sales_per_type = df.groupby('day_type')['total'].sum().reset_index()
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
plt.show(block=False)"""


table_albums_month = """albumn_data = df[~df['type'].isin(['Photo','Unknown'])]
monthly_sales = albumn_data.groupby(pd.Grouper(key=#ACTION#, freq='M'))[#QUANTITY#].sum().reset_index()
monthly_sales.columns = ['Month','Total Albums']
monthly_sales['Month']=monthly_sales['Month'].dt.strftime('%B %Y')

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=monthly_sales.values, 
    colLabels=monthly_sales.columns, 
    cellLoc='center'
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

ax.set_title('Album Sales per Month', fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

replacement_count = """staff_replacement_days = df.groupby(#REPLACED#)['Date'].nunique().reset_index(name='Days')
staff_replacement_days = staff_replacement_days.dropna()
all_staff = df[#STAFF#].unique()
all_staff_df = pd.DataFrame(all_staff, columns=[#STAFF#])
staff_replacement_days_complete = all_staff_df.merge(staff_replacement_days, left_on=#STAFF#, right_on=#REPLACED#, how='left')
staff_replacement_days_complete['Days'] = staff_replacement_days_complete['Days'].fillna(0)
staff_replacement_days_complete = staff_replacement_days_complete.drop(columns=[#REPLACED#])
staff_replacement_days_complete = staff_replacement_days_complete.sort_values(by='Days', ascending=False)

fig, ax = plt.subplots()
ax.bar(staff_replacement_days_complete[#STAFF#], staff_replacement_days_complete['Days'], color=medium)
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
plt.show(block=False)"""

replacement_count_table = """staff_replacement_days = df.groupby(#REPLACED#)['Date'].nunique().reset_index(name='Days')
staff_replacement_days = staff_replacement_days.dropna()
all_staff = df[#STAFF#].unique()
all_staff_df = pd.DataFrame(all_staff, columns=[#STAFF#])
staff_replacement_days_complete = all_staff_df.merge(staff_replacement_days, left_on=#STAFF#, right_on=#REPLACED#, how='left')
staff_replacement_days_complete['Days'] = staff_replacement_days_complete['Days'].fillna(0)
staff_replacement_days_complete = staff_replacement_days_complete.drop(columns=[#REPLACED#])
staff_replacement_days_complete = staff_replacement_days_complete.sort_values(by='Days',ascending=False)

fig, ax = plt.subplots(figsize=(8,1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=staff_replacement_days_complete.values, 
    colLabels=staff_replacement_days_complete.columns, 
    cellLoc='center'
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

ax.set_title('Table of all Employees that needed Replacements', fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

album_distribution_sales = """fig, ax = plt.subplots()
physical_sales_df = df[(~df['type'].isin(['Photo','Unknown'])) & (~pd.isna(df['total']))]
physical_sales_per_product = physical_sales_df.groupby('type')['total'].sum().reset_index()
fig, ax = plt.subplots(figsize=(12,12))
ax.pie(physical_sales_per_product['total'], labels=physical_sales_per_product['type'], autopct='%1.1f%%', textprops={'fontproperties': manjari_bold})
ax.set_title('Distribution of Album Sales', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.tight_layout()
plt.show(block=False)"""

album_distribution_sales_actual = """def format_autopct(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f"${absolute} ({pct:.1f}%)"

fig, ax = plt.subplots(figsize=(9,9))
physical_sales_df = df[(~df['type'].isin(['Photo','Unknown'])) & (~pd.isna(df['total']))]
physical_sales_per_product = physical_sales_df.groupby('type')['total'].sum().reset_index()
ax.pie(physical_sales_per_product['total'], labels=physical_sales_per_product['type'], autopct=lambda pct: format_autopct(pct, physical_sales_per_product['total']), textprops={'fontproperties': manjari_bold})
ax.set_title('Distribution of Album Sales', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.tight_layout()
plt.show(block=False)"""

machine_sales = """total_sales = df[df['type']=='Photo']
total_sales_grouped = total_sales.groupby('product')['total'].sum().reset_index()
total_sales_grouped.columns = ['Machine','Total Sales']

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=total_sales_grouped.values, 
    colLabels=total_sales_grouped.columns, 
    cellLoc='center'
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

ax.set_title('Total Machine Sales', fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

machine_count = """count_sales = df[df['type']=='Photo']
count_sales_grouped = count_sales.groupby('product')['total'].count().reset_index()
count_sales_grouped.columns = ['Album','Total Sales']

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=count_sales_grouped.values, 
    colLabels=count_sales_grouped.columns, 
    cellLoc='center'
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

ax.set_title('Machine Sales', fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

total_sales_per_day_of_week = """df['Day'] = df[#ACTION#].dt.day_name()
total_sales_per_day = df.groupby('Day')['total'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
).reset_index()
total_sales_per_day.columns = ['Day of Week', 'Total Sales']
total_sales_per_day['Total Sales'] = total_sales_per_day['Total Sales'].apply(lambda x: f'${x:,.2f}')

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=total_sales_per_day.values, 
    colLabels=total_sales_per_day.columns, 
    cellLoc='center'
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

ax.set_title('Total Sales per Day of Week', fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

total_sales_per_day_of_week_bar = """df['Day'] = df[#ACTION#].dt.day_name()
total_sales_per_day = df.groupby('Day')['total'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)
total_sales_per_day.columns = ['Day of Week', 'Total Sales ($)']
fig, ax = plt.subplots()
total_sales_per_day.plot(kind='bar', color=medium, ax=ax)
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
plt.show(block=False)"""

avg_sales_by_day_of_week = """df_grouped = df.groupby('Date')['total'].sum().reset_index()
df_grouped['Day'] = pd.to_datetime(df_grouped['Date']).dt.day_name()
avg_sales_per_day = df_grouped.groupby('Day')['total'].mean().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)
avg_sales_per_day.columns = ['Day of Week', 'Total Sales ($)']
fig, ax = plt.subplots()
avg_sales_per_day.plot(kind='bar', color=medium, ax=ax)
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
plt.show(block=False)"""

bts_sales = """filtered_df = df[df['type']=='BTS']
count_sales = filtered_df.groupby(#QUANTITY#).sum().reset_index()
count_sales.columns = ['Group', 'Count of Sales']

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=count_sales.values, 
    colLabels=count_sales.columns, 
    cellLoc='center'
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

ax.set_title('Count of Sales for BTS Albums', fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

album_photo_sales = """fig, ax = plt.subplots(figsize=(9,9))
album_photo_comparison = df[(df['type'] != 'Unknown') & (~pd.isna(df['total']))]
album_photo_comparison['Album/Photo'] = album_photo_comparison['type'].apply(lambda x: 'Photo' if x == 'Photo' else 'Album')
album_photo_comparison_grouped = album_photo_comparison.groupby('Album/Photo')['total'].sum().reset_index()
ax.pie(album_photo_comparison_grouped['total'], labels=album_photo_comparison_grouped['Album/Photo'], autopct='%1.1f%%', textprops={'fontproperties': manjari_bold})
ax.set_title('Album and Photo Sales Comparison', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.tight_layout()
plt.show(block=False)"""

karmel_sales = """filtered_df = df[(df[#STAFF#]=='Karmel') & ~df['type'].isin(['Photo','Unknown'])]
count_sales = filtered_df.groupby(#STAFF#)[#QUANTITY#].sum().reset_index()
count_sales.columns = ['Staff', 'Count of Sales']

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=count_sales.values, 
    colLabels=count_sales.columns, 
    cellLoc='center'
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

ax.set_title("Count of Karmel's Album Sales", fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

jess_total_sales="""filtered_df = df[(df[#STAFF#]=='Jess') & df['type'].isin(['Photo'])]
count_sales = filtered_df.groupby(#STAFF#)['total'].sum().reset_index()
count_sales.columns = ['Staff', 'Total Sales']
count_sales['Total Sales'] = count_sales['Total Sales'].apply(lambda x: f'${x:,.2f}')

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=count_sales.values, 
    colLabels=count_sales.columns, 
    cellLoc='center'
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

ax.set_title("Total Photo Sales for Jess", fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

machine_by_month_comparison = """photo_df = df[df['type']=='Photo']
photo_df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M')
monthly_sales = photo_df.groupby(['Month', 'product'])['total'].sum().reset_index()
monthly_sales['Month']=monthly_sales['Month'].dt.strftime('%B %Y')
pivot_sales = monthly_sales.pivot(index='Month', columns='product', values='total').fillna(0)
months = pivot_sales.index.astype(str)
products = pivot_sales.columns
num_products = len(products)
x = np.arange(len(months))
bar_width = 0.8 / num_products  # Adjust the width based on the number of products
fig, ax = plt.subplots()

for i, product in enumerate(products):
    if i % 2 == 0:
        ax.bar(x + i * bar_width, pivot_sales[product], width=bar_width, label=product,color=blue)
    else:
        ax.bar(x + i * bar_width, pivot_sales[product], width=bar_width, label=product,color=medium)

ax.set_xlabel('Month', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sale ($)', color=dark, font_properties=manjari_bold)
ax.set_xticks(x + bar_width * (num_products - 1) / 2, months)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.set_title('Total Photo Sales by Product and Month', color=dark, font_properties=manjari_bold)
ax.legend(title='Product')
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.tight_layout()
plt.show(block=False)"""

album_sales="""sales_data = df[~df['type'].isin(['Photo','Unknown'])]
sales_data = sales_data.groupby('Date')['total'].sum().reset_index()
fig, ax = plt.subplots()
ax.plot(sales_data['Date'], sales_data['total'], color=dark, linewidth=2)
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
plt.show(block=False)"""

shift_count_per_staff="""staff_shift_count = df.groupby(#STAFF#)['Date'].nunique().reset_index()
staff_shift_count.columns = ['Staff','Shift Count']

fig, ax = plt.subplots()
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
plt.show(block=False)"""

average_sales_per_shift="""total_per_employee_day = df.groupby([#STAFF#,'Date'])['total'].sum().reset_index()
avg_per_employee = total_per_employee_day.groupby([#STAFF#])['total'].mean().reset_index()
avg_per_employee.columns=['Staff','Average']

fig, ax = plt.subplots()
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
plt.show(block=False)"""

average_sales_per_shift_table="""total_per_employee_day = df.groupby([#STAFF#,'Date'])['total'].sum().reset_index()
avg_per_employee = total_per_employee_day.groupby([#STAFF#])['total'].mean().round(2).reset_index()
avg_per_employee.columns=['Staff','Average']
avg_per_employee['Average'] = avg_per_employee['Average'].apply(lambda x: f'${x:,.2f}')

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=avg_per_employee.values, 
    colLabels=avg_per_employee.columns, 
    cellLoc='center'
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

ax.set_title("Staff Average Sales per Shift", fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

top_day_sales="""sales_by_date = df.groupby(['Date'])['total'].sum().reset_index()
top_10_sales_by_date = sales_by_date.sort_values(by='total', ascending=False).head(10)
top_10_sales_by_date.columns = ['Date','Total Sales']
top_10_sales_by_date['Total Sales'] = top_10_sales_by_date['Total Sales'].apply(lambda x: f'${x:,.2f}')
top_10_sales_by_date['Date'] = top_10_sales_by_date['Date'].dt.strftime('%d/%m/%Y')

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=top_10_sales_by_date.values, 
    colLabels=top_10_sales_by_date.columns, 
    cellLoc='center'
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

ax.set_title("Top 10 Best Day Sales", fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

employee_sales_pie_chart = """def format_autopct(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f"${absolute} ({pct:.1f}%)"

fig, ax = plt.subplots(figsize=(9,9))
total_sales_per_employee = df[~pd.isna(df['total'])]
total_sales_per_employee_grouped = total_sales_per_employee.groupby(#STAFF#)['total'].sum().reset_index()
ax.pie(total_sales_per_employee_grouped['total'], labels=total_sales_per_employee_grouped[#STAFF#], autopct=lambda pct: format_autopct(pct, total_sales_per_employee_grouped['total']), textprops={'fontproperties': manjari_bold})
ax.set_title('Distribution of Sales per Employee', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.tight_layout()
plt.show(block=False)"""

boxplot_per_employee="""grouped_by_day = df.groupby([#STAFF#,'Date'])['total'].sum().reset_index()
staff_names = grouped_by_day[#STAFF#].unique()
grouped_by_staff = [grouped_by_day[grouped_by_day[#STAFF#] == staff]['total'].values for staff in staff_names]
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

plt.tight_layout()
plt.show(block=False)"""

daily_statistics="""daily_statistics = df.groupby('Date')['total'].sum().reset_index()
daily_statistics_agg = daily_statistics['total'].agg(['mean','median','std','max','min']).round(2).reset_index()
daily_statistics_agg.columns = ['Measurement','Value']
daily_statistics_agg['Measurement']=daily_statistics_agg['Measurement'].str.title()

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=daily_statistics_agg.values, 
    colLabels=daily_statistics_agg.columns, 
    cellLoc='center'
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

ax.set_title("Overview of Daily Sales", fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

moving_avg_week = """total_sales_per_day = df.groupby('Date')['total'].sum().reset_index()
total_sales_per_day.set_index('Date', inplace=True)
total_sales_per_day['Weekly Moving Average'] = total_sales_per_day['total'].rolling(window=7).mean()
total_sales_per_day.columns=['Total Sales ($)', 'Weekly Moving Average ($)']

fig, ax = plt.subplots()
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
plt.show(block=False)"""

tally_days_less_than_50="""total_sales_per_day = df.groupby('Date')['total'].sum().reset_index()
low_sales = total_sales_per_day[total_sales_per_day['total']<50]
low_sales['Day'] = pd.to_datetime(low_sales['Date']).dt.day_name()
low_sales_grouped = low_sales.groupby('Day')['Date'].nunique().reset_index()
low_sales_grouped.columns=['Day','Tally']

fig, ax = plt.subplots(figsize=(8, 1))
ax.axis('off')
ax.axis('tight')
table = ax.table(
    cellText=low_sales_grouped.values, 
    colLabels=low_sales_grouped.columns, 
    cellLoc='center'
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

ax.set_title("Tally of Days with less than $50 in sales", fontsize=20, weight='bold', font_properties=manjari_bold)
plt.tight_layout()
plt.show(block=False)"""

area_chart_albums_sold_over_time="""album_sales = df[~df['type'].isin(['Unknown','Photo'])]
total_album_sales = album_sales.groupby(['Date','type'])[#QUANTITY#].sum().reset_index()
pivot_df = total_album_sales.pivot(index='Date', columns='type', values=#QUANTITY#).fillna(0)
x = pivot_df.index  
y = pivot_df.values.T 
fig, ax = plt.subplots()
ax.stackplot(x, y, labels=pivot_df.columns, alpha=0.8)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Albums Sold', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
for tick in ax.get_xticklabels():
    tick.set_ha('right')
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Sales over Time', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
ax.set_xlim(df['Date'].min()-pd.Timedelta(days=3),df['Date'].max()+pd.Timedelta(days=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
ax.legend(loc='center right',bbox_to_anchor=(1.35, 0.5))
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show(block=False)
"""

quantity_albums_over_time="""album_sales = df[~df['type'].isin(['Unknown','Photo'])]
total_album_sales = album_sales.groupby(['Date'])[#QUANTITY#].sum().reset_index()
total_album_sales['Date']=pd.to_datetime(total_album_sales['Date'])
fig, ax = plt.subplots()
ax.bar(total_album_sales['Date'], total_album_sales[#QUANTITY#], color=medium)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Albums Sold', color=dark, font_properties=manjari_bold)
ax.tick_params(axis='x', labelrotation=45)
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
plt.show(block=False)"""

copies_over_time="""copy_sales = df[(df['type']=='Copy/Print')]
total_copy_sales = copy_sales.groupby(['Date'])[#QUANTITY#].sum().reset_index()
total_copy_sales['Date']=pd.to_datetime(total_copy_sales['Date'])
fig, ax = plt.subplots()
ax.bar(total_copy_sales['Date'], total_copy_sales[#QUANTITY#], color=medium)
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
plt.show()"""

copies_july="""copy_sales = df[(df['type']=='Copy/Print')]
total_copy_sales = copy_sales.groupby(['Date'])[#QUANTITY#].sum().reset_index()
total_copy_sales['Date']=pd.to_datetime(total_copy_sales['Date'])
fig, ax = plt.subplots()
ax.bar(total_copy_sales['Date'], total_copy_sales[#QUANTITY#], color=medium)
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
plt.show()"""

correlation_between_album_photo = """photos_df = df[df['type'].isin(['Photo','Copy/Print'])]
albums_df = df[~df['type'].isin(['Photo','Copy/Print','Unknown'])]
photo_sales = photos_df.groupby('Date')['total'].sum().reset_index(name='photo_sales')
album_sales = albums_df.groupby('Date')['total'].sum().reset_index(name='album_sales')
merged_sales = pd.merge(photo_sales, album_sales, on='Date', how='inner')

fig, ax = plt.subplots()
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
plt.show()"""

correlation_between_copy_photo="""photos_df = df[df['type']=='Photo']
copy_df = df[df['type']=='Copy/Print']
photo_sales = photos_df.groupby('Date')['total'].sum().reset_index(name='photo_sales')
copy_df = copy_df.groupby('Date')['total'].sum().reset_index(name='copy_sales')
merged_sales = pd.merge(photo_sales, copy_df, on='Date', how='inner')

fig, ax = plt.subplots()
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
plt.show()"""

total_sales_per_day_of_week_barh = """df['Day'] = df[#ACTION#].dt.day_name()
total_sales_per_day = df.groupby('Day')['total'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)
total_sales_per_day.columns = ['Day of Week', 'Total Sales ($)']
fig, ax = plt.subplots()
total_sales_per_day.plot(kind='barh', color=medium, ax=ax)
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
plt.show(block=False)"""

staff_copy =  """copy_sales = df[df['type']=='Copy/Print']
copy_sales_per_staff = copy_sales.groupby(#STAFF#)['total'].sum().reset_index()
copy_sales_per_staff.columns = ['Staff', 'Total Sales ($)']
fig, ax = plt.subplots()
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
plt.show(block=False)"""

#total revenue generated per album

total_revenue_generated_per_album = """album_sales = df[~df['type'].isin(['Photo','Copy/Print'])]
album_sales_summary = copy_sales.groupby(#STAFF#)['total'].sum().reset_index()
copy_sales_per_staff.columns = ['Staff', 'Total Sales ($)']
fig, ax = plt.subplots()
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
plt.show(block=False)"""

#average sales per transaction

#average quantity per transaction

#which product had highest total revenue

#average transaction value per staff

#number of times each album sold

#top 5 albumns sold

#bottom 5 albumns sold










base_data = [
{
    "instruction": "show me machine sales over time",
    "input": '',
    "output": machine_over_time
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
    "instruction": "give me machine sales over time for july?",
    "input": '',
    "output": machine_over_time_july
},
{
    "instruction": "Can I have machine sales over time for august?",
    "input": '',
    "output": machine_over_time_august
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

}


]

#SCRAMBLE

print(len(base_data))

new_code_list = []

for i,_ in enumerate(base_data):
    random.seed(120)
    index_arr = [random.randint(0,len(code_scrambler.df_columns_list)) for _ in range(5)]
    for index in index_arr:
        filename = code_scrambler.df_columns_list[index]['filename']
        output= base_data[i]['output'].replace('#STAFF#',code_scrambler.df_columns_list[index]['staff'])
        output = output.replace('#REPLACED#',code_scrambler.df_columns_list[index]['replaced'])
        output = output.replace('#ACTION#',code_scrambler.df_columns_list[index]['action'])
        output = output.replace('#QUANTITY#',code_scrambler.df_columns_list[index]['quantity'])

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

# breakpoint()

with open('Training/final_file.json', 'w') as json_file:
   
    json.dump(new_code_list, json_file, indent=4) 

