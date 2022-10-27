import React from "react";

const ToDoItem = ({todo})=>{
    return(
    <tr>
        <td>{todo.id}</td>
        <td>{todo.project}</td>
        <td>{todo.text}</td>
        <td>{todo.creator}</td>
    </tr>
    )
}

const ToDoList=({todos})=>{

    return(
        <table>
            <th>Id</th>
            <th>Project ID</th>
            <th>Text</th>
            <th>Creator</th>
            {todos.map((todo_) => <ToDoItem todo={todo_} />)}
        </table>
    )
}

export default ToDoList
