"""
    Test Plainsight prediction API
"""

from requests import post

class Connexion:
    def __init__(self):
        self.hostname = "app.plainsight.ai"
        self.api_key = None # API KEY
        self.model_versionId = None # MODEL VERSION
        self.input_image = None # INPUT IMAGE PATH
        #________________________________________________________________________CROSS ACCOUNT FIXED
        self.url_resquest = f"https://{self.hostname}/v1/models/{self.model_versionId}/predict"
        
    def send_image(self):
        """
        Send image to Plainsight API endpoint as form data
        :return:
        """

        post_reply = post(self.url_resquest,
                          headers={"Authorization": "Bearer " + self.api_key},
                          files={"file": open(self.input_image, "rb")})
        print(f">> Request: \n {post_reply.url} \n {post_reply.request.headers}")
        print(f">> Response {post_reply.content}")


if __name__ == "__main__":
    # Send image for prediction
    c = Connexion()
    c.send_image()
