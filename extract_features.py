import os, sys


directory = "the_directory_of_the_audio_files"

for root, subdirectories, files in os.walk(directory):
    #for subdirectory in subdirectories:
        #print(os.path.join(root, subdirectory))
    for file in files:
        if (".wav" in file): # You can specify a specific condition for the audio files
           #print(os.path.join(root, file))
           filedir = os.path.join(root, file)
           filename = os.path.splitext(file)[0]
           os.system("SMILExtract -C /the_full_directory_of_config_file_in_opensmile_folder/eGeMAPSv01a.conf -I "+filedir+" -csvoutput /output_folder/"+filename+".csv")

