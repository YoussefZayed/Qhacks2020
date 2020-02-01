import React, {Component} from 'react';
import {Figure} from 'react-bootstrap';

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
                <input type='file' 
                    name='file' 
                    onChange={this.uploadImage}/>
                <Figure 
                    id='imageOutput' 
                    width={300}
                    height={300}
                />
            </div>
        )
    }
}