import logo from './logo.svg';
import './App.css';
import React from 'react';
import Menu from "./components/Menu";
import AuthorList from "./components/Author";
import ToDoList from "./components/ToDo";
import ToDoCreator from "./components/ToDosCreator";
import ProjectList from "./components/Projects";
import Footer from "./components/Footer";
import NotFound404 from "./components/NotFound404";
import axios from 'axios';
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom"

class App extends React.Component {
    constructor (props) {
        super(props);
        this.state={
            'authors':[],
            'todos':[],
            'projects':[],
        }
    }

    componentDidMount(){

        axios.get('http://127.0.0.1:8000/api/users/').then(response =>{
            this.setState({
            'authors': response.data
        })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/').then(response =>{
            this.setState({
            'todos': response.data
        })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/project/').then(response =>{
            this.setState({
            'projects': response.data
        })
        }).catch(error => console.log(error))

    }

render(){
  return (
  <div>
    <div>
        <BrowserRouter>
        <Menu />
            <Routes>
                <Route exact path='/' element={<Navigate to='/authors'/>}/>
                <Route path='/authors'>
                    <Route index element={<AuthorList authors={this.state.authors}/>} />
                    <Route path=':creatorId' element={<ToDoCreator todos={this.state.todos}/>}/>
                </Route>
                <Route exact path='/todo' element={<ToDoList todos={this.state.todos}/>}/>
                <Route exact path='/project' element={<ProjectList projects={this.state.projects}/>}/>
                <Route path='*' element={<NotFound404/>}/>
            </Routes>
        </BrowserRouter>
    </div>
    <Footer />
    </div>
  );
}
}

export default App;
