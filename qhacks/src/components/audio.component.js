import React, {Component} from 'react';
import {Card, Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

export default class SpiralWave extends Component {

    constructor(props) {
        super(props);

        this.state = {
            audio_clip: null
        }
    }

    render() {
        return (
            <div>
                <Card border="success" 
                      style={{marginRight: '20px', 
                              marginLeft: '20px', 
                              width: '500px',
                              height: '500px'}}>
                    <Card.Header style = {{fontSize: '1.1rem'}}>Record an audio clip</Card.Header>
                    <Card.Body>
                        <div style={{display: 'flex', 
                                     justifyContent: 'center',
                                     marginLeft: '20px', 
                                     marginRight: '20px'}}>
                            Test
                        </div>
                    </Card.Body>
                    <Card.Footer>
                        <Button variant='success'>Do I have Parkinson's?</Button>
                    </Card.Footer>
                </Card>
            </div>
        )
    }
}