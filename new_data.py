import json
import pandas as pd

machine_over_time = """sales_data = df.groupby('Date')['total'].sum().reset_index()
fig, ax = plt.subplots()
ax.plot(sales_data['Date'], sales_data['total'], color=dark, linewidth=2)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
plt.xticks(rotation=90)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Machine Sales Over Time', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show()"""

machine_over_time_july = """sales_data = df[(df['action_time']>='2024-07-01') & (df['action_time']<='2024-07-31')].groupby('Date')['total'].sum().reset_index()
fig, ax = plt.subplots()
ax.plot(sales_data['Date'], sales_data['total'], color=dark, linewidth=2)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
plt.xticks(rotation=90)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Machine Sales Over Time', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show()"""

machine_over_time_august = """sales_data = df[(df['action_time']>='2024-08-01') & (df['action_time']<='2024-08-31')].groupby('Date')['total'].sum().reset_index()
fig, ax = plt.subplots()
ax.plot(sales_data['Date'], sales_data['total'], color=dark, linewidth=2)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
plt.xticks(rotation=90)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.set_title('Machine Sales Over Time', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show()"""

by_people = """staff_data = df.groupby('staff')['total'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(staff_data['staff'], staff_data['total'], color=medium, linewidth=2)
ax.set_xlabel('Staff', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
plt.xticks(rotation=90)
ax.set_title('Machine Sales per Employee', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show()"""

table_albums_month = """albumn_data = df[~df['type'].isin(['Photo','Unknown'])]
albumn_data['action_time'] = pd.to_datetime(df['action_time'], errors='coerce')
monthly_sales = albumn_data.groupby(pd.Grouper(key='action_time', freq='M'))['quantity'].sum().reset_index()
monthly_sales.columns = ['Month','Total Albums']

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
plt.show()"""

replacement_count = """staff_replacement_days = df.groupby('replaced')['Date'].nunique().reset_index(name='Days')
staff_replacement_days = staff_replacement_days.dropna()
all_staff = df['staff'].unique()
all_staff_df = pd.DataFrame(all_staff, columns=['staff'])
staff_replacement_days_complete = all_staff_df.merge(staff_replacement_days, left_on='staff', right_on='replaced', how='left')
staff_replacement_days_complete['Days'] = staff_replacement_days_complete['Days'].fillna(0)
staff_replacement_days_complete = staff_replacement_days_complete.drop(columns=['replaced'])
staff_replacement_days_complete = staff_replacement_days_complete.sort_values(by='Days', ascending=False)

fig, ax = plt.subplots()
ax.bar(staff_replacement_days_complete['staff'], staff_replacement_days_complete['Days'], color=medium)
ax.set_xlabel('Staff', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Days', color=dark, font_properties=manjari_bold)
plt.xticks(rotation=45)
ax.set_title('Count of Shifts that Needed Replacing', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show()"""

replacement_count_table = """staff_replacement_days = df.groupby('replaced')['Date'].nunique().reset_index(name='Days')
staff_replacement_days = staff_replacement_days.dropna()
all_staff = df['staff'].unique()
all_staff_df = pd.DataFrame(all_staff, columns=['staff'])
staff_replacement_days_complete = all_staff_df.merge(staff_replacement_days, left_on='staff', right_on='replaced', how='left')
staff_replacement_days_complete['Days'] = staff_replacement_days_complete['Days'].fillna(0)
staff_replacement_days_complete = staff_replacement_days_complete.drop(columns=['replaced'])
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
plt.show()"""

album_distribution_sales = """fig, ax = plt.subplots()
physical_sales_df = df[(~df['type'].isin(['Photo','Unknown'])) & (~pd.isna(df['total'])]
physical_sales_per_product = physical_sales_df.groupby('type')['total'].sum().reset_index()
plt.figure(figsize=(12,12))
ax.pie(physical_sales_per_product['total'], labels=physical_sales_per_product['type'], autopct='%1.1f%%', textprops={'fontproperties': manjari_bold})
ax.set_title('Distribution of Album Sales', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.tight_layout()
plt.show()"""

album_distribution_sales_actual = """def format_autopct(pct, allvalues):
    absolute = int(pct / 100. * sum(allvalues))
    return f"{absolute} ({pct:.1f}%)"

fig, ax = plt.subplots()
physical_sales_df = df[(~df['type'].isin(['Photo','Unknown'])) & (~pd.isna(df['total'])]
physical_sales_per_product = physical_sales_df.groupby('type')['total'].sum().reset_index()
plt.figure(figsize=(12,12))
ax.pie(physical_sales_per_product['total'], labels=physical_sales_per_product['type'], autopct=lambda pct: format_autopct(pct, physical_sales_per_product['total']), textprops={'fontproperties': manjari_bold})
ax.set_title('Distribution of Album Sales', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.tight_layout()
plt.show()"""

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
plt.show()"""

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
plt.show()"""

