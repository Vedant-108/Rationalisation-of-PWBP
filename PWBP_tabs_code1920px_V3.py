import numpy as np
import tkinter as tk
from tkinter import ttk
import os
from PIL import Image, ImageTk
import json
import tkinter.messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.platypus import Image as img
from datetime import datetime
import os

def export_to_pdf(remarks_text):
    # Filename for the PDF report
    filename = "remarks.pdf"

    # Create a PDF document object
    doc = SimpleDocTemplate(filename, pagesize=letter)

    # Define styles for the document
    styles = getSampleStyleSheet()
    header_style = styles['Heading1']
    body_style = styles['BodyText']

    # Story to hold all content
    story = []

    # Logo (adjust path as necessary)
    logo_path = "IITlogo.png"  # Replace with the actual path to your logo
    logo = img(logo_path, width=2*inch, height=1.93*inch)
    logo.hAlign = 'CENTER'  # Align logo to the left side
    story.append(logo)


    # Title and organization name
    program_name = "Design of Protective Water Barrier pillar"
    organization_name = "Mining Department, IIT BHU"

    # Title
    title_text = f"<b>{program_name}</b>"
    title_style = ParagraphStyle(name='TitleStyle', parent=header_style, fontSize=22)
    title = Paragraph(title_text, title_style)
    story.append(title)

    # Organization
    org_text = f"<i>{organization_name}</i>"
    org_style = ParagraphStyle(name='OrgStyle', parent=body_style, fontSize=14)
    org = Paragraph(org_text, org_style)
    story.append(org)

    # Copyright and current date
    current_date = datetime.now().strftime("%B %d, %Y")
    copyright_text = f"© {current_date} Mining Department, IIT BHU. All rights reserved."
    copyright_style = ParagraphStyle(name='CopyrightStyle', parent=body_style, fontSize=10)
    copyright = Paragraph(copyright_text, copyright_style)
    story.append(copyright)

    # Spacer
    story.append(Spacer(1, 0.5*inch))  # Spacer for separation

    # Body content from remarks_text
    lines = remarks_text.split('\n')
    for line in lines:
        p = Paragraph(line, body_style)
        story.append(p)
        story.append(Spacer(1, 0.1*inch))  # Spacer between paragraphs

    # Build the PDF document
    doc.build(story)

    # Open the PDF file after saving (macOS specific)
    open_pdf(filename)

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as img, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def export_custom_pdf(D, Wc, Wsp, Wr, Wh):
    # Filename for the PDF report
    filename = "Rationaisation_report.pdf"

    # Create a PDF document object
    doc = SimpleDocTemplate(filename, pagesize=letter)

    # Define styles for the document
    styles = getSampleStyleSheet()
    header_style = styles['Heading1']
    body_style = styles['BodyText']

    # Story to hold all content
    story = []

    # Logo (adjust path as necessary)
    logo_path = "IITlogo.png"  # Replace with the actual path to your logo
    logo = img(logo_path, width=1.5*inch, height=1.4475*inch)
    logo.hAlign = 'CENTER'  # Align logo to the center
    story.append(logo)

    # Program name
    program_name = "Design of Protect Water Barrier"
    program_name_text = f"<b>{program_name}</b>"
    program_name_style = ParagraphStyle(name='ProgramNameStyle', parent=header_style, fontSize=16, alignment=1)
    program_name_paragraph = Paragraph(program_name_text, program_name_style)
    story.append(program_name_paragraph)

    # Organization name
    organization_name = "Mining Department, IIT BHU"
    organization_text = f"<i>{organization_name}</i>"
    organization_style = ParagraphStyle(name='OrgStyle', parent=body_style, fontSize=12, alignment=1)
    organization = Paragraph(organization_text, organization_style)
    story.append(organization)

    # Copyright and current date
    current_date = datetime.now().strftime("%B %d, %Y")
    copyright_text = f"© {current_date} Mining Department, IIT BHU. All rights reserved."
    copyright_style = ParagraphStyle(name='CopyrightStyle', parent=body_style, fontSize=10, alignment=1)
    copyright = Paragraph(copyright_text, copyright_style)
    story.append(copyright)

    story.append(Spacer(1, 0.1 * inch))

    # Title
    title_text = "Estimation of Critical Width, Controlled Seepage Width, Rational Width and Desired Water Head"
    title_style = ParagraphStyle(name='TitleStyle', parent=header_style, fontSize=14, alignment=1)
    title = Paragraph(title_text, title_style)
    story.append(title)

    # Spacer
    story.append(Spacer(1, 0.1*inch))

    # Add the plot image to the PDF
    plot_image_path = 'plot.png'
    plot_image = img(plot_image_path, width=6*inch, height=4.5*inch)
    plot_image.hAlign = 'CENTER'
    story.append(plot_image)

    # Spacer
    story.append(Spacer(1, 0.1*inch))

    # Table data
    data = [
        ["Depth(m)", "Critical Width(m)", "Controlled Seepage Width(m)", "Rational Width(m)", "Desired Water Head(m)"],
        [D, Wc, Wsp, Wr, Wh]
    ]

    # Create the table
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), '#d3d3d3'),
        ('TEXTCOLOR', (0, 0), (-1, 0), '#000000'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), '#f0f0f0'),
        ('GRID', (0, 0), (-1, -1), 1, '#000000')
    ]))
    story.append(table)

    # Spacer
    story.append(Spacer(1, 0.1*inch))



    # Build the PDF document
    doc.build(story)

    print(f"PDF saved as {filename}")

    # Open the PDF file after saving (macOS specific)
    open_pdf(filename)


def exit_program():
    global root
    root.destroy()
    os._exit(0)


lst = []
def store():
    my_dict2 = {
        'D': lst[0], 'Wg': lst[1], 'Wp': lst[2],
        'Tr': lst[3], 'Tp': lst[4], 'Tf': lst[5],
        'H': lst[6], 'Er': lst[7], 'Ec': lst[8],
        'Shir': lst[9], 'Ship': lst[10], 'Shif': lst[11],
        'Scr': lst[12], 'Scp': lst[13], 'Scf': lst[14],
        'Str': lst[15], 'Stp': lst[16], 'Stf': lst[17],
        'Kr': lst[18], 'Kp': lst[19], 'Kf': lst[20], 'Shic': lst[21],
        'Scc': lst[22], 'Ef': lst[23], 'Wc': lst[24], 'Wsp': lst[25], 'Wr': lst[26],
        'Wh': lst[27]
    }
    for i in my_dict2:
        print(my_dict2[i], " ")

    # Write dictionary to a JSON file
    with open('data.json', 'w') as json_file:
        json.dump(my_dict2, json_file)

# code for windows based program
'''
def export_to_pdf(remarks_text):
    filename = "remarks.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    y_position = 750  # Starting y-position for drawing text

    # Split remarks_text into lines to fit within the PDF page width
    lines = remarks_text.split('\n')
    for line in lines:
        c.drawString(30, y_position, line)
        y_position -= 20  # Move to the next line
        if y_position <= 30:
            c.showPage()  # Move to the next page if the current page is full
            y_position = 750  # Reset y-position for the new page

    c.save()
    # Example usage:
    filename = "remarks.pdf"
    open_pdf(filename)


def open_pdf(filename):
    os.system(f"start {filename}")
'''


'''
#Code for mac based systems
def export_to_pdf(remarks_text):
    filename = "remarks.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    y_position = 750  # Starting y-position for drawing text

    # Split remarks_text into lines to fit within the PDF page width
    lines = remarks_text.split('\n')
    for line in lines:
        c.drawString(30, y_position, line)
        y_position -= 20  # Move to the next line
        if y_position <= 30:
            c.showPage()  # Move to the next page if the current page is full
            y_position = 750  # Reset y-position for the new page

    c.save()

    # Open the PDF file after saving (macOS specific)
    open_pdf(filename)  '''

def open_pdf(filename):
    # Use the 'open' command to open the PDF file with the default application on macOS
    os.system(f"open {filename}")


def calculate_all(cover_depth, gallery_width, pillar_width, influence_zone_roof, height_coal_pillar,
                  influence_zone_floor, water_head, youngs_modulus_roof, youngs_modulus_floor, youngs_modulus_coal,
                  mean_horizontal_stress_roof, mean_horizontal_stress_pillar, mean_horizontal_stress_floor,
                  mean_compressive_strength_roof, mean_compressive_strength_pillar,
                  mean_compressive_strength_floor, mean_tensile_strength_roof, mean_tensile_strength_pillar,
                  mean_tensile_strength_floor, permeability_roof, permeability_pillar, permeability_floor,
                  ):
    try:
        # Get user inputs
        D = cover_depth
        Wg = gallery_width
        Wp = pillar_width  # Corrected label here
        Tr = influence_zone_roof
        Tp = height_coal_pillar
        Tf = influence_zone_floor
        H = water_head
        Ec = youngs_modulus_coal
        Er = youngs_modulus_roof
        Ef = youngs_modulus_floor
        Shir = mean_horizontal_stress_roof
        Ship = mean_horizontal_stress_pillar
        Shif = mean_horizontal_stress_floor
        Scr = mean_compressive_strength_roof
        Scp = mean_compressive_strength_pillar
        Scf = mean_compressive_strength_floor
        Str = mean_tensile_strength_roof
        Stp = mean_tensile_strength_pillar
        Stf = mean_tensile_strength_floor
        Kr = permeability_roof
        Kp = permeability_pillar
        Kf = permeability_floor
        #Shic =  in_situ_horizontal_stress_coal
        #Scc = rock_mass_compressive_strength_coal

        Shic = Ship
        Scc = Scp

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

        lst.extend([D, Wg, Wp, Tr, Tp, Tf, H, Er, Ec, Shif, Ship, Shir, Scr, Scp, Scf, Str, Stp, Stf, Kr, Kp, Kf, Shic,
                    Scc, Ef])

        #Value of Ei
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

        lst.extend([Wc, Wsp, Wr, Wh])
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

    except ValueError:
        tkinter.messagebox.showinfo("Message", "Please enter valid numerical values.")

def display_calculated_values(ZoPVS, Qrpf, Wc, Wh, Wsp, Wr):
    root = tk.Tk()
    root.title("Remarks ")
    #root.geometry("1366x768")
    root.geometry("1250x450")

    # Add a button to export to PDF
    export_pdf_button = tk.Button(root, text="Export to PDF", command=lambda: export_to_pdf(remarks_text), width=20,
                                  height=2)
    export_pdf_button.grid(row=15, column=2, columnspan=2, padx=10, pady=10, sticky='w')

    # Remarks for ZoPVS
    zo_pvs_remark_label = tk.Label(root, text="Assessment of Mechanical performance of PWBP :",
                                   font=("Helvetica", 18, "bold"), fg="purple")
    zo_pvs_remark_label.grid(row=1, column=2, columnspan=2, padx=10, pady=5, sticky='w')

    zo_pvs_label = tk.Label(root, text=f"Zone of Positive Volumetric Strain (ZoPVS):", font=("Helvetica", 14, "bold"))
    zo_pvs_label.grid(row=2, column=2, columnspan=2, padx=10, pady=5, sticky='w')
    zo_pvs_value = tk.Label(root, text=f"{ZoPVS:.2f} %", font=("Helvetica", 14, "bold"))
    zo_pvs_value.grid(row=2, column=4, columnspan=2, padx=10, pady=5, sticky='w')

    zo_pvs_remark_label = tk.Label(root, text="Remark:",
                                   font=("Helvetica", 14, "bold"), fg="blue")
    zo_pvs_remark_label.grid(row=3, column=2, columnspan=2, padx=10, pady=5, sticky='w')

    zo_pvs_remark = "PWBP is Liable to piping failure" if ZoPVS >= 100 else "PWBP is not Liable to piping failure"
    zo_pvs_remark_value = tk.Label(root, text=zo_pvs_remark, font=("Helvetica", 12, "bold"))
    zo_pvs_remark_value.grid(row=4, column=4, columnspan=2, padx=10, pady=5, sticky='w')

    # Remarks for Seepage
    zo_pvs_remark_label = tk.Label(root, text="Assessment of Hydraulic performance of PWBP :",
                                   font=("Helvetica", 18, "bold"), fg="Purple")
    zo_pvs_remark_label.grid(row=5, column=2, columnspan=2, padx=10, pady=5, sticky='w')

    seepage_label = tk.Label(root, text=f"Seepage (Qrpf):", font=("Helvetica", 14, "bold"))
    seepage_label.grid(row=6, column=2, columnspan=2, padx=10, pady=5, sticky='w')
    seepage_value = tk.Label(root, text=f"{Qrpf:.2f} GPM/km", font=("Helvetica", 14, "bold"))
    seepage_value.grid(row=6, column=4, columnspan=2, padx=10, pady=5, sticky='w')

    seepage_remark_label = tk.Label(root, text="Remark:", font=("Helvetica", 14, "bold"), fg="blue", anchor="w")
    seepage_remark_label.grid(row=7, column=2, columnspan=2, padx=10, pady=5, sticky='w')
    if Qrpf > 5000:
        seepage_remark = "Pillar Width is Inadequate\nHigh Seepage Severity\nExtremely difficult to manage such seepage, which has a \nconsiderable adverse effect on mine productivity"
    elif 1500 <= Qrpf <= 5000:
        seepage_remark = "Pillar width is Adequate\n-Moderate Seepage Severity\nIt is moderately difficult to manage such seepage \nas it affects the normal production of the mine"
    else:
        seepage_remark = "Pillar width is Adequate\n-Low Seepage Severity\n-Can be managed easily without any strain on the \nnormal productivity of the mine working"
    seepage_remark_value = tk.Label(root, text=seepage_remark, font=("Helvetica", 12, "bold"))
    seepage_remark_value.grid(row=8, column=4, columnspan=2, padx=10, pady=5, sticky='w')

    remarks_text = ""

    # Generate remarks text
    remarks_text += "Assessment of Mechanical performance of PWBP:\n"
    remarks_text += f"Zone of Positive Volumetric Strain (ZoPVS): {ZoPVS:.2f}%\n"
    zo_pvs_remark = "PWBP is Liable to piping failure" if ZoPVS >= 100 else "PWBP is not Liable to piping failure"
    remarks_text += f"Remark: {zo_pvs_remark}\n\n"

    remarks_text += "Assessment of Hydraulic performance of PWBP:\n"
    remarks_text += f"Seepage (Qrpf): {Qrpf:.2f} GPM/km\n"
    if Qrpf > 5000:
        seepage_remark = "- Pillar Width is Inadequate\n- High Seepage Severity\n- Extremely difficult to manage such seepage, which has a \nconsiderable adverse effect on mine productivity"
    elif 1500 <= Qrpf <= 5000:
        seepage_remark = "- Pillar width is Adequate\n- Moderate Seepage Severity\n- It is moderately difficult to manage such seepage \n-as it affects the normal production of the mine"
    else:
        seepage_remark = "- Pillar width is Adequate\n- Low Seepage Severity\n- Can be managed easily without any strain on the \nnormal productivity of the mine working"
    remarks_text += f"Remark: {seepage_remark}\n\n"

