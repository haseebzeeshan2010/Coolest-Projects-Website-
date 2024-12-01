from django.shortcuts import render
import google.generativeai as genai
from decouple import config
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def ai(request):
    print(request.POST)
    genai.configure(api_key=config('SECRET_API_KEY'))
    model = genai.GenerativeModel("gemini-1.5-flash-8b")
    response = model.generate_content("Give me a healthy omelette recipe(do not use rich-text, bullet points or bold in the response and number steps and add bullet points to ingredients with a one line space between each step). Explain with detail.").text

    return render(request, 'core/ai_test.html', {'response':response})
