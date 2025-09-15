from django import forms
from .models import ThreeDModel

class ModelUploadForm(forms.ModelForm):
    class Meta:
        model = ThreeDModel
        fields = ['name', 'description', 'model_file', 'format', 'thumbnail', 'scale', 'position_x', 'position_y', 'position_z']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'model_file': forms.FileInput(attrs={'class': 'form-control', 'accept': '.gltf,.glb,.obj'}),
            'format': forms.Select(attrs={'class': 'form-control'}),
            'scale': forms.NumberInput(attrs={'step': '0.1', 'min': '0.1', 'class': 'form-control'}),
            'position_x': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'position_y': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
            'position_z': forms.NumberInput(attrs={'step': '0.1', 'class': 'form-control'}),
        }
    
    def clean_model_file(self):
        file = self.cleaned_data['model_file']
        if file:
            allowed_extensions = ['.gltf', '.glb', '.obj']
            file_extension = file.name.lower().split('.')[-1]
            if f'.{file_extension}' not in allowed_extensions:
                raise forms.ValidationError(
                    "Unsupported file extension. Allowed extensions are: .gltf, .glb, .obj"
                    )
            if file.size > 100 *1024 *1024:  # 100 MB limit
                raise forms.ValidationError(
                    "File size exceeds the limit of 50MB."
                    )
        return file
    
