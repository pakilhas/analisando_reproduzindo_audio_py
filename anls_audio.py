
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display as ld
from IPython.display import Audio





plt.rcParams.update()
Audio(filename='Young PK - Dama (online-audio-converter.com).wav') #mostra o arquivo de audio

data, fs = librosa.load('Young PK - Dama (online-audio-converter.com).wav') #dados correspondente arquivo de audio e a frequencia

Audio(data=data, rate=fs *1.2) #array correspondente e a frequencia de reproducao

plt.figure(figsize=(14, 5))
ld.waveshow(data, sr =fs)

DATA = librosa.stft(data)
DATAdb = librosa.amplitude_to_db(abs(DATA))

plt.figure(figsize=(14, 5))
ld.specshow(DATAdb, sr=fs, x_axis='time', y_axis='hz')






