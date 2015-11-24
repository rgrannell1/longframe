

"""
Name:
	longframe

Usage:
	long-frame (-f <frames> | --frames <frames>)
	long-frame (-h | --help | --version)

Description:
	Take a long, blended screenshot using a webcam.

Options:
	-f <frames>, --frames <frames>     the number of frames to merge.
"""

from docopt import docopt
import app





if __name__ == '__main__':

	arguments = docopt(__doc__)
	app.main(arguments)
