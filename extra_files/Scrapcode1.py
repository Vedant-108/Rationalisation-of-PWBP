import tkinter as tk
import numpy as np
import json
import os
from tkinter import messagebox


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




def calculate_all(cover_depth, gallery_width, pillar_width, influence_zone_roof, height_coal_pillar,
                  influence_zone_floor, water_head, youngs_modulus_roof_floor, youngs_modulus_coal,
                  mean_horizontal_stress_roof, mean_horizontal_stress_pillar, mean_horizontal_stress_floor,
                  mean_compressive_strength_roof, mean_compressive_strength_pillar,
                  mean_compressive_strength_floor, mean_tensile_strength_roof, mean_tensile_strength_pillar,
                  mean_tensile_strength_floor, permeability_roof, permeability_pillar, permeability_floor,
                  in_situ_horizontal_stress_coal, rock_mass_compressive_strength_coal):
    try:
        # Get user inputs
        D = cover_depth
        Wg = gallery_width
        Wp = pillar_width  # Corrected label here
        Tr = influence_zone_roof
        Tp = height_coal_pillar
        Tf = influence_zone_floor
        H = water_head
        Ei = youngs_modulus_roof_floor
        Ec =  youngs_modulus_coal
        Shir =  mean_horizontal_stress_roof
        Ship = mean_horizontal_stress_pillar
        Shif = mean_horizontal_stress_floor
        Scr = mean_compressive_strength_roof
        Scp = mean_compressive_strength_pillar
        Scf = mean_compressive_strength_floor
        Str = mean_tensile_strength_roof
        Stp =  mean_tensile_strength_pillar
        Stf = mean_tensile_strength_floor
        Kr = permeability_roof
        Kp = permeability_pillar
        Kf = permeability_floor
        Shic =  in_situ_horizontal_stress_coal
        Scc = rock_mass_compressive_strength_coal

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

        # Function to display calculated values in a pop-up message box
        '''def display_calculated_values(E, Krpf, St, Sc, Shi, ZoPVS, Qrpf, Wc, Wsp, Wr, Wh):
            calculated_values_text = (
                f"Calculated Values:\n\n"
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
                f"Wh:Water Head  {Wh:.2f}"
            )
            messagebox.showinfo("Calculated Values", calculated_values_text)

        display_calculated_values(E, Krpf, St, Sc, Shi, ZoPVS, Qrpf, Wc, Wsp, Wr, Wh)'''


        '''# Display results
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
                                            f"Wh:Water Head  {Wh:.2f}")'''

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
    #input_entries = create_input_fields(root)
    # Create input fields

    # Define input fields separately
    cover_depth_label = tk.Label(root, text='Cover Depth (D) [m]:', font=("Helvetica", 18))
    cover_depth_label.grid(row=0, column=0, padx=10, pady=2, sticky='e')
    entry_cover_depth = tk.Entry(root, width=10 , font=("Helvetica", 18) )
    entry_cover_depth.grid(row=0, column=1, padx=10, pady=2)
    #entry_cover_depth.insert(tk.END, '350')

    gallery_width_label = tk.Label(root, text='Gallery Width (Wg) [m]:', font=("Helvetica", 18))
    gallery_width_label.grid(row=1, column=0, padx=10, pady=2, sticky='e')
    entry_gallery_width = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_gallery_width.grid(row=1, column=1, padx=10, pady=2)

    pillar_width_label = tk.Label(root, text='Pillar Width (Wp) [m]:', font=("Helvetica", 18))
    pillar_width_label.grid(row=2, column=0, padx=10, pady=2, sticky='e')
    entry_pillar_width = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_pillar_width.grid(row=2, column=1, padx=10, pady=2)

    roof_influence_label = tk.Label(root, text='Influence Zone of Immediate Roof (Tr) [m]:', font=("Helvetica", 18))
    roof_influence_label.grid(row=3, column=0, padx=10, pady=2, sticky='e')
    entry_roof_influence = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_roof_influence.grid(row=3, column=1, padx=10, pady=2)

    pillar_height_label = tk.Label(root, text='Height of the Coal Pillar (Tp) [m]:', font=("Helvetica", 18))
    pillar_height_label.grid(row=4, column=0, padx=10, pady=2, sticky='e')
    entry_pillar_height = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_pillar_height.grid(row=4, column=1, padx=10, pady=2)

    floor_influence_label = tk.Label(root, text='Influence Zone of Immediate Floor (Tf) [m]:', font=("Helvetica", 18))
    floor_influence_label.grid(row=5, column=0, padx=10, pady=2, sticky='e')
    entry_floor_influence = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_floor_influence.grid(row=5, column=1, padx=10, pady=2)

    water_head_label = tk.Label(root, text='Water Head (H) [m]:', font=("Helvetica", 18))
    water_head_label.grid(row=6, column=0, padx=10, pady=2, sticky='e')
    entry_water_head = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_water_head.grid(row=6, column=1, padx=10, pady=2)

    roof_floor_modulus_label = tk.Label(root, text="Young’s Modulus of Roof/Floor (Ei) [GPa]:", font=("Helvetica", 18))
    roof_floor_modulus_label.grid(row=7, column=0, padx=10, pady=2, sticky='e')
    entry_roof_floor_modulus = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_roof_floor_modulus.grid(row=7, column=1, padx=10, pady=2)

    coal_modulus_label = tk.Label(root, text="Young’s Modulus of Coal (Ec) [GPa]:", font=("Helvetica", 18))
    coal_modulus_label.grid(row=8, column=0, padx=10, pady=2, sticky='e')
    entry_coal_modulus = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_coal_modulus.grid(row=8, column=1, padx=10, pady=2)

    roof_stress_label = tk.Label(root, text="Mean Horizontal Stress in Immediate Roof (Shir) [MPa]:", font=("Helvetica", 18))
    roof_stress_label.grid(row=9, column=0, padx=10, pady=2, sticky='e')
    entry_roof_stress = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_roof_stress.grid(row=9, column=1, padx=10, pady=2)

    pillar_stress_label = tk.Label(root, text="Mean Horizontal Stress in Pillar (Ship) [MPa]:", font=("Helvetica", 18))
    pillar_stress_label.grid(row=10, column=0, padx=10, pady=2, sticky='e')
    entry_pillar_stress = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_pillar_stress.grid(row=10, column=1, padx=10, pady=2)

    floor_stress_label = tk.Label(root, text="Mean Horizontal Stress in Immediate Floor (Shif) [MPa]:", font=("Helvetica", 18))
    floor_stress_label.grid(row=0, column=3, padx=10, pady=2, sticky='e')
    entry_floor_stress = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_floor_stress.grid(row=0, column=4, padx=10, pady=2)

    roof_compressive_strength_label = tk.Label(root, text="Mean Compressive Strength of Immediate Roof (Scr) [MPa]:", font=("Helvetica", 18))
    roof_compressive_strength_label.grid(row=1, column=3, padx=10, pady=2, sticky='e')
    entry_roof_compressive_strength = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_roof_compressive_strength.grid(row=1, column=4, padx=10, pady=2)

    pillar_compressive_strength_label = tk.Label(root, text="Mean Compressive Strength of Pillar (Scp) [MPa]:", font=("Helvetica", 18))
    pillar_compressive_strength_label.grid(row=2, column=3, padx=10, pady=2, sticky='e')
    entry_pillar_compressive_strength = tk.Entry(root, width=10 , font=("Helvetica", 18))
    entry_pillar_compressive_strength.grid(row=2, column=4, padx=10, pady=2)

    floor_compressive_strength_label = tk.Label(root, text="Mean Compressive Strength of Immediate Floor (Scf) [MPa]:", font=("Helvetica", 18))
    floor_compressive_strength_label.grid(row=3, column=3, padx=10, pady=2, sticky='e')
    entry_floor_compressive_strength = tk.Entry(root, width=10, font=("Helvetica", 18))
    entry_floor_compressive_strength.grid(row=3, column=4, padx=10, pady=2)

    roof_tensile_strength_label = tk.Label(root, text="Mean Tensile Strength of Immediate Roof (Str) [MPa]:", font=("Helvetica", 18))
    roof_tensile_strength_label.grid(row=4, column=3, padx=10, pady=2, sticky='e')
    entry_roof_tensile_strength = tk.Entry(root, width=10, font=("Helvetica", 18))
    entry_roof_tensile_strength.grid(row=4, column=4, padx=10, pady=2)

    pillar_tensile_strength_label = tk.Label(root, text="Mean Tensile Strength of Pillar (Stp) [MPa]:", font=("Helvetica", 18))
    pillar_tensile_strength_label.grid(row=5, column=3, padx=10, pady=2, sticky='e')
    entry_pillar_tensile_strength = tk.Entry(root, width=10, font=("Helvetica", 18))
    entry_pillar_tensile_strength.grid(row=5, column=4, padx=10, pady=2)

    floor_tensile_strength_label = tk.Label(root, text="Mean Tensile Strength of Immediate Floor (Stf) [MPa]:", font=("Helvetica", 18))
    floor_tensile_strength_label.grid(row=6, column=3, padx=10, pady=2, sticky='e')
    entry_floor_tensile_strength = tk.Entry(root, width=10, font=("Helvetica", 18))
    entry_floor_tensile_strength.grid(row=6, column=4, padx=10, pady=2)

    roof_permeability_label = tk.Label(root, text="Permeability of Immediate Roof (Kr) [mD]:", font=("Helvetica", 18))
    roof_permeability_label.grid(row=7, column=3, padx=10, pady=2, sticky='e')
    entry_roof_permeability = tk.Entry(root, width=10, font=("Helvetica", 18))
    entry_roof_permeability.grid(row=7, column=4, padx=10, pady=2)

    pillar_permeability_label = tk.Label(root, text="Permeability of Coal Pillar (Kp) [mD]:", font=("Helvetica", 18))
    pillar_permeability_label.grid(row=8, column=3, padx=10, pady=2, sticky='e')
    entry_pillar_permeability = tk.Entry(root, width=10, font=("Helvetica", 18))
    entry_pillar_permeability.grid(row=8, column=4, padx=10, pady=2)

    floor_permeability_label = tk.Label(root, text="Permeability of Immediate Floor (Kf) [mD]:", font=("Helvetica", 18))
    floor_permeability_label.grid(row=9, column=3, padx=10, pady=2, sticky='e')
    entry_floor_permeability = tk.Entry(root, width=10, font=("Helvetica", 18))
    entry_floor_permeability.grid(row=9, column=4, padx=10, pady=2)

    in_situ_stress_coal_label = tk.Label(root, text="In situ Horizontal Stress in Coal (Shic) [MPa]:", font=("Helvetica", 18))
    in_situ_stress_coal_label.grid(row=10, column=3, padx=10, pady=2, sticky='e')
    entry_in_situ_stress_coal = tk.Entry(root, width=10, font=("Helvetica", 18))
    entry_in_situ_stress_coal.grid(row=10, column=4, padx=10, pady=2)

    rock_mass_compressive_strength_label = tk.Label(root, text="Rock Mass Compressive Strength of Coal (Scc) [MPa]:", font=("Helvetica", 18))
    rock_mass_compressive_strength_label.grid(row=11, column=3, padx=10, pady=2, sticky='e')
    entry_rock_mass_compressive_strength = tk.Entry(root, width=10, font=("Helvetica", 18))
    entry_rock_mass_compressive_strength.grid(row=11, column=4, padx=10, pady=2)

    # Default values for each entry field
    default_values = {
        entry_cover_depth: '350',
        entry_gallery_width: '5',
        entry_pillar_width: '10',
        entry_roof_influence: '6',
        entry_pillar_height: '3',
        entry_floor_influence: '6',
        entry_water_head: '350',
        entry_roof_floor_modulus: '3.01',
        entry_coal_modulus: '2',
        entry_roof_stress: '3.91',
        entry_pillar_stress: '5.89',
        entry_floor_stress: '3.98',
        entry_roof_compressive_strength: '4.01',
        entry_pillar_compressive_strength: '2.04',
        entry_floor_compressive_strength: '4.01',
        entry_roof_tensile_strength: '0.39',
        entry_pillar_tensile_strength: '0.04',
        entry_floor_tensile_strength: '0.39',
        entry_roof_permeability: '1000',
        entry_pillar_permeability: '100',
        entry_floor_permeability: '1000',
        entry_in_situ_stress_coal: '5.89',
        entry_rock_mass_compressive_strength: '2.04'
    }

    # Add default values to each entry field
    for entry_widget, default_value in default_values.items():
        entry_widget.insert(tk.END, default_value)

    def calculate_values():
        # Retrieve values from input fields and convert them to float
        cover_depth = float(entry_cover_depth.get())
        gallery_width = float(entry_gallery_width.get())
        pillar_width = float(entry_pillar_width.get())
        influence_zone_roof = float(entry_roof_influence.get())
        height_coal_pillar = float(entry_pillar_height.get())
        influence_zone_floor = float(entry_floor_influence.get())
        water_head = float(entry_water_head.get())
        youngs_modulus_roof_floor = float(entry_roof_floor_modulus.get())
        youngs_modulus_coal = float(entry_coal_modulus.get())
        mean_horizontal_stress_roof = float(entry_roof_stress.get())
        mean_horizontal_stress_pillar = float(entry_pillar_stress.get())
        mean_horizontal_stress_floor = float(entry_floor_stress.get())
        mean_compressive_strength_roof = float(entry_roof_compressive_strength.get())
        mean_compressive_strength_pillar = float(entry_pillar_compressive_strength.get())
        mean_compressive_strength_floor = float(entry_floor_compressive_strength.get())
        mean_tensile_strength_roof = float(entry_roof_tensile_strength.get())
        mean_tensile_strength_pillar = float(entry_pillar_tensile_strength.get())
        mean_tensile_strength_floor = float(entry_floor_tensile_strength.get())
        permeability_roof = float(entry_roof_permeability.get())
        permeability_pillar = float(entry_pillar_permeability.get())
        permeability_floor = float(entry_floor_permeability.get())
        in_situ_horizontal_stress_coal = float(entry_in_situ_stress_coal.get())
        rock_mass_compressive_strength_coal = float(entry_rock_mass_compressive_strength.get())

        # Pass the values to calculate_all function
        calculate_all(cover_depth, gallery_width, pillar_width, influence_zone_roof, height_coal_pillar,
                      influence_zone_floor, water_head, youngs_modulus_roof_floor, youngs_modulus_coal,
                      mean_horizontal_stress_roof, mean_horizontal_stress_pillar, mean_horizontal_stress_floor,
                      mean_compressive_strength_roof, mean_compressive_strength_pillar,
                      mean_compressive_strength_floor, mean_tensile_strength_roof, mean_tensile_strength_pillar,
                      mean_tensile_strength_floor, permeability_roof, permeability_pillar, permeability_floor,
                      in_situ_horizontal_stress_coal, rock_mass_compressive_strength_coal)



    #calculate_button.grid(row=24, column=0, columnspan=2, padx=10, pady=5, sticky="we")

    # Calculated values label
    #global calculated_values_label
    #calculated_values_label = tk.Label(root, text="Calculated Values:\n\n")
    #calculated_values_label.grid(row=1, column=2, rowspan=10, padx=10, pady=10, sticky="nswe")

    calculate_button = tk.Button(root, text="Calculate", command=calculate_values, width=20, height=2)


    def press_buttons():
        calculate_button.invoke()
        os.system("python3 test2.py")  # Execute test2.py after simulating button click

    # Create the r-button
    r_button = tk.Button(root, text="Rationalise the Width of PWBP", command=press_buttons , width=20, height=2, font=("Helvetica", 18))
    r_button.grid(row=24 , column=0, columnspan=2, padx=10, pady=5, sticky="we")

    # Exit button
    exit_button = tk.Button(root, text="Exit", command=root.quit , width=20, height=2, font=("Helvetica", 18))
    exit_button.grid(row=25, column=0, columnspan=2, padx=10, pady=10, sticky="we")

    # Configure grid weights for responsive resizing
    root.grid_rowconfigure(11, weight=1)
    root.grid_columnconfigure(2, weight=1)

    #root.attributes('-fullscreen', True)  # Start in fullscreen mode
    # Set window size and position to fullscreen with 1920x1080 resolution
    #root.attributes('-fullscreen', True)
    root.geometry("1920x1080")


    root.mainloop()


if __name__ == "__main__":
    create_gui()
