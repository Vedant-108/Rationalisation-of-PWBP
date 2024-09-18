from tkinter import *
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import json
import os
import tkinter.messagebox

with open('../data.json', 'r') as json_file:
    loaded_dict = json.load(json_file)

my_dict3 = loaded_dict

# Get user inputs
D = float(my_dict3['D'])
Wg = float(my_dict3['Wg'])
Wp = float(my_dict3['Wp'])  # Corrected label here
Tr = float(my_dict3['Tr'])
Tp = float(my_dict3['Tp'])
Tf = float(my_dict3['Tf'])
H = float(my_dict3['H'])
Er = float(my_dict3['Er'])
Ec = float(my_dict3['Ec'])
Shir = float(my_dict3['Shir'])
Ship = float(my_dict3['Ship'])
Shif = float(my_dict3['Shif'])
Scr = float(my_dict3['Scr'])
Scp = float(my_dict3['Scp'])
Scf = float(my_dict3['Scf'])
Str = float(my_dict3['Str'])
Stp = float(my_dict3['Stp'])
Stf = float(my_dict3['Stf'])
Kr = float(my_dict3['Kr'])
Kp = float(my_dict3['Kp'])
Kf = float(my_dict3['Kf'])
Shic = float(my_dict3['Shic'])  # New parameter
Scc = float(my_dict3['Scc'])
Ef = float(my_dict3['Ef'])
Wc = float(my_dict3['Wc'])
Wsp = float(my_dict3['Wsp'])
Wr = float(my_dict3['Wr'])
Wh = float(my_dict3['Wh'])  # New parameter '''



''' Wg = float(my_dict['Gallery Width (Wg) [m]:'].get())
    Wp = float(entries['Pillar Width (Wp) [m]:'].get())  # Corrected label here
    Tr = float(entries['Influence Zone of Immediate Roof (Tr) [m]:'].get())
    Tp = float(entries['Height of the Coal Pillar (Tp) [m]:'].get())
    Tf = float(entries['Influence Zone of Immediate Floor (Tf) [m]:'].get())
    H = float(entries['Water Head (H) [m]:'].get())
    Ei = float(entries['Young’s Modulus of Roof/Floor (Ei) [GPa]:'].get())
    Ec = float(entries['Young’s Modulus of Coal (Ec) [GPa]:'].get())
    Shir = float(entries['Mean Horizontal Stress in Immediate Roof (Shir) [MPa]:'].get())
    Ship = float(entries['Mean Horizontal Stress in Pillar (Ship) [MPa]:'].get())
    Shif = float(entries['Mean Horizontal Stress in Immediate Floor (Shif) [MPa]:'].get())
    Scr = float(entries['Mean Compressive Strength of Immediate Roof (Scr) [MPa]:'].get())
    Scp = float(entries['Mean Compressive Strength of Pillar (Scp) [MPa]:'].get())
    Scf = float(entries['Mean Compressive Strength of Immediate Floor (Scf) [MPa]:'].get())
    Str = float(entries['Mean Tensile Strength of Immediate Roof (Str) [MPa]:'].get())
    Stp = float(entries['Mean Tensile Strength of Pillar (Stp) [MPa]:'].get())
    Stf = float(entries['Mean Tensile Strength of Immediate Floor (Stf) [MPa]:'].get())
    Kr = float(entries['Permeability of Immediate Roof (Kr) [mD]:'].get())
    Kp = float(entries['Permeability of Coal Pillar (Kp) [mD]:'].get())
    Kf = float(entries['Permeability of Immediate Floor (Kf) [mD]:'].get())
    Shic = float(entries['In situ Horizontal Stress in Coal (Shic) [MPa]:'].get())  # New parameter
    Scc = float(entries['Rock Mass Compressive Strength of Coal (Scc) [MPa]:'].get())  # New parameter'''

