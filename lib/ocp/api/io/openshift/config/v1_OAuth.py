from ocp.api.base import OcpBase

class v1_OAuth(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "config.openshift.io/v1", "OAuth")
    
