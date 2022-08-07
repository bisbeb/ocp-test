from ocp.api.base import OcpBase

class v1_SecurityContextConstraints(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "security.openshift.io/v1", "SecurityContextConstraints")
    
