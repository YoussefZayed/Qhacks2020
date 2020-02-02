import React, {Component} from 'react';
import {Container, Button, Tabs, Tab} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../index.css';
import './spiral-wave.css';
import Canvas from './canvas.component.js';

export default class WaveTest extends Component {

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
            <Container className='container' border='dark'>
                <div style={{fontSize: '2.2rem', padding: '2%'}}>Wave Drawing Test</div>
                <Tabs defaultActiveKey='profile' id='tab'>

                    <Tab className='tab' eventKey='Draw' title='Draw' variant='success'>
                        <div style = {{padding: '2%', marginTop: '2%', marginBottom: '2%', fontSize: '1.5rem'}}>Draw a wave</div>
                        <div style={{display: 'flex', justifyContent: 'center'}}>
                            <Canvas id='canvas'/>
                        </div> 
                    </Tab>

                    <Tab className='tab' eventKey='Upload' title='Upload'>
                        <input type='file'
                            accept='image/png, image/jpg'
                            style={{marginTop: '1%', marginBottom: '1%'}}
                            onChange={this.uploadImage}/>
                        <img id='imageOutput' style={{justify: 'center', width: '90%', height: '90%'}}/>
                    </Tab>

                </Tabs>
            </Container>
        );
    }
}