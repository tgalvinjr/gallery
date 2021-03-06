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
        self.alvin.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    #Test for the Delete method
    def test_delete_method(self):
        self.alvin.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) ==0)
        
    def tearDown(self):
        Editor.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()


class LocationTestClass(TestCase):
    '''
    Testing the Location model
    '''

    def setUp(self):
         self.location = Location(name= 'Wendani')

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    #Test for the save method
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    
    #Test for the Delete method
    def test_delete_method(self):
        self.location.save_location()
        self.location.delete_location()    
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)