def calculate_all1(cover_depth, gallery_width, pillar_width, influence_zone_roof, height_coal_pillar,
                  influence_zone_floor, water_head, youngs_modulus_roof, youngs_modulus_floor, youngs_modulus_coal,
                  mean_horizontal_stress_roof, mean_horizontal_stress_pillar, mean_horizontal_stress_floor,
                  mean_compressive_strength_roof, mean_compressive_strength_pillar,
                  mean_compressive_strength_floor, mean_tensile_strength_roof, mean_tensile_strength_pillar,
                  mean_tensile_strength_floor, permeability_roof, permeability_pillar, permeability_floor
                  ):
    try:
        # Get user inputs
        D = cover_depth
        Wg = gallery_width
        Wp = pillar_width  # Corrected label here
        Tr = influence_zone_roof
        Tp = height_coal_pillar
        Tf = influence_zone_floor
        H = water_head
        Ec = youngs_modulus_coal
        Er = youngs_modulus_roof
        Ef = youngs_modulus_floor
        Shir = mean_horizontal_stress_roof
        Ship = mean_horizontal_stress_pillar
        Shif = mean_horizontal_stress_floor
        Scr = mean_compressive_strength_roof
        Scp = mean_compressive_strength_pillar
        Scf = mean_compressive_strength_floor
        Str = mean_tensile_strength_roof
        Stp = mean_tensile_strength_pillar
        Stf = mean_tensile_strength_floor
        Kr = permeability_roof
        Kp = permeability_pillar
        Kf = permeability_floor

        Shic = Ship
        Scc = Scp

        lst.extend([D, Wg, Wp, Tr, Tp, Tf, H, Er, Ec, Shif, Ship, Shir, Scr, Scp, Scf, Str, Stp, Stf, Kr, Kp, Kf, Shic,
                    Scc, Ef])

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

        # Adjust ZoPVS if greater than 100
        if ZoPVS > 100:
            ZoPVS = 100

        # Calculate Qrpf
        Qrpf = (0.48 * Krpf * (Sc / St) ** 0.21 * (Ei / Ec) ** 0.03 * D ** 0.18 * E ** 0.02 * H ** 1.01) / (
                Shi ** 0.26 * Wp ** 0.9)

        ZoPVS_atwc = 1.0
        ZoPVS_atwsp = 1.0
        # Calculate Wc by iterating over Wp until ZoPVS reaches 100
        Wc = 0.1  # Initial guess for Wc
        while True:
            E = (1 - ((Wc ** 2) / ((Wc + Wg) ** 2)))
            ZoPVS_temp = (2.28 * (Ei / Ec) ** 0.3 * D ** 2.39 * E ** 0.07) / (Shic ** 3.88 * Scc ** 0.66 * Wc ** 0.82)
            if (99.5 <= ZoPVS_temp <= 100.5):
                break
            Wc += 0.1  # Increment Wc by 0.1
            ZoPVS_atwc = (2.28 * (Ei / Ec) ** 0.3 * D ** 2.39 * E ** 0.07) / (Shic ** 3.88 * Scc ** 0.66 * Wc ** 0.82)
            # print ("ZoPVS_atwc" , ZoPVS_atwc)

        # Calculate Wsp by iterating over Wp until Qrpf reaches 5000
        Wsp = 1  # Initial guess for Wsp
        while True:
            E = (1 - ((Wsp ** 2) / ((Wsp + Wg) ** 2)))
            Qrpf_temp = (0.48 * Krpf * (Sc / St) ** 0.21 * (Ei / Ec) ** 0.03 * D ** 0.18 * E ** 0.02 * H ** 1.01) / (
                    Shi ** 0.26 * Wsp ** 0.9)
            if (4995 <= Qrpf_temp <= 5005):
                break
            Wsp += 0.1  # Increment Wsp by 0.1
            ZoPVS_atwsp = (2.28 * (Ei / Ec) ** 0.3 * D ** 2.39 * E ** 0.07) / (Shic ** 3.88 * Scc ** 0.66 * Wsp ** 0.82)

        Qrpf_temp = 5000.0
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
        Qrpf_atwr = (0.48 * Krpf * (Sc / St) ** 0.21 * (Ei / Ec) ** 0.03 * D ** 0.18 * E ** 0.02 * H ** 1.01) / (
                Shi ** 0.26 * Wr ** 0.9)

        lst.extend([Wc, Wsp, Wr, Wh])
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

        # Display calculated values and remarks
        #display_calculated_values(ZoPVS, Qrpf, Wc, Wh, Wsp, Wr)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")

def calculate_all2(cover_depth, gallery_width, pillar_width, influence_zone_roof, height_coal_pillar,
                  influence_zone_floor, water_head, youngs_modulus_roof, youngs_modulus_floor, youngs_modulus_coal,
                  mean_horizontal_stress_roof, mean_horizontal_stress_pillar, mean_horizontal_stress_floor,
                  mean_compressive_strength_roof, mean_compressive_strength_pillar,
                  mean_compressive_strength_floor, mean_tensile_strength_roof, mean_tensile_strength_pillar,
                  mean_tensile_strength_floor, permeability_roof, permeability_pillar, permeability_floor
                  ):
    try:
        # Get user inputs
        D = cover_depth
        Wg = gallery_width
        Wp = pillar_width  # Corrected label here
        Tr = influence_zone_roof
        Tp = height_coal_pillar
        Tf = influence_zone_floor
        H = water_head
        Ec = youngs_modulus_coal
        Er = youngs_modulus_roof
        Ef = youngs_modulus_floor
        Shir = mean_horizontal_stress_roof
        Ship = mean_horizontal_stress_pillar
        Shif = mean_horizontal_stress_floor
        Scr = mean_compressive_strength_roof
        Scp = mean_compressive_strength_pillar
        Scf = mean_compressive_strength_floor
        Str = mean_tensile_strength_roof
        Stp = mean_tensile_strength_pillar
        Stf = mean_tensile_strength_floor
        Kr = permeability_roof
        Kp = permeability_pillar
        Kf = permeability_floor

        Shic = Ship
        Scc = Scp

        lst.extend([D, Wg, Wp, Tr, Tp, Tf, H, Er, Ec, Shif, Ship, Shir, Scr, Scp, Scf, Str, Stp, Stf, Kr, Kp, Kf, Shic,
                    Scc, Ef])

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

        # Adjust ZoPVS if greater than 100
        if ZoPVS > 100:
            ZoPVS = 100

        # Calculate Qrpf
        Qrpf = (0.48 * Krpf * (Sc / St) ** 0.21 * (Ei / Ec) ** 0.03 * D ** 0.18 * E ** 0.02 * H ** 1.01) / (
                Shi ** 0.26 * Wp ** 0.9)

        ZoPVS_atwc = 1.0
        ZoPVS_atwsp = 1.0
        # Calculate Wc by iterating over Wp until ZoPVS reaches 100
        Wc = 0.1  # Initial guess for Wc
        while True:
            E = (1 - ((Wc ** 2) / ((Wc + Wg) ** 2)))
            ZoPVS_temp = (2.28 * (Ei / Ec) ** 0.3 * D ** 2.39 * E ** 0.07) / (Shic ** 3.88 * Scc ** 0.66 * Wc ** 0.82)
            if (99.5 <= ZoPVS_temp <= 100.5):
                break
            Wc += 0.1  # Increment Wc by 0.1
            ZoPVS_atwc = (2.28 * (Ei / Ec) ** 0.3 * D ** 2.39 * E ** 0.07) / (Shic ** 3.88 * Scc ** 0.66 * Wc ** 0.82)
            # print ("ZoPVS_atwc" , ZoPVS_atwc)

        # Calculate Wsp by iterating over Wp until Qrpf reaches 5000
        Wsp = 1  # Initial guess for Wsp
        while True:
            E = (1 - ((Wsp ** 2) / ((Wsp + Wg) ** 2)))
            Qrpf_temp = (0.48 * Krpf * (Sc / St) ** 0.21 * (Ei / Ec) ** 0.03 * D ** 0.18 * E ** 0.02 * H ** 1.01) / (
                    Shi ** 0.26 * Wsp ** 0.9)
            if (4995 <= Qrpf_temp <= 5005):
                break
            Wsp += 0.1  # Increment Wsp by 0.1
            ZoPVS_atwsp = (2.28 * (Ei / Ec) ** 0.3 * D ** 2.39 * E ** 0.07) / (Shic ** 3.88 * Scc ** 0.66 * Wsp ** 0.82)

        Qrpf_temp = 5000.0
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
        Qrpf_atwr = (0.48 * Krpf * (Sc / St) ** 0.21 * (Ei / Ec) ** 0.03 * D ** 0.18 * E ** 0.02 * H ** 1.01) / (
                Shi ** 0.26 * Wr ** 0.9)

        lst.extend([Wc, Wsp, Wr, Wh])
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

        # Display calculated values and remarks
        display_calculated_values(ZoPVS, Qrpf, Wc, Wh, Wsp, Wr)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numerical values.")


