from ocp.api.base import OcpBase

class v1_Route(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "route.openshift.io/v1", "Route")
    
