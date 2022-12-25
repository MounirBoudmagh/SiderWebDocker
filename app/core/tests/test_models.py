from django.test import TestCase

from core import models

class ModelTests(TestCase):
    """Test Models"""

    def test_contactUs(self):
        contactus = models.Contact.objects.create(
            Full_Name = 'Mounir BOudmagh',
            Email = 'boudmaghmouni@gmail.comr',
            Company_name = 'SIDER',
            Country = 'algeria',
            Phone_Number = '0770862806',
            Message = 'testing ',
        )

        self.assertEqual(str(contactus), contactus.Full_Name)
