import json

machine_over_time = """
sales_data = df.groupby('Date')['total'].sum().reset_index()
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
plt.show()
"""

machine_over_time_july = """
sales_data = df[(df['action_time']>='2024-07-01') & (df['action_time']<='2024-07-31')].groupby('Date')['total'].sum().reset_index()
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
plt.show()
"""

machine_over_time_august = """
sales_data = df[(df['action_time']>='2024-08-01') & (df['action_time']<='2024-08-31')].groupby('Date')['total'].sum().reset_index()
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
plt.show()
"""

by_people = """
staff_data = df.groupby('staff')['total'].sum().reset_index()
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
plt.show()
"""

table_albums_month = """
albumn_data = df[(df['type']=='Physical') & (df['product'])]
albumn_data['action_time'] = pd.to_datetime(df['action_time'], errors='coerce')
monthly_sales = albumn_data.groupby(pd.Grouper(key='action_time', freq='M'))['quantity'].sum().reset_index()
monthly_sales.columns = ['Month','Total Albums']
monthly_sales
"""

dataa = [
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
}


]


with open('ProcessedData/data.json', 'w') as json_file:
    json.dump(dataa, json_file, indent=4) 
