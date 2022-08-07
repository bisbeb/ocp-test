from ocp.api.base import OcpBase

class v1_MutatingWebhookConfiguration(OcpBase):
  def __init__(self, dyn_client):
      super().__init__(dyn_client, "admissionregistration.k8s.io/v1", "MutatingWebhookConfiguration")
    
