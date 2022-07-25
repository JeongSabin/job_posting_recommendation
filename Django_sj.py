from tensorflow import keras
model = keras.models.load_model('./6emo_model_06_0.71.h5', compile=False)

export_path = './saved_model'
model.save(export_path, save_format='tf')