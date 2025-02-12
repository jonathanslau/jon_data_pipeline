from pathlib import Path

def get_root():
    """Git based method for returning root path"""
    project_path = Path(__file__).resolve().parent
    while not (project_path / ".git").exists() and project_path != project_path.parent:
        project_path = project_path.parent

    return project_path


if __name__ == "__main__":
    
    print(get_root())