'''# Sample values
D = new_pwbp.D
Wg = 5
Wp = 10
Tp = 3
Tr = 6
Tf = 6
H = 350
Shir = 3.91
Shif = 3.98
Ship = 5.89
Scr = 4.01
Scf = 4.01
Scp = 2.04
Str = 0.39
Stf = 0.39
Stp = 0.04
Kr = 1000
Kf = 1000
Kp = 100
Shic = 5.89
Scc = 2.04
Ei = 3.01
Ec = 2
Wr = 5.0
Qrpf_atwr = 100
ZoPVS_atwsp = 50
Wc = 20
Wsp = 40 '''

list1 = [D, Wg, Wp, Tr, Tp, Tf, H, Er, Ec, Shir, Ship, Shir, Scr, Scp, Scf, Str, Stp,
         Stf, Kr, Kp, Kf, Shic, Scc , Ef]
for i in my_dict3:
    print(my_dict3[i])




# Dictionary to store notes for each heading
heading_notes = {
    "Depth (m)": "This column represents the depth in meters.",
    "Critical Width (m)": "Width corresponding to ZoPVS =100%",
    "Controlled Seepage Width (m)": "Width corresponding to Seepage \n(Qrpf) of 5000 GPM/km",
    "Rational Width (m)": "Width corresponding to ZoPVS =50%",
    "Desired Water Head (m)": "Water head corresponding seepage of \n5000 GPM/km at rational width:\nvary water head"}


# Function to show tooltip
def show_tooltip(event, text):
    note = heading_notes.get(text, "")
    tooltip_text.set(note)
    x, y = event.x + canvas.winfo_rootx() + 10, event.y + canvas.winfo_rooty() + 10
    tooltip_label.place(x=x, y=y)
    tooltip_label.lift()

# Function to hide tooltip
def hide_tooltip(event):
    tooltip_label.place_forget()


