from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

from .models import igpm
from django.template import loader
from django.shortcuts import get_object_or_404,render
from django.http import Http404
from django.urls import reverse
from decimal import Decimal

def list(request):
    latest_igpm_list = igpm.objects.order_by('-data')[:5]
    output = ', <BR>'.join([q.data.strftime("%B %Y") for q in latest_igpm_list])
    return HttpResponse(output)

def index(request):
    latest_igpm_list = igpm.objects.order_by('-data')[:5]
#    template = loader.get_template('juroComposto/index.html')
    context = {'latest_igpm_list': latest_igpm_list,}
 #   return HttpResponse(template.render(context, request))
    return render(request, 'juroComposto/index.html', context)

def detail(request, igpm_id):
    try:
        igpmt = igpm.objects.get(pk=igpm_id)
    except igpm.DoesNotExist:
        raise Http404("igpm does not exist")
    return render(request, 'juroComposto/detail.html', {'igpm': igpmt})

def updateIgpm(request, igpm_id):
    igpmt = get_object_or_404(igpm, pk=igpm_id)
    try:
        newTaxa = Decimal(request.POST['taxa'])
        print(request.POST['taxa'])
        print(newTaxa)
    except Exception as e:
        # Redisplay the question voting form.
        return render(request, 'juroComposto/detail.html', {
            'igpm': igpmt,
            'error_message': "Valor nao numerico",
        })
    else:
        igpmt.taxa = newTaxa
        igpmt.multiplicadorAbsoluto = 1 + (newTaxa/100)
        igpmt.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('juroComposto:index', args=(igpmt.id,)))