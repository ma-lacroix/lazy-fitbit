from openai import OpenAI


class GPT4Vision:
    def __init__(self, key: str, url: str):
        self.client = OpenAI(api_key=key)
        self.url = url
        self.foods = []

    def get_image_data(self):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "Return a simple comma separated list with just the food items in your response"
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": self.url
                                },
                            },
                        ],
                    }
                ],
                max_tokens=100,
            )
            foods = response.dict()["choices"][0]['message']['content'].split(",")
            if type(foods) != list:
                raise IOError("Failed to get a proper list from OpenAI")
            print(f"\nGPT-4-1106-vision results: {foods}\n")
            self.foods = foods
        except Exception as e:
            raise ConnectionRefusedError(f"Failed to request data from OpenAI - {e}")
