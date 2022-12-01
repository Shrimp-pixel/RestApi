import React from "react";

class ToDoForm extends React.Component {

        constructor(props){
            super(props);
            this.state = {'text':'', 'project':'', 'creator':''}
        }

        handleChange(event){
            this.setState(
                {
                    [event.target.name]: event.target.value
                }
            );
        }

        handleCreatorChange(event){
            if(!event.target.selectedOptions){
                this.setState({
                    'creator':''
                    })
                return;
                }

                let creator = ''

                // for(let i = 0; i < event.target.selectedOptions.length; i++){
                //     creator = event.target.selectedOptions.item(i).value
                // }

                creator = event.target.selectedOptions.item(0).value
                this.setState(
                    {'creator':creator}
                )
        }

        handleProjectChange(event){
            if(!event.target.selectedOptions){
                this.setState({
                    'project':''
                    })
                return;
                }

                let project = ''
                //for(let i = 0; i < event.target.selectedOptions.length; i++){
                //    project=event.target.selectedOptions.item(i).value
                //}
                project=event.target.selectedOptions.item(0).value

                this.setState(
                    {'project':project}
                )
        }

        handleSubmit(event){
            this.props.create_todo(this.state.text, this.state.project, this.state.creator)
            event.preventDefault()
        }

        render() {
            return (
                <form onSubmit={(event)=> this.handleSubmit(event)}>

                <div className="form-group">
                    <label htmlFor='text'></label>
                    <input type="text" name="text" placeholder="text" required
                        value={this.state.text}
                        onChange={(event)=>this.handleChange(event)} />
                </div>

                <select name='creator' id='' onChange={(event) => this.handleCreatorChange(event)} required>
                <option value="none" selected disabled hidden>Select an Option</option>
                    {this.props.creator.map((item)=><option value={item.id}>{item.id} {item.username}</option>)}
                </select>

                <select name='project' id='' onChange={(event) => this.handleProjectChange(event)} required>
                <option value="none" selected disabled hidden>Select an Option</option>
                    {this.props.project.map((item)=><option value={item.id}>{item.id} {item.name}</option>)}
                </select>

                    <input type="submit" value="Save" />
                </form>);
        }
}

export default ToDoForm
