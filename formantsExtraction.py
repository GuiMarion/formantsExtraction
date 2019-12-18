import parselmouth
import numpy as np
import matplotlib.pyplot as plt

def linearly_interpolate_nans(y):
    # Fit a linear regression to the non-nan y values

    # Create X matrix for linreg with an intercept and an index
    X = np.vstack((np.ones(len(y)), np.arange(len(y))))

    # Get the non-NaN values of X and y
    X_fit = X[:, ~np.isnan(y)]
    y_fit = y[~np.isnan(y)].reshape(-1, 1)

    # Estimate the coefficients of the linear regression
    beta = np.linalg.lstsq(X_fit.T, y_fit, rcond=-1)[0]

    # Fill in all the nan values using the predicted coefficients
    y.flat[np.isnan(y)] = np.dot(X[:, np.isnan(y)].T, beta)
    return y

def getFormants(file):
	'''
	Return the formants as a matrix (formants * time (ms))
	from the path to the wave file.
	'''

	snd = parselmouth.Sound(file)

	formants_raw = snd.to_formant_burg()
	formants = []
	for formant in range(0,5):
		formants.append([])
		for t in np.arange(0, formants_raw.duration, 0.001):
			formants[formant].append(formants_raw.get_value_at_time(formant+1, t))

		formants[formant] = linearly_interpolate_nans(np.array(formants[formant]))

	return np.array(formants)

def getRangeFormants(file, formant):
	'''
	Returns the range (min, max) of the formant (int)
	from the path to the wave file.
	'''
	formants = getFormants(file)
	return np.array([min(formants[int(formant-1)]), max(formants[int(formant-1)])])

def getMeanFormants(file, formant):
	'''
	Returns the frequency average of the formant (int)
	from the path to the wave file.
	'''
	formants = getFormants(file)
	return np.mean(formants[int(formant-1)])
