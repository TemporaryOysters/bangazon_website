from django.test import TestCase
import sys 
sys.path.append('../') 

from bangazon_webstore.models.paymenttypes import PaymentType
from bangazon_webstore.models.customer import Customer
from django.contrib.auth.models import User



class TestPaymentType(TestCase): 

    """
    Purpose: Test PaymentType
    Author: Zach
    Tests: 
    test_can_create_a_payment_type
    test_if_payment_has_relevant_properties
    test_can_get_payment_id***


    """


    @classmethod
    def setUp(self):

        self.Zachuser = User(email = "z@z.com", password = "1234")


        self.zach = Customer(
        first_name = "Zachary", 
        last_name="Cline", 
        address = "300 Winter's End",
        city = "Nah Penzance" ,
        state_province = "Rhode Island" ,
        country = "USA" ,
        postal_code = "52801",
        user = self.Zachuser
        )

        self.visa = PaymentType(
        card_type = "Visa",
        card_number = "2224-333-3344",
        cvv = 111,
        expiration = "08/20",
        name_on_card = "Zachary A Cline",
        customer= self.zach.id
        )


    def test_can_create_a_payment_type(self):
        # Test is visa a type of PaymentType
        self.assertIsInstance(self.visa, PaymentType)

    def test_payment_has_properties(self):
        # Testing if visa Has All Required Field Properties
        self.assertIsNotNone(self.visa.get_name_on_card())
        self.assertIsNotNone(self.visa.get_card_type())
        self.assertIsNotNone(self.visa.get_card_number())
        self.assertIsNotNone(self.visa.get_expiration())
        self.assertIsNotNone(self.visa.get_cvv())

    def test_if_payment_has_relevant_properties(self):
        self.assertEqual("Zachary A Cline", self.visa.get_name_on_card())
        self.assertEqual("Visa", self.visa.get_card_type())
        self.assertEqual("2224-333-3344", self.visa.get_card_number())
        self.assertEqual("08/20", self.visa.get_expiration())
        self.assertEqual(111, self.visa.get_cvv())
        self.assertEqual(self.zach.id, self.visa.get_customer())



    def test_can_get_payment_type_id_from_database(self):
    #   self.assertEqual(1, self.visa.get_payment_id(self.visa))
        pass







