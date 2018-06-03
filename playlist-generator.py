#!/usr/bin/env python3

import os
from sys import path
from time import time

UTF8_BOM = b'\xef\xbb\xbf'

audio_ext = {'aac', 'opus', 'aiff', 'flac', 'midi', 'amr', 'ape', 'mpc',
			 'mp3', 'ac3', 'alac', 'ogg', 'wav', 'm4a', 'mid', 'wv'}
video_ext = {'mp4', 'mkv', 'mov', 'mpg', 'webm', '3gp', 'flv', 'ogv',
			 'wmv', 'swf'}
media_ext = audio_ext.union(video_ext)

def is_media(filename):
		file_ext = filename.split('.')[-1]
		return file_ext in media_ext

def write_playlist(filename, found_media):
	with open(filename, 'wb') as output_file:
		output_file.write(UTF8_BOM)
		found_media.sort()
		return output_file.write('\n'.join(found_media).encode('utf-8'))


def main():
	current_dir = path[0]
	for dirpath, _, files in os.walk(current_dir):
		output_filename = os.path.join(dirpath, 'playlist.m3u8')
		found_media = [file for file in files if is_media(file)]
		if found_media:
			write_playlist(output_filename, found_media)
		# else:
			# safe_remove(output_filename)

if __name__ == '__main__':
	start_time = time()
	main()
	done_time = time()
	print('Done in {:.3f} s'.format(done_time-start_time))
