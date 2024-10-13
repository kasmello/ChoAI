import json
import csv
import random
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

data_0_file = 'ProcessedData/Joined_DF_0.csv'
data_0_str = turn_df_into_input(data_0_file)

def scramble_matplotlib_code(code_string):
    # Split the code into lines
    code_lines = code_string.strip().split('\n')
    
    # Extract lines that contain certain matplotlib functions
    plot_commands = [line for line in code_lines if "plt.plot" in line]
    label_commands = [line for line in code_lines if any(func in line for func in ["plt.title", "plt.xlabel", "plt.ylabel", 'ax.set_title','ax.set_xlabel','ax.set_ylabel'])]
    grid_or_legend_commands = [line for line in code_lines if "plt.grid" in line or "plt.legend" in line]
    
    # Shuffle the order of these components
    random.shuffle(plot_commands)
    random.shuffle(label_commands)
    random.shuffle(grid_or_legend_commands)
    
    # Combine the scrambled parts back into the code
    scrambled_code = "\n".join(plot_commands + label_commands + grid_or_legend_commands)
    
    # Add plt.show() if it is not in the original code
    if "plt.show()" not in code_string:
        scrambled_code += "\nplt.show()"
    
    return scrambled_code

# def replace_database


#things to modulate:
#colour
#date
#title
#axis
#coding format

#steps:
#provide base format
#replace date, colour, title, axis with tags #DATE#, #COLOUR#, #TITLE#, #AXIS#
#replace appropriate columns with tags 
#scramble code after tags replaced
#change coding format



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

machine_over_time_july = """sales_data = df[(df['action_time']>='2024-07-01') & (df['action_time']<='2024-07-31')].groupby('Date')['total'].sum().reset_index()
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
plt.show(block=False))"""

