# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

from django import forms
from .models import Sms


class SmsForm(forms.ModelForm):
	to = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

	class Meta:
		model = Sms
		fields = ('to', 'message')


def sms_list(request):
    sph_messages = Sms.objects.all()
    return render(request, 'sms_list.html', {'sph_messages': sph_messages})


username = "athmanziri"
apikey   = "6083c1f67ac28d2fb5525ed9be1ffac58a1fcda9998fc9d64ba672ef1baf9414"


def sms_create(request):
    if request.method == 'POST':
        form = SmsForm(request.POST)

        if form.is_valid():
            to = form.cleaned_data['to']
            message = form.cleaned_data['message']

            gateway = AfricasTalkingGateway(username, apikey)

            results = gateway.sendMessage(to, message)

            form.save()

            form = SmsForm()

            # messages.success(request, "Successfully Created")
    else:
        form = SmsForm()
    return render(request, 'sms_create.html', {'form': form})