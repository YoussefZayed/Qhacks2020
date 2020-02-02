import React, {Component} from 'react';
import {Container, Tabs, Tab} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../index.css';
import Canvas from './canvas.component.js';

export default class WaveTest extends Component {

    constructor(props) {
        super(props);

        this.state = {
            image_file: null
        }

        this.uploadImage = this.uploadImage.bind(this);
    }

    static getCanvasBase64() {
        return Canvas.svgToBase64();
    }

    uploadImage(event) {

        var file = event.target.files[0]
        var reader = new FileReader();
        reader.readAsBinaryString(file);
      
        this.setState({
            image_file: reader.result
        })

        var output = document.getElementById('imageOutputWave');
        output.src = URL.createObjectURL(event.target.files[0]);
    }

    render() {
        return (
            <Container className='container' border='dark'>
                <div style={{padding: '2%'}}>
                    <div className='header'>Wave Drawing Test</div>
                </div>
                <Tabs defaultActiveKey='profile' id='tab'>

                    <Tab className='tab' eventKey='Draw' title='Draw' variant='success'>
                        <div style = {{padding: '2%', marginTop: '2%', marginBottom: '2%', fontSize: '1.5rem'}}>Draw a wave</div>
                        <div style={{display: 'flex', justifyContent: 'center'}}>
                            <Canvas id='canvas'/>
                        </div> 
                    </Tab>

                    <Tab className='tab' eventKey='Upload' title='Upload' >
                        <div style={{display: 'inline-block', width: '500px', height: '500px'}}>
                            <div style = {{padding: '2%', marginTop: '2%', marginBottom: '2%', fontSize: '1.5rem'}}>Upload an image of a hand-drawn wave</div>
                            <input type='file'
                                accept='image/*'
                                style={{marginTop: '1%'}}
                                onChange={this.uploadImage}/>
                            <div style={{display: 'flex', maxWidth: '100%', maxHeight: '100%', padding: '1%'}}>
                                <img id='imageOutputWave'/>
                            </div>
                        </div>
                    </Tab>

                </Tabs>
            </Container>
        );
    }
}