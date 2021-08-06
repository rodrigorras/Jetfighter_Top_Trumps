class JetFighter:
    def __init__(self, cost_per_unit, thrust_weight, maximum_speed, maximum_range, combat_radius, roll_rate,
                 flight_ceiling, max_payload, number_engines):
        self.cost_per_unit = cost_per_unit
        self.thrust_weight = thrust_weight
        self.maximum_speed = maximum_speed
        self.maximum_range = maximum_range
        self.combat_radius = combat_radius
        self.roll_rate = roll_rate
        self.flight_ceiling = flight_ceiling
        self.max_payload = max_payload
        self.number_engines = number_engines

    def __repr__(self):
        rep = 'Fighter(' + self.name + ',' + str(self.age) + ')'
        return rep


    def shuffle_cards(self):
        pass


    def set_of_cards(self, List_of_Players):
        # Return An Equal amount of cards per user player
        pass


    def card_comparison_result(self, JetFighter, choosen_parameter, List_of_players ):
        # Return the winner of the Round

        if not isinstance(self, JetFighter):
            raise ValueError('the Top Trumps comparison requires a Top Trump card Object')
            pass
















F14_tomcat = JetFighter("38 million", 0.88, "2485 km/h", "2960 Km", "960 Km", 720, "15500m", "6700 Kg", 2)
# F16_falcon = JetFighter("64 million"),1.096, "2531,34",




if __name__ == '__main__':
    print("F14 Speed = ", F14_tomcat.maximum_speed)

