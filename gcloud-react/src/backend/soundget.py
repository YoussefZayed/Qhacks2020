import numpy as np
import urllib.parse
from parselmouth.praat import call
import parselmouth
import sys

def getfeatures(sound,gender=0):
    f0min = 75
    f0max = 500

    sound = parselmouth.Sound(sound)
    pointProcess = call(sound, "To PointProcess (periodic, cc)", f0min, f0max)


    shimmer = call([sound, pointProcess], "Get shimmer (local)", 0, 0, 0.0001, 0.02, 1.3, 1.6)  # localShimmer
    shimmerDb = call([sound, pointProcess], "Get shimmer (local_dB)", 0, 0, 0.0001, 0.02, 1.3, 1.6)  # localdbShimmer

    apq3Shimmer = call([sound, pointProcess], "Get shimmer (apq3)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    apq5Shimmer = call([sound, pointProcess], "Get shimmer (apq5)", 0, 0, 0.0001, 0.02, 1.3, 1.6)
    apq11Shimmer = call([sound, pointProcess], "Get shimmer (apq11)", 0, 0, 0.0001, 0.02, 1.3, 1.6)


    # Return the features in the order the model will need them in
    return np.array([gender,shimmer, shimmerDb, apq3Shimmer, apq5Shimmer, apq11Shimmer])
