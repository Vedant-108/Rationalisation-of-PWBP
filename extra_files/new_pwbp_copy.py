import tkinter as tk
import numpy as np
import json
import os


def open_test2():
    # Function to open the New PWBP program or code
    os.system("python3 test2.py")




'''def open_test2():
    """
    Execute the test2.py Python file.
    """
    try:
        # Replace "test2.py" with the path to your test2.py file if it's not in the same directory
        subprocess.Popen(["python", "test2.py"], shell=True)
    except Exception as e:
        print(f"An error occurred: {e}") '''


# Close the Program button
'''def close_programs():
    programs = ["opening_screen.py", "next_screen.py", "existing_pwbp.py"]  # Replace with your program names
    system = platform.system()

    for program in programs:
        if system == "Windows":
            subprocess.run(["taskkill", "/F", "/IM", program, "/T"], check=True)
        elif system in ["Linux", "Darwin"]:  # macOS and Linux
            # Get the process ID (pid) of the program
            pid = None
            try:
                pid = int(subprocess.check_output(["pgrep", "-f", program]))
            except subprocess.CalledProcessError:
                pass

            if pid is not None:
                try:
                    os.kill(pid, 9)  # Sends a SIGKILL signal to terminate the process
                except ProcessLookupError:
                    pass
        else:
            print("Unsupported system:", system)'''

lst = []
def store():
    my_dict2 = {
        'D': lst[0], 'Wg': lst[1], 'Wp': lst[2],
        'Tr': lst[3], 'Tp': lst[4], 'Tf': lst[5],
        'H': lst[6], 'Ei': lst[7], 'Ec': lst[8],
        'Shir': lst[9], 'Ship': lst[10], 'Shif': lst[11],
        'Scr': lst[12], 'Scp': lst[13], 'Scf': lst[14],
        'Str': lst[15], 'Stp': lst[16], 'Stf': lst[17],
        'Kr': lst[18], 'Kp': lst[19], 'Kf': lst[20], 'Shic': lst[21],
        'Scc': lst[22], 'Wc': lst[23], 'Wsp': lst[24],'Wr': lst[25],
        'Wh' : lst[26]
    }
    for i in my_dict2:
        print( my_dict2[i] , " ")

    # Write dictionary to a JSON file
    with open('../data.json', 'w') as json_file:
        json.dump(my_dict2, json_file)




