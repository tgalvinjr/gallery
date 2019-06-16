from django.test import TestCase
from . models import Editor,Location,Category,Image
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):
    '''
    Testing the Editor class
    '''

    #setup method
    def setUp(self):
        self.alvin= Editor(first_name = 'Alvin', last_name = 'Michoma', email = 'alvinmichoma@gnmail.com')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.alvin,Editor)) 

    #Test for the save method
    def test_save_method(self):
        self.pius.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)