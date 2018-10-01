from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello_name(request, name):
    return HttpResponse(("Hello ", name))

def times2(request, userNum):
    return HttpResponse(("The product times 2 is: ", userNum*2))

def sum(request, userNum):
    numSum = 0
    for x in range(0,userNum):
        print(x)
        numSum += x
    return HttpResponse(("Sum is: ", numSum))