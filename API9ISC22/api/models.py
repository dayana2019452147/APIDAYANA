from django.db import models 

class Respuestaschatbot(models.Model):
    marca_temporal = models.DateTimeField()
    nombre_completo = models.CharField(max_length=100)
    pregunta1 = models.CharField(max_length=2)
    pregunta2 = models.TextField()
    pregunta3 = models.CharField(max_length=10)
    pregunta4 = models.TextField()
    pregunta5 = models.TextField()
    pregunta6 = models.CharField(max_length=20)
    pregunta7 = models.CharField(max_length=10)

    def str(self):
        return str(self.nombre_completo)
    

