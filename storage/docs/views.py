import reversion
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView
from docs.forms import CreateForm, EditForm
from docs.models import Document
from reversion.models import Version

from . import messages


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
        for version in versions[1::]:
            version_dict = version.field_dict
            version_dict['revision'] = version.revision
            version_list.append(version_dict)
        context['versions'] = version_list
        return self.render_to_response(context)


class CreateDocument(CreateView):
    form_class = CreateForm
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


@login_required
def edit_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    version = Version.objects.filter(object_id=pk).first()
    if version:
        version = version.field_dict
    title, content = document.title, document.content
    if document.author != request.user:
        return redirect('docs:doc_detail', pk=document.id)
    form = EditForm(request.POST or None,
                    instance=document)
    context = {
        'object': document,
        'form': form,
        'is_edit': True,
        'version': version
    }
    if form.is_valid():
        if form.cleaned_data.get('for_deleting'):
            return delete_document(request, pk=pk)
        with reversion.create_revision():
            if (title, content) == (form.cleaned_data.get('title'),
                                    form.cleaned_data.get('content')
                                    ):
                return render(request, 'document_create.html', context)
            form.save()
            return redirect('docs:doc_detail', pk=document.id)
    return render(request, 'document_create.html', context)


@login_required
@transaction.atomic
def delete_document(request, pk):
    obj = get_object_or_404(Document, pk=pk)
    version = Version.objects.filter(object_id=pk).first()
    revision = version.revision
    obj.delete()
    revision.comment = messages.DELETE_DOC
    revision.save()
    return redirect('docs:index')
