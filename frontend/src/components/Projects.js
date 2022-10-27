import React from "react";

const ProjectItem = ({project})=>{
    return(
    <tr>
        <td>{project.name}</td>
        <td>{project.url}</td>
        <td>{project.users}</td>
    </tr>
    )
}

const ProjectList=({projects})=>{

    return(
        <table>
            <th>Name</th>
            <th>Project URL</th>
            <th>Users</th>
            {projects.map((project_) => <ProjectItem project={project_} />)}
        </table>
    )
}

export default ProjectList