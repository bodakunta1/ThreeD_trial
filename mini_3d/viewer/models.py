from django.db import models
import os

# Create your models here.

def model_upload_path(instance, filename):
    """Generate upload path for 3D models"""
    return f'models/{instance.name}/{filename}'

class ThreeDModel(models.Model):
    FORMATS = [
        ('gltf', 'GLTF'),
        ('glb', 'GLB'),
        ('obj', 'OBJ'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    model_file = models.FileField(upload_to=model_upload_path)
    format = models.CharField(max_length=10, choices=FORMATS, default='gltf')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    scale = models.FloatField(default=1.0)
    position_x = models.FloatField(default=0.0)
    position_y = models.FloatField(default=0.0)
    position_z = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_file_extension(self):
        return os.path.splitext(self.model_file.name)[1].lower()
    