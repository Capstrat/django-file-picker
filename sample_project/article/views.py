import os
import tempfile

from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseServerError
from django.utils import simplejson as json
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile

from sample_project.article.models import Image
from sample_project.article.forms import AjaxImageForm

from sorl.thumbnail.main import DjangoThumbnail 

import file_picker


class ImagePicker(file_picker.FilePickerBase):
    model = Image
    form = AjaxImageForm
    
    def get_queryset(self,search):
        return Image.objects.filter(name__icontains=search)
    
    def append(self, obj):
        thumb = DjangoThumbnail(obj.file, (150, 150))
        return {
            'name': unicode(obj), 'url': obj.file.url,
            'thumb': {
                'url': thumb.absolute_url,
                'width': thumb.width(),
                'height': thumb.height(),
            },
            'insert': '<img src="%s" />' % obj.file.url
        }
    