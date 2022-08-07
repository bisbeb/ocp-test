from ocp.api.base import OcpBase

class v1_User(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "user.openshift.io/v1", "User")
    
