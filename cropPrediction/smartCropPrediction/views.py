from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pickle
import os
from django.conf import settings
from django.shortcuts import render

model=""
prediction =''
model_path = os.path.join(settings.BASE_DIR, r'C:\Users\RAMAVATH PEDARAYUDU\miniproject\cropPrediction\smartCropPrediction\model\model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)
    print("Successfully loaded the model")

def home(request):
    return render(request, 'home.html')

def predict(request):
    print("hello ")
    return render(request,"prediction.html")

def demo(request):
    return render(request, "demo.html")

def chatbot(request):
    return render(request, 'chatbot.html')
# , {'prediction': str(prediction[0])}
    

@csrf_exempt  # Only if you are disabling CSRF protection for this view
def prediction_factor(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print("Received data:", data)
        
        # Process the data here
        features = [5.1, 3.5, 1.4, 0.2]  # Replace this with actual data extraction logic

        # Reshape the features to 2D array
        features_reshaped = [features]       
        print(features_reshaped,"reshaping done")
        prediction = model.predict(features_reshaped)
        print("prediction done")
        print(prediction)
        response_data = {
            'status': 'success',
            'message': 'Data received successfully',
            'prediction':str(prediction),
        }
        
        # return render(request, 'home.html')

        return JsonResponse(response_data)
    else:
        response_data = {
            'status': 'failure',
            'message': 'Invalid request method',
        }
        return JsonResponse(response_data, status=400)



# Load the model
