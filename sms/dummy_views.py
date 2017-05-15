# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

from django import forms
from .models import Sms


class SmsForm(forms.ModelForm):

	class Meta:
		model = Sms
		fields = ('to', 'message')


username = "athmanziri"
apikey   = "6083c1f67ac28d2fb5525ed9be1ffac58a1fcda9998fc9d64ba672ef1baf9414"


def sms_create(request):
    if request.method == 'POST':
        form = SmsForm(request.POST)

        if form.is_valid():
            to = form.cleaned_data['to']
            message = form.cleaned_data['message']

            gateway = AfricasTalkingGateway(username, apikey)

            try:
            	results = gateway.sendMessage(to, message)

            	for recipient in results:
            		print 'number=%s;status=%s;messageId=%s;cost=%s' % (recipient['number'],
			                                                            recipient['status'],
			                                                            recipient['messageId'],
			                                                            recipient['cost'])
        	except AfricasTalkingGatewayException as e:
		    	print 'Encountered an error while sending: %s' % str(e)

            form.save()

            form = SmsForm()

            messages.success(request, "Successfully Created")
    else:
        form = SmsForm()
    return render(request, 'sms_create.html', {'form': form})