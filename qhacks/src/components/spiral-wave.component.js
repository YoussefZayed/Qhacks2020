import React, {Component} from 'react';
import {Card, Button} from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

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
            <div>
                <Card border="success" 
                      style={{marginRight: '20px', 
                              marginLeft: '20px', 
                              width: '500px',
                              height: '500px'}}>
                    <Card.Header style = {{fontSize: '1.1rem'}}>Upload a file of a spiral or wave</Card.Header>
                    <Card.Body>
                        <input type='file'
                            accept='image/png, image/jpg'
                            style={{fontSize: '1rem'}}
                            onChange={this.uploadImage}/>
                        <div style={{display: 'flex', 
                                     justifyContent: 'center'}}>
                            <img id='imageOutput' src={null}/>
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