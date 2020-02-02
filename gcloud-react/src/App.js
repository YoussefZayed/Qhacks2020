import React from 'react';
import './App.css';
import './index.css';
import {Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import SpiralTest from './components/spiral.component';
import WaveTest from './components/wave.component';
import Audio from './components/audio.component';

const cors = require('cors');
const express = require('express');

const app = express();

app.use(cors());
app.use(express.json());

const aiRouter = require('./backend/routes/ai');
app.use('/ai', aiRouter);


function collectData() {
  var spiral64 = SpiralTest.getCanvasBase64();
  var wave64 = WaveTest.getCanvasBase64();
/*
  app.get('/spiral_test', function(req, res) {
      res.send(spiral64);
  });

  app.get('/wave_test', function(req, res) {
    res.send(wave64);
  });
*/
}

function App() {
  return (
    <div className='App' style={{display: 'flex'}}>
      <div>
        
          <div className='title' style={{fontSize: 56, marginTop: '20%'}}>
            Do you have Parkinson's disease?
          </div>
          <div className='title' style={{fontFamily: 'SourceSansProLight', fontSize: 28, color: 'white', marginTop: '5%'}}>
            Complete the following tests to find out
          </div>

          <div style={{marginTop: '15%'}}>
            <SpiralTest/>
          </div>

          <div style={{marginTop: '12%'}}>
            <WaveTest/>
          </div>

          <div style={{marginTop: '12%'}}>
            <Audio/>
          </div>

          <div style={{marginTop: '12%', marginBottom: '12%'}}>
            <Button className='button' 
                    variant='success' 
                    style={{padding: '1%', fontSize: 36, borderRadius: '15px'}}
                    onClick={collectData}
                    >
                    Predit
                    </Button>
          </div>
      </div>
    </div>
  );
}

export default App;