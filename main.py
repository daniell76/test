import urllib.request


def get_project_id():
    url = "https://metadata.google.internal/computeMetadata/v1/project/project-id"
    req = urllib.request.Request(url)
    req.add_header("Metadata-Flavor", "Google")
    project_id = urllib.request.urlopen(req).read().decode()
    print(f"current project_id = {project_id}")


get_project_id()