def plot_graph():


    # Value of Ei
    Ei = (Ef * Tf + Er * Tr) / (Tf + Tr)

    # Calculate E
    E = 1 - ((Wp ** 2) / ((Wp + Wg) ** 2))
    # Calculate Krpf
    Krpf = (Kr * Tr + Kp * Tp + Kf * Tf) / (Tr + Tp + Tf)
    # Calculate St
    St = (Str * Tr + Stp * Tp + Stf * Tf) / (Tr + Tp + Tf)
    # Calculate Sc
    Sc = (Scr * Tr + Scp * Tp + Scf * Tf) / (Tr + Tp + Tf)
    # Calculate Shi
    Shi = (Shir * Tr + Ship * Tp + Shif * Tf) / (Tr + Tp + Tf)
    # Calculate ZoPVS with updated formula
    ZoPVS = (2.28 * (Ei / Ec) ** 0.3 * D ** 2.39 * E ** 0.07) / (Shic ** 3.88 * Scc ** 0.66 * Wp ** 0.82)

    # Apply condition: if ZoPVS > 100, set ZoPVS to 100
    ZoPVS = min(ZoPVS, 100)

    # Calculate Qrpf
    Qrpf = (0.48 * Krpf * (Sc / St) ** 0.21 * (Ei / Ec) ** 0.03 * D ** 0.18 * E ** 0.02 * H ** 1.01) / (
            Shi ** 0.26 * Wp ** 0.9)

    # Calculate Wc by iterating over Wp until ZoPVS reaches 100
    Wc = 0.1  # Initial guess for Wc
    while True:
        E = (1 - ((Wc ** 2) / ((Wc + Wg) ** 2)))
        ZoPVS_temp = ((2.28 * (Ei / Ec) ** 0.3 * D ** 2.39 * E ** 0.07) /
                      (Shic ** 3.88 * Scc ** 0.66 * Wc ** 0.82))
        if (99.5 <= ZoPVS_temp <= 100.5):
            break
        Wc += 0.1  # Increment Wc by 0.1

    # Calculate Wsp by iterating over Wp until Qrpf reaches 5000
    Qrpf_temp = 5000.0
    Wsp = 1  # Initial guess for Wsp
    while True:
        E = (1 - ((Wsp ** 2) / ((Wsp + Wg) ** 2)))
        Qrpf_temp = ((0.48 * Krpf * (Sc / St) ** 0.21 * (Ei / Ec) ** 0.03 * D ** 0.18 * E ** 0.02 * H ** 1.01) /
                     (Shi ** 0.26 * Wsp ** 0.9))
        if 4995 <= Qrpf_temp <= 5005:
            break
        Wsp += 0.1  # Increment Wsp by 0.1

    Qrpf_atwr = 1.0
    # Calculate Wr by iterating over Wp until ZoPVS reaches 50
    Wh = 1.0
    Wr = 0.1  # Initial guess for Wr
    while True:
        E = (1 - ((Wr ** 2) / ((Wr + Wg) ** 2)))
        ZoPVS_temp = (2.28 * (Ei / Ec) ** 0.3 * D ** 2.39 * E ** 0.07) / (Shic ** 3.88 * Scc ** 0.66 * Wr ** 0.82)
        if (49.5 <= ZoPVS_temp <= 50.5):
            break
        Wr += 0.1  # Increment Wr by 0.1
        Wh = ((Qrpf_temp * (Shi ** 0.26) * (Wr ** 0.9)) / (
                0.48 * Krpf * ((Sc / St) ** 0.21) * ((Ei / Ec) ** 0.03) * (D ** 0.18) * (E ** 0.02))) ** (
                     1 / 1.01)

    # Plotting ZoPVS and Qrpf vs. Wp
    Wp_values = np.linspace(Wc, 200, 1000)  # Generate Wp values for plotting

    ZoPVS_values = (
                           2.28 * (Ei / Ec) ** 0.3 * D ** 2.39 * (
                           1 - ((Wp_values ** 2) / ((Wp_values + Wg) ** 2))) ** 0.07) / (
                           Shic ** 3.88 * Scc ** 0.66 * Wp_values ** 0.82
                   )

    Qrpf_values = (
                          0.48 * Krpf * (Sc / St) ** 0.21 * (Ei / Ec) ** 0.03 * D ** 0.18 * (
                          1 - ((Wp_values ** 2) / ((Wp_values + Wg) ** 2))) ** 0.02 * H ** 1.01) / (
                          Shir ** 0.26 * Wp_values ** 0.9)

    # Create figure
    fig, ax1 = plt.subplots()

    # Plot ZoPVS_values on the left y-axis
    color1 = 'tab:blue'
    ax1.set_xlabel('Width of pillar (m)')
    ax1.set_ylabel('Seepage (GPM/km) ', color=color1)
    ax1.plot(Wp_values, Qrpf_values, color=color1, label='Qrpf (GPM/km)')
    ax1.tick_params(axis='y', labelcolor=color1)

    # Create a second y-axis on the right for ZoPVS_values
    ax2 = ax1.twinx()
    color2 = 'tab:red'
    ax2.set_ylabel('ZoPVS(%)', color=color2)
    ax2.plot(Wp_values, ZoPVS_values, color=color2, label='ZoPVS')
    ax2.tick_params(axis='y', labelcolor=color2)


    # Set the scale range for ZoPVS to be between 0 and 100
    ax2.set_ylim(0, 100)
    # ax1.set_ylim(0, 25000)

    # Mark points for Wh, Wc, Wr, Wsp on the graph
    Wc_point = (Wc, 100)  # Wc point on the graph (ZoPVS scale)
    Wr_point = (Wr, 50)  # Wr point on the graph (ZoPVS scale)
    Wsp_point = (Wsp, 5000)  # Wsp point on the graph (Qrpf scale)

    markersize = 8 # Adjust the size of the markers as needed
    ax2.plot(*Wc_point, marker='o', markersize=markersize, color='purple', label='Wc (ZoPVS scale)')
    ax2.plot(*Wr_point, marker='o', markersize=markersize, color='orange', label='Wr (ZoPVS scale)')
    ax1.plot(*Wsp_point, marker='o', markersize=markersize, color='brown', label='Wsp (Qrpf scale)')

    # Add legends for both axes with custom location
    ax1.legend(loc='upper left', bbox_to_anchor=(0.63, 0.8))
    ax2.legend(loc='upper right')

    y_min2, y_max2 = ax2.get_ylim()
    y_min1, y_max1 = ax1.get_ylim()

    x_min1, x_max1 = ax1.get_xlim()

    # Plot dashed vertical line at Wr
    ax2.axvline(Wr, ymin=(0- y_min2) / (y_max2 - y_min2), ymax=(50 - y_min2) / (y_max2 - y_min2), color='orange', linestyle='--', linewidth=1)
    ax2.axvline(Wc, ymin=(0 - y_min2) / (y_max2 - y_min2), ymax=(100 - y_min2) / (y_max2 - y_min2), color='purple',linestyle='--', linewidth=1)
    ax2.axhline(100, xmin=(Wc- x_min1) / (x_max1 - x_min1), xmax=(x_max1 - x_min1) / (x_max1 - x_min1), color='purple', linestyle='--', linewidth=1)
    ax2.axhline(50, xmin=(Wr - x_min1) / (x_max1 - x_min1), xmax=(x_max1 - x_min1) / (x_max1 - x_min1), color='orange', linestyle='--', linewidth=1)

    ax1.axvline(Wsp, ymin=(0 - y_min1) / (y_max1 - y_min1), ymax=(5000 - y_min1) / (y_max1 - y_min1), color='brown',
                linestyle='--', linewidth=1)
    ax1.axhline(5000, xmin=(0 - x_min1) / (x_max1 - x_min1), xmax=(Wsp - x_min1) / (x_max1 - x_min1), color='brown',
                linestyle='--', linewidth=1)

    # Calculate the fraction of the axis range for the desired length
    line_fraction = 0.7  # Adjust this value as needed
    # Add dotted lines
    #ax2.axvline(Wc, ymin=0, ymax=100, color='purple', linestyle='--', linewidth=1)
    #ax2.axhline(100, xmin=Wc, xmax=400, color='purple', linestyle='--', linewidth=1)

    #ax2.axvline(Wr, ymin=0, ymax=70, color='orange', linestyle='--', linewidth=1)
    #ax2.axhline(50, xmin=Wr, xmax=400 , color='orange', linestyle='--', linewidth=1)

    # Plot dashed vertical line at Wr
    #ax2.axvline(Wr, ymin=(y_start - y_min) / (y_max - y_min), ymax=(y_end - y_min) / (y_max - y_min), color='orange',
                #linestyle='--', linewidth=1)

    '''ax2.axvline(Wc, color='purple', linestyle='--', linewidth=1)
    ax2.axhline(100, color='purple', linestyle='--', linewidth=1)
    ax2.axvline(Wr, color='orange', linestyle='--', linewidth=1)
    ax2.axhline(50, color='orange', linestyle='--', linewidth=1)
    ax1.axvline(Wsp, color='brown', linestyle='--', linewidth=1)
    ax1.axhline(5000, color='brown', linestyle='--', linewidth=1)'''

    # Remove the top outline (spine)
    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)

    # Add a title
    plt.title('ZoPVS and Qrpf vs Wp with Marked Points')


    # Embed the matplotlib graph into the tkinter window
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack( expand=True)

    # Create a FigureCanvasTkAgg to display the plot in the GUI
    #canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    #canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Fill both directions and expand

    '''# Create a canvas to display the plot in the GUI
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)'''

    # Update the graph_frame size based on the figure size
    # canvas.get_tk_widget().bind("<Configure>", lambda e: canvas.get_tk_widget().config(width=e.width, height=e.height))

    # Disable the button after clicking
    graph_button.config(state=tk.DISABLED)


