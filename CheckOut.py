class Checkout:
    def __init__(self, checkout_id, customer_email, first_name, last_name, card_number, billing_address, cvv, day, month, email_notification):
        self.__checkout_id = checkout_id
        self.__customer_email = customer_email
        self.__first_name = first_name
        self.__last_name= last_name
        self.__card_number = card_number
        self.__billing_address = billing_address
        self.__cvv = cvv
        self.__expiry_date_day = day  # Assuming day and month are parts of the expiry date
        self.__expiry_date_month = month
        self.__email_notification = email_notification


    def set_checkout_id(self, checkout_id):
        self.__checkout_id = checkout_id
    def get_checkout_id(self):
        return self.__checkout_id

    # Customer Email
    def set_customer_email(self, email):
        self.__customer_email = email

    def get_customer_email(self):
        return self.__customer_email

    # Customer Name
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    # Card Number
    def set_card_number(self, number):
        self.__card_number = number

    def get_card_number(self):
        return self.__card_number

    # Billing Address
    def set_billing_address(self, address):
        self.__billing_address = address

    def get_billing_address(self):
        return self.__billing_address

    # CVV
    def set_cvv(self, cvv):
        self.__cvv = cvv

    def get_cvv(self):
        return self.__cvv

    # Expiry Date
    def set_expiry_date(self, day, month):
        self.__expiry_date_day = day
        self.__expiry_date_month = month

    def get_expiry_date(self):
        return f"{self.__expiry_date_month}/{self.__expiry_date_day}"

    # Email Notification
    def set_email_notification(self, notification):
        self.__email_notification = notification

    def get_email_notification(self):
        return self.__email_notification

