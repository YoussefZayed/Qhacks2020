import React, {Component} from 'react';
import {Container, Card, Button, Tabs, Tab} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import './spiral-wave.css';
import CanvasArea from './canvas-area.component.js';

export default class SpiralWave extends Component {

    constructor(props) {
        super(props);

        this.state = {
            image_file: null
        }

        this.uploadImage = this.uploadImage.bind(this);
    }

    uploadImage(event) {

        var file = event.target.files[0]
        var reader = new FileReader();
        reader.readAsBinaryString(file);
      
        this.setState({
            image_file: reader.result
        })

        var output = document.getElementById('imageOutput');
        output.src = URL.createObjectURL(event.target.files[0]);
    }

    render() {
        return (
            <Container className='container' border='dark' 
                       style={{width: '500px', height: '600px'}}>
                <div>
                    <Tabs defaultActiveKey='profile' id='tab'>
                        <Tab className='tab' eventKey='Draw' title='Draw' variant='success'>
                            <Card justify='center'>
                                <Card.Header style = {{fontSize: '1.1rem'}}>Upload a file of a spiral or wave</Card.Header>
                                <Card.Body>
                                    <div style={{display: 'flex', justifyContent: 'center'}}>
                                        <CanvasArea/>
                                    </div>
                                </Card.Body>
                                <Card.Footer>
                                    <Button className='button' variant='success'>Do I have Parkinson's?</Button>
                                </Card.Footer>
                            </Card>
                        </Tab>
                        <Tab className='tab' eventKey='Upload' title='Upload'>
                            <input type='file'
                                accept='image/png, image/jpg'
                                style={{fontSize: '1rem'}}
                                onChange={this.uploadImage}/>
                            <img id='imageOutput'/>
                        </Tab>
                    </Tabs>
                </div>
            </Container>
        );
    }
}