import React from "react";

class ProjectForm extends React.Component {

        constructor(props){
            super(props);
            this.state = {'name':'', 'url':'', 'users':[]}
        }

        handleChange(event){
            this.setState(
                {
                    [event.target.name]: event.target.value
                }
            );
        }

        handleUserChange(event){
            if(!event.target.selectedOptions){
                this.setState({
                    'users':[]
                    })
                return;
                }

                let users = []

                for(let i = 0; i < event.target.selectedOptions.length; i++){
                    users.push(event.target.selectedOptions.item(i).value)
                }
                this.setState(
                    {'users':users}
                )
        }



        handleSubmit(event){
            this.props.create_project(this.state.name, this.state.url, this.state.users)
            event.preventDefault()
        }

        render() {
            return (
                <form onSubmit={(event)=> this.handleSubmit(event)}>

                <div className="form-group">
                    <label htmlFor='name'></label>
                    <input type="name" name="name" placeholder="name" required
                        value={this.state.name}
                        onChange={(event)=>this.handleChange(event)} />

                    <label htmlFor='url'></label>
                    <input type="url" name="url" placeholder="url" required
                        value={this.state.url}
                        onChange={(event)=>this.handleChange(event)} />
                </div>

                <select name='users' multiple id='' onChange={(event) => this.handleUserChange(event)} required>
                    {this.props.users.map((item)=><option value={item.id}>{item.id} {item.username}</option>)}
                </select>

                    <input type="submit" value="Save" />
                </form>);
        }
}

export default ProjectForm