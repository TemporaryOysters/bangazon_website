from django.db import models


class PaymentType(models.Model):
    
    """PaymentType model class
        The purpose of this class is to define customer's payment types
        author: Zachary
        methods: string return
        meta: plural name
    """
    card_type = models.CharField(max_length=30)
    card_number = models.CharField(max_length=25)
    cvv = models.CharField(max_length=4)
    expiration = models.DateField(auto_now=False)
    name_on_card = models.CharField(max_length=55)
    customer = models.ForeignKey(Customer, null=True)

    class Meta:
        verbose_name_plural = "PaymentTypes"

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.card_type, self.card_number, self.cvv, self.expiration, self.name_on_card, self.customer,)

    def get_name_on_card(self):
        return self.__name_on_card

    def get_card_type(self):
        return self.__card_type

    def get_card_number(self):
        return self.__card_number

    def get_exp_date(self):
        return self.__exp_date

    def get_cvv(self):
        return self.__cvv

    def get_customer(self):
        return self.__customer


    def get_customer_name(self):
        return self.__customer.get_full_name()