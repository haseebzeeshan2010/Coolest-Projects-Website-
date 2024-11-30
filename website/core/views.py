from django.shortcuts import render
# import google.generativeai as genai


# Create your views here.
def index(request):
    print("eh")
    return render(request, 'core/index.html')

# def ai(request):
#     genai.configure(api_key="")
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     response = model.generate_content("Give me a healthy omelette recipe").text
#     print(response)
#     return render(request, 'core/index.html', response)
