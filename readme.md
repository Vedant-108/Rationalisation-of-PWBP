# Program Versions and Deployment

## Program Versions

### Initial Drafts
- `Opening_screen_1920px.py`
- `Opening_screen_copy.py`
- `Opening_screen_smallscreen.py`

These initial drafts were the preliminary versions of the program. 

### Improved Versions
The following are the deployable versions with sequential improvements:

- `PWBP_tabs_code1920px_V1.py`
- `PWBP_tabs_code1920px_V2.py`
- `PWBP_tabs_code1920px_V2_v1.py`
- `PWBP_tabs_code1920px_V3.py` (RQD integration not complete; backend for RQD needs to be created before deployment)
- `PWBP_tabs_code1920px_V3_v1.py` (With deployable code)
- `PWBP_tabs_code1920px_V3_v1_withoutlogos.py` (Used to produce the screenshots for the research paper)

## Deployment

The program was deployed using [PyInstaller](https://pyinstaller.org/en/stable/).

### Deployment Instructions

- **Mac Version**: Use PyInstaller on macOS to create the Mac version of the executable.
- **Windows Version**: Use PyInstaller on Windows to create the Windows version of the executable.

Alternatively, you can use `auto-py-to-exe` for a GUI-based implementation:

- Install `auto-py-to-exe` via pip: `pip install auto-py-to-exe`
- Launch `auto-py-to-exe` and configure the settings as needed to convert the Python script to an executable.

## Notes

- Ensure that the backend for RQD is created before deploying version `PWBP_tabs_code1920px_V3.py`.
- `PWBP_tabs_code1920px_V3_v1_withoutlogos.py` was specifically used for producing research paper screenshots.

For further details on PyInstaller and auto-py-to-exe, refer to their respective documentation.
