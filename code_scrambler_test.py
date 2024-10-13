import code_scrambler
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
import numpy as np

df = pd.read_csv('processeddata/joined_df_0.csv')
df['action_time'] = pd.to_datetime(df['action_time'])
df['Date']=pd.to_datetime(df['Date'])

manjari_bold_path = 'font/Manjari-Bold.ttf'
manjari_regular_path = 'font/Manjari-Regular.ttf'
manjari_thin_path = 'font/Manjari-thin.ttf'

dark = "#3B3365"
medium = "#8F81DD"
light = "#BCADFF"
peach = "#FFEEDD"
blue = "#A7C7E7"
pink = "#FFB7C5"
green = "#B0E57C"
yellow = "#FFF2B2"
orange = "#FFD1BA"
mint = "#B5EAD7"
aqua = "#A1EAFB"


logo_img = mpimg.imread('Media/horizontal-logo.png')

# Load the custom font
manjari_bold = fm.FontProperties(fname=manjari_bold_path)
manjari_regular = fm.FontProperties(fname=manjari_regular_path)
manjari_thin = fm.FontProperties(fname=manjari_thin_path)

album_success = 0
album_total = 0

test_ax_code = """copy_sales = df[(df['type']=='Copy/Print')]
total_copy_sales = copy_sales.groupby(['Date'])['quantity'].sum().reset_index()
total_copy_sales['Date']=pd.to_datetime(total_copy_sales['Date'])
fig, ax = plt.subplots()
ax.bar(total_copy_sales['Date'], total_copy_sales['quantity'], color=medium)
ax.set_xlabel('Date', color=dark, font_properties=manjari_bold)
ax.set_ylabel('Copies Printed', color=dark, font_properties=manjari_bold)
plt.xticks(rotation=45,ha='right')
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


scramble_total = 0
scramble_success = 0
print('=========================\nTESTING AX TO PLT\n=========================\n')
scramble_total += 1
try:
    new_code =  code_scrambler.rewrite_ast_to_plot(test_ax_code)
    print(test_ax_code)
    print(new_code)
    exec(new_code)
    print('Success')
    scramble_success += 1
except Exception as e:
    print(f'Fail{e}')





print(f'\nAPI Fetcher Result: {scramble_success}/{scramble_total}\n')



