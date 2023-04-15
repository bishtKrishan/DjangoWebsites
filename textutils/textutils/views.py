from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    global params
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuation_list = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation_list:
                analyzed = analyzed + char

        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercas', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Liner', 'analyzed_text': analyzed}
        djtext = analyzed

    if (spaceremove == "on"):
        analyzed = djtext.replace(" ", "")
        params = {'purpose': 'Space Remove', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        analyzed2 = djtext[0:].replace(" ", "")
        analyzed = len(analyzed2)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        djtext = analyzed

    if (
            removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremove != "on" and charcount != "on"):
        return render(request, 'nontanalyze.html')

    return render(request, 'analyze.html', params)


def aboutus(request):
    return render(request, 'aboutus.html')


def ContactUs(request):
    return render(request, 'ContactUs.html')