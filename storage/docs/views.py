from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView
from docs.models import Document
from docs.forms import PostForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import reversion


class IndexView(ListView):
    model = Document
    template_name = 'index.html'


class CreateDocument(CreateView):
    form_class = PostForm
    template_name = 'document_create.html'
    success_url = reverse_lazy('documents:index')

    @method_decorator(login_required)
    def get(self, request):
        return super().get(request)

    @method_decorator(login_required)
    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            with reversion.create_revision():
                document = form.save(commit=False)
                document.author = request.user
                document.save()
        return redirect('docs:index')


class DocumentDetail(DetailView):
    model = Document
    template_name = 'doc_detail.html'
