import librosa
import librosa.display
import matplotlib.pyplot as plt

# Load an example audio file
audio_path = librosa.example('trumpet')  # Change to your audio file path

# Load audio file with sampling rate
y, sr = librosa.load(audio_path)

# Extract features
mfccs = librosa.feature.mfcc(y=y, sr=sr)
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
zero_crossings = librosa.feature.zero_crossing_rate(y)[0]
rms = librosa.feature.rms(y)[0]
tempo, _ = librosa.beat.beat_track(y, sr=sr)

# Plotting the features
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
librosa.display.specshow(mfccs, x_axis='time')
plt.title('MFCCs')

plt.subplot(2, 2, 2)
librosa.display.specshow(chroma, x_axis='time')
plt.title('Chroma')

plt.subplot(2, 2, 3)
plt.plot(librosa.times_like(centroid), centroid, label='Spectral Centroid')
plt.plot(librosa.times_like(bandwidth), bandwidth, alpha=0.5, label='Spectral Bandwidth')
plt.xlabel('Time (s)')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(librosa.times_like(zero_crossings), zero_crossings, label='Zero Crossing Rate')
plt.plot(librosa.times_like(rms), rms, alpha=0.5, label='RMS Energy')
plt.xlabel('Time (s)')
plt.legend()

plt.tight_layout()
plt.show()

print(f'Tempo: {tempo} BPM')
