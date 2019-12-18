import matplotlib.pyplot as plt

import formantsExtraction as fe

'''
We extract formants from the folowing two wav files and plot them.
'''
formantsLaurel = fe.getFormants("Laurel.wav")
plt.figure()
for elem in formantsLaurel:
	plt.plot(elem)
plt.title("Laurel Formants")
plt.xlabel('Time (ms)')
plt.ylabel('Frequency (Hz)') 
plt.show(block=False)


formantsLaurel = fe.getFormants("Yawhee.wav")
plt.figure()
for elem in formantsLaurel:
	plt.plot(elem)
plt.title("Yawhee Formants")
plt.xlabel('Time (ms)')
plt.ylabel('Frequency (Hz)') 
plt.show(block=False)

'''
We extract formant means from files
'''
meanFormant3 = fe.getMeanFormants("Laurel.wav", 3);
print("Average frequency 3rd formant Laurel " + str(meanFormant3));

meanFormant2 = fe.getMeanFormants("Yawhee.wav", 2);
print("Average frequency 2rd formant Yawhee " + str(meanFormant2));

'''
We extract formant range (min, max) from files
'''
rangeFormant3 = fe.getRangeFormants("Laurel.wav", 3);
print("Range frequency 3rd formant Laurel " + str(rangeFormant3));

rangeFormant2 = fe.getRangeFormants("Yawhee.wav", 2);
print("Range frequency 2rd formant Yawhee " + str(rangeFormant2));

plt.show() # To leave the figures in place
