
from __future__ import division # sigh...


import numpy as np
import cv2





def captureFrames(length):

	camera = cv2.VideoCapture(0)
	frames = [ ]

	try:

		for ith in range(length):

			_, frame  = camera.read( )
			frames.append(frame)

	except Exception, e:

		raise e

	finally:

		camera.release( )

	return frames





def mergeFrames(frames):

	aggregate = None

	for ith in range(len(frames)):

		n     = ith + 1
		frame = frames[ith]

		if aggregate is None:

			aggregate = frame

		else:

			weight = {
				'aggregate': 1 - (1 / n),
				'current':   1 / n
			}

			aggregate = cv2.addWeighted(aggregate, weight['aggregate'], frame, weight['current'], 0)

	return aggregate





def main(arguments):

	noFrames = int(arguments['<frames>'])
	frames   = captureFrames(noFrames)

	_, img    = cv2.imencode('.png', mergeFrames(frames))
	print(img.tostring( ))
