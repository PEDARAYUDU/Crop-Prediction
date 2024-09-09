from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pickle
import os
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, redirect

model=""
ms=""
sc=""
model_path1 = os.path.join(settings.BASE_DIR, r'C:\Users\RAMAVATH PEDARAYUDU\miniproject\cropPrediction\smartCropPrediction\model\minmaxscaler.pkl')
with open(model_path1, 'rb') as file:
    ms = pickle.load(file)
    print("Successfully loaded the model")
model_path2 = os.path.join(settings.BASE_DIR, r'C:\Users\RAMAVATH PEDARAYUDU\miniproject\cropPrediction\smartCropPrediction\model\standscaler.pkl')
with open(model_path2, 'rb') as file:
    sc = pickle.load(file)
    print("Successfully loaded the model")
model_path3 = os.path.join(settings.BASE_DIR, r'C:\Users\RAMAVATH PEDARAYUDU\miniproject\cropPrediction\smartCropPrediction\model\modelfinal.pkl')
with open(model_path3, 'rb') as file:
    model = pickle.load(file)
    print("Successfully loaded the mode1")
print(model.predict([[60.000000,55.000000,44.000000,23.004459,82.320763,7.840207,263.964248,3588.772799]]),"final result done")
    
# dataset=[[118.495093,28.682286,31.477236,23.991854,69.226607,6.334144,175.571323,11902.816946]]

    
# return render_template('index.html',result = result)


# result = model.predict([[118.495093,28.682286,31.477236,23.991854,69.226607,6.334144,175.571323,11902.816946]])
# print(result)

# import sklearn
# print(sklearn.__version__)
# # Load the function
# predict_crop=""
# model_path = os.path.join(settings.BASE_DIR, r'C:\Users\RAMAVATH PEDARAYUDU\miniproject\cropPrediction\smartCropPrediction\model\model2.pkl')
# with open(model_path, 'rb') as func_file:
#     predict_crop = pickle.load(func_file)

# Use the loaded function
# result = predict_crop.predict([[60.000000,55.000000,44.000000,23.004459,82.320763,7.840207,263.964248,3588.772799]])
# print(result)





def home(request):
    return render(request, 'home.html')

def predict(request):
    print("hello ")
    return render(request,"prediction.html")

def demo(request):
    return render(request, "demo.html")

def about(request):
    return render(request,"About.html")

def chatbot(request):
    return render(request, 'chatbot.html')
# , {'prediction': str(prediction[0])}
    
def result(request):
    context = {
        'pH': request.GET.get('pH', ''),
        'Nitrogen': request.GET.get('Nitrogen', ''),
        'Phosphorus': request.GET.get('Phosphorus', ''),
        'Potassium': request.GET.get('Potassium', ''),
        'Temperature': request.GET.get('Temperature', ''),
        'Humidity': request.GET.get('Humidity',''),
        'Rainfall': request.GET.get('Rainfall', ''),
        'Price': request.GET.get('Price', ''),
        'crop_name': request.GET.get('crop_name', ''),
        'image_url':request.GET.get('image_url','')
        
    }
    print(context,"result method called")
    return render(request, 'result.html', context)



# @csrf_exempt  # Only if you are disabling CSRF protection for this view
# def prediction_factor(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         print("Received data:", data)
        
#         # Process the data here
#         features = [60.000000,55.000000,44.000000,23.004459,82.320763,7.840207,263.964248,3588.772799]  # Replace this with actual data extraction logic

#         # Reshape the features to 2D array
#         features_reshaped = [features]       
#         print(features_reshaped,"reshaping done")
        
#         # prediction = model.predict(features_reshaped)
#         print("prediction done")
#         # print(prediction)
#         return redirect(f'/result?crop={"hello"}')
#         response_data = {
#             'status': 'success',
#             'message': 'Data received successfully',
#             'prediction':str(prediction),
#         }
        
#         # return render(request, 'home.html')

#         return JsonResponse(response_data)
#     else:
#         response_data = {
#             'status': 'failure',
#             'message': 'Invalid request method',
#         }
#         return JsonResponse(response_data, status=400)
from django.http import JsonResponse
from django.shortcuts import render

