from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

from .forms import ResultForm
from .models import Content, Result


class Index(ListView):
    model = Content


class Detail(DetailView):
    model = Content

    def post(self, request, *args, **kwargs):
        result_form = ResultForm(request.POST)

        if result_form.is_valid():
            result = result_form.save(commit=False)
            result.question_id = result_form.data["question"]
            result.user_id = result_form.data["user"][0]
            result.save()
            request.result_form_errors = None

            return self.get(request, *args, **kwargs)
        else:
            request.result_form_errors = result_form.errors

            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Detail, self).get_context_data(**kwargs)

        try:
            context["form_error"] = self.request.result_form_errors
        except AttributeError:
            pass

        context["result_form"] = ResultForm()

        question_list = context['content'].question_set.all()

        if self.request.user.is_authenticated():
            user_response_list = Result.objects.filter(user=self.request.user)
        else:
            user_response_list = []

        modified_question_list = []
        for question in question_list:
            if question in [response.question for response in user_response_list]:
                question.user_response = Result.objects.get(user=self.request.user, question=question)
                question.user_response_correct = Result.objects.get(user=self.request.user, question=question).result == question.answer
            else:
                question.user_response = None
                question.user_response_correct = None

            modified_question_list.append(question)

        context['question_list'] = modified_question_list

        return context


class Profile(DetailView):
    model = User