def gui_test2(notebook):
    # Check if 'test2' tab already exists
    for tab_id in notebook.tabs():
        if notebook.tab(tab_id, "text") == 'Rationalisation of PWBP':
            notebook.select(tab_id)  # Switch to the existing tab
            return  # Exit the function if tab already exists

    # Create the new tab
    new_tab = ttk.Frame(notebook)
    notebook.add(new_tab, text="Rationalisation of PWBP")
    notebook.select(new_tab)  # Switch to the new tab

    # Populate new pwbp tab
    frame = ttk.Frame(new_tab, padding=20)
    frame.pack(fill=tk.BOTH, expand=True)

    # Create main window
    #root = tk.Tk()
    #root.title("Design of Protective Water Barrier Pillar (PWBP)")
    # root.attributes('-fullscreen', True)  # Run in full screen
    # Set window size and position to fullscreen with 1920x1080 resolution
    # root.attributes('-fullscreen', True)
    #root.geometry("1366x768")
    #root.resizable(False, False)
    #root.geometry("1920x1080")

    with open('data.json', 'r') as json_file:
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

    list1 = [D, Wg, Wp, Tr, Tp, Tf, H, Er, Ec, Shir, Ship, Shir, Scr, Scp, Scf, Str, Stp,
             Stf, Kr, Kp, Kf, Shic, Scc, Ef]
    for i in my_dict3:
        print(my_dict3[i])



    '''# Function to show tooltip
    def show_tooltip(event, text):
        tooltip_text.set(text)
        tooltip_label.place(x=event.x_root, y=event.y_root)

    def hide_tooltip(event):
        tooltip_label.place_forget()'''

    def show_tooltip(event, text):
        tooltip_text.set(text)
        tooltip_label.place(x=event.x_root-100, y=event.y_root-80)

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
        # root
        # Mark points for Wh, Wc, Wr, Wsp on the graph
        Wc_point = (Wc, 100)  # Wc point on the graph (ZoPVS scale)
        Wr_point = (Wr, 50)  # Wr point on the graph (ZoPVS scale)
        Wsp_point = (Wsp, 5000)  # Wsp point on the graph (Qrpf scale)
        # ax.text(xi, yi, f'Point {i + 1}', fontsize=8, ha='center', va='bottom', color='black')
        markersize = 8  # Adjust the size of the markers as needed
        ax2.plot(*Wc_point, marker='o', markersize=markersize, color='purple', label='Wc (ZoPVS scale)')
        ax2.plot(*Wr_point, marker='o', markersize=markersize, color='orange', label='Wr (ZoPVS scale)')
        ax1.plot(*Wsp_point, marker='o', markersize=markersize, color='brown', label='Wsp (Qrpf scale)')
        # ax2.text(Wc,90, f'Critical Width' , fontsize= 6 , color='black' , ha='left', va='bottom' )

        ax2.text(Wc + 2, 100, f'Critical Width', fontsize=10, color='purple', ha='left', va='bottom')
        ax2.text(Wr + 5, 55, f'Rational Width', fontsize=10, color='orange', ha='left', va='top')
        ax1.text(Wsp - 5, 5000 + 1000, f'Controlled Seepage Width', fontsize=10, color='brown', ha='right', va='top')

        # Add legends for both axes with custom location
        ax1.legend(loc='upper left', bbox_to_anchor=(0.63, 0.8))
        ax2.legend(loc='upper right')

        y_min2, y_max2 = ax2.get_ylim()
        y_min1, y_max1 = ax1.get_ylim()

        x_min1, x_max1 = ax1.get_xlim()

        # Plot dashed vertical line at Wr
        ax2.axvline(Wr, ymin=(0 - y_min2) / (y_max2 - y_min2), ymax=(50 - y_min2) / (y_max2 - y_min2), color='orange',
                    linestyle='--', linewidth=1)
        ax2.axvline(Wc, ymin=(0 - y_min2) / (y_max2 - y_min2), ymax=(100 - y_min2) / (y_max2 - y_min2), color='purple',
                    linestyle='--', linewidth=1)
        ax2.axhline(100, xmin=(Wc - x_min1) / (x_max1 - x_min1), xmax=(x_max1 - x_min1) / (x_max1 - x_min1),
                    color='purple', linestyle='--', linewidth=1)
        ax2.axhline(50, xmin=(Wr - x_min1) / (x_max1 - x_min1), xmax=(x_max1 - x_min1) / (x_max1 - x_min1),
                    color='orange', linestyle='--', linewidth=1)

        ax1.axvline(Wsp, ymin=(0 - y_min1) / (y_max1 - y_min1), ymax=(5000 - y_min1) / (y_max1 - y_min1), color='brown',
                    linestyle='--', linewidth=1)
        ax1.axhline(5000, xmin=(0 - x_min1) / (x_max1 - x_min1), xmax=(Wsp - x_min1) / (x_max1 - x_min1), color='brown',
                    linestyle='--', linewidth=1)

        # Calculate the fraction of the axis range for the desired length
        line_fraction = 0.7  # Adjust this value as needed
        # Add dotted lines
        # ax2.axvline(Wc, ymin=0, ymax=100, color='purple', linestyle='--', linewidth=1)
        # ax2.axhline(100, xmin=Wc, xmax=400, color='purple', linestyle='--', linewidth=1)

        # ax2.axvline(Wr, ymin=0, ymax=70, color='orange', linestyle='--', linewidth=1)
        # ax2.axhline(50, xmin=Wr, xmax=400 , color='orange', linestyle='--', linewidth=1)

        # Plot dashed vertical line at Wr
        # ax2.axvline(Wr, ymin=(y_start - y_min) / (y_max - y_min), ymax=(y_end - y_min) / (y_max - y_min), color='orange',
        # linestyle='--', linewidth=1)

        '''ax2.axvline(Wc, color='purple', linestyle='--', linewidth=1)
        ax2.axhline(100, color='purple', linestyle='--', linewidth=1)
        ax2.axvline(Wr, color='orange', linestyle='--', linewidth=1)
        ax2.axhline(50, color='orange', linestyle='--', linewidth=1)
        ax1.axvline(Wsp, color='brown', linestyle='--', linewidth=1)
        ax1.axhline(5000, color='brown', linestyle='--', linewidth=1)'''

        # Remove the top outline (spine)
        ax1.spines['top'].set_visible(False)
        ax2.spines['top'].set_visible(False)

        plt.savefig('plot.png')

        # Add a title
        # plt.title('ZoPVS and Qrpf vs Wp with Marked Points')

        # Embed the matplotlib graph into the tkinter window
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(expand=True)

        # Create a FigureCanvasTkAgg to display the plot in the GUI
        # canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        # canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Fill both directions and expand

        '''# Create a canvas to display the plot in the GUI
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)'''

        # Update the graph_frame size based on the figure size
        # canvas.get_tk_widget().bind("<Configure>", lambda e: canvas.get_tk_widget().config(width=e.width, height=e.height))

        # Disable the button after clicking
        graph_button.config(state=tk.DISABLED)



    def exit_app():
        # Attempt to delete the file
        os.remove("data.json")
        print('file deleted')
        #root.destroy()
        os._exit(0)




    def place_graph():
        # Dummy graph widget (replace with your actual graph)
        graph = ttk.Label(graph_frame, text="Graph Widget")
        graph.grid(row=0, column=0, sticky="nsew")  # Grid the graph to fill the frame

    # Heading
    heading_label = tk.Label(frame, text="Estimates of Critical Width, Controlled Seepage Width,"
                                        " and Rational Width & Desired Water Head",
                             font=("Arial", 20, "bold"), pady=10)
    heading_label.pack()

    graph_frame = ttk.Frame(frame, width=1000, height=450)
    graph_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its content
    graph_frame.pack(expand=True, padx=10, pady=10)  # Fixed size

    # Configure grid for the graph frame
    graph_frame.grid_rowconfigure(0, weight=1)  # Make row 0 expandable
    graph_frame.grid_columnconfigure(0, weight=1)  # Make column 0 expandable

    # Graph Frame
    # graph_frame = ttk.Frame(root)
    # graph_frame.pack(fill="both", expand=True)

    # Set the window state to maximized (zoomed)
    #root.wm_state('zoomed')
    # Function to show tooltip



    # Table Frame
    table_frame = ttk.Frame(frame)
    table_frame.pack()
    Wc = round(Wc, 2)
    Wsp = round(Wsp, 2)
    Wr = round(Wr, 2)
    Wh = round(Wh, 2)


    # Sample table data
    table_data = [
        ["Depth (m)"'   ', "Critical Width (m)", "Controlled Seepage Width (m)", "Rational Width (m)",
         "Desired Water Head (m)"],
        [D, Wc, Wsp, Wr, Wh]]

    # Define cell dimensions
    # cell_width = 220
    cell_height = 50

    # Create a Canvas widget
    canvas = tk.Canvas(table_frame, width=1030, height=100, relief="sunken", borderwidth=1, bg="#ADADF5")
    canvas.pack()

    # Define fonts
    header_font = ("Arial", 12, "bold")
    cell_font = ("Arial", 12, "bold")




    # Function to draw the table
    def draw_table(data, canvas, info_image):
        # Calculate column widths based on the length of the headings
        column_widths = [(len(cell) * 10) + 10 for cell in
                         data[0]]  # len(cell) * 10 to convert length to pixel approx., + 50 for padding

        for i, row in enumerate(data):
            x1 = 0  # Start position for the first column
            for j, cell in enumerate(row):
                cell_width = column_widths[j]
                y1 = i * cell_height
                x2 = x1 + cell_width
                y2 = y1 + cell_height

                # Draw cell border
                canvas.create_rectangle(x1, y1, x2, y2, outline="black", width=2)

                # Determine font and anchor
                font = header_font if i == 0 else cell_font
                anchor = "center" if i == 0 else "nw"

                # Adjust text position for non-header cells
                text_x = x1 + cell_width // 2 if i == 0 else x1 + (cell_width / 2) - 10
                text_y = y1 + cell_height // 2 if i == 0 else y1 + 10

                # Draw cell content
                canvas.create_text(text_x, text_y, text=cell, font=font, anchor=anchor, tags=f"cell_{i}_{j}")

                # Add info icon beside the heading
                if i == 0:
                    icon_x = x2 - 20
                    icon_y = y1 + 10
                    icon = canvas.create_image(icon_x, icon_y, image=info_image, anchor="nw", tags=f"icon_{i}_{j}")
                    tooltip_texts = {
                        "Depth (m)"'   ': "This column represents the depth in meters.",
                        "Critical Width (m)": "Width corresponding to ZoPVS =100%",
                        "Controlled Seepage Width (m)": "Width corresponding to Seepage \n(Qrpf) of 5000 GPM/km",
                        "Rational Width (m)": "Width corresponding to ZoPVS =50%",
                        "Desired Water Head (m)": "Water head corresponding seepage\n of 5000 GPM/km at rational width:\nvary water head"
                    }
                    tooltip_text = tooltip_texts.get(cell, "")
                    canvas.tag_bind(icon, "<Enter>", lambda event, text=tooltip_text: show_tooltip(event, text))
                    canvas.tag_bind(icon, "<Leave>", hide_tooltip)

                # Update x1 for the next cell in the row
                x1 = x2





    # Create a tooltip label
    tooltip_text = tk.StringVar()
    tooltip_label = tk.Label(frame, textvariable=tooltip_text, font=("Arial", 10, "bold"), bg="yellow", relief="solid",
                             borderwidth=1)
    tooltip_label.place_forget()

    # Create a tooltip label
    tooltip_text = tk.StringVar()
    tooltip_label = tk.Label(frame, textvariable=tooltip_text, font=("Arial", 10, "bold"),
                             bg="Yellow", relief="solid", borderwidth=1)
    tooltip_label.place_forget()

    # Load the info icon image
    info_image_path = "IITlogo.png"  # Path to your info icon image
    info_image = Image.open(info_image_path)
    info_image = info_image.resize((20, 20), Image.LANCZOS)
    info_photo = ImageTk.PhotoImage(info_image)

    # Keep a reference to the image
    frame.info_image = info_image

    # Draw the table with the sample data
    draw_table(table_data, canvas, info_photo)

    # Exit Button
    exit_button = tk.Button(frame, text="Quit", command=exit_app, width=20, height=2)
    exit_button.pack(side="right", padx=10, pady=5)  # Adjust padx and pady as needed

    # Plot Graph Button
    graph_button = tk.Button(frame, text="Plot Graph", command=lambda: plot_graph(), width=20, height=2)
    #graph_button.pack(side="left", padx=10, pady=10)  # Adjust padx and pady as needed

    # export Plot Graph Button
    exportgraph_button = tk.Button(frame, text="Export Report", command=lambda: export_custom_pdf(D, Wc, Wsp, Wr, Wh), width=20, height=2)
    exportgraph_button.pack(side="left", padx=10, pady=5)  # Adjust padx and pady as needed

    graph_button.invoke()