def exit_app():
    # root.destroy()
    os._exit(0)


# Create main window
root = tk.Tk()
root.title("Design of Protective Water Barrier Pillar (PWBP)")
# root.attributes('-fullscreen', True)  # Run in full screen
# Set window size and position to fullscreen with 1920x1080 resolution
# root.attributes('-fullscreen', True)
root.geometry("1920x1080")


def place_graph():
    # Dummy graph widget (replace with your actual graph)
    graph = ttk.Label(graph_frame, text="Graph Widget")
    graph.grid(row=0, column=0, sticky="nsew")  # Grid the graph to fill the frame



# Heading
heading_label = tk.Label(root, text="Estimates of Critical Width, Controlled Seepage Width,"
                                    " and Rational Width & Desired Water Head",
                         font=("Arial", 25, "bold"), pady=10)
heading_label.pack()

graph_frame = ttk.Frame(root, width=1000, height=450)
graph_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its content
graph_frame.pack(expand=True, padx=10, pady=10)  # Fixed size


# Graph Frame
#graph_frame = ttk.Frame(root)
#graph_frame.pack(fill="both", expand=True)

# Configure grid for the graph frame
graph_frame.grid_rowconfigure(0, weight=1)  # Make row 0 expandable
graph_frame.grid_columnconfigure(0, weight=1)  # Make column 0 expandable



