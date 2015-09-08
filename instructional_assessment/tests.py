from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Content, Question, Result


class SimpleTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            first_name="foo",
            last_name="bar",
            email="test@test.com",
            username="admin"
        )
        self.user.set_password("admin")
        self.user.save()
        self.action = Content.objects.create(
            title="This is test Content",
            body="Django is written in python.Django is a framework.",
            source="http://www.example.com",

            )
        self.action = Question.objects.create(
            content=Content.objects.first(),
            question_content="Django is written in python.",
            answer=True,

            )
        self.action = Result.objects.create(
            user=User.objects.first(),
            question=Question.objects.first(),
            result=True,

            )

    def test_index(self):
        self.client.login(username=self.user.username, password='admin')
        expected_status_code = 200
        expected_template_path = "instructional_assessment/content_list.html"
        response = self.client.get(reverse("index"))
        self.assertContains(response, "Mexicoder")
        self.assertContains(response, "productions")

        self.assertEqual(
            expected_status_code,
            response.status_code
        )
        self.assertTemplateUsed(response, expected_template_path)

    def test_detail(self):
        self.client.login(username=self.user.username, password="admin")
        content = Content.objects.first()
        expected_status_code = 200
        expected_template_path = "instructional_assessment/content_detail.html"
        response = self.client.get(reverse("detail", kwargs={"pk": content.pk}))
        self.assertContains(response, "written")

        self.assertEqual(
           expected_status_code,
           response.status_code
        )
        self.assertTemplateUsed(response, expected_template_path)

    def test_detail_un(self):
        content = Content.objects.first()
        expected_status_code = 200
        expected_template_path = "instructional_assessment/content_detail.html"
        response = self.client.get(reverse("detail", kwargs={"pk": content.pk}))
        self.assertContains(response, "python")
        self.assertEqual(
           expected_status_code,
           response.status_code
        )
        self.assertTemplateUsed(response, expected_template_path)

    def test_user_detail(self):
        Result.objects.create(
            user=User.objects.first(),
            question=Question.objects.first(),
            result=True,

            )
        self.client.login(username=self.user.username, password="admin")
        user = User.objects.first()
        expected_status_code = 200
        expected_template_path = "auth/user_detail.html"
        response = self.client.get("/profile/{pk}/".format(pk=user.pk))
        self.assertContains(response, "True")

        self.assertEqual(
           expected_status_code,
           response.status_code
        )
        self.assertTemplateUsed(response, expected_template_path)

    def test_content_creation(self):
        self.client.login(username=self.user.username, password="admin")
        Content.objects.create(title="A Text", body="A body")
        response = self.client.get("/")
        expected_status_code = 200
        self.assertContains(response, "A Text")
        self.assertContains(response, "A body")

        self.assertEqual(
           expected_status_code,
           response.status_code
        )

    def test_question_creation(self):
        self.client.login(username=self.user.username, password="admin")
        Question.objects.create(
            content=Content.objects.first(),
            question_content="Django is written in python.",
            answer=True,

            )
        response = self.client.get("/")
        expected_status_code = 200
        self.assertContains(response, "Django")
        self.assertContains(response, "Content")

        self.assertEqual(
           expected_status_code,
           response.status_code
        )
