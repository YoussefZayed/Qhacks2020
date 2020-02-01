import React from 'react';
import './App.css';
import SpiralWave from './components/spiral-wave.component';

function App() {
  return (
    <div className="App">
      <div>
        Upload an image of a spiral or wave drawing
        <SpiralWave />
      </div>
    </div>
  );
}

export default App;