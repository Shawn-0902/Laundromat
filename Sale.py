class Sale:
    def __init__(self, sale_id, machine_id, date, time_slot, price_per_use):
        self.__sale_id = sale_id
        self.__machine_id = machine_id
        self.__date = date
        self.__time_slot = time_slot
        self.__price_per_use = price_per_use

    def get_sale_id(self):
        return self.__sale_id

    def get_machine_id(self):
        return self.__machine_id

    def get_date(self):
        return self.__date

    def get_time_slot(self):
        return self.__time_slot

    def get_price_per_use(self):
        return self.__price_per_use

    # Setters
    def set_sale_id(self, sale_id):
        self.__sale_id = sale_id

    def set_machine_id(self, machine_id):
        self.__machine_id = machine_id

    def set_date(self, date):
        self.__date = date

    def set_time_slot(self, time_slot):
        self.__time_slot = time_slot

    def set_price_per_use(self, price_per_use):
        self.__price_per_use = price_per_use

