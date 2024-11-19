from django.db import models
from django.contrib.auth.models import User

class DroneCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

class Drone(models.Model):
    name = models.CharField(max_length=250, unique=True)
    drone_category = models.ForeignKey(
        DroneCategory, related_name="drones", on_delete=models.CASCADE
    )
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User, related_name="drones", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

class Pilot(models.Model):
    MALE = "M"
    FEMALE = "F"
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )
    name = models.CharField(max_length=150, blank=False, unique=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=MALE,
    )
    races_count = models.IntegerField()
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

class Competition(models.Model):
    pilot = models.ForeignKey(
        Pilot, related_name="competitions", on_delete=models.CASCADE
    )
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    distance_in_feet = models.IntegerField()
    distance_achievement_date = models.DateTimeField()

    class Meta:
        # Order by distance in descending order
        ordering = ("-distance_in_feet",)

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    publicado_em = models.DateField()

    def __str__(self):
        return self.titulo

class Colecao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)
    livros = models.ManyToManyField(Livro, related_name="colecoes")
    colecionador = models.ForeignKey(User, on_delete=models.CASCADE, related_name="colecoes")

    def __str__(self):
        return f"{self.nome} - {self.colecionador.username}"
