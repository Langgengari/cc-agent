from services.gitlab_client import get_project_files

def generate_documentation(repository_type: str, project_identifier: str) -> str:
    """
    Generates technical API documentation based on source code from the specified repository.

    Inputs:
    - repository_type (string): The type of repository (e.g., 'gitlab', 'github').
    - project_identifier (string): The project ID or full path (e.g., '12345678', 'my-group/my-project').

    Outputs: 
    - Returns the documentation for the user.
    """
    print(f"Generating documentation for repository: {repository_type}, project: {project_identifier}")

    if repository_type.lower() != 'gitlab':
        return "Currently, only GitLab repositories are supported."

    files = get_project_files(project_identifier)
    print(f"Return from get_project_files: {files}")

    if isinstance(files, dict) and 'error_message' in files:
        return files['error_message']
    
    joined_files = "\n\n".join([
        f"### {f['name']}\n```js\n{f['content']}\n```"
        for f in files
    ])
    
    return joined_files