def calculate_all(entries):
    try:
        # Get user inputs
        D = float(entries['Cover Depth (D) [m]:'].get())
        Wg = float(entries['Gallery Width (Wg) [m]:'].get())
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
        Scc = float(entries['Rock Mass Compressive Strength of Coal (Scc) [MPa]:'].get())  # New parameter

        '''my_dict2 = {
            'D': D,
            'Wg': Wg,
            'Wp': Wp,
            'Tr': Tr,
            'Tp': Tp,
            'Tf': Tf,
            'H': H,
            'Ei': Ei,
            'Ec': Ec,
            'Shir': Shir,
            'Ship': Ship,
            'Shif': Shif,
            'Scr': Scr,
            'Scp': Scp,
            'Scf': Scf,
            'Str': Str,
            'Stp': Stp,
            'Stf': Stf,
            'Kr': Kr,
            'Kp': Kp,
            'Kf': Kf,
            'Shic': Shic,
            'Scc': Scc} '''

        lst.extend([D, Wg, Wp, Tr, Tp, Tf, H, Ei, Ec, Shif, Ship, Shir, Scr, Scp, Scf, Str, Stp, Stf, Kr, Kp, Kf, Shic,
                   Scc ] )

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
            ZoPVS_temp = (2.28 * (Ei / Ec) ** 0.3 * D ** 2.39 * E ** 0.07) / (Shic ** 3.88 * Scc ** 0.66 * Wc ** 0.82)
            if (99.5 <= ZoPVS_temp <= 100.5):
                break
            Wc += 0.1  # Increment Wc by 0.1


        # Calculate Wsp by iterating over Wp until Qrpf reaches 5000
        Wsp = 1  # Initial guess for Wsp
        while True:
            E = (1 - ((Wsp ** 2) / ((Wsp + Wg) ** 2)))
            Qrpf_temp = (0.48 * Krpf * (Sc / St) ** 0.21 * (Ei / Ec) ** 0.03 * D ** 0.18 * E ** 0.02 * H ** 1.01) / (
                    Shi ** 0.26 * Wsp ** 0.9)
            if (4995 <= Qrpf_temp <= 5005):
                break
            Wsp += 0.1  # Increment Wsp by 0.1


        Qrpf_temp = 5000.0
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




        # Wh=1.0
        # Calculate Wh by iterating over H until Qrpf reaches 5000
        # Wh = 1  # Initial guess for Wh
        # while True:
        # E = (1 - ((Wh ** 2) / ((Wh + Wg) ** 2)))
        ## Shi ** 0.26 * Wr ** 0.9)

        # if (4995 <= Qrpf_temp <= 5005):
        # break
        # Wh += 0.1  # Increment Wh by 0.1

        lst.extend([Wc , Wsp , Wr , Wh])
        print(lst)
        store()

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
                              Shi ** 0.26 * Wp_values ** 0.9)

        # Display results
        calculated_values_label.config(text=f"Calculated Values:\n\n"
                                            f"E: {E:.2f}\n"
                                            f"Krpf: {Krpf:.2f}\n"
                                            f"St: {St:.2f}\n"
                                            f"Sc: {Sc:.2f}\n"
                                            f"Shi: {Shi:.2f}\n"
                                            f"ZoPVS: {ZoPVS:.2f} %\n"
                                            f"Qrpf: {Qrpf:.2f} GPM/km\n"
                                            f"Wc:Critical Width {Wc:.2f}\n"
                                            f"Wsp:Controlled Seepage Width {Wsp:.2f}\n"
                                            f"Wr:Rational Width {Wr:.2f}\n"
                                            f"Wh:Water Head  {Wh:.2f}")

        """
        # Create figure and first axes

        fig, ax1 = plt.subplots()

        # Plot ZoPVS_values on the left y-axis
        color1 = 'tab:blue'
        ax1.set_xlabel('Wp (in m )')
        ax1.set_ylabel('Qrpf (GPM/km) ', color=color1)
        ax1.plot(Wp_values, Qrpf_values, color=color1, label='Qrpf (GPM/km)')
        ax1.tick_params(axis='y', labelcolor=color1)

        # Create a second y-axis on the right for Qrpf_values
        ax2 = ax1.twinx()
        color2 = 'tab:red'
        ax2.set_ylabel('ZoPVS %', color=color2)
        ax2.plot(Wp_values, ZoPVS_values, color=color2, label='ZoPVS')
        ax2.tick_params(axis='y', labelcolor=color2)

        # Set the scale range for ZoPVS to be between 0 and 100
        ax2.set_ylim(0, 100)

        # Add legends for both axes
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        # Add a title
        plt.title('ZoPVS and Qrpf vs Wp ')

        # Mark points for Wh, Wc, Wr, Wsp on the graph
        # Wh_point = (Wh, 100)  # Wh point on the graph (ZoPVS scale)
        Wc_point = (Wc, 100)  # Wc point on the graph (Qrpf scale)
        Wr_point = (Wr, 50 )  # Wr point on the graph (ZoPVS scale)#Qrpf_atwr
        Wsp_point = (Wsp,5000 )  # Wsp point on the graph (Qrpf scale)#ZoPVS_atwsp

        markersize = 8  # Adjust the size of the markers as needed
        # ax1.plot(*Wh_point, marker='o', markersize=markersize, color='green', label='Wh (ZoPVS scale)')
        ax2.plot(*Wc_point, marker='o', markersize=markersize, color='purple', label='Wc (Qrpf scale)')
        ax2.plot(*Wr_point, marker='o', markersize=markersize, color='orange', label='Wr (ZoPVS scale)')
        ax1.plot(*Wsp_point, marker='o', markersize=markersize, color='brown', label='Wsp (Qrpf scale)')

        # Add legends for both axes
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        # Add a title
        plt.title('ZoPVS and Qrpf vs Wp with Marked Points')

        # Show the plot
        plt.show()"""



    except ValueError:
        calculated_values_label.config(text="Please enter valid numerical values.")


