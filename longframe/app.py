
from __future__ import division # sigh...
import cv2





def captureFrames(length):

	camera = cv2.VideoCapture(0)

	try:

		frames = [camera.read( )[1] for _ in range(length)]

	except Exception, e:

		raise e

	finally:

		camera.release( )

	return frames





def mergeFrames(frames):

	accum = None

	for ith, frame in enumerate(frames):

		n = ith + 1

		if accum is None:

			accum = frame

		else:

			weight = {
				'accum': 1 - (1 / n),
				'current':   1 / n
			}

			accum = cv2.addWeighted(accum, weight['accum'], frame, weight['current'], 0)

	return accum





def main(arguments):

	noFrames = int(arguments['<frames>'])
	frames   = captureFrames(noFrames)

	_, img    = cv2.imencode('.png', mergeFrames(frames))

	print(img.tostring( ))
