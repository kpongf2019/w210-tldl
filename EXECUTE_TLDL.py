import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--audio_file_name", help="name of the input audio file")
args = parser.parse_args()
  
os.system('python Transcribe_Audio_Input_File.py --audio_file_name ' + args.audio_file_name + ' --dest_bucket_name w210-tl-dl-bucket --hash_registry_table_name transcript_md5_hash_registry.csv --transcript_dir_name Transcripts/')
os.system('python model_output.py --article model_transcript.txt --model_dir model_multi_news/ --model_name multi_news')