def new_pwbp(notebook):
    #Check if 'Next Screen' tab already exists
    for tab_id in notebook.tabs():
        if notebook.tab(tab_id, "text") == 'Design of New PWBP':
            notebook.select(tab_id)  # Switch to the existing tab
            return  # Exit the function if tab already exists

    #root_ns.withdraw()

    # Create the new tab
    new_tab = ttk.Frame(notebook)
    notebook.add(new_tab, text="Design of New PWBP")
    notebook.select(new_tab)  # Switch to the new tab

    # Populate new pwbp tab
    frame = ttk.Frame(new_tab, padding=20)
    frame.pack(fill=tk.BOTH, expand=True)

    #frame = tk.Tk()
    #frame.title("Design of New PWBP")

    # Create input fields
    #input_entries = create_input_fields(root)
    # Create input fields

    # Define input fields separately using place for exact positioning
    cover_depth_label = tk.Label(frame, text='Cover Depth (D) [m]:', font=("Inter", 14, "bold"))
    cover_depth_label.place(x=130, y=90-60)
    entry_cover_depth = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_cover_depth.place(x=420, y=90-60)

    pillar_height_label = tk.Label(frame, text='Height of the Coal Pillar (Tp) [m]:', font=("Inter", 14, "bold"))
    pillar_height_label.place(x=130, y=117-60)
    entry_pillar_height = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_height.place(x=420, y=117-60)

    pillar_width_label = tk.Label(frame, text='Pillar Width (Wp) [m]:', font=("Inter", 14, "bold"))
    pillar_width_label.place(x=130, y=145-60)
    entry_pillar_width = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_width.place(x=420, y=145-60)

    gallery_width_label = tk.Label(frame, text='Gallery Width (Wg) [m]:', font=("Inter", 14, "bold"))
    gallery_width_label.place(x=130, y=175-60)
    entry_gallery_width = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_gallery_width.place(x=420, y=175-60)

    roof_RQD_label = tk.Label(frame, text="RQD of Immediate Roof :", font=("Inter", 14, "bold"))
    roof_RQD_label.place(x=130, y=230-60)
    entry_roof_RQD = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_roof_RQD.place(x=420, y=227-60)

    floor_RQD_label = tk.Label(frame, text="RQD of Immediate Floor :", font=("Inter", 14, "bold"))
    floor_RQD_label.place(x=130, y=257-60)
    entry_floor_RQD = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_RQD.place(x=420, y=258-60)

    pillar_RQD_label = tk.Label(frame, text="RQD of Pillar :", font=("Inter", 14, "bold"))
    pillar_RQD_label.place(x=130, y=285-60)
    entry_pillar_RQD = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_RQD.place(x=420, y=289-60)

    roof_compressive_strength_label = tk.Label(frame, text="Mean Compressive Strength of \nImmediate Roof (Scr) [MPa]:",
                                               font=("Inter", 14, "bold"), anchor='w')
    roof_compressive_strength_label.place(x=130, y=354-60)
    entry_roof_compressive_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_roof_compressive_strength.place(x=420, y=350-60)

    pillar_compressive_strength_label = tk.Label(frame, text="Mean Compressive Strength of \nPillar (Scp) [MPa]:",
                                                 font=("Inter", 14, "bold"), anchor='w')
    pillar_compressive_strength_label.place(x=130, y=400-60)
    entry_pillar_compressive_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_compressive_strength.place(x=420, y=398-60)

    floor_compressive_strength_label = tk.Label(frame,
                                                text="Mean Compressive Strength of \nImmediate Floor (Scf) [MPa]:",
                                                font=("Inter", 14, "bold"), anchor='w')
    floor_compressive_strength_label.place(x=130, y=446-60)
    entry_floor_compressive_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_compressive_strength.place(x=420, y=444-60)

    roof_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of \nImmediate Roof (Str) [MPa]:",
                                           font=("Inter", 14, "bold"), anchor='w')
    roof_tensile_strength_label.place(x=130, y=534-60)
    entry_roof_tensile_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_roof_tensile_strength.place(x=420, y=532-60)

    pillar_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of \nPillar (Stp) [MPa]:",
                                             font=("Inter", 14, "bold"), anchor='w')
    pillar_tensile_strength_label.place(x=130, y=585-60)
    entry_pillar_tensile_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_tensile_strength.place(x=420, y=581-60)

    floor_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of \nImmediate Floor (Stf) [MPa]:",
                                            font=("Inter", 14, "bold"), anchor='w')
    floor_tensile_strength_label.place(x=130, y=641-60)
    entry_floor_tensile_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_tensile_strength.place(x=420, y=637-60)

    roof_modulus_label = tk.Label(frame, text="Young’s Modulus of Roof (Er) [GPa]:", font=("Inter", 14, "bold"))
    roof_modulus_label.place(x=751, y=90-60)
    entry_roof_modulus = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_roof_modulus.place(x=1104, y=86-60)

    floor_modulus_label = tk.Label(frame, text="Young’s Modulus of Floor (Ef) [GPa]:", font=("Inter", 14, "bold"))
    floor_modulus_label.place(x=751, y=117-60)
    entry_floor_modulus = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_modulus.place(x=1104, y=119-60)

    coal_modulus_label = tk.Label(frame, text="Young’s Modulus of Coal (Ec) [GPa]:", font=("Inter", 14, "bold"))
    coal_modulus_label.place(x=751, y=147-60)
    entry_coal_modulus = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_coal_modulus.place(x=1104, y=153-60)

    #roof_permeability_label = tk.Label(frame, text="Permeability of Immediate Roof (Kr) [mD]:",
                                       #font=("Inter", 14, "bold"))
    #roof_permeability_label.place(x=751, y=229-60)
    #entry_roof_permeability = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    #entry_roof_permeability.place(x=1104, y=227-60)



    # Dropdown values
    permeability_values = {"High": 1000, "Medium": 500, "Low": 100}
    # Label for dropdown
    roof_permeability_label = tk.Label(frame, text="Permeability of Immediate Roof (Kr) [mD]:",
                                       font=("Inter", 14, "bold"))
    roof_permeability_label.place(x=751, y=229-60)
    # Entry widget for typing value
    entry_roof_permeability = tk.Entry(frame, width=10, font=("Inter", 14 , "bold"))
    entry_roof_permeability.place(x=1104, y=227-60)
    entry_roof_permeability.configure(state='disabled')  # Initially disabled
    # Dropdown widget
    permeability_dropdown = ttk.Combobox(frame, width=10, values=list(permeability_values.keys()) + ["Type Value"], state='readonly')
    permeability_dropdown.place(x=1104, y=227-60)
    permeability_dropdown.current(0)  # Set default selection
    # Function to enable/disable entry based on dropdown selection
    def enable_entry(event):
        selected_value = permeability_dropdown.get()
        if selected_value == "Type Value":
            permeability_dropdown.place_forget()
            entry_roof_permeability.configure(state='normal')
            entry_roof_permeability.delete(0, tk.END)
        else:
            entry_roof_permeability.configure(state='disabled')
            entry_roof_permeability.delete(0, tk.END)
            entry_roof_permeability.insert(tk.END, permeability_values[permeability_dropdown.get()])
    permeability_dropdown.bind("<<ComboboxSelected>>", enable_entry)
    # Function to show the dropdown widget again if needed
    def show_dropdown(event):
        permeability_dropdown.place(x=1104, y=227-60)
    entry_roof_permeability.bind("<FocusOut>", show_dropdown)
    # Function to get the value of permeability
    def get_permeability():
        if permeability_dropdown.get() == "Type Value":
            return entry_roof_permeability.get()
        else:
            return permeability_values[permeability_dropdown.get()]
    # Example button to print the permeability value
    def print_permeability():
        print(float(get_permeability()))
    print_button = tk.Button(frame, text="Print Permeability", command=print_permeability)
    #print_button.place(x=400, y=100)







    #pillar_permeability_label = tk.Label(frame, text="Permeability of Coal Pillar (Kp) [mD]:",
                                         #font=("Inter", 14, "bold"))
    #pillar_permeability_label.place(x=751, y=260-60)
    #entry_pillar_permeability = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    #entry_pillar_permeability.place(x=1104, y=258-60)

    # Dropdown values
    pillar_permeability_values = {"High": 100, "Medium": 50, "Low": 10}

    # Label for dropdown
    pillar_permeability_label = tk.Label(frame, text="Permeability of Coal Pillar (Kp) [mD]:",
                                         font=("Inter", 14, "bold"))
    pillar_permeability_label.place(x=751, y=200)

    # Entry widget for typing value
    entry_pillar_permeability = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_permeability.place(x=1104, y=200)
    entry_pillar_permeability.configure(state='disabled')  # Initially disabled

    # Dropdown widget
    pillar_permeability_dropdown = ttk.Combobox(frame, width=10,
                                                values=list(pillar_permeability_values.keys()) + ["Type Value"], state='readonly')
    pillar_permeability_dropdown.place(x=1104, y=200)
    pillar_permeability_dropdown.current(0)  # Set default selection

    # Function to enable/disable entry based on dropdown selection
    def enable_entry(event):
        selected_value = pillar_permeability_dropdown.get()
        if selected_value == "Type Value":
            pillar_permeability_dropdown.place_forget()
            entry_pillar_permeability.configure(state='normal')
            entry_pillar_permeability.delete(0, tk.END)
        else:
            entry_pillar_permeability.configure(state='disabled')
            entry_pillar_permeability.delete(0, tk.END)
            entry_pillar_permeability.insert(tk.END, pillar_permeability_values[selected_value])

    pillar_permeability_dropdown.bind("<<ComboboxSelected>>", enable_entry)

    # Function to show the dropdown widget again if needed
    def show_dropdown(event):
        pillar_permeability_dropdown.place(x=1104, y=200)

    entry_pillar_permeability.bind("<FocusOut>", show_dropdown)

    # Function to get the value of permeability
    def get_pillar_permeability():
        if pillar_permeability_dropdown.get() == "Type Value":
            return entry_pillar_permeability.get()
        else:
            return pillar_permeability_values[pillar_permeability_dropdown.get()]

    # Example button to print the permeability value
    def print_pillar_permeability():
        print(float(get_pillar_permeability()))

    print_button = tk.Button(frame, text="Print Permeability", command=print_pillar_permeability)
    #print_button.place(x=900, y=250)

    #floor_permeability_label = tk.Label(frame, text="Permeability of Immediate Floor (Kf) [mD]:",
                                        #font=("Inter", 14, "bold"))
    #floor_permeability_label.place(x=751, y=291-60)
    #entry_floor_permeability = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    #entry_floor_permeability.place(x=1104, y=289-60)

    # For floor permeability

    # Dropdown values
    floor_permeability_values = {"High": 1000, "Medium": 500, "Low": 100}
    # Label for dropdown
    floor_permeability_label = tk.Label(frame, text="Permeability of Immediate Floor (Kf) [mD]:",
                                        font=("Inter", 14, "bold"))
    floor_permeability_label.place(x=751, y=229)

    # Entry widget for typing value
    entry_floor_permeability = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_permeability.place(x=1104, y=229)
    entry_floor_permeability.configure(state='disabled')  # Initially disabled

    # Dropdown widget
    floor_permeability_dropdown = ttk.Combobox(frame, width=10,
                                               values=list(floor_permeability_values.keys()) + ["Type Value"], state='readonly')
    floor_permeability_dropdown.place(x=1104, y=229)
    floor_permeability_dropdown.current(0)  # Set default selection

    # Function to enable/disable entry based on dropdown selection
    def enable_entry_floor(event):
        selected_value = floor_permeability_dropdown.get()
        if selected_value == "Type Value":
            floor_permeability_dropdown.place_forget()
            entry_floor_permeability.configure(state='normal')
            entry_floor_permeability.delete(0, tk.END)
        else:
            entry_floor_permeability.configure(state='disabled')
            entry_floor_permeability.delete(0, tk.END)
            entry_floor_permeability.insert(tk.END, floor_permeability_values[selected_value])

    floor_permeability_dropdown.bind("<<ComboboxSelected>>", enable_entry_floor)

    # Function to show the dropdown widget again if needed
    def show_dropdown_floor(event):
        floor_permeability_dropdown.place(x=1104, y=229)

    entry_floor_permeability.bind("<FocusOut>", show_dropdown_floor)

    # Function to get the value of permeability
    def get_floor_permeability():
        if floor_permeability_dropdown.get() == "Type Value":
            return entry_floor_permeability.get()
        else:
            return floor_permeability_values[floor_permeability_dropdown.get()]

    # Example button to print the permeability value
    def print_floor_permeability():
        print(float(get_floor_permeability()))

    print_button_floor = tk.Button(frame, text="Print Permeability", command=print_floor_permeability)
    #print_button_floor.place(x=900, y=300)










    water_head_label = tk.Label(frame, text='Water Head (H) [m]:', font=("Inter", 14, "bold"))
    water_head_label.place(x=751, y=356-60)
    entry_water_head = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_water_head.place(x=1104, y=350-60)

    roof_influence_label = tk.Label(frame, text='Influence Zone of Immediate Roof (Tr) [m]:',
                                    font=("Inter", 14, "bold"))
    roof_influence_label.place(x=751, y=382-60)
    entry_roof_influence = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_roof_influence.place(x=1104, y=381-60)

    floor_influence_label = tk.Label(frame, text='Influence Zone of Immediate Floor (Tf) [m]:',
                                     font=("Inter", 14, "bold"))
    floor_influence_label.place(x=751, y=409-60)
    entry_floor_influence = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_influence.place(x=1104, y=412-60)



    roof_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Immediate Roof (Shir) [MPa]:",
                                 font=("Inter", 14, "bold"))
    # roof_stress_label.place(x=10, y=410)
    entry_roof_stress = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    # entry_roof_stress.place(x=250, y=410)

    floor_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Immediate Floor (Shif) [MPa]:",
                                  font=("Inter", 14, "bold"))
    # floor_stress_label.place(x=10, y=450)
    entry_floor_stress = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    # entry_floor_stress.place(x=250, y=450)

    pillar_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Pillar (Ship) [MPa]:",
                                   font=("Inter", 14, "bold"))
    # pillar_stress_label.place(x=10, y=490)
    entry_pillar_stress = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    # entry_pillar_stress.place(x=250, y=490)

    '''
    # Define input fields separately
    cover_depth_label = tk.Label(frame, text='Cover Depth (D) [m]:', font=("Helvetica", 12))
    cover_depth_label.grid(row=0, column=0, padx=10, pady=2, sticky='w')
    entry_cover_depth = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_cover_depth.grid(row=0, column=1, padx=10, pady=2)
    #entry_cover_depth.insert(tk.END, '350')

    gallery_width_label = tk.Label(frame, text='Gallery Width (Wg) [m]:', font=("Helvetica", 12))
    gallery_width_label.grid(row=1, column=0, padx=10, pady=2, sticky='w')
    entry_gallery_width = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_gallery_width.grid(row=1, column=1, padx=10, pady=2)

    pillar_width_label = tk.Label(frame, text='Pillar Width (Wp) [m]:', font=("Helvetica", 12))
    pillar_width_label.grid(row=2, column=0, padx=10, pady=2, sticky='w')
    entry_pillar_width = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_width.grid(row=2, column=1, padx=10, pady=2)

    water_head_label = tk.Label(frame, text='Water Head (H) [m]:', font=("Helvetica", 12))
    water_head_label.grid(row=3, column=0, padx=10, pady=2, sticky='w')
    entry_water_head = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_water_head.grid(row=3, column=1, padx=10, pady=2)

    roof_influence_label = tk.Label(frame, text='Influence Zone of Immediate Roof (Tr) [m]:', font=("Helvetica", 12))
    roof_influence_label.grid(row=6, column=0, padx=10, pady=2, sticky='w')
    entry_roof_influence = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_influence.grid(row=6, column=1, padx=10, pady=2)

    pillar_height_label = tk.Label(frame, text='Height of the Coal Pillar (Tp) [m]:', font=("Helvetica", 12))
    pillar_height_label.grid(row=7, column=0, padx=10, pady=2, sticky='w')
    entry_pillar_height = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_height.grid(row=7, column=1, padx=10, pady=2)

    floor_influence_label = tk.Label(frame, text='Influence Zone of Immediate Floor (Tf) [m]:', font=("Helvetica", 12))
    floor_influence_label.grid(row=8, column=0, padx=10, pady=2, sticky='w')
    entry_floor_influence = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_influence.grid(row=8, column=1, padx=10, pady=2)

    roof_modulus_label = tk.Label(frame, text="Young’s Modulus of Roof(Er) [GPa]:", font=("Helvetica", 12))
    roof_modulus_label.grid(row=10, column=0, padx=10, pady=2, sticky='w')
    entry_roof_modulus = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_modulus.grid(row=10, column=1, padx=10, pady=2)

    floor_modulus_label = tk.Label(frame, text="Young’s Modulus of Floor(Ef) [GPa]:", font=("Helvetica", 12))
    floor_modulus_label.grid(row=11, column=0, padx=10, pady=2, sticky='w')
    entry_floor_modulus = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_modulus.grid(row=11, column=1, padx=10, pady=2)

    coal_modulus_label = tk.Label(frame, text="Young’s Modulus of Coal (Ec) [GPa]:", font=("Helvetica", 12))
    coal_modulus_label.grid(row=12, column=0, padx=10, pady=2, sticky='w')
    entry_coal_modulus = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_coal_modulus.grid(row=12, column=1, padx=10, pady=2)

    roof_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Immediate Roof (Shir) [MPa]:",
                                 font=("Helvetica", 12))
    roof_stress_label.grid(row=14, column=0, padx=10, pady=2, sticky='w')
    entry_roof_stress = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_stress.grid(row=14, column=1, padx=10, pady=2)

    floor_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Immediate Floor (Shif) [MPa]:",
                                  font=("Helvetica", 12))
    floor_stress_label.grid(row=15, column=0, padx=10, pady=2, sticky='w')
    entry_floor_stress = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_stress.grid(row=15, column=1, padx=10, pady=2)

    pillar_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Pillar (Ship) [MPa]:", font=("Helvetica", 12))
    pillar_stress_label.grid(row=16, column=0, padx=10, pady=2, sticky='w')
    entry_pillar_stress = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_stress.grid(row=16, column=1, padx=10, pady=2)

    roof_compressive_strength_label = tk.Label(frame, text="Mean Compressive Strength of Immediate Roof (Scr) [MPa]:",
                                               font=("Helvetica", 12))
    roof_compressive_strength_label.grid(row=0, column=3, padx=10, pady=2, sticky='w')
    entry_roof_compressive_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_compressive_strength.grid(row=0, column=4, padx=10, pady=2)

    pillar_compressive_strength_label = tk.Label(frame, text="Mean Compressive Strength of Pillar (Scp) [MPa]:",
                                                 font=("Helvetica", 12))
    pillar_compressive_strength_label.grid(row=1, column=3, padx=10, pady=2, sticky='w')
    entry_pillar_compressive_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_compressive_strength.grid(row=1, column=4, padx=10, pady=2)

    floor_compressive_strength_label = tk.Label(frame, text="Mean Compressive Strength of Immediate Floor (Scf) [MPa]:",
                                                font=("Helvetica", 12))
    floor_compressive_strength_label.grid(row=2, column=3, padx=10, pady=2, sticky='w')
    entry_floor_compressive_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_compressive_strength.grid(row=2, column=4, padx=10, pady=2)

    roof_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of Immediate Roof (Str) [MPa]:",
                                           font=("Helvetica", 12))
    roof_tensile_strength_label.grid(row=4, column=3, padx=10, pady=2, sticky='w')
    entry_roof_tensile_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_tensile_strength.grid(row=4, column=4, padx=10, pady=2)

    pillar_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of Pillar (Stp) [MPa]:",
                                             font=("Helvetica", 12))
    pillar_tensile_strength_label.grid(row=5, column=3, padx=10, pady=2, sticky='w')
    entry_pillar_tensile_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_tensile_strength.grid(row=5, column=4, padx=10, pady=2)

    floor_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of Immediate Floor (Stf) [MPa]:",
                                            font=("Helvetica", 12))
    floor_tensile_strength_label.grid(row=6, column=3, padx=10, pady=2, sticky='w')
    entry_floor_tensile_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_tensile_strength.grid(row=6, column=4, padx=10, pady=2)



    roof_permeability_label = tk.Label(frame, text="Permeability of Immediate Roof (Kr) [mD]:", font=("Helvetica", 12))
    roof_permeability_label.grid(row=8, column=3, padx=10, pady=2, sticky='w')
    entry_roof_permeability = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_permeability.grid(row=8, column=4, padx=10, pady=2)'''
    '''
    # Dropdown values
    permeability_values = {"High": 1000, "Medium": 500, "Low": 100}

    # Label for dropdown
    roof_permeability_label = tk.Label(frame, text="Permeability of Immediate Roof (Kr) [mD]:", font=("Helvetica", 12))
    roof_permeability_label.grid(row=8, column=3, padx=10, pady=2, sticky='w')

    # Dropdown widget
    permeability_dropdown = ttk.Combobox(frame, width=10, values=list(permeability_values.keys()) + ["Type Value"])
    permeability_dropdown.grid(row=8, column=4, padx=10, pady=2)
    permeability_dropdown.current(0)  # Set default selection

    # Entry widget for typing value
    entry_roof_permeability = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_permeability.grid(row=8, column=4, padx=10, pady=5)
    entry_roof_permeability.configure(state='disabled')  # Initially disabled

    # Function to enable/disable entry based on dropdown selection
    def enable_entry(event):
        if permeability_dropdown.get() == "Type Value":
            entry_roof_permeability.configure(state='normal')
            entry_roof_permeability.delete(0, tk.END)
        else:
            entry_roof_permeability.configure(state='disabled')

    permeability_dropdown.bind("<<ComboboxSelected>>", enable_entry)'''


    '''
    pillar_permeability_label = tk.Label(frame, text="Permeability of Coal Pillar (Kp) [mD]:", font=("Helvetica", 12))
    pillar_permeability_label.grid(row=9, column=3, padx=10, pady=2, sticky='w')
    entry_pillar_permeability = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_permeability.grid(row=9, column=4, padx=10, pady=2)

    floor_permeability_label = tk.Label(frame, text="Permeability of Immediate Floor (Kf) [mD]:", font=("Helvetica", 12))
    floor_permeability_label.grid(row=10, column=3, padx=10, pady=2, sticky='w')
    entry_floor_permeability = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_permeability.grid(row=10, column=4, padx=10, pady=2)
    '''
    #in_situ_stress_coal_label = tk.Label(root, text="In situ Horizontal Stress in Coal (Shic) [MPa]:", font=("Helvetica", 18))
    #in_situ_stress_coal_label.grid(row=10, column=3, padx=10, pady=2, sticky='w')
    #entry_in_situ_stress_coal = tk.Entry(root, width=10, font=("Helvetica", 18))
    #entry_in_situ_stress_coal.grid(row=10, column=4, padx=10, pady=2)

    #rock_mass_compressive_strength_label = tk.Label(root, text="Rock Mass Compressive Strength of Coal (Scc) [MPa]:", font=("Helvetica", 18))
    #rock_mass_compressive_strength_label.grid(row=11, column=3, padx=10, pady=2, sticky='w')
    #entry_rock_mass_compressive_strength = tk.Entry(root, width=10, font=("Helvetica", 18))
    #entry_rock_mass_compressive_strength.grid(row=11, column=4, padx=10, pady=2)

    # Default values for each entry field
    default_values = {
        entry_cover_depth: '350',
        entry_gallery_width: '5',
        entry_pillar_width: '10',
        entry_roof_influence: '6',
        entry_pillar_height: '3',
        entry_floor_influence: '6',
        entry_water_head: '350',
        entry_roof_modulus: '3.01',
        entry_floor_modulus: '1',
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
        #entry_roof_permeability: '1000',
        #entry_pillar_permeability: '100',
        #entry_floor_permeability: '1000',
        #entry_in_situ_stress_coal: '5.89',
        #entry_rock_mass_compressive_strength: '2.04'
    }

    def update_roof_influence(event):
        try:
            height_coal_pillar = float(entry_pillar_height.get())
            influence_zone_roof = 2 * height_coal_pillar
            entry_roof_influence.delete(0, tk.END)
            entry_roof_influence.insert(tk.END, str(influence_zone_roof))
            influence_zone_floor = 2 * height_coal_pillar
            entry_floor_influence.delete(0, tk.END)
            entry_floor_influence.insert(tk.END, str(influence_zone_roof))
        except ValueError:
            entry_roof_influence.delete(0, tk.END)
            entry_roof_influence.insert(tk.END, '6')  # Default value if input is invalid
            entry_floor_influence.delete(0, tk.END)
            entry_floor_influence.insert(tk.END, '6')  # Default value if input is invalid

    # Function to update the water head dynamically
    def update_water_head(event):
        try:
            cover_depth = float(entry_cover_depth.get())
            water_head = cover_depth
            entry_water_head.delete(0, tk.END)
            entry_water_head.insert(tk.END, str(water_head))
        except ValueError:
            entry_water_head.delete(0, tk.END)
            entry_water_head.insert(tk.END, '350')  # Default value if input is invalid

    # Bind the update function to the pillar height entry field
    entry_pillar_height.bind("<KeyRelease>", update_roof_influence)
    entry_cover_depth.bind("<KeyRelease>", update_water_head)

    # Add default values to each entry field
    for entry_widget, default_value in default_values.items():
        entry_widget.insert(tk.END, default_value)

    def calculate_values():
        print_permeability()

        #print_permeability()
        # Retrieve values from input fields and convert them to float
        cover_depth = float(entry_cover_depth.get())
        gallery_width = float(entry_gallery_width.get())
        pillar_width = float(entry_pillar_width.get())
        influence_zone_roof = float(entry_roof_influence.get())
        height_coal_pillar = float(entry_pillar_height.get())
        influence_zone_floor = float(entry_floor_influence.get())
        water_head = float(entry_water_head.get())
        youngs_modulus_roof = float(entry_roof_modulus.get())
        youngs_modulus_floor = float(entry_floor_modulus.get())

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
        #permeability_roof = float(entry_roof_permeability.get())
        permeability_roof = float(get_permeability())
        #permeability_pillar = float(entry_pillar_permeability.get())
        permeability_pillar =float(get_pillar_permeability())
        #permeability_floor = float(entry_floor_permeability.get())
        permeability_floor = float(get_floor_permeability())
        #in_situ_horizontal_stress_coal = float(entry_in_situ_stress_coal.get())
        #rock_mass_compressive_strength_coal = float(entry_rock_mass_compressive_strength.get())

        # Pass the values to calculate_all function
        calculate_all1(cover_depth, gallery_width, pillar_width, influence_zone_roof, height_coal_pillar,
                      influence_zone_floor, water_head, youngs_modulus_roof, youngs_modulus_floor, youngs_modulus_coal,
                      mean_horizontal_stress_roof, mean_horizontal_stress_pillar, mean_horizontal_stress_floor,
                      mean_compressive_strength_roof, mean_compressive_strength_pillar,
                      mean_compressive_strength_floor, mean_tensile_strength_roof, mean_tensile_strength_pillar,
                      mean_tensile_strength_floor, permeability_roof, permeability_pillar, permeability_floor,
                      )

    #calculate_button.grid(row=24, column=0, columnspan=2, padx=10, pady=5, sticky="we")

    # Calculated values label
    #global calculated_values_label
    #calculated_values_label = tk.Label(root, text="Calculated Values:\n\n")
    #calculated_values_label.grid(row=1, column=2, rowspan=10, padx=10, pady=10, sticky="nswe")

    calculate_button = tk.Button(frame, text="Calculate", command=calculate_values, width=20, height=2)

    def press_buttons():
        calculate_button.invoke()
        gui_test2(notebook)
        #os.system("python test2.py")  # Execute test2.py after simulating button click

    # Create the r-button
    #r_button = tk.Button(frame, text="Rationalise the Width of PWBP", command=press_buttons, width=20, height=2,
                        # font=("Helvetica", 12))
    #r_button.grid(row=20, column=3, columnspan=2, padx=10, pady=5, sticky="we")

    # Exit button
    #exit_button = tk.Button(frame, text="Quit", command=frame.quit, width=20, height=2, font=("Helvetica", 12))
    #exit_button.grid(row=21, column=3, columnspan=2, padx=10, pady=10, sticky="we")

    # Create the r-button
    r_button = tk.Button(frame, text="Rationalise the Width of PWBP", command=press_buttons, width=30, height =2,
                         font=("Inter", 14))
    r_button.place(x=850, y=549-60)

    # Close the Program button
    # close_button = tk.Button(root, text="Close the Steps", command=close_programs)
    # close_button.grid(row=len(labels) + 2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

    # Create an Exit button
    exit_button = tk.Button(frame, text="Quit", command=frame.quit, width=30, height =2 , font=("Inter", 14))
    exit_button.place(x=850, y=615-60)

    # Configure grid weights for responsive resizing
    #frame.grid_rowconfigure(11, weight=1)
    #frame.grid_columnconfigure(2, weight=1)

    #root.attributes('-fullscreen', True)  # Start in fullscreen mode
    # Set window size and position to fullscreen with 1920x1080 resolution
    #root.attributes('-fullscreen', True)
    #frame.geometry("1366x768")
    #frame.resizable(False, False)
    #root.geometry("1920x1080")

    # Set the window state to maximized (zoomed)
    #root.wm_state('zoomed')