machine_over_time_august = """sales_data = df[(df['action_time']>='2024-08-01') & (df['action_time']<='2024-08-31')].groupby('Date')['total'].sum().reset_index()
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

by_people = """staff_data = df.groupby('staff')['total'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(staff_data['staff'], staff_data['total'], color=medium)
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

table_albums_month = """albumn_data = df[~df['type'].isin(['Photo','Unknown'])]
monthly_sales = albumn_data.groupby(pd.Grouper(key='action_time', freq='M'))['quantity'].sum().reset_index()
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

total_sales_per_day_of_week = """df['Day'] = df['action_time'].dt.day_name()
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

total_sales_per_day_of_week_bar = """df['Day'] = df['action_time'].dt.day_name()
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

karmel_sales = """filtered_df = df[(df['staff']=='Karmel') & ~df['type'].isin(['Photo','Unknown'])]
count_sales = filtered_df.groupby('staff')['quantity'].sum().reset_index()
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

jess_total_sales="""filtered_df = df[(df['staff']=='Jess') & df['type'].isin(['Photo'])]
count_sales = filtered_df.groupby('staff')['total'].sum().reset_index()
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

shift_count_per_staff="""staff_shift_count = df.groupby('staff')['Date'].nunique().reset_index()
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

average_sales_per_shift="""total_per_employee_day = df.groupby(['staff','Date'])['total'].sum().reset_index()
avg_per_employee = total_per_employee_day.groupby(['staff'])['total'].mean().reset_index()
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

average_sales_per_shift_table="""total_per_employee_day = df.groupby(['staff','Date'])['total'].sum().reset_index()
avg_per_employee = total_per_employee_day.groupby(['staff'])['total'].mean().round(2).reset_index()
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
total_sales_per_employee_grouped = total_sales_per_employee.groupby('staff')['total'].sum().reset_index()
ax.pie(total_sales_per_employee_grouped['total'], labels=total_sales_per_employee_grouped['staff'], autopct=lambda pct: format_autopct(pct, total_sales_per_employee_grouped['total']), textprops={'fontproperties': manjari_bold})
ax.set_title('Distribution of Sales per Employee', color=dark, font_properties=manjari_bold)
logo_ax = fig.add_axes([0.8, 0.85, 0.15, 0.15], anchor='NE', zorder=1)
logo_ax.imshow(logo_img)
logo_ax.axis('off') 
plt.tight_layout()
plt.show(block=False)"""

boxplot_per_employee="""grouped_by_day = df.groupby(['staff','Date'])['total'].sum().reset_index()
staff_names = grouped_by_day['staff'].unique()
grouped_by_staff = [grouped_by_day[grouped_by_day['staff'] == staff]['total'].values for staff in staff_names]
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
total_album_sales = album_sales.groupby(['Date','type'])['quantity'].sum().reset_index()
pivot_df = total_album_sales.pivot(index='Date', columns='type', values='quantity').fillna(0)
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
total_album_sales = album_sales.groupby(['Date'])['quantity'].sum().reset_index()
total_album_sales['Date']=pd.to_datetime(total_album_sales['Date'])
fig, ax = plt.subplots()
ax.bar(total_album_sales['Date'], total_album_sales['quantity'], color=medium)
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
total_copy_sales = copy_sales.groupby(['Date'])['quantity'].sum().reset_index()
total_copy_sales['Date']=pd.to_datetime(total_copy_sales['Date'])
fig, ax = plt.subplots()
ax.bar(total_copy_sales['Date'], total_copy_sales['quantity'], color=medium)
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

copies_july="""#how many copies were printed over july

copy_sales = df[(df['type']=='Copy/Print')]
total_copy_sales = copy_sales.groupby(['Date'])['quantity'].sum().reset_index()
total_copy_sales['Date']=pd.to_datetime(total_copy_sales['Date'])
fig, ax = plt.subplots()
ax.bar(total_copy_sales['Date'], total_copy_sales['quantity'], color=medium)
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

total_sales_per_day_of_week_barh = """df['Day'] = df['action_time'].dt.day_name()
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









data_1 = [
{
    "instruction": "show me machine sales over time",
    "input": data_0_str,
    "output": machine_over_time
},
{
    "instruction": "give me sales results based off employee as a bar graph",
    "input": data_0_str,
    "output": by_people
},
{
    "instruction": "give me a table of total albumns sold per month",
    "input": data_0_str,
    "output": table_albums_month
},
{
    "instruction": "give me machine sales over time for july?",
    "input": data_0_str,
    "output": machine_over_time_july
},
{
    "instruction": "Can I have machine sales over time for august?",
    "input": data_0_str,
    "output": machine_over_time_august
},
{
    "instruction": "Hi, can you show me in a table the number of times employees needed to be replaced on a shift",
    "input": data_0_str,
    "output": replacement_count_table
},
{
    "instruction": "Show how many employees needed to be replaced on a shift",
    "input": data_0_str,
    "output": replacement_count
},
{
    "instruction": "give distribution of album sales",
    "input": data_0_str,
    "output": album_distribution_sales
},
{
    "instruction": "Generate the distribution of album sales as a pie graph with actual numbers",
    "input": data_0_str,
    "output": album_distribution_sales_actual
},
{
    "instruction": "Can you sum up the sales on both machines",
    "input": data_0_str,
    "output": machine_sales
},
{
    "instruction": "How many times has each machine been used?",
    "input": data_0_str,
    "output": machine_count
},
{
    "instruction": "total sales per day of week",
    "input": data_0_str,
    "output": total_sales_per_day_of_week
},
{
    "instruction": "give me the total sales per day of week as a barchart",
    "input": data_0_str,
    "output": total_sales_per_day_of_week_bar
},
{
    "instruction": "avg sales per day of week",
    "input": data_0_str,
    "output": avg_sales_by_day_of_week
},
{
    "instruction": "how many BTS albums have we sold so far?",
    "input": data_0_str,
    "output": bts_sales
},
{
    "instruction": "album sales vs photo sales?",
    "input": data_0_str,
    "output": album_photo_sales
},
{
    "instruction": "how many album sales did Karmel have?",
    "input": data_0_str,
    "output": karmel_sales
},
{
    "instruction": "total of photobooth sales on Jess' shifts?",
    "input": data_0_str,
    "output": jess_total_sales
},
{
    "instruction": "total sales per month blue vs purple machine",
    "input": data_0_str,
    "output": machine_by_month_comparison
},
{
    "instruction": "album sales over time",
    "input": data_0_str,
    "output": album_sales
},
{
    "instruction": "can you count how many shifts each staff have been on",
    "input": data_0_str,
    "output": shift_count_per_staff
},
{
    "instruction": "can you give me the average sales per shift per staff",
    "input": data_0_str,
    "output": average_sales_per_shift
},
{
    "instruction": "What is the average sales each employee gets",
    "input": data_0_str,
    "output": average_sales_per_shift_table
},
{
    "instruction": "Hi! What are our best selling days?",
    "input": data_0_str,
    "output": top_day_sales
},
{
    "instruction": "pie chart of total sales per employee",
    "input": data_0_str,
    "output": employee_sales_pie_chart
},
{
    "instruction": "Generate a visual showing a boxplot each employee sale",
    "input": data_0_str,
    "output": boxplot_per_employee
},
{
    "instruction": "Give me a rundown of daily sales statistics",
    "input": data_0_str,
    "output": daily_statistics
},
{
    "instruction": "get me the moving average of sales per week",
    "input": data_0_str,
    "output": moving_avg_week
},
{
    "instruction": "tally the days with less than $50 in sales",
    "input": data_0_str,
    "output": tally_days_less_than_50
},
{
    "instruction": "area chart of albums sold over time",
    "input": data_0_str,
    "output": area_chart_albums_sold_over_time
},
{
    "instruction": "make me a plot of albums sold over time",
    "input": data_0_str,
    "output": quantity_albums_over_time
},
{
    "instruction": "how many copies of photos were printed over time?",
    "input": data_0_str,
    "output":  copies_over_time
},
{
    "instruction": "Can you produce a bar graph which shows number of copies printed in July",
    "input": data_0_str,
    "output":  copies_july
},
{
    "instruction": "Can you show me the correlation between album sales and photo sales",
    "input": data_0_str,
    "output":  correlation_between_album_photo
},
{
    "instruction": "Are sales of copies related to sales of photos",
    "input": data_0_str,
    "output":  correlation_between_copy_photo
},
{
    "instruction": "can you give me a horizontal bar chart of the count of sales per day?",
    "input": data_0_str,
    "output":  total_sales_per_day_of_week_barh
}






]


with open('Training/manual_add.json', 'w') as json_file:
   
    json.dump(data_1, json_file, indent=4) 

