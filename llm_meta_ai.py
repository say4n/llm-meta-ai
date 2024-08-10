import llm
from meta_ai_api import MetaAI as meta_upstream

@llm.hookimpl
def register_models(register):
    register(MetaAI())

class MetaAI(llm.Model):
    model_id = "meta.ai"
    client = meta_upstream()

    def execute(self, prompt, stream, response, conversation):
        client_response = self.client.prompt(
            message=prompt.prompt, 
            stream=stream, 
            new_conversation=True if not conversation else False
        )

        return client_response["message"] if "message" in client_response else "Oops, error!"