def existing_pwbp(notebook):
    # Check if 'Next Screen' tab already exists
    for tab_id in notebook.tabs():
        if notebook.tab(tab_id, "text") == 'Design of Existing PWBP':
            notebook.select(tab_id)  # Switch to the existing tab
            return  # Exit the function if tab already exists

    # Create the new tab
    new_tab = ttk.Frame(notebook)
    notebook.add(new_tab, text="Design of Existing PWBP")
    notebook.select(new_tab)  # Switch to the new tab

    # Populate new pwbp tab
    frame = ttk.Frame(new_tab, padding=20)
    frame.pack(fill=tk.BOTH, expand=True)

    #frame = tk.Tk()
    #frame.title("Design of Existing PWBP")
    # Define input fields separately using place for exact positioning
    cover_depth_label = tk.Label(frame, text='Cover Depth (D) [m]:', font=("Inter", 14, "bold"))
    cover_depth_label.place(x=130, y=90 - 60)
    entry_cover_depth = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_cover_depth.place(x=420, y=90 - 60)

    pillar_height_label = tk.Label(frame, text='Height of the Coal Pillar (Tp) [m]:', font=("Inter", 14, "bold"))
    pillar_height_label.place(x=130, y=117 - 60)
    entry_pillar_height = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_height.place(x=420, y=117 - 60)

    pillar_width_label = tk.Label(frame, text='Pillar Width (Wp) [m]:', font=("Inter", 14, "bold"))
    pillar_width_label.place(x=130, y=145 - 60)
    entry_pillar_width = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_width.place(x=420, y=145 - 60)

    gallery_width_label = tk.Label(frame, text='Gallery Width (Wg) [m]:', font=("Inter", 14, "bold"))
    gallery_width_label.place(x=130, y=175 - 60)
    entry_gallery_width = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_gallery_width.place(x=420, y=175 - 60)

    roof_RQD_label = tk.Label(frame, text="RQD of Immediate Roof :", font=("Inter", 14, "bold"))
    roof_RQD_label.place(x=130, y=230 - 60)
    entry_roof_RQD = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_roof_RQD.place(x=420, y=227 - 60)

    floor_RQD_label = tk.Label(frame, text="RQD of Immediate Floor :", font=("Inter", 14, "bold"))
    floor_RQD_label.place(x=130, y=257 - 60)
    entry_floor_RQD = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_RQD.place(x=420, y=258 - 60)

    pillar_RQD_label = tk.Label(frame, text="RQD of Pillar :", font=("Inter", 14, "bold"))
    pillar_RQD_label.place(x=130, y=285 - 60)
    entry_pillar_RQD = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_RQD.place(x=420, y=289 - 60)

    roof_compressive_strength_label = tk.Label(frame, text="Mean Compressive Strength of \nImmediate Roof (Scr) [MPa]:",
                                               font=("Inter", 14, "bold"), anchor='w')
    roof_compressive_strength_label.place(x=130, y=354 - 60)
    entry_roof_compressive_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_roof_compressive_strength.place(x=420, y=350 - 60)

    pillar_compressive_strength_label = tk.Label(frame, text="Mean Compressive Strength of \nPillar (Scp) [MPa]:",
                                                 font=("Inter", 14, "bold"), anchor='w')
    pillar_compressive_strength_label.place(x=130, y=400 - 60)
    entry_pillar_compressive_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_compressive_strength.place(x=420, y=398 - 60)

    floor_compressive_strength_label = tk.Label(frame,
                                                text="Mean Compressive Strength of \nImmediate Floor (Scf) [MPa]:",
                                                font=("Inter", 14, "bold"), anchor='w')
    floor_compressive_strength_label.place(x=130, y=446 - 60)
    entry_floor_compressive_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_compressive_strength.place(x=420, y=444 - 60)

    roof_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of \nImmediate Roof (Str) [MPa]:",
                                           font=("Inter", 14, "bold"), anchor='w')
    roof_tensile_strength_label.place(x=130, y=534 - 60)
    entry_roof_tensile_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_roof_tensile_strength.place(x=420, y=532 - 60)

    pillar_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of \nPillar (Stp) [MPa]:",
                                             font=("Inter", 14, "bold"), anchor='w')
    pillar_tensile_strength_label.place(x=130, y=585 - 60)
    entry_pillar_tensile_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_tensile_strength.place(x=420, y=581 - 60)

    floor_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of \nImmediate Floor (Stf) [MPa]:",
                                            font=("Inter", 14, "bold"), anchor='w')
    floor_tensile_strength_label.place(x=130, y=641 - 60)
    entry_floor_tensile_strength = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_tensile_strength.place(x=420, y=637 - 60)

    roof_modulus_label = tk.Label(frame, text="Young’s Modulus of Roof (Er) [GPa]:", font=("Inter", 14, "bold"))
    roof_modulus_label.place(x=751, y=90 - 60)
    entry_roof_modulus = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_roof_modulus.place(x=1104, y=86 - 60)

    floor_modulus_label = tk.Label(frame, text="Young’s Modulus of Floor (Ef) [GPa]:", font=("Inter", 14, "bold"))
    floor_modulus_label.place(x=751, y=117 - 60)
    entry_floor_modulus = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_modulus.place(x=1104, y=119 - 60)

    coal_modulus_label = tk.Label(frame, text="Young’s Modulus of Coal (Ec) [GPa]:", font=("Inter", 14, "bold"))
    coal_modulus_label.place(x=751, y=147 - 60)
    entry_coal_modulus = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_coal_modulus.place(x=1104, y=153 - 60)


    # Dropdown values
    permeability_values = {"High": 1000, "Medium": 500, "Low": 100}
    # Label for dropdown
    roof_permeability_label = tk.Label(frame, text="Permeability of Immediate Roof (Kr) [mD]:",
                                       font=("Inter", 14, "bold"))
    roof_permeability_label.place(x=751, y=229-60)
    # Entry widget for typing value
    entry_roof_permeability = tk.Entry(frame, width=10, font=("Inter", 14 , "bold"))
    entry_roof_permeability.place(x=1104, y=227-60)
    entry_roof_permeability.configure(state='disabled')  # Initially disabled
    # Dropdown widget
    permeability_dropdown = ttk.Combobox(frame, width=10, values=list(permeability_values.keys()) + ["Type Value"], state='readonly')
    permeability_dropdown.place(x=1104, y=227-60)
    permeability_dropdown.current(0)  # Set default selection
    # Function to enable/disable entry based on dropdown selection
    def enable_entry(event):
        selected_value = permeability_dropdown.get()
        if selected_value == "Type Value":
            permeability_dropdown.place_forget()
            entry_roof_permeability.configure(state='normal')
            entry_roof_permeability.delete(0, tk.END)
        else:
            entry_roof_permeability.configure(state='disabled')
            entry_roof_permeability.delete(0, tk.END)
            entry_roof_permeability.insert(tk.END, permeability_values[permeability_dropdown.get()])
    permeability_dropdown.bind("<<ComboboxSelected>>", enable_entry)
    # Function to show the dropdown widget again if needed
    def show_dropdown(event):
        permeability_dropdown.place(x=1104, y=227-60)
    entry_roof_permeability.bind("<FocusOut>", show_dropdown)
    # Function to get the value of permeability
    def get_permeability():
        if permeability_dropdown.get() == "Type Value":
            return entry_roof_permeability.get()
        else:
            return permeability_values[permeability_dropdown.get()]
    # Example button to print the permeability value
    def print_permeability():
        print(float(get_permeability()))
    print_button = tk.Button(frame, text="Print Permeability", command=print_permeability)
    #print_button.place(x=400, y=100)







    #pillar_permeability_label = tk.Label(frame, text="Permeability of Coal Pillar (Kp) [mD]:",
                                         #font=("Inter", 14, "bold"))
    #pillar_permeability_label.place(x=751, y=260-60)
    #entry_pillar_permeability = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    #entry_pillar_permeability.place(x=1104, y=258-60)

    # Dropdown values
    pillar_permeability_values = {"High": 100, "Medium": 50, "Low": 10}

    # Label for dropdown
    pillar_permeability_label = tk.Label(frame, text="Permeability of Coal Pillar (Kp) [mD]:",
                                         font=("Inter", 14, "bold"))
    pillar_permeability_label.place(x=751, y=200)

    # Entry widget for typing value
    entry_pillar_permeability = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_pillar_permeability.place(x=1104, y=200)
    entry_pillar_permeability.configure(state='disabled')  # Initially disabled

    # Dropdown widget
    pillar_permeability_dropdown = ttk.Combobox(frame, width=10,
                                                values=list(pillar_permeability_values.keys()) + ["Type Value"], state='readonly')
    pillar_permeability_dropdown.place(x=1104, y=200)
    pillar_permeability_dropdown.current(0)  # Set default selection

    # Function to enable/disable entry based on dropdown selection
    def enable_entry(event):
        selected_value = pillar_permeability_dropdown.get()
        if selected_value == "Type Value":
            pillar_permeability_dropdown.place_forget()
            entry_pillar_permeability.configure(state='normal')
            entry_pillar_permeability.delete(0, tk.END)
        else:
            entry_pillar_permeability.configure(state='disabled')
            entry_pillar_permeability.delete(0, tk.END)
            entry_pillar_permeability.insert(tk.END, pillar_permeability_values[selected_value])

    pillar_permeability_dropdown.bind("<<ComboboxSelected>>", enable_entry)

    # Function to show the dropdown widget again if needed
    def show_dropdown(event):
        pillar_permeability_dropdown.place(x=1104, y=200)

    entry_pillar_permeability.bind("<FocusOut>", show_dropdown)

    # Function to get the value of permeability
    def get_pillar_permeability():
        if pillar_permeability_dropdown.get() == "Type Value":
            return entry_pillar_permeability.get()
        else:
            return pillar_permeability_values[pillar_permeability_dropdown.get()]

    # Example button to print the permeability value
    def print_pillar_permeability():
        print(float(get_pillar_permeability()))

    print_button = tk.Button(frame, text="Print Permeability", command=print_pillar_permeability)
    #print_button.place(x=900, y=250)

    #floor_permeability_label = tk.Label(frame, text="Permeability of Immediate Floor (Kf) [mD]:",
                                        #font=("Inter", 14, "bold"))
    #floor_permeability_label.place(x=751, y=291-60)
    #entry_floor_permeability = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    #entry_floor_permeability.place(x=1104, y=289-60)

    # For floor permeability

    # Dropdown values
    floor_permeability_values = {"High": 1000, "Medium": 500, "Low": 100}
    # Label for dropdown
    floor_permeability_label = tk.Label(frame, text="Permeability of Immediate Floor (Kf) [mD]:",
                                        font=("Inter", 14, "bold"))
    floor_permeability_label.place(x=751, y=229)

    # Entry widget for typing value
    entry_floor_permeability = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_permeability.place(x=1104, y=229)
    entry_floor_permeability.configure(state='disabled')  # Initially disabled

    # Dropdown widget
    floor_permeability_dropdown = ttk.Combobox(frame, width=10,
                                               values=list(floor_permeability_values.keys()) + ["Type Value"], state='readonly')
    floor_permeability_dropdown.place(x=1104, y=229)
    floor_permeability_dropdown.current(0)  # Set default selection

    # Function to enable/disable entry based on dropdown selection
    def enable_entry_floor(event):
        selected_value = floor_permeability_dropdown.get()
        if selected_value == "Type Value":
            floor_permeability_dropdown.place_forget()
            entry_floor_permeability.configure(state='normal')
            entry_floor_permeability.delete(0, tk.END)
        else:
            entry_floor_permeability.configure(state='disabled')
            entry_floor_permeability.delete(0, tk.END)
            entry_floor_permeability.insert(tk.END, floor_permeability_values[selected_value])

    floor_permeability_dropdown.bind("<<ComboboxSelected>>", enable_entry_floor)

    # Function to show the dropdown widget again if needed
    def show_dropdown_floor(event):
        floor_permeability_dropdown.place(x=1104, y=229)

    entry_floor_permeability.bind("<FocusOut>", show_dropdown_floor)

    # Function to get the value of permeability
    def get_floor_permeability():
        if floor_permeability_dropdown.get() == "Type Value":
            return entry_floor_permeability.get()
        else:
            return floor_permeability_values[floor_permeability_dropdown.get()]

    # Example button to print the permeability value
    def print_floor_permeability():
        print(float(get_floor_permeability()))

    print_button_floor = tk.Button(frame, text="Print Permeability", command=print_floor_permeability)
    #print_button_floor.place(x=900, y=300)






    water_head_label = tk.Label(frame, text='Water Head (H) [m]:', font=("Inter", 14, "bold"))
    water_head_label.place(x=751, y=356 - 60)
    entry_water_head = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_water_head.place(x=1104, y=350 - 60)

    roof_influence_label = tk.Label(frame, text='Influence Zone of Immediate Roof (Tr) [m]:',
                                    font=("Inter", 14, "bold"))
    roof_influence_label.place(x=751, y=382 - 60)
    entry_roof_influence = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_roof_influence.place(x=1104, y=381 - 60)

    floor_influence_label = tk.Label(frame, text='Influence Zone of Immediate Floor (Tf) [m]:',
                                     font=("Inter", 14, "bold"))
    floor_influence_label.place(x=751, y=409 - 60)
    entry_floor_influence = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    entry_floor_influence.place(x=1104, y=412 - 60)

    roof_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Immediate Roof (Shir) [MPa]:",
                                 font=("Inter", 14, "bold"))
    # roof_stress_label.place(x=10, y=410)
    entry_roof_stress = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    # entry_roof_stress.place(x=250, y=410)

    floor_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Immediate Floor (Shif) [MPa]:",
                                  font=("Inter", 14, "bold"))
    # floor_stress_label.place(x=10, y=450)
    entry_floor_stress = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    # entry_floor_stress.place(x=250, y=450)

    pillar_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Pillar (Ship) [MPa]:",
                                   font=("Inter", 14, "bold"))
    # pillar_stress_label.place(x=10, y=490)
    entry_pillar_stress = tk.Entry(frame, width=10, font=("Inter", 14, "bold"))
    # entry_pillar_stress.place(x=250, y=490)







    '''# Define input fields separately
    cover_depth_label = tk.Label(frame, text='Cover Depth (D) [m]:', font=("Helvetica", 12))
    cover_depth_label.grid(row=0, column=0, padx=10, pady=2, sticky='w')
    entry_cover_depth = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_cover_depth.grid(row=0, column=1, padx=10, pady=2)
    # entry_cover_depth.insert(tk.END, '350')

    gallery_width_label = tk.Label(frame, text='Gallery Width (Wg) [m]:', font=("Helvetica", 12))
    gallery_width_label.grid(row=3, column=0, padx=10, pady=2, sticky='w')
    entry_gallery_width = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_gallery_width.grid(row=3, column=1, padx=10, pady=2)

    pillar_width_label = tk.Label(frame, text='Pillar Width (Wp) [m]:', font=("Helvetica", 12))
    pillar_width_label.grid(row=2, column=0, padx=10, pady=2, sticky='w')
    entry_pillar_width = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_width.grid(row=2, column=1, padx=10, pady=2)

    water_head_label = tk.Label(frame, text='Water Head (H) [m]:', font=("Helvetica", 12))
    water_head_label.grid(row=3, column=0, padx=10, pady=2, sticky='w')
    entry_water_head = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_water_head.grid(row=3, column=1, padx=10, pady=2)

    roof_influence_label = tk.Label(frame, text='Influence Zone of Immediate Roof (Tr) [m]:', font=("Helvetica", 12))
    roof_influence_label.grid(row=6, column=0, padx=10, pady=2, sticky='w')
    entry_roof_influence = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_influence.grid(row=6, column=1, padx=10, pady=2)

    pillar_height_label = tk.Label(frame, text='Height of the Pillar (Tp) [m]:', font=("Helvetica", 12))
    pillar_height_label.grid(row=1, column=0, padx=10, pady=2, sticky='w')
    entry_pillar_height = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_height.grid(row=1, column=1, padx=10, pady=2)

    floor_influence_label = tk.Label(frame, text='Influence Zone of Immediate Floor (Tf) [m]:', font=("Helvetica", 12))
    floor_influence_label.grid(row=8, column=0, padx=10, pady=2, sticky='w')
    entry_floor_influence = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_influence.grid(row=8, column=1, padx=10, pady=2)

    roof_modulus_label = tk.Label(frame, text="Young’s Modulus of Roof(Er) [GPa]:", font=("Helvetica", 12))
    roof_modulus_label.grid(row=10, column=0, padx=10, pady=2, sticky='w')
    entry_roof_modulus = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_modulus.grid(row=10, column=1, padx=10, pady=2)

    floor_modulus_label = tk.Label(frame, text="Young’s Modulus of Floor(Ef) [GPa]:", font=("Helvetica", 12))
    floor_modulus_label.grid(row=11, column=0, padx=10, pady=2, sticky='w')
    entry_floor_modulus = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_modulus.grid(row=11, column=1, padx=10, pady=2)

    coal_modulus_label = tk.Label(frame, text="Young’s Modulus of Coal (Ec) [GPa]:", font=("Helvetica", 12))
    coal_modulus_label.grid(row=12, column=0, padx=10, pady=2, sticky='w')
    entry_coal_modulus = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_coal_modulus.grid(row=12, column=1, padx=10, pady=2)

    roof_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Immediate Roof (Shir) [MPa]:",
                                 font=("Helvetica", 12))
    roof_stress_label.grid(row=14, column=0, padx=10, pady=2, sticky='w')
    entry_roof_stress = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_stress.grid(row=14, column=1, padx=10, pady=2)

    floor_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Immediate Floor (Shif) [MPa]:",
                                  font=("Helvetica", 12))
    floor_stress_label.grid(row=15, column=0, padx=10, pady=2, sticky='w')
    entry_floor_stress = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_stress.grid(row=15, column=1, padx=10, pady=2)

    pillar_stress_label = tk.Label(frame, text="Mean Horizontal Stress in Pillar (Ship) [MPa]:", font=("Helvetica", 12))
    pillar_stress_label.grid(row=16, column=0, padx=10, pady=2, sticky='w')
    entry_pillar_stress = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_stress.grid(row=16, column=1, padx=10, pady=2)

    roof_compressive_strength_label = tk.Label(frame, text="Mean Compressive Strength of Immediate Roof (Scr) [MPa]:",
                                               font=("Helvetica", 12))
    roof_compressive_strength_label.grid(row=0, column=3, padx=10, pady=2, sticky='w')
    entry_roof_compressive_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_compressive_strength.grid(row=0, column=4, padx=10, pady=2)

    pillar_compressive_strength_label = tk.Label(frame, text="Mean Compressive Strength of Pillar (Scp) [MPa]:",
                                                 font=("Helvetica", 12))
    pillar_compressive_strength_label.grid(row=1, column=3, padx=10, pady=2, sticky='w')
    entry_pillar_compressive_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_compressive_strength.grid(row=1, column=4, padx=10, pady=2)

    floor_compressive_strength_label = tk.Label(frame, text="Mean Compressive Strength of Immediate Floor (Scf) [MPa]:",
                                                font=("Helvetica", 12))
    floor_compressive_strength_label.grid(row=2, column=3, padx=10, pady=2, sticky='w')
    entry_floor_compressive_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_compressive_strength.grid(row=2, column=4, padx=10, pady=2)

    roof_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of Immediate Roof (Str) [MPa]:",
                                           font=("Helvetica", 12))
    roof_tensile_strength_label.grid(row=4, column=3, padx=10, pady=2, sticky='w')
    entry_roof_tensile_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_tensile_strength.grid(row=4, column=4, padx=10, pady=2)

    pillar_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of Pillar (Stp) [MPa]:",
                                             font=("Helvetica", 12))
    pillar_tensile_strength_label.grid(row=5, column=3, padx=10, pady=2, sticky='w')
    entry_pillar_tensile_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_tensile_strength.grid(row=5, column=4, padx=10, pady=2)

    floor_tensile_strength_label = tk.Label(frame, text="Mean Tensile Strength of Immediate Floor (Stf) [MPa]:",font=("Helvetica", 12))
    floor_tensile_strength_label.grid(row=6, column=3, padx=10, pady=2, sticky='w')
    entry_floor_tensile_strength = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_tensile_strength.grid(row=6, column=4, padx=10, pady=2)

    roof_permeability_label = tk.Label(frame, text="Permeability of Immediate Roof (Kr) [mD]:", font=("Helvetica", 12))
    roof_permeability_label.grid(row=8, column=3, padx=10, pady=2, sticky='w')
    entry_roof_permeability = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_roof_permeability.grid(row=8, column=4, padx=10, pady=2)

    pillar_permeability_label = tk.Label(frame, text="Permeability of Coal Pillar (Kp) [mD]:", font=("Helvetica", 12))
    pillar_permeability_label.grid(row=9, column=3, padx=10, pady=2, sticky='w')
    entry_pillar_permeability = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_pillar_permeability.grid(row=9, column=4, padx=10, pady=2)

    floor_permeability_label = tk.Label(frame, text="Permeability of Immediate Floor (Kf) [mD]:", font=("Helvetica", 12))
    floor_permeability_label.grid(row=10, column=3, padx=10, pady=2, sticky='w')
    entry_floor_permeability = tk.Entry(frame, width=10, font=("Helvetica", 12))
    entry_floor_permeability.grid(row=10, column=4, padx=10, pady=2)'''

    # Default values for each entry field
    default_values = {
        entry_cover_depth: '350',
        entry_gallery_width: '5',
        entry_pillar_width: '10',
        entry_roof_influence: '6',
        entry_pillar_height: '3',
        entry_floor_influence: '6',
        entry_water_head: '350',
        entry_roof_modulus: '3.01',
        entry_floor_modulus: '1',
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
        # entry_roof_permeability: '1000',
        # entry_pillar_permeability: '100',
        # entry_floor_permeability: '1000',
        # entry_in_situ_stress_coal: '5.89',
        # entry_rock_mass_compressive_strength: '2.04'
    }



    def update_roof_influence(event):
        try:
            height_coal_pillar = float(entry_pillar_height.get())
            influence_zone_roof = 2 * height_coal_pillar
            entry_roof_influence.delete(0, tk.END)
            entry_roof_influence.insert(tk.END, str(influence_zone_roof))
            influence_zone_floor = 2 * height_coal_pillar
            entry_floor_influence.delete(0, tk.END)
            entry_floor_influence.insert(tk.END, str(influence_zone_roof))
        except ValueError:
            entry_roof_influence.delete(0, tk.END)
            entry_roof_influence.insert(tk.END, '6')  # Default value if input is invalid
            entry_floor_influence.delete(0, tk.END)
            entry_floor_influence.insert(tk.END, '6')  # Default value if input is invalid

    # Function to update the water head dynamically
    def update_water_head(event):
        try:
            cover_depth = float(entry_cover_depth.get())
            water_head = cover_depth
            entry_water_head.delete(0, tk.END)
            entry_water_head.insert(tk.END, str(water_head))
        except ValueError:
            entry_water_head.delete(0, tk.END)
            entry_water_head.insert(tk.END, '350')  # Default value if input is invalid

    # Bind the update function to the pillar height entry field
    entry_pillar_height.bind("<KeyRelease>", update_roof_influence)
    entry_cover_depth.bind("<KeyRelease>", update_water_head)

    # Add default values to each entry field
    for entry_widget, default_value in default_values.items():
        entry_widget.insert(tk.END, default_value)

    def calculate_values():
        print_permeability()

        #print_permeability()
        # Retrieve values from input fields and convert them to float
        cover_depth = float(entry_cover_depth.get())
        gallery_width = float(entry_gallery_width.get())
        pillar_width = float(entry_pillar_width.get())
        influence_zone_roof = float(entry_roof_influence.get())
        height_coal_pillar = float(entry_pillar_height.get())
        influence_zone_floor = float(entry_floor_influence.get())
        water_head = float(entry_water_head.get())
        youngs_modulus_roof = float(entry_roof_modulus.get())
        youngs_modulus_floor = float(entry_floor_modulus.get())

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
        #permeability_roof = float(entry_roof_permeability.get())
        permeability_roof = float(get_permeability())
        #permeability_pillar = float(entry_pillar_permeability.get())
        permeability_pillar =float(get_pillar_permeability())
        #permeability_floor = float(entry_floor_permeability.get())
        permeability_floor = float(get_floor_permeability())
        #in_situ_horizontal_stress_coal = float(entry_in_situ_stress_coal.get())
        #rock_mass_compressive_strength_coal = float(entry_rock_mass_compressive_strength.get())

        # Pass the values to calculate_all function
        calculate_all2(cover_depth, gallery_width, pillar_width, influence_zone_roof, height_coal_pillar,
                      influence_zone_floor, water_head, youngs_modulus_roof, youngs_modulus_floor, youngs_modulus_coal,
                      mean_horizontal_stress_roof, mean_horizontal_stress_pillar, mean_horizontal_stress_floor,
                      mean_compressive_strength_roof, mean_compressive_strength_pillar,
                      mean_compressive_strength_floor, mean_tensile_strength_roof, mean_tensile_strength_pillar,
                      mean_tensile_strength_floor, permeability_roof, permeability_pillar, permeability_floor)

    # Create the "Calculate" button
    calculate_button = tk.Button(frame, text="Adequacy Assessment", command=calculate_values, width=25, height=2,
                                 font=("Helvetica", 14))
    calculate_button.place(x = 850 , y = 500-60)

    # Create calculated values display
    # global calculated_values_label
    # calculated_values_label = tk.Label(root, text="Calculated Values:\n\n", justify="left")
    # calculated_values_label.grid(row=0, column=2, rowspan=10, padx=10, pady=5, sticky='nsew')



    # Create the r-button
    r_button = tk.Button(frame, text="Rationalise the Width of PWBP", command=lambda: gui_test2(notebook), width=25, height=2,
                         font=("Helvetica", 14))
    r_button.place(x=850, y=550-60)

    # Close the Program button
    # close_button = tk.Button(root, text="Close the Steps", command=close_programs)
    # close_button.grid(row=len(labels) + 2, column=0, columnspan=2, padx=10, pady=10, sticky="we")

    # Create an Exit button
    exit_button = tk.Button(frame, text="Quit", command=frame.quit, width=25 ,height=2 ,  font=("Helvetica", 14))
    exit_button.place(x=850, y=600-60)

    # Configure column weights
    #frame.grid_columnconfigure(0, weight=1)
    #frame.grid_columnconfigure(1, weight=1)
    #frame.grid_columnconfigure(2, weight=2)

    # root.attributes('-fullscreen', True)  # Start in fullscreen mode

    # Set window size and position to fullscreen with 1920x1080 resolution
    # root.attributes('-fullscreen', True)
    #frame.geometry("1366x768")
    #frame.resizable(False, False)
    #root.geometry("1920x1080")

    # Set the window state to maximized (zoomed)
    #root.wm_state('zoomed')
