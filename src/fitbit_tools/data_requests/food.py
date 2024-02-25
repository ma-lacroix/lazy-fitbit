from datetime import datetime

import fitbit


def get_meal_type():
    # FitBit needs to know if this is breakfast, a snack etc.
    current_hour = int(datetime.today().strftime('%H'))
    if current_hour < 10:
        return 1
    elif 10 <= current_hour < 11:
        return 2
    elif 11 <= current_hour < 13:
        return 3
    elif 13 <= current_hour < 17:
        return 4
    else:
        return 5


class Food:
    def __init__(self, client: fitbit.Fitbit, foodId: int, unitId):
        self.client = client
        self.food_request_object = {
            'foodId': foodId,
            'mealTypeId': get_meal_type(),
            'unitId': unitId,
            'amount': 1,  # TODO: check to see if OpenAI can actually validate this
            'date': datetime.today().strftime('%Y-%m-%d')
        }

    def register_food(self):
        try:
            response = self.client._COLLECTION_RESOURCE('foods/log', date=self.food_request_object.get("date"),
                                                        data=self.food_request_object)
            print(
                f"Log ID successfully entered: {response['foodLog']['logId']} -> {response['foodLog']['loggedFood']['name']}")
        except Exception as e:
            raise ConnectionRefusedError(f"Failed to register food to FitBit account - {e}")
