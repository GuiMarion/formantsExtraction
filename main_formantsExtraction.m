%% Please run the install.m installer before to use this script
% If you want to modify the python functions, mind that you'll
% need to restart Matlab or call py.reload(mod) to update them.

%% We extract formants from wave files
formantsLaurel = double(py.formantsExtraction.getFormants("Laurel.wav"));
figure; plot(formantsLaurel'); title("Laurel Formants"); xlabel('Time (ms)'); ylabel('Frequency (Hz)') 
 
formantsYawhee = double(py.formantsExtraction.getFormants("Yawhee.wav"));
figure; plot(formantsYawhee'); title("Yawhee Formants"); xlabel('Time (ms)'); ylabel('Frequency (Hz)') 
%% We extract formant means from files
meanFormant3 = double(py.formantsExtraction.getMeanFormants("Laurel.wav", 3));
disp("Average frequency 3rd formant Laurel " + num2str(meanFormant3));

meanFormant2 = double(py.formantsExtraction.getMeanFormants("Yawhee.wav", 2));
disp("Average frequency 2rd formant Yawhee " + num2str(meanFormant2));

%% We extract formant range (min, max) from files
rangeFormant3 = double(py.formantsExtraction.getRangeFormants("Laurel.wav", 3));
disp("Range frequency 3rd formant Laurel " + num2str(rangeFormant3));

rangeFormant2 = double(py.formantsExtraction.getRangeFormants("Yawhee.wav", 2));
disp("Range frequency 2rd formant Yawhee " + num2str(rangeFormant2));