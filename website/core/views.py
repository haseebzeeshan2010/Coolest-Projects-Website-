from django.shortcuts import render
import google.generativeai as genai
from decouple import config
from .models import Recipes
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def browse(request):
    data = Recipes.objects.all()
    return render(request, 'core/browse.html', {'data': data})



def ai(request):
    response = ""
    if request.POST:
        ai_prompt_var = request.POST
        print()
        genai.configure(api_key=config('SECRET_API_KEY'))
        model = genai.GenerativeModel("gemini-1.5-flash-8b", system_instruction="You are an italian chef named 'Chefie Alberto'. If a question is not related to recipes or music, the response should be 'I'm a chef compadre, I  do not know what you mean' ")
        # response = model.generate_content("Give me a healthy omelette recipe(do not use rich-text, bullet points or bold in the response and number steps and add bullet points to ingredients with a one line space between each step). Explain with detail.").text
        response = model.generate_content(ai_prompt_var['ai_prompt']+"(do not use rich-text, bullet points or bold in the headers and number steps and add bullet points to ingredients with a one line space between each step).").text

    return render(request, 'core/ai_test.html', {'response':response})
