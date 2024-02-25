from utils import utils
from fitbit_tools.fitbit_tools import FitBitTools
from openai_tools.gpt4_vision import GPT4Vision


def main():
    # # getting image data
    openai_key = utils.fetch_openai_key()
    # TODO: url is temporary - for demo purposes
    gpt4_vision = GPT4Vision(openai_key, "https://c8.alamy.com/comp/J2T7AD/nice-plate-of-american-food-J2T7AD.jpg")
    gpt4_vision.get_image_data()

    # # registering data to fitbit account
    fitbit_keys = utils.fetch_fitbit_keys()
    fitbit_tools = FitBitTools(fitbit_keys, gpt4_vision.foods)
    fitbit_tools.register_foods()


if __name__ == "__main__":
    main()
