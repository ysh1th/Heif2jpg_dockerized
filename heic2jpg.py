import os
import logging
#import pyheif
from PIL import Image
from pillow_heif import register_heif_opener
from sys import argv

logging.basicConfig(level=logging.INFO, format='%(message)s')

register_heif_opener()

def heic_to_jpg(heic_dir):
  if not os.path.isdir(heic_dir):
    logging.error(f"Directory '{heic_dir}' does not exist.")
    return
  
  # create a directory to store converted files
  jpg_dir = os.path.join(heic_dir, "ConvertedFiles")
  os.makedirs(jpg_dir, exist_ok=True)

  # get all heic files from specified dir
  heic_files = [file for file in os.listdir(heic_dir) if file.lower().endswith(".heic")]
  total_files = len(heic_files)

  # convert each heic file to jpg
  convert_num = 0
  for file_index, file_name in enumerate(heic_files, start=1):
    heic_path = os.path.join(heic_dir, file_name)
    jpg_path = os.path.join(jpg_dir, os.path.splitext(file_name)[0] + ".jpg")

    try:
      # open heic file using pyheif
      with Image.open(heic_path) as heic_file:
        heic_file.convert("RGB").save(jpg_path, "JPEG", quality=85)
        convert_num += 1
        # heif_file = pyheif.read(heic_file)
        # image = Image.frombytes(
        #   heif_file.mode,
        #   heif_file.size,
        #   heif_file.data,
        #   "raw",
        #   heif_file.mode,
        #   heif_file.stride
        # )

      # save image as jpg
      # with open(jpg_path, "wb") as jpg_file:
      #   image.save(jpg_file, "JPEG", quality = 50)
      #   convert_num += 1

      # calculate and display percent progress
      progress = int((file_index / total_files) * 100)
      print(f"Conversion progress: {progress}%", end = "\r", flush=True)
    except Exception as e:
      logging.error(f"Error converting {file_name}: {str(e)}")
  print(f"\nConversion completed successfully. {convert_num}/{total_files} files converted.")

heic_directory = argv[1]

heic_to_jpg(heic_directory)