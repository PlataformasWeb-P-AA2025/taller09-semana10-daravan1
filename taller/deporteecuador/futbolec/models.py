from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=100)
    user_twitter = models.CharField(max_length=100)

    def __str__(self):
        return "%s (%s) - %s " % (self.nombre, self.siglas, self.user_twitter)
    
class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=100)
    numero = models.IntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return "%s (%s) - num: %d, sueldo: %s, equipo: %s" % (
            self.nombre, self.posicion, self.numero, self.sueldo, self.equipo.nombre
        )

class Campeonato(models.Model):
    nom_campeonato = models.CharField(max_length=100)
    nom_auspiciador = models.CharField(max_length=100)

    def __str__(self):
        return "%s - auspiciado por %s" % (self.nom_campeonato, self.nom_auspiciador)
    
class CameponatoEquipo(models.Model):
    anio = models.IntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s: %d" % (self.campeonato.nom_campeonato, self.equipo.nombre, self.anio)