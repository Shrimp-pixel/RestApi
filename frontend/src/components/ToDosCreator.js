import React from "react";
import {useParams} from "react-router-dom";

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

const ToDoCreator=({todos})=>{
    let {creatorId} = useParams()
    console.log(creatorId)
    let filter_todos = todos.filter((todo)=> todo.creator == (parseInt(creatorId)))
    return(
        <table>
            <th>Id</th>
            <th>Project ID</th>
            <th>Text</th>
            <th>Creator</th>
            {filter_todos.map((todo_)=> <ToDoItem todo={todo_} />)}
        </table>
    )
}

export default ToDoCreator
