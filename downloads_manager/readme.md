I. Short Description:
       - Available for Windows7 and Windows10
       - This Python script is classifying all files located in Downloads, based on their extensions, and creates a structured hierarchy of folders, easier to manage.

II. Usage:
    - Download and Install python3.7 from https://www.python.org/downloads/
    - Download and Install anaconda from https://www.anaconda.com/distribution/
    - Open anaconda cmd prompt and type pip install pywin32 win10toast
    In path/to/downloads/Downloads paste downloads_manager.py and functions_amatei and run with python3.7 downloads_manager.py.
    That's it! Now you should receive notifications that your download files are moved based on their extensions in real time!
    
    Example: 
    Initial Downloads content: path/to/downloads/Downloads/: -all_files.jpg
                                                             -all_files.mp4
                                                             -all_files.png
                                                             -all_files.rar
                                                             -all_files.mp3
                                                             -all_files.pdf
                                                             -all_files.ppt
                                                             -all_files.exe
                                                             
    After running downloads_manager.py: path/to/downloads/Downloads/: -Executables/ -all_files.exe
                                                                      -Images/ -all_files.jpg
                                                                               -all_files.png
                                                                      -Music/ -all_files.mp3
                                                                      -PDF/ -all_files.pdf
                                                                      -PPT/ -all_files.ppt
                                                                      -RAR/ -all_files.rar
                                                                      -Videos/ -all_files.mp4
