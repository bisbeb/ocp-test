from ocp.api.base import OcpBase

class v1_OpenShiftAPIServer(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "operator.openshift.io/v1", "OpenShiftAPIServer")
    
