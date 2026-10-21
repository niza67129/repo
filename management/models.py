from django.db import models

class Proyecto(models.Model):
    # Campo de texto corto (máximo 100 caracteres)[cite: 1]
    nombre = models.CharField(max_length=100)
    # Campo de texto largo[cite: 1]
    descripcion = models.TextField()
    # Campo tipo fecha[cite: 1]
    fecha_inicio = models.DateField()

    def __str__(self):
        # Muestra el nombre del proyecto en el administrador
        return self.nombre

class Tarea(models.Model):
    # Campo de texto corto (máximo 100 caracteres)[cite: 1]
    titulo = models.CharField(max_length=100)
    # Campo booleano por defecto False[cite: 1]
    completada = models.BooleanField(default=False)
    # Llave foránea hacia Proyecto con eliminación en cascada[cite: 1, 2]
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        # Muestra el título de la tarea en el administrador
        return self.titulo