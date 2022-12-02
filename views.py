def memoCreateView(request):
    template_name="note_input.html"

    if request.POST:
        title = request.POST["title"]
        f = cgi.FieldStorage()
        text = f.getfirst("text")
        image = request.POST["image"]
        # content = request.POST["content"]
        
    return render(request, template_name)
