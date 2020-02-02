const router = require('express').Router();
const cors = require('cors');
const tf = require('@tensorflow/tfjs');

router.route('/').get((req, res) => {
    res.json("connected")
});

router.route('/spiral_test').get((req, res) => {
  const model = tf.loadLayersModel('../spiralJson/model.json');
  const example =  tf.browser.fromPixels('hi');  // for example
  const prediction = model.predict(example); 
  res.json(prediction);
  console.log(prediction);
})

router.route('/wave_test').get((req, res) => {
  const model = tf.loadLayersModel('../waveJson/model.json');
  const example =  tf.browser.fromPixels('hi');  // for example
  const prediction = model.predict(example); 
  res.json(prediction);
  console.log(prediction);
})

/*
router.route('/audio_test').get((req, res) => {
  print("neat (audio)");
})
*/



module.exports = router;