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


# base_data_old = [

# {
#     "instruction": "give me a table of total albumns sold per month",
#     "input": '',
#     "output": table_albums_month
# },
# {
#     "instruction": "give me total sales over time for july?",
#     "input": '',
#     "output": total_over_time_july
# },
# {
#     "instruction": "Can I have total sales over time for august?",
#     "input": '',
#     "output": total_over_time_august
# },
# {
#     "instruction": "Hi, can you show me in a table the number of times employees needed to be replaced on a shift",
#     "input": '',
#     "output": replacement_count_table
# },
# {
#     "instruction": "Show how many employees needed to be replaced on a shift",
#     "input": '',
#     "output": replacement_count
# },
# {
#     "instruction": "give distribution of album sales",
#     "input": '',
#     "output": album_distribution_sales
# },
# {
#     "instruction": "Generate the distribution of album sales as a pie graph with actual numbers",
#     "input": '',
#     "output": album_distribution_sales_actual
# },
# {
#     "instruction": "Can you sum up the sales on both machines",
#     "input": '',
#     "output": machine_sales
# },
# {
#     "instruction": "How many times has each machine been used?",
#     "input": '',
#     "output": machine_count
# },
# {
#     "instruction": "total sales per day of week",
#     "input": '',
#     "output": total_sales_per_day_of_week
# },
# {
#     "instruction": "give me the total sales per day of week as a barchart",
#     "input": '',
#     "output": total_sales_per_day_of_week_bar
# },
# {
#     "instruction": "avg sales per day of week",
#     "input": '',
#     "output": avg_sales_by_day_of_week
# },
# {
#     "instruction": "how many BTS albums have we sold so far?",
#     "input": '',
#     "output": bts_sales
# },
# {
#     "instruction": "album sales vs photo sales?",
#     "input": '',
#     "output": album_photo_sales
# },
# {
#     "instruction": "how many album sales did Karmel have?",
#     "input": '',
#     "output": karmel_sales
# },
# {
#     "instruction": "total of photobooth sales on Jess' shifts?",
#     "input": '',
#     "output": jess_total_sales
# },
# {
#     "instruction": "total sales per month blue vs purple machine",
#     "input": '',
#     "output": machine_by_month_comparison
# },
# {
#     "instruction": "album sales over time",
#     "input": '',
#     "output": album_sales
# },
# {
#     "instruction": "can you count how many shifts each staff have been on",
#     "input": '',
#     "output": shift_count_per_staff
# },
# {
#     "instruction": "can you give me the average sales per shift per staff",
#     "input": '',
#     "output": average_sales_per_shift
# },
# {
#     "instruction": "What is the average sales each employee gets",
#     "input": '',
#     "output": average_sales_per_shift_table
# },
# {
#     "instruction": "Hi! What are our best selling days?",
#     "input": '',
#     "output": top_day_sales
# },
# {
#     "instruction": "pie chart of total sales per employee",
#     "input": '',
#     "output": employee_sales_pie_chart
# },
# {
#     "instruction": "Generate a visual showing a boxplot each employee sale",
#     "input": '',
#     "output": boxplot_per_employee
# },
# {
#     "instruction": "Give me a rundown of daily sales statistics",
#     "input": '',
#     "output": daily_statistics
# },
# {
#     "instruction": "get me the moving average of sales per week",
#     "input": '',
#     "output": moving_avg_week
# },
# {
#     "instruction": "tally the days with less than $50 in sales",
#     "input": '',
#     "output": tally_days_less_than_50
# },
# {
#     "instruction": "area chart of albums sold over time",
#     "input": '',
#     "output": area_chart_albums_sold_over_time
# },
# {
#     "instruction": "make me a plot of albums sold over time",
#     "input": '',
#     "output": quantity_albums_over_time
# },
# {
#     "instruction": "how many copies of photos were printed over time?",
#     "input": '',
#     "output":  copies_over_time
# },
# {
#     "instruction": "Can you produce a bar graph which shows number of copies printed in July",
#     "input": '',
#     "output":  copies_july
# },
# {
#     "instruction": "Can you show me the correlation between album sales and photo sales",
#     "input": '',
#     "output":  correlation_between_album_photo
# },
# {
#     "instruction": "Are sales of copies related to sales of photos",
#     "input": '',
#     "output":  correlation_between_copy_photo
# },
# {
#     "instruction": "can you give me a horizontal bar chart of the count of sales per day?",
#     "input": '',
#     "output":  total_sales_per_day_of_week_barh

# },
# {
#     "instruction": "can you summarise the number of sales per hour?",
#     "input": '',
#     "output":  peak_hours_quantity

# },
# {
#     "instruction": "Tell me the total sales per hour?",
#     "input": '',
#     "output":  peak_hours_total

# },
# {
#     "instruction": "How many transactions have been $0",
#     "input": '',
#     "output":  total_0_sale_transactions_over_time

# },
# {
#     "instruction": "Do customers only buy photos, or do they buy copies too?",
#     "input": '',
#     "output":  photo_vs_copy

# },
# {
#     "instruction": "inform me which staff sells more copies",
#     "input": '',
#     "output":  staff_copy

# },
# {
#     "instruction": "tell me in table the total sales on weekends vs weekdays",
#     "input": '',
#     "output":  weekend_vs_weekday_table

# },
# {
#     "instruction": "tell me the total sales on weekends vs weekdays",
#     "input": '',
#     "output":  weekend_vs_weekday

# },
# {
#     "instruction": "what is the revenue of each unique album",
#     "input": '',
#     "output":  total_revenue_generated_per_album

# },
# {
#     "instruction": "what is the average sale per transactions",
#     "input": '',
#     "output":  average_sale_per_transaction

# },
# {
#     "instruction": "what is the average quantity per transaction",
#     "input": '',
#     "output":  average_quantity_per_transaction

# },
# {
#     "instruction": "which items in store sold the most",
#     "input": '',
#     "output":  product_highest_revenue

# },
# {
#     "instruction": "what is the average revenue per transaction per staff?",
#     "input": '',
#     "output":  average_transaction_value_per_staff

# },
# {
#     "instruction": "count of album sales?",
#     "input": '',
#     "output":  album_quantity_sales

# },
# {
#     "instruction": "top 5 albums sold",
#     "input": '',
#     "output":  top_5_albums_sold

# },
# {
#     "instruction": "bottom 5 albums sold",
#     "input": '',
#     "output":  bottom_5_albums

# },


# ]