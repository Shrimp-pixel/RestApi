import logo from './logo.svg';
import './App.css';
import React from 'react';
import Menu from "./components/Menu"
import AuthorList from "./components/Author"
import Footer from "./components/Footer"
import axios from 'axios';

class App extends React.Component {
    constructor (props) {
        super(props);
        this.state={
            'authors':[]
        }
    }

    componentDidMount(){

        axios.get('http://127.0.0.1:8000/api/users/').then(response =>{
            this.setState({
            'authors': response.data
        })
        }).catch(error => console.log(error))

    }

render(){
  return (
  <div>
    <Menu />
    <div>

        <AuthorList authors={this.state.authors}/>

    </div>
    <Footer />
    </div>
  );
}
}

export default App;
