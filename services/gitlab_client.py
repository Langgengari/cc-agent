import gitlab
import base64
from gitlab.exceptions import GitlabGetError, GitlabError
from config.constants import GITLAB_TOKEN

def get_project_files(project_identifier: str, limit=15):
    """
    Fetches relevant files from a GitLab project for technical documentation generation.
    Handles errors like 404 Not Found.
    """
    try:  
        gl = gitlab.Gitlab('https://gitlab.com', private_token=GITLAB_TOKEN)
        project = gl.projects.get(project_identifier)

        print(f"Project '{project.name}' found successfully.")

        # 🔹 Recursively searches for all files

        files = project.repository_tree(ref='main', recursive=True, get_all=True)
        print(f"Total files found: {len(files)}")

        # 🔹 Filters out relevant files for documentation
        
        relevant_files = []
        for f in files:
            file_path = f['path'].lower()
            if (
                file_path.endswith('.js') or
                file_path.endswith('.json') or
                file_path.endswith('dockerfile') or 
                file_path.endswith('.yml') or 
                file_path.endswith('.env_example') 
            ):
        
                relevant_files.append(f)
        
        if not relevant_files:
            return {"error_message": "ERROR: Project '{project.name}' found, but no relevant files for documentation were identified."}        
    
        print(f"\nRelevant files for documentation: {[f['path'] for f in relevant_files]}")

        contents = []
        for f in relevant_files[:limit]:
            file_data = project.files.get(file_path=f['path'], ref='main')
            decoded = base64.b64decode(file_data.content).decode('utf-8')
            contents.append({"name": f['path'], "content": decoded})
    
        return contents
    
    except GitlabGetError as e:
        if e.response_code == 404:
            error_message = f"ERROR: The project with identifier '{project_identifier}' was not found in GitLab. Please check the ID or path and try again."
            return {"error_message": error_message, "code": e.response_code}
        else:
            error_message = f"ERROR: Error accessing the GitLab project: {e}"
            return {"error_message": error_message, "code": e.response_code}
    except (GitlabError, Exception) as e:
        error_message = f"ERROR: An unexpected error occurred: {e}"
        return {"error_message": error_message, "code": e.response_code}