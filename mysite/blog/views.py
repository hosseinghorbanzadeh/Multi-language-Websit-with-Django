from django.shortcuts import render,HttpResponse

# Create your views here.
def index_view(request):
    return render(request,'website/index.html')
    #return HttpResponse("Hello Word ")
