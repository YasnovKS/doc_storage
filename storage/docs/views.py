import reversion
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from docs.forms import PostForm
from docs.models import Document
from reversion.models import Version
from django.urls import reverse_lazy


class IndexView(ListView):
    model = Document
    template_name = 'index.html'


class DocumentDetail(DetailView):
    model = Document
    template_name = 'doc_detail.html'

    def get(self, request, pk):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        versions = Version.objects.filter(object_id=pk)
        version_list = list()
        for version in versions:
            version_list.append(version.field_dict)
        context['versions'] = version_list
        return self.render_to_response(context)


class CreateDocument(CreateView):
    form_class = PostForm
    template_name = 'document_create.html'

    @method_decorator(login_required)
    def post(self, request):
        form = self.get_form()
        if form.is_valid():
            with reversion.create_revision():
                document = form.save(commit=False)
                document.author = request.user
                document.save()
        return redirect('docs:doc_detail', pk=document.id)


class EditDocument(UpdateView):
    model = Document
    template_name = 'document_create.html'
    fields = ['title', 'content']
