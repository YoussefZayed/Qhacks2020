import React, {Component} from 'react';
import {Container, Form, Col, Button} from 'react-bootstrap';
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
            <Container className='container'>
                <div style={{fontSize: '2.2rem', padding: '2%'}}>Audio Test</div>
                <Form.Row style={{padding: '2%'}}>
                    <Form.Group as={Col} controlId="formAge">
                    <Form.Label style={{fontSize: '1.5rem'}}>Age</Form.Label>
                    <Form.Control required type='number'/>
                    </Form.Group>

                    <Form.Group as={Col} controlId="formGender">
                    <Form.Label style={{fontSize: '1.5rem'}}>Gender</Form.Label>
                    <Form.Control as="select">
                        <option>Male</option>
                        <option>Female</option>
                    </Form.Control>
                    </Form.Group>
                </Form.Row>

                <div style = {{padding: '2%', marginTop: '2%', marginBottom: '2%', fontSize: '1.5rem'}}>Upload an audio clip</div>
                <input type='file'
                    accept='audio/wav'
                    style={{marginTop: '3%', marginBottom: '3%'}}
                    onChange={this.uploadImage}/>
            </Container>
        )
    }
}