# The rest of the code remains the same...




def create_input_fields(root):
    labels = ['Cover Depth (D) [m]:', 'Gallery Width (Wg) [m]:', 'Pillar Width (Wp) [m]:',
              'Influence Zone of Immediate Roof (Tr) [m]:', 'Height of the Coal Pillar (Tp) [m]:',
              'Influence Zone of Immediate Floor (Tf) [m]:', 'Water Head (H) [m]:',
              "Young’s Modulus of Roof/Floor (Ei) [GPa]:", "Young’s Modulus of Coal (Ec) [GPa]:",
              "Mean Horizontal Stress in Immediate Roof (Shir) [MPa]:",
              "Mean Horizontal Stress in Pillar (Ship) [MPa]:",
              "Mean Horizontal Stress in Immediate Floor (Shif) [MPa]:",
              "Mean Compressive Strength of Immediate Roof (Scr) [MPa]:",
              "Mean Compressive Strength of Pillar (Scp) [MPa]:",
              "Mean Compressive Strength of Immediate Floor (Scf) [MPa]:",
              "Mean Tensile Strength of Immediate Roof (Str) [MPa]:", "Mean Tensile Strength of Pillar (Stp) [MPa]:",
              "Mean Tensile Strength of Immediate Floor (Stf) [MPa]:", "Permeability of Immediate Roof (Kr) [mD]:",
              "Permeability of Coal Pillar (Kp) [mD]:", "Permeability of Immediate Floor (Kf) [mD]:",
              "In situ Horizontal Stress in Coal (Shic) [MPa]:",  # New parameter
              "Rock Mass Compressive Strength of Coal (Scc) [MPa]:"  # New parameter
              ]

    entries = {}
    for i, label in enumerate(labels):
        tk.Label(root, text=label).grid(row=i, column=0, sticky='e', padx=10, pady=2)
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=1, padx=10, pady=2)
        # Set default values for some inputs
        if label == 'Gallery Width (Wg) [m]:':
            entry.insert(tk.END, '5')  # Default value for Wg
        elif label in ['Height of the Coal Pillar (Tp) [m]:']:
            entry.insert(tk.END, '3')  # Default value for Tp

        elif label in ['Water Head (H) [m]:']:
            entry.insert(tk.END, '350')  # Default value for H

        elif label in ['Cover Depth (D) [m]:']:
            entry.insert(tk.END, '350')  # Default value for D

        elif label in ['Gallery Width (Wg) [m]:']:
            entry.insert(tk.END, '5')  # Default value for Wg

        elif label in ['Pillar Width (Wp) [m]:']:
            entry.insert(tk.END, '10')  # Default value for Wp

        elif label in ['Height of the Coal Pillar (Tp) [m]:']:
            entry.insert(tk.END, '3')  # Default value for Tp

        elif label in ['Influence Zone of Immediate Roof (Tr) [m]:']:
            entry.insert(tk.END, '6')  # Default value for Tr

        elif label in ['Influence Zone of Immediate Floor (Tf) [m]:']:
            entry.insert(tk.END, '6')  # Default value for Tf

        elif label in ['Water Head (H) [m]:']:
            entry.insert(tk.END, '350')  # Default value for H

        elif label in ['Mean Horizontal Stress in Immediate Roof (Shir) [MPa]:']:
            entry.insert(tk.END, '3.91')  # Default value for Shir

        elif label in ['Mean Horizontal Stress in Immediate Floor (Shif) [MPa]:']:
            entry.insert(tk.END, '3.98')  # Default value for Shif

        elif label in ['Mean Horizontal Stress in Pillar (Ship) [MPa]:']:
            entry.insert(tk.END, '5.89')  # Default value for Ship

        elif label in ['Mean Compressive Strength of Immediate Roof (Scr) [MPa]:']:
            entry.insert(tk.END, '4.01')  # Default value for Scr

        elif label in ['Mean Compressive Strength of Immediate Floor (Scf) [MPa]:']:
            entry.insert(tk.END, '4.01')  # Default value for Scf

        elif label in ['Mean Compressive Strength of Pillar (Scp) [MPa]:']:
            entry.insert(tk.END, '2.04')  # Default value for Scp

        elif label in ['Mean Tensile Strength of Immediate Roof (Str) [MPa]:']:
            entry.insert(tk.END, '0.39')  # Default value for Str

        elif label in ['Mean Tensile Strength of Immediate Floor (Stf) [MPa]:']:
            entry.insert(tk.END, '0.39')  # Default value for Stf

        elif label in ['Mean Tensile Strength of Pillar (Stp) [MPa]:']:
            entry.insert(tk.END, '0.04')  # Default value for Stp

        elif label in ['Permeability of Immediate Roof (Kr) [mD]:']:
            entry.insert(tk.END, '1000')  # Default value for Kr

        elif label in ['Permeability of Coal Pillar (Kp) [mD]:']:
            entry.insert(tk.END, '100')  # Default value for Kp

        elif label in ['Permeability of Immediate Floor (Kf) [mD]:']:
            entry.insert(tk.END, '1000')  # Default value for Kf

        elif label in ['In situ Horizontal Stress in Coal (Shic) [MPa]:']:
            entry.insert(tk.END, '5.89')  # Default value for Shic

        elif label in ['Rock Mass Compressive Strength of Coal (Scc) [MPa]:']:
            entry.insert(tk.END, '2.04')  # Default value for Scc

        elif label in ["Young’s Modulus of Roof/Floor (Ei) [GPa]:"]:
            entry.insert(tk.END, '3.01')  # Default value for Ei

        elif label in ["Young’s Modulus of Coal (Ec) [GPa]:"]:
            entry.insert(tk.END, '2')  # Default value for Ec


        else:
            entry.insert(tk.END, '1')  # Default value for other inputs
        entries[label] = entry  # Store the entry in a dictionary
    return entries


