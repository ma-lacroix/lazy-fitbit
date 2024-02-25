import time

import fitbit

from src.fitbit_tools.auth_requests import authorization
from src.fitbit_tools.data_requests.food import Food


class FitBitTools:
    def __init__(self, keys: list, foods: list):
        self.auth_info = authorization.make_auth_call(keys[0], keys[1])
        self.foods = foods
        self.client = fitbit.Fitbit(client_id=keys[0],
                                    client_secret=keys[1],
                                    access_token=self.auth_info.access_token,
                                    refresh_token=self.auth_info.refresh_token,
                                    expires_at=self.auth_info.expires_at)

    def register_foods(self):

        if len(self.foods) == 0:
            raise IOError("List of foods is empty!")

        for food in self.foods:
            food_search_response = self.search_for_foods(food)
            if len(food_search_response) == 0:
                print(f"Nothing found for: {food} - nothing registered!")
                continue
            first_choice = food_search_response[0]
            flag = True
            for row in food_search_response:
                if row['brand'] == '':
                    food_data = Food(self.client, row['foodId'], row['units'][-1])
                    food_data.register_food()
                    flag = False
                    break
            if flag:  # sometimes non-branded foods can't be found
                food_data = Food(self.client, first_choice['foodId'], first_choice['units'][-1])
                food_data.register_food()
            time.sleep(0.1)

    def search_for_foods(self, food):
        retry = 0
        while retry < 3:
            food_search_response = self.client.search_foods(query=food)['foods']
            if len(food_search_response) == 0:
                # FitBit's API sometimes doesn't respond right away
                print(f"No food found for: {food}...retrying in 5 seconds...")
                retry += 1
                time.sleep(5)
            else:
                return food_search_response


