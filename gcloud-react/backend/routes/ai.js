const router = require('express').Router();


router.route('/').get((req, res) => {
  res.json("test")
});

router.route('/spiral_test').get((req, res) => {
  print("haha cool (spiral)");
})

router.route('/wave_test').get((req, res) => {
  print("very nice (wave)");
})

router.route('/audio_test').get((req, res) => {
  print("neat (audio)");
})



module.exports = router;