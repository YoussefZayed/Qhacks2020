import * as tf from '@tensorflow/tfjs';
const model = await tf.loadLayersModel("spiralJson/model.json")

const test_case = tf.fromPixels("parkinsons-drawings/spiral/training/parkinson/V01PE03.png")
var prediction = model.predict(test_case)

print(prediction);