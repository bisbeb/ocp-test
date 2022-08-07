from ocp.api.base import OcpBase

class v1_OAuthAccessToken(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "oauth.openshift.io/v1", "OAuthAccessToken")
    