def create_gui():
    root = tk.Tk()
    root.title("Coal Pillar Stability Calculator")

    # Create input fields
    input_entries = create_input_fields(root)

    # Calculate button
    calculate_button = tk.Button(root, text="Calculate", command=lambda: calculate_all(input_entries) , width=20, height=2)
    calculate_button.grid(row=len(input_entries), column=0, columnspan=2, padx=10, pady=5, sticky="we")

    # Calculated values label
    global calculated_values_label
    calculated_values_label = tk.Label(root, text="Calculated Values:\n\n")
    calculated_values_label.grid(row=1, column=2, rowspan=len(input_entries) + 2, padx=10, pady=10, sticky="nswe")

    # Create the r-button
    r_button = tk.Button(root, text="Rationalise the Width of PWBP", command=open_test2 , width=20, height=2)
    r_button.grid(row=len(input_entries) +1 , column=0, columnspan=2, padx=10, pady=5, sticky="we")



    # Exit button
    exit_button = tk.Button(root, text="Exit", command=root.quit , width=20, height=2)
    exit_button.grid(row=len(input_entries) + 2, column=3, columnspan=2, padx=10, pady=10, sticky="we")

    # Configure grid weights for responsive resizing
    root.grid_rowconfigure(len(input_entries) + 1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    #root.attributes('-fullscreen', True)  # Start in fullscreen mode
    # Set window size and position to fullscreen with 1920x1080 resolution
    root.attributes('-fullscreen', True)
    #root.geometry("1920x1080")

    root.mainloop()


if __name__ == "__main__":
    create_gui()
