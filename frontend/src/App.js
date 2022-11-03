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
import LoginForm from "./components/Auth";
import axios from 'axios';
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom"
import Cookies from 'universal-cookie'

const styles = {
    display: 'flex',
    justifyContent:'space-around'
};

class App extends React.Component {
    constructor (props) {
        super(props);
        this.state={
            'authors':[],
            'todos':[],
            'projects':[],
            'token':'',
        }
    }

    logout(){
        this.set_token('')
        this.setState({'authors':[]})
        this.setState({'todos':[]})
        this.setState({'projects':[]})
    }

    is_auth(){
        return !!this.state.token
    }

    set_token(token){
        console.log(token)
        const cookies = new Cookies()
        cookies.set('token',token)
        this.setState({'token':token}, ()=>this.load_data())
    }

    get_token_storage(){
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token':token}, () => this.load_data())
    }

    get_token(username, password){
        const data = {username:username, password:password}
        axios.post('http://127.0.0.1:8000/api-token-auth/', data).then(response => {
            this.set_token(response.data['token'])
        }).catch(error=> alert('Неверный логин или пароль'))
    }

    get_headers(){
        let headers = {
            'Content-Type': 'application/json'
        }

        if (this.is_auth()){
            headers['Authorization'] = 'Token '+this.state.token
        }
        return headers
    }

    load_data(){
    const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers}).then(response =>{
            this.setState({
            'authors': response.data
        })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/', {headers}).then(response =>{
            this.setState({
            'todos': response.data
        })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/project/', {headers}).then(response =>{
            this.setState({
            'projects': response.data
        })
        }).catch(error => console.log(error))

    }


    componentDidMount(){
        this.get_token_storage()
    }


render(){
  return (
  <div>
    <div>
        <BrowserRouter>
        <header class="site-header">
    <div>
        <nav style = {styles}>
            <li>
                <Link to='/'>Author</Link>
            </li>
            <li>
                <Link to='/todo'>Todo</Link>
            </li>
            <li>
                <Link to='/project'>Project</Link>
            </li>
            <li>
                {this.is_auth() ?<button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
            </li>
        </nav>
     </div>
    </header>
            <Routes>
                <Route exact path='/' element={<Navigate to='/authors'/>}/>
                <Route path='/authors'>
                    <Route index element={<AuthorList authors={this.state.authors}/>} />
                    <Route path=':creatorId' element={<ToDoCreator todos={this.state.todos}/>}/>
                </Route>
                <Route exact path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)}/>}/>
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
