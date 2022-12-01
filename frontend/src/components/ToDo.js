import React from "react";

const ToDoItem = ({todo, delete_todo})=>{
    return(
    <tr>
        <td>{todo.id}</td>
        <td>{todo.project}</td>
        <td>{todo.text}</td>
        <td>{todo.creator}</td>
        <td><button onClick={()=>delete_todo(todo.id)} type='button'>Delete</button></td>
    </tr>
    )
}

const ToDoList=({todos, delete_todo})=>{

    return(
        <table>
            <th>Id</th>
            <th>Project ID</th>
            <th>Text</th>
            <th>Creator</th>
            <th></th>
            {todos.map((todo_) => <ToDoItem todo={todo_} delete_todo={delete_todo} />)}
        </table>
    )
}

export default ToDoList
