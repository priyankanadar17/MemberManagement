from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from MemberManagement.tests.integration import IntegrationTest

from alumni.models import Alumni


class SkillsTest(IntegrationTest, StaticLiveServerTestCase):
    fixtures = ['registry/tests/fixtures/signup_04_job.json']

    def setUp(self):
        super().setUp()
        self.login('Mounfem')

    def test_signup_skills_complete(self):
        self.submit_form('setup_skills', 'input_id_submit', send_form_keys={
            'id_otherDegrees': 'Bachelor of Computer Science from IUB',
            'id_spokenLanguages': 'German, English, Spanish',
            'id_programmingLanguages': 'HTML, CSS, JavaScript, Python',
            'id_areasOfInterest': 'Start-Ups, Surfing, Big Data, Human Rights'
        }, select_checkboxes={
            'id_alumniMentor': True,
        })

        self.assertEqual(self.current_url, reverse('setup_atlas'),
                         'Check that the user gets redirected to the atlas page')

        obj = Alumni.objects.first().skills
        self.assertEqual(obj.otherDegrees, "Bachelor of Computer Science from IUB")
        self.assertEqual(obj.spokenLanguages, "German, English, Spanish")
        self.assertEqual(obj.programmingLanguages, "HTML, CSS, JavaScript, Python")
        self.assertEqual(obj.areasOfInterest, "Start-Ups, Surfing, Big Data, Human Rights")
        self.assertEqual(obj.alumniMentor, True)

    def test_signup_job_empty(self):
        self.submit_form('setup_skills', 'input_id_submit', send_form_keys={
            'id_otherDegrees': '',
            'id_spokenLanguages': '',
            'id_programmingLanguages': '',
            'id_areasOfInterest': ''
        }, select_checkboxes={
            'id_alumniMentor': False,
        })

        self.assertEqual(self.current_url, reverse('setup_atlas'),
                         'Check that the user gets redirected to the atlas page')

        obj = Alumni.objects.first().skills
        self.assertEqual(obj.otherDegrees, '')
        self.assertEqual(obj.spokenLanguages, '')
        self.assertEqual(obj.programmingLanguages, '')
        self.assertEqual(obj.areasOfInterest, '')
        self.assertEqual(obj.alumniMentor, False)
