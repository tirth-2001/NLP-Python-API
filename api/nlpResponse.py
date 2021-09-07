import random
import tensorflow as tf

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import os

# Reload the model
modelPath = os.path.join("data", 'model_iot_english')
# print(modelPath)
new_model = tf.keras.models.load_model(modelPath)

# Check its architecture
# print(new_model.summary())

vocab_size = 50
embedding_dim = 16
max_length = 5
trunc_type = 'post'
padding_type = 'post'
oov_tok = "<OOV>"
training_size = 12


dataset = [{
    'status': 0,
    'input': "Turn off the light"
}, {
    'status': 1,
    'input': "Turn on the light"
}, {
    'status': 0,
    'input': "Turn off the fan"
}, {
    'status': 1,
    'input': "activate the bulb"
}, {
    'status': 0,
    'input': "switch off the AC"
}, {
    'status': 1,
    'input': "Glow on the tubelight"
}, {
    'status': 0,
    'input': "shut off the bulb"
}, {
    'status': 1,
    'input': "Switch on the TV"
}, {
    'status': 0,
    'input': "please disconnect the light"
}, {
    'status': 1,
    'input': "Power on the light bulb"
}, {
    'status': 0,
    'input': "flick off the TV"
}, {
    'status': 1,
    'input': "Flick on the fan"
}, {
    'status': 0,
    'input': "you can powerdown the AC"
}, {
    'status': 1,
    'input': "Activate the AC"
}, {
    'status': 0,
    'input': "Cut off the light bulb"
}, {
    'status': 1,
    'input': "Connect the TV"
}
]

print(dataset)

sentences = []
labels = []

# print(dataset[0])

for item in dataset:
    sentences.append(item['input'])
    labels.append(item['status'])

# print(sentences)
# print(labels)

training_sentences = sentences[0:training_size]
testing_sentences = sentences[training_size:]
training_labels = labels[0:training_size]
testing_labels = labels[training_size:]
# print(testing_labels)

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)


def predict(command):
    # print(command)
    sequences = tokenizer.texts_to_sequences([command])
    # print(sequences)
    data = pad_sequences(sequences, maxlen=max_length,
                         padding=padding_type, truncating=trunc_type)
    # print(data)
    prediction = new_model.predict(data)
    # print(prediction)
    return prediction[0][0]
