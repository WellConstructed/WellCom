from django.test import TestCase
from wellcom_app.models import Well, Note, DeviceData, WaterTest, Usage
from django.utils import timezone
from django.core.urlresolvers import reverse
from time import sleep

# Using this for Django testing guidance:
# https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/


# MODELS TESTS
class WellTest(TestCase):

    def create_well(self, name="Test Well", latitude=35.993078,
                    longitude=-78.904689, country="United States",
                    date_installed="2016-07-11", last_update=timezone.now(),
                    estimated_users=500, cost_usd=8000.50,
                    contractor="Test Contractor", flow_rate_lpm=120):
        return Well.objects.create(name=name, latitude=latitude,
                                   longitude=longitude, country=country,
                                   date_installed=date_installed,
                                   last_update=last_update,
                                   estimated_users=estimated_users,
                                   cost_usd=cost_usd, contractor=contractor,
                                   flow_rate_lpm=flow_rate_lpm
                                   )

    def test_well_creation(self):
        well = self.create_well()
        self.assertTrue(isinstance(well, Well))
        self.assertEqual(well.__str__(), well.name)

    def test_well_save(self):
        well = self.create_well()
        create_time = well.last_update
        sleep(1)
        well.name = 'Test Saved Well'
        well.save()

        self.assertTrue(create_time is not w.last_update)
        self.assertTrue(isinstance(w, Well))
        self.assertEqual(w.__str__(), 'Test Saved Well')


class NoteTest(TestCase):

    def create_note(self, well=WellTest.create_well(),
                    title="Test note title", text="Test note text"):
        return Note.objects.create()

    def test_note_creation(self):
        note = self.create_well()
        self.assertTrue(isinstance(note, Note))
        self.assertEqual(note.__str__(), note.title)


class DeviceDataTest(TestCase):
    pass


class WaterTestTest(TestCase):
    pass


class UsageTest(TestCase):
    pass


# VIEWS TESTS
