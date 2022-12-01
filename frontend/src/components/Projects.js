import React from "react";
import { useState } from "react";

const ProjectItem = ({project, delete_project})=>{
    return(
    <tr>
        <td>{project.name}</td>
        <td>{project.url}</td>
        <td>{project.users}</td>
        <td><button onClick={()=>delete_project(project.id)} type='button'>Delete</button></td>
    </tr>
    )
}

const ProjectList=({projects, delete_project})=>{
    const [query, setQuery] = useState("")
    return(
    <div>
    <input type="text" placeholder="Search" className='search' onChange={(e) => setQuery(e.target.value)}/>
        <table>
            <th>Name</th>
            <th>Project URL</th>
            <th>Users</th>
            {projects.filter((project) => project.name.toLowerCase().includes(query)
            ).map((project_) => <ProjectItem project={project_} delete_project={delete_project} />)}
        </table>
    </div>
    )
}

export default ProjectList