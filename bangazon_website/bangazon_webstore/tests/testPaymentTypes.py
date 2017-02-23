from django.test import TestCase
import sys 
sys.path.append('../') 

from bangazon_webstore.models.paymenttypes import PaymentType


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
    def setUpClass(self):


        self.zach = Customer(
        id= 1,
        first_name = "Zachary", 
        last_name="Cline", 
        email = "z@s.com",
        phone_number="555-999-4444",
        city = "Nah Penzance" ,
        state = "Rhode Island" ,
        postalZip = "52801",
        address = "300 Winter's End"
        )

        self.visa = PaymentType(
        card_type = "Visa",
        card_number = "2224-333-3344",
        cvv = 111,
        expiration = "08/20",
        name_on_card = "Zachary A Cline",
        customer= self.zach.id)


    def test_can_create_a_payment_type(self):
        # Test is visa a type of PaymentType
        self.assertIsInstance(self.visa, PaymentType)

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






