from ocp.api.base import OcpBase

class v1_Project(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "project.openshift.io/v1", "Project")
    
