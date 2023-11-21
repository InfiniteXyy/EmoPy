from EmoPy.src.fermodel import FERModel
from pkg_resources import resource_filename

target_emotions = ['happiness', 'anger']
model = FERModel(target_emotions, verbose=True)

print('Predicting on happy image...')
model.predict(resource_filename('src','image_data/happy.png'))

print('Predicting on angry image...')
model.predict(resource_filename('src','image_data/angry.png'))