def prediction_crop(request):
    print("function called ")
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Extract the factors
        pH = float(data.get('pH'))  # Use float if the value is a decimal
        nitrogen = float(data.get('Nitrogen'))
        phosphorus = float(data.get('phosphorus'))
        potassium = float(data.get('potassium'))
        temperature = float(data.get('Temperature'))
        humidity = float(data.get('Humidity'))
        rainfall = float(data.get('Rainfall'))
        price = float(data.get('price'))
        
        # Perform prediction logic
        crop_name = perform_crop_prediction(pH, nitrogen, phosphorus, potassium, temperature,humidity, rainfall, price)
        print(crop_name)
        response_data = {
            'pH': pH,
            'Nitrogen': nitrogen,
            'Phosphorus': phosphorus,
            'Potassium': potassium,
            'Temperature': temperature,
            'Humidity':humidity,
            'Rainfall': rainfall,
            'Price': price,
            'crop_name': crop_name[0],
            'image_url': crop_name[1]
        }
        
        print(response_data,"method called")
        
        # Send back the predicted crop name
        return JsonResponse(response_data)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def perform_crop_prediction(pH, nitrogen, phosphorus, potassium, temperature,humidity, rainfall, price):
    print(pH, nitrogen, phosphorus, potassium, temperature,humidity, rainfall, price)
    dataset=[[nitrogen, phosphorus, potassium, temperature,humidity,pH,rainfall, price]]
    # dataset = [[40,50,50,40.0,20,100,100,10000]]
    # dataset=[[90.0,42.0,43.0,20.879744,82.002744,6.502985,202.935536,3599.264532]]

    # scaled_features = ms.transform(dataset)

    # final_features = sc.transform(scaled_features)

    prediction = model.predict(dataset)
    print(prediction)

    crop_dict = {1: ["Rice","https://tse3.mm.bing.net/th?id=OIP.M-SZvSkkZR7IcYB57P2JwQHaE8&pid=Api&P=0&h=180"],
                 2: ["Maize","https://tse2.mm.bing.net/th?id=OIP.ugm-cFh8OEOeHUoz6PFH9AAAAA&pid=Api&P=0&h=180"],
                 3:["Jute","https://t3.ftcdn.net/jpg/01/91/27/76/360_F_191277640_tdXKlzGlKAI8701Wd0WHQm6ljHAgDGPw.jpg"],
                    4:["Cotton","https://t3.ftcdn.net/jpg/06/69/99/98/360_F_669999869_h9wNAaEWgbidk2AWunnDwWlKZ5gwD3nG.jpg"],
                    5:["Coconut","https://img.freepik.com/premium-photo/ripe-sweet-coconut-coconut-halves-isolated_531456-7.jpg"],
                    6:["Papaya","https://t3.ftcdn.net/jpg/01/77/22/44/360_F_177224431_6S50Gr64wFWjkDHBGXq7PkaG5kcrgEgd.jpg"],
                    7:["Orange","https://t4.ftcdn.net/jpg/00/61/19/53/360_F_61195341_rR4lMptEspj16GvOdmy0MaMznSRveh2M.jpg"],
                    8:["Apple","https://t4.ftcdn.net/jpg/04/96/45/49/360_F_496454926_VsM8D2yyMDFzAm8kGCNFd7vkKpt7drrK.jpg"],
                    9:["Muskmelon","https://cdn.grofers.com/cdn-cgi/image/f=auto,fit=scale-down,q=70,metadata=none,w=900/app/images/products/sliding_image/264020a.jpg?ts=1691661227"],
                    10:["Watermelon","https://thumbs.dreamstime.com/b/big-watermelon-slice-white-background-as-package-design-element-44517200.jpg"],
                    11:["Grapes","https://www.shutterstock.com/image-photo/dark-blue-grape-leaves-isolated-600nw-604667843.jpg"],
                    12:["Mango","https://t4.ftcdn.net/jpg/00/99/07/25/360_F_99072593_6rdXXrxVEz7pSItOhfCB6y4oKDANeQLa.jpg"],
                    13:["Banana","https://images2.alphacoders.com/133/1338260.png"],
                    14:["Pomegranate","https://www.pngitem.com/pimgs/m/524-5245232_pomegranate-hd-png-download.png"],
                    15:["Lentil","https://i.pinimg.com/736x/e9/20/a0/e920a0049052111e182bb73bac0f498c.jpg"],
                    16:["Blackgram","https://media.istockphoto.com/id/1225389860/photo/black-gram-or-a-pile-of-dry-black-beans-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=c_7yDxn255F5rSowZB74AWD7UL68WbEhOMD9OnKZvK8="],
                    17:["Mungbean","https://t3.ftcdn.net/jpg/03/77/63/94/360_F_377639412_FOEg3T7ECckXYzDrKwagqJOwHODm4wR9.jpg"],
                    18:["Mothbeans","https://www.greendna.in/cdn/shop/products/moth2_594x.jpg?v=1591178564"],
                    19:["Pigeonpeas","https://www.shutterstock.com/image-photo/fresh-green-pigeon-pea-seed-260nw-1878368575.jpg"],
                    20:["Kidneybeans","https://t4.ftcdn.net/jpg/04/65/75/43/360_F_465754343_chzIIFu8ys7Bpj8hMbDVSjXTtw7EcLsc.jpg"],
                    21:["Chickpea","https://t3.ftcdn.net/jpg/02/83/97/16/360_F_283971637_l01oKnCdtSDjeSrr0HzsK35wQtx91CNc.jpg"],
                    22:["Coffee","https://media.istockphoto.com/id/1572106495/photo/coffee-beans.webp?b=1&s=170667a&w=0&k=20&c=dD7aobJtywiLWCQrsYC-ikPRhJIUEG5vfg-tCUuABJo="]
}
    

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is the best crop to be cultivated right there".format(crop)
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
        

    # Dummy prediction logic, replace with actual model or logic
    return crop_dict[prediction[0]]  # Example crop name




# Load the model