# Table Frame
table_frame = ttk.Frame(root)
table_frame.pack()
Wc = round(Wc, 2)
Wsp = round(Wsp, 2)
Wr = round(Wr, 2)
Wh = round(Wh, 2)
# Sample table data
table_data = [
    ["Depth (m)", "Critical Width (m)", "Controlled Seepage Width (m)", "Rational Width (m)",
     "Desired Water Head (m)"],
    [D , Wc , Wsp, Wr , Wh] ]

# Define cell dimensions
cell_width = 220
cell_height = 50

# Create a Canvas widget
canvas = tk.Canvas(table_frame, width=1100, height=100 , relief="sunken" , borderwidth=1 , bg="#ADADF5")
canvas.pack()

# Define fonts
header_font = ("Arial", 15, "bold" )
cell_font = ("Arial",15 , "bold")




# Function to draw the table
def draw_table(data, canvas):

    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            x1 = j * cell_width
            y1 = i * cell_height
            x2 = x1 + cell_width
            y2 = y1 + cell_height

            # Draw cell border
            canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2 )

            # Determine font and anchor
            font = header_font if i == 0 else cell_font
            anchor = "center" if i == 0 else "nw"

            # Adjust text position for non-header cells
            text_x = x1 + cell_width // 2 if i == 0 else x1 + 100
            text_y = y1 + cell_height // 2 if i == 0 else y1 + 10

            # Draw cell content
            canvas.create_text(text_x, text_y, text=cell, font=font, anchor=anchor, tags=f"cell_{i}_{j}")

            # Bind hover event to the header cells
            if i == 0:
                canvas.tag_bind(f"cell_{i}_{j}", "<Enter>", lambda event, text=cell: show_tooltip(event, text))
                canvas.tag_bind(f"cell_{i}_{j}", "<Leave>", hide_tooltip)



# Draw the table with the sample data
draw_table(table_data, canvas)

# Create a tooltip label
tooltip_text = tk.StringVar()
tooltip_label = tk.Label(root, textvariable=tooltip_text, font=("Arial", 12, "bold"),
                         bg="yellow", relief="solid", borderwidth=1)
tooltip_label.place_forget()




# Exit Button
exit_button = tk.Button(root, text="Exit", command=exit_app, width=20, height=2)
exit_button.pack(side="right", padx=10, pady=10)  # Adjust padx and pady as needed

# Plot Graph Button
graph_button = tk.Button(root, text="Plot Graph", command=plot_graph, width=20, height=2)
graph_button.pack(side="left", padx=10, pady=10)  # Adjust padx and pady as needed





# Run the GUI
root.mainloop()


