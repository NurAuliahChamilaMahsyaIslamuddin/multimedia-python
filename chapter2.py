from PIL import Image
from PIL import ImageFilter
from pydub import AudioSegment

# Memuat gambar
image = Image.open('fot.JPG')
cropped_image = image.crop((10, 10, 200, 200))
resized_image = cropped_image.resize((100, 100))
filtered_image = resized_image.filter(ImageFilter.BLUR)
audio = AudioSegment.from_file('lagu.mp3')
clipped_audio = audio[:10000] 
combined_audio = audio + clipped_audio
audio.export('result.wav', format='wav')
louder_audio = audio + 10 
