# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import shutil
import requests
import json

# Rest framework
from rest_framework.decorators import api_view, permission_classes

# Django http
from django.http import JsonResponse

""" OCR """
APP_ID = 'math24'
APP_KEY = '15c9af36a4d8882b1aa2ba98ac13e0df'


@api_view(['POST'])
@permission_classes(())
def ocr(request):
    if request.method == 'POST':
        """ Get image url """
        image = request.data['url']

        """ Download image """
        get_image = requests.get(image, stream=True)

        with open("image.jpg", "wb") as out_file:
            shutil.copyfileobj(get_image.raw, out_file)
        del get_image

        """ Push image to OCR """
        r = requests.post('http://api.mathpix.com/v2/latex',
                          files={'file': open('image.jpg', 'rb')},
                          headers={"app_id": APP_ID, "app_key": APP_KEY})

        answer = json.loads(r.text)
        return JsonResponse({'answer': answer["latex"].encode("utf-8").replace(' ', '')})
