from ocp.api.base import OcpBase

class v1_Tuned(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "tuned.openshift.io/v1", "Tuned")
    
