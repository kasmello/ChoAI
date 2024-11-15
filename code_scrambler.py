import ast
import astor
import pandas as pd
import json
import random
import re
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.image as mpimg
from datetime import datetime

def load_df(path):
    df = pd.read_csv(path)
    df['action_time'] = pd.to_datetime(df['action_time'])
    df['Date']=pd.to_datetime(df['Date'])
    return df


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

with open('ProcessedData/df_column_desc.txt','r') as file:
    df_columns_list = json.load(file)


mat_plot_lib_all_plots = [
    'plot',             # Line plot
    'table',            # Table
    'scatter',          # Scatter plot
    'bar',              # Bar plot
    'barh',             # Horizontal bar plot
    'hist',             # Histogram
    'boxplot',          # Box plot
    'violinplot',       # Violin plot
    'pie',              # Pie chart
    'stem',             # Stem plot
    'step',             # Step plot
    'fill_between',     # Fill between plot
    'stackplot',        # Stack plot
    'errorbar',         # Error bar plot
    'quiver',           # Quiver plot
    'contour',          # Contour plot
    'contourf',         # Filled contour plot
    'imshow',           # Image plot
    'pcolor',           # Pseudocolor plot
    'pcolormesh',       # Pseudocolor mesh plot
    'hexbin',           # Hexbin plot
    'polar',            # Polar plot
    'loglog',           # Log-log scale plot
    'semilogx',         # Semilogarithmic plot (x-axis log scale)
    'semilogy',         # Semilogarithmic plot (y-axis log scale)
    'spy',              # Spy plot (sparse matrix plot)
    'spectrogram',      # Spectrogram plot
    'matshow',          # Matrix plot
    'tripcolor',        # Triangular pseudocolor plot
    'tricontour',       # Triangular contour plot
    'tricontourf',      # Filled triangular contour plot
    'plot_surface',     # Surface plot (3D)
    'plot_wireframe',   # Wireframe plot (3D)
    'plot_trisurf',     # Triangular surface plot (3D)
]

misc = [
    "axis"
]

#scramble Title

def scramble_title(title):
    return None
    # tokenizer = BartTokenizer.from_pretrained('facebook/bart-base')
    # model = BartModel.from_pretrained('facebook/bart-base')

    # inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")
    # outputs = model(**inputs)

    # last_hidden_states = outputs.last_hidden_state
    # print(outputs)
    # print(f"{title}", max_length=12))

    


# Define a class to rewrite 'ax' to 'plt'
class RewriteAxToPlt(ast.NodeTransformer):
    def visit_Attribute(self, node):
        # Replace ax.plot -> plt.plot, ax.set_xlabel -> plt.xlabel, etc.
        if isinstance(node.value, ast.Name) and node.value.id == 'ax':
            # For ax.plot(), we replace it with plt.plot()
            if node.attr in mat_plot_lib_all_plots or node.attr in misc:
                return ast.Attribute(value=ast.Name(id='plt', ctx=ast.Load()), attr=node.attr, ctx=ast.Load())
            # For ax.set_* functions, replace them with plt.*
            elif node.attr == 'xaxis':
                return ast.Attribute(
                    value=ast.Call(
                        func=ast.Attribute(value=ast.Name(id="plt", ctx=ast.Load()), attr="gca", ctx=ast.Load()),
                        args=[],
                        keywords=[]
                    ),
                    attr="xaxis",
                    ctx=ast.Load()
                )
            elif node.attr == "tick_params":
                return ast.Attribute(
                    value=ast.Call(
                        func=ast.Attribute(value=ast.Name(id="plt", ctx=ast.Load()), attr="gca", ctx=ast.Load()),
                        args=[],
                        keywords=[]
                    ),
                    attr="tick_params",
                    ctx=ast.Load()
                )
            elif node.attr =="get_xticklabels":
                return ast.Attribute(
                    value=ast.Call(
                        func=ast.Attribute(value=ast.Name(id="plt", ctx=ast.Load()), attr="gca", ctx=ast.Load()),
                        args=[],
                        keywords=[]
                    ),
                    attr="get_xticklabels",
                    ctx=ast.Load()
                )
            elif node.attr =="get_yticklabels":
                return ast.Attribute(
                    value=ast.Call(
                        func=ast.Attribute(value=ast.Name(id="plt", ctx=ast.Load()), attr="gca", ctx=ast.Load()),
                        args=[],
                        keywords=[]
                    ),
                    attr="get_yticklabels",
                    ctx=ast.Load()
                )
            elif node.attr.startswith('set_'):
                plt_func = node.attr.replace('set_', '')  # e.g., set_xlabel -> xlabel
                return ast.Attribute(value=ast.Name(id='plt', ctx=ast.Load()), attr=plt_func, ctx=ast.Load())
            
        # elif isinstance(node.value, ast.Name) and node.value.id == 'fig':
        #     if node.attr == 'add_axes':
        #         return ast.Attribute(
        #             value=ast.Call(
        #                 func=ast.Attribute(
        #                     value=ast.Name(id="plt", ctx=ast.Load()), attr="axes", ctx=ast.Load()
        #                 ),
        #                 args=node.args,         # Retain the original arguments (e.g., the position and size)
        #                 keywords=node.keywords
                        
        #             ),
        #             attr = [],
        #             ctx = ast.load()
        #         )
        return self.generic_visit(node)
    

code = """
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
ax.set_title('Title')
ax.set_xlabel('X-axis label')
ax.set_ylabel('Y-axis label')
plt.show()
"""

def rewrite_ast_to_plot(code):
#    Parse the code into an AST
    tree = ast.parse(code)

    # Apply the transformation
    converter = RewriteAxToPlt()
    transformed_tree = converter.visit(tree)

    # Convert the AST back to source code
    new_code = astor.to_source(transformed_tree)
    new_code = re.sub(r"fig, ax = ", "", new_code)
    new_code = new_code.replace('fig.add_axes','plt.axes')
    return new_code

def change_title_axes(code):
    None
    

def additional_code_rewrites(code):
    old_1 = """
    """




#scramble titles and axes label
new_file_name = 'Training/final_file.json'
if __name__=='__main__':
    with open('Training/manual_add.json', 'r') as json_file:
        data = json.load(json_file) 
        for e in range(0,len(data)):
            instruction = data[e]["instruction"]
            input_csv = data[e]["input"]
            output = data[e]["output"]
            try:
                
                print(f'\n===============================\n{instruction}\n===============================\n')
                new_output = rewrite_ast_to_plot(output)
                exec(new_output)
                # option = input('(Y)es if input matches graph, (N) if input does not match:\t')
                # while option.upper() not in ['Y','N']:
                #     print('Invalid option!')
                #     option = input('(Y)es if input matches graph, (N) if input does not match:\t')
                option = 'Y'
                
                exec("plt.close(fig)")
                if option.upper()=='Y':
                    data.append({
                        "instruction": instruction,
                        "input": input_csv,
                        "output": new_output
                    })

            except Exception as e:
                #fails to run - don't add!
                success=False
                print(f'{instruction} - Fail\n')
                print(e)

    with open(new_file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)


