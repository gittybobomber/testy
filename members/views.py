from django.http import HttpResponse
from django.template import loader
import numpy

#x = [1,2,3]
#testnumber = np.mean(x)
#print(testnumber)
def members(request):
  template = loader.get_template('basy.html')
  #context = {
    #'testnum': testnumber
  #}
  return HttpResponse(template.render())