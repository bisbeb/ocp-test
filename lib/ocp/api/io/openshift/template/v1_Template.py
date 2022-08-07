from ocp.api.base import OcpBase

class v1_Template(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "template.openshift.io/v1", "Template")
    
