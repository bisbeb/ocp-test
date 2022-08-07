from ocp.api.base import OcpBase

class v1_CredentialsRequest(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "cloudcredential.openshift.io/v1", "CredentialsRequest")
    
