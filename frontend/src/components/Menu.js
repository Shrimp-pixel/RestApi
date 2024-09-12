import React from "react";
const styles = {
    display: 'flex',
    justifyContent:'space-around'
};

const Menu = () =>{
    return(
    <header class="site-header">
    <div style = {styles}>
      <a href="#">Django ToDoApp</a>
      <a href="#">Add task</a>
      </div>
    </header>
    )
}

export default Menu