total_sales_per_day_of_week = """df['Day'] = df['action_time'].dt.day_name()
total_sales_per_day = df.groupby('Day')['total'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
).reset_index()
total_sales_per_day.columns = ['Day of Week', 'Total Sales']

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
plt.show()"""

total_sales_per_day_of_week_bar = """df['Day'] = df['action_time'].dt.day_name()
total_sales_per_day = df.groupby('Day')['total'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)
total_sales_per_day.columns = ['Day of Week', 'Total Sales']
fig, ax = plt.subplots()
total_sales_per_day.plot(kind='bar', color=medium, ax=ax)
ax.set_xlabel('Day of Week', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
plt.xticks(rotation=90)
ax.set_title('Total Sales by Day of Week', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show()"""

avg_sales_by_day_of_week = """df_grouped = df.groupby('Date')['total'].sum().reset_index()
df_grouped['Day'] = pd.to_datetime(df_grouped['Date']).dt.day_name()
avg_sales_per_day = df_grouped.groupby('Day')['total'].mean().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)
avg_sales_per_day.columns = ['Day of Week', 'Total Sales']
fig, ax = plt.subplots()
avg_sales_per_day.plot(kind='bar', color=medium, ax=ax)
ax.set_xlabel('Day of Week', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Total Sales', color=dark, font_properties=manjari_bold)
plt.xticks(rotation=90)
ax.set_title('Average Sales by Day of Week', color=dark, font_properties=manjari_bold)
ax.tick_params(colors=dark)
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontproperties(manjari_regular)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.show()"""

bts_sales = """filtered_df = df[df['type']=='BTS']
count_sales = filtered_df.groupby('quantity').sum().reset_index()
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
plt.show()"""

album_photo_sales = """fig, ax = plt.subplots()
album_photo_comparison = df[(df['type'] != 'Unknown') & (~pd.isna(df['total']))]
album_photo_comparison['Album/Photo'] = album_photo_comparison['type'].apply(lambda x: 'Photo' if x == 'Photo' else 'Album')
album_photo_comparison_grouped = album_photo_comparison.groupby('Album/Photo')['total'].sum().reset_index()
plt.figure(figsize=(12,12))
ax.pie(album_photo_comparison_grouped['total'], labels=album_photo_comparison_grouped['Album/Photo'], autopct='%1.1f%%', textprops={'fontproperties': manjari_bold})
ax.set_title('Album and Photo Sales Comparison', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.tight_layout()
plt.show()"""

data = [
{
    "instruction": "show me machine sales over time",
    "output": machine_over_time
},
{
    "instruction": "give me sales results based off employee as a bar graph",
    "output": by_people
},
{
    "instruction": "give me a table of total albumns sold per month",
    "output": table_albums_month
},
{
    "instruction": "give me machine sales over time for july?",
    "output": machine_over_time_july
},
{
    "instruction": "Can I have machine sales over time for august?",
    "output": machine_over_time_august
},
{
    "instruction": "Hi, can you show me in a table the number of times employees needed to be replaced on a shift",
    "output": replacement_count_table
},
{
    "instruction": "Show how many employees needed to be replaced on a shift",
    "output": replacement_count
},
{
    "instruction": "give distribution of album sales",
    "output": album_distribution_sales
},
{
    "instruction": "Generate the distribution of album sales as a pie graph with actual numbers",
    "output": album_distribution_sales_actual
},
{
    "instruction": "Can you sum up the sales on both machines",
    "output": machine_sales
},
{
    "instruction": "How many times has each machine been used?",
    "output": machine_count
},
{
    "instruction": "total sales per day of week",
    "output": total_sales_per_day_of_week
},
{
    "instruction": "give me the total sales per day of week as a barchart",
    "output": total_sales_per_day_of_week_bar
},
{
    "instruction": "avg sales per day of week",
    "output": avg_sales_by_day_of_week
},
{
    "instruction": "how many BTS albums have we sold so far?",
    "output": bts_sales
},
{
    "instruction": "album sales vs photo sales?",
    "output": album_photo_sales
},


]


with open('Training/manual_add.json', 'w') as json_file:
    json.dump(data, json_file, indent=4) 
