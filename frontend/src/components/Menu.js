import React from "react";
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom"

const styles = {
    display: 'flex',
    justifyContent:'space-around'
};

const Menu = () =>{
    return(
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
    )
}


export default Menu