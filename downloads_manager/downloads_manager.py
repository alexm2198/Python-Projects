import os
from functions_amatei import functions

# Downloads path
path = os.getcwd()

while True:
    # Images directory built for gathering all new downloaded photos
    images_folder = "Images"
    images_path = path + fr"\{images_folder}"
    images_ext = ['*.jpg', '*.png', "*.jpeg"]

    functions.create_new_dir(path, images_folder)
    for ext in images_ext:
        functions.get_files_of_type_and_move(path, ext, images_path)

    # PDF directory
    pdf_folder = "PDF"
    pdf_path = path + rf"\{pdf_folder}"
    pdf_ext = "*.pdf"

    functions.create_new_dir(path, pdf_folder)
    functions.get_files_of_type_and_move(path, pdf_ext, pdf_path)

    # RAR and ZIP Archives files
    zip_folder = "ZIP"
    zip_path = path + rf"\{zip_folder}"
    zip_ext = ['*.zip','*.rar','*.gz','*.7z']

    functions.create_new_dir(path, zip_folder)
    for ext in zip_ext:
        functions.get_files_of_type_and_move(path, ext, zip_path)

    # Executables files
    exe_folder = "Executables"
    exe_path = path + rf"\{exe_folder}"
    exe_ext = "*.exe"

    functions.create_new_dir(path, exe_folder)
    functions.get_files_of_type_and_move(path, exe_ext, exe_path)

    # ISO images
    iso_folder = "ISO"
    iso_path = path + rf"\{iso_folder}"
    iso_ext = '*.iso'

    functions.create_new_dir(path, iso_folder)
    functions.get_files_of_type_and_move(path, iso_ext, iso_path)

    # Music files
    music_folder = "Music"
    music_path = path + rf"\{music_folder}"
    music_ext = ['*.mp3', '*.wav']

    functions.create_new_dir(path, music_folder)
    for ext in music_ext:
        functions.get_files_of_type_and_move(path, ext, music_path)

    # PowerPoint Presentations
    ppt_folder = "PPT"
    ppt_path = path + rf"\{ppt_folder}"
    ppt_ext = ['*.ppt', '*.pptx', '*.potx']

    functions.create_new_dir(path, ppt_folder)
    for ext in ppt_ext:
        functions.get_files_of_type_and_move(path, ext, ppt_path)

    # Video files
    video_folder = "Videos"
    video_path = path + rf"\{video_folder}"
    video_ext = ['*.mp4', '*.vid', '*.avi']

    functions.create_new_dir(path, video_folder)
    for ext in video_ext:
        functions.get_files_of_type_and_move(path, ext, video_path)
