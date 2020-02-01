import React from 'react';
import './App.css';
import './assets/css/font-awesome.min.css';
import {Col} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import SpiralWave from './components/spiral-wave.component';
import Audio from './components/audio.component';

function App() {
  return (
    <div className='App' style={{display: 'flex'}}>
      <div>
        
          <div className='title' style={{fontSize: 56, marginTop: '15%'}}>
            Do you have Parkinson's disease?
          </div>

          <div style={{marginTop: '10%'}}>
            <SpiralWave/>
          </div>

      </div>
    </div>
  );
}

export default App;