import React from 'react';
import './App.css';
import {Container, Col, Row} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import SpiralWave from './components/spiral-wave.component';
import Audio from './components/audio.component';

function App() {
  return (
    <Container className="App">
      <div style={{marginTop: '30px', fontSize: '2rem'}}>
        Parkinson's Checker

        <Row style={{marginTop: '20px'}}>

          <Col>
            <SpiralWave/>
          </Col>

          <Col>
            <Audio/>
          </Col>

        </Row>

      </div>
    </Container>
  );
}

export default App;