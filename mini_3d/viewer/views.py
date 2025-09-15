from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import ThreeDModel
from .forms import ModelUploadForm
import json

def home(request):
    """Main viewer page with all 3D models"""
    models = ThreeDModel.objects.all()

     
    # Prepare models data for JavaScript
    models_data = []
    for model in models:
        model_dict = {
            'id': model.id,
            'name': model.name,
            'url': model.model_file.url,
            'format': model.format,
            'scale': model.scale,
            'position': {
                'x': model.position_x,
                'y': model.position_y,
                'z': model.position_z
            }
        }
        models_data.append(model_dict)
        print(f"  -  Added to JS : {model_dict}")
    
    context = {
        'models': models,
        'models_json': json.dumps(models_data)
    }
    return render(request, 'viewer/home.html', context)

def upload_model(request):
    """Handle 3D model uploads"""
    if request.method == 'POST':
        form = ModelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '3D model uploaded successfully!')
            return redirect('viewer:home')
    else:
        form = ModelUploadForm()
    
    return render(request, 'viewer/upload.html', {'form': form})

