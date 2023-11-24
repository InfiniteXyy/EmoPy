from EmoPy.src.fermodel import FERModel
from pkg_resources import resource_filename
import sys

target_emotions = ['happiness', 'anger']
model = FERModel(target_emotions, verbose=True)

# python fermodel_example.py a.png => the argv list will be ["fermodel_example.py", "a.png"]
model.predict(resource_filename('src', "image_data/%s" % sys.argv[1]))



