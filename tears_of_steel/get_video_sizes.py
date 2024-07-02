import os
import glob
from tqdm import tqdm 

TOTAL_VIDEO_CHUNCK = 245
BITRATE_LEVELS = [1,2,3,4,5,6]
VIDEO_PATH = 'video/'
# VIDEO_FOLDER = 'video'

# assume videos are in ../video_servers/video[1, 2, 3, 4, 5]
# the quality at video5 is the lowest and video1 is the highest


for bitrate,folder in enumerate(BITRATE_LEVELS):
	print('bitrate:',bitrate,'folder:',folder)
	print('filename:','video_size_' + str(len(BITRATE_LEVELS)-bitrate-1))
	with open('video_size_' + str(len(BITRATE_LEVELS)-bitrate-1), 'w') as f:
		for chunk_num in tqdm(range(1, TOTAL_VIDEO_CHUNCK+1)):
			# video_chunk_path = VIDEO_PATH + \
			# 				   VIDEO_FOLDER + \
			# 				   str(BITRATE_LEVELS - bitrate) + \
			# 				   '/' + \
			# 				   str(chunk_num) + \
			# 				   '.m4s'
			video_chunk_path = glob.glob(
				VIDEO_PATH + '/' + str(folder) + '/*seg-'+str(chunk_num)+'.m4f'
				)[0]
			chunk_size = os.path.getsize(video_chunk_path)
			f.write(str(chunk_size) + '\n')