def open_next_screen(notebook):
    # Check if 'Next Screen' tab already exists
    for tab_id in notebook.tabs():
        if notebook.tab(tab_id, "text") == 'Next Screen':
            notebook.select(tab_id)  # Switch to the existing tab
            return  # Exit the function if tab already exists

    # Create the new tab
    new_tab = ttk.Frame(notebook)
    notebook.add(new_tab, text='Next Screen')
    notebook.select(new_tab)  # Switch to the new tab

    # Populate Next Screen tab
    frame = ttk.Frame(new_tab, padding=20)
    frame.pack(fill=tk.BOTH, expand=True)

    # Title label
    #label_title = ttk.Label(frame, text="   Hydro-mechanical performance of \n Protective Water Barrier pillar (PWBP)",
                            #font=("Arial", 35, "bold"))
    #label_title.pack(pady=20)

    # Title label
    #label_title2 = ttk.Label(frame, text="Select Type of PWBP:", font=("Arial", 28, "bold"))
    #label_title2.pack(pady=30)
    #label_title2.place(x=855, y=270)

    # Set the window size
    window_width = 1366
    window_height = 786

    # Button to open New PWBP
    btn_new_pwbp = tk.Button(frame, text="Design of New Barrier", command=lambda: new_pwbp(notebook), width=40,
                             height=3, font=("Helvetica", 18))
    btn_new_pwbp.place(x=(window_width - btn_new_pwbp.winfo_reqwidth()) // 2, y=(window_height - 200) // 2 - 100)

    # Button to open Existing PWBP
    btn_existing_pwbp = tk.Button(frame, text="Design of Existing Barrier", command=lambda: existing_pwbp(notebook),
                                  width=40, height=3, font=("Helvetica", 18))
    btn_existing_pwbp.place(x=(window_width - btn_existing_pwbp.winfo_reqwidth()) // 2, y=(window_height - 200) // 2)

    # Exit button
    btn_exit = tk.Button(frame, text="Quit", command=exit_program, width=40, height=3, font=("Helvetica", 18))
    btn_exit.place(x=(window_width - btn_exit.winfo_reqwidth()) // 2, y=(window_height - 200) // 2 + 100)
    '''
    #Button to open New PWBP
    btn_new_pwbp = tk.Button(frame, text="Design of New Barrier", command=lambda: new_pwbp(notebook), width=40, height=3, font=("Helvetica", 18))
    btn_new_pwbp.pack(pady=10)
    btn_new_pwbp.place(x=400, y=293)


    # Button to open Existing PWBP
    btn_existing_pwbp = tk.Button(frame, text="Design of Existing Barrier", command=lambda: existing_pwbp(notebook), width=40, height=3, font=("Helvetica", 18))
    btn_existing_pwbp.pack(pady=10)
    btn_existing_pwbp.place(x=400, y=393)

    # Exit button
    btn_exit = tk.Button(frame, text="Quit", command=exit_program, width=40, height=3, font=("Helvetica", 18))
    btn_exit.pack(pady=20)
    btn_exit.place(x=400, y=493)'''


    # Footer frame
    footer_frame = tk.Frame(frame, bg='lightgray', height=30)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

    # Copyright text
    current_year = datetime.now().year
    copyright_text = f"© {current_year} Mining Department, IIT BHU. All rights reserved."
    copyright_label = tk.Label(footer_frame, text=copyright_text, font=("Arial", 10), fg='gray', bg='lightgray')
    copyright_label.pack(side=tk.RIGHT, padx=10, pady=5)




def exit_program():
    global root
    root.destroy()
    os._exit(0)

def create_gui():
    global root
    root = tk.Tk()
    root.title("Design of Protective Water Barrier Pillar (PWBP)")

    # Set window size and position to fullscreen with 1366x768 resolution
    root.geometry("1366x768")
    root.resizable(False, False)

    # Create a notebook for tabs
    notebook = ttk.Notebook(root)
    notebook.pack(fill=tk.BOTH, expand=True)

    # Create frame for the initial tab
    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text='Home')

    # Populate Home tab
    frame1 = ttk.Frame(tab1)
    frame1.pack(fill=tk.BOTH, expand=True)

    # Load the image file
    image_path = "IITlogo.png"
    original_image = Image.open(image_path)
    resized_image = original_image.resize((original_image.width // 2, original_image.height // 2), Image.LANCZOS)
    photo = ImageTk.PhotoImage(resized_image)
    label = tk.Label(tab1, image=photo)
    label.photo = photo  # Keep a reference to avoid garbage collection
    label.place(x=20, y=20)

    image_path2 = "ECLlogo.png"
    original_image2 = Image.open(image_path2)
    resized_image2 = original_image2.resize((original_image2.width // 2, original_image2.height // 2), Image.LANCZOS)
    photo2 = ImageTk.PhotoImage(resized_image2)
    label2 = tk.Label(tab1, image=photo2)
    label2.photo = photo2  # Keep a reference to avoid garbage collection
    label2.place(x=1100, y=20)

    # Title label
    label_title = ttk.Label(frame1, text="Department of Mining Engineering \n            IIT (BHU), Varanasi", font=("Arial", 35 , "bold"))
    label_title.pack(pady=20)

    label_title2 = ttk.Label(frame1, text="Design of Protective Water Barrier Pillar (PWBP)", font=("Arial", 35 , "bold"  ))
    label_title2.pack(pady=100)

    #label_writers = ttk.Label(frame1, text="Version 1.0 Year 2023", font=("Times", 24))
    #label_writers.place(x=1150, y=650)

    # help module button
    btn_next = tk.Button(frame1, text="Help Module", command=lambda: open_pdf("help.pdf"), width=30, height=2,
                         font=("Helvetica", 18))
    btn_next.pack(pady=10)
    # Next Screen button
    btn_next = tk.Button(frame1, text="Enter", command=lambda: open_next_screen(notebook), width=30, height=2, font=("Helvetica", 18))
    btn_next.pack(pady=10)

    # Button to open Next Screen
    #btn_next_screen = tk.Button(frame1, text="Next Screen", command=lambda: open_next_screen(notebook), width=20,
                                #height=2, font=("Helvetica", 18))
    #btn_next_screen.pack(pady=10)
    #btn_next_screen.place(x=880, y=360)

    # Exit button
    btn_exit = tk.Button(frame1, text="Quit", command=exit_program, width=30, height=2, font=("Helvetica", 18))
    btn_exit.pack(pady=10)

    # Footer frame
    footer_frame = tk.Frame(frame1, bg='lightgray', height=30)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)

    # Copyright text
    current_year = datetime.now().year
    copyright_text = f"© {current_year} Mining Department, IIT BHU. All rights reserved."
    copyright_label = tk.Label(footer_frame, text=copyright_text, font=("Arial", 10), fg='gray', bg='lightgray')
    copyright_label.pack(side=tk.RIGHT, padx=10, pady=5)

    # Exit button at the bottom right corner
    #btn_exit = tk.Button(frame1, text="Quit", command=exit_program, width=5, height=1, font=("Helvetica", 18))
    #btn_exit.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
