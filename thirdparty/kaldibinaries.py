import shutil, os
import argparse

def CollectBinaries(directory):
	outdirectory = os.path.dirname(os.path.realpath(__file__))
	for root, dirs, files in os.walk(directory):
		for name in files:
			ext = os.path.splitext(name)
			(key, value) = ext
			if value == '' and key != '.DS_Store' and key != 'configure' and key != 'Doxyfile' and key != 'INSTALL' and key != 'NOTES' and key != 'TODO' and key != 'Makefile':
				shutil.copy(root + '/' + name, outdirectory)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('dir')
	args = parser.parse_args()
	directory = args.dir
	CollectBinaries(directory)