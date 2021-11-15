from django.db import models


# gère un objet teams afin d'avoir une équipe de 5 pokémon
# les pokemon son enregrister par leurs id
# si un id vaut 0 c'est qu'il n'y a pas de mokémon
class Teams(models.Model):
    name = models.CharField(max_length=100)
    pokemon1 = models.IntegerField()
    pokemon2 = models.IntegerField()
    pokemon3 = models.IntegerField()
    pokemon4 = models.IntegerField()
    pokemon5 = models.IntegerField()

    # renvoie simplement le nom de la teams
    def __str__(self):
        return self.name

    # renvoie un dictionary des id des pokemon dans la teams
    def getPokemon(self):
        return {
            'pokemon1': self.pokemon1,
            'pokemon2': self.pokemon2,
            'pokemon3': self.pokemon3,
            'pokemon4': self.pokemon4,
            'pokemon5': self.pokemon5,
        }

    # recherche l'id passé en paramète dans les pokemons et supprime le premier trouver
    def deletePokemon(self, id):
        if self.pokemon1 == id:
            self.pokemon1 = 0
        elif self.pokemon2 == id:
            self.pokemon2 = 0
        elif self.pokemon3 == id:
            self.pokemon3 = 0
        elif self.pokemon4 == id:
            self.pokemon4 = 0
        elif self.pokemon5 == id:
            self.pokemon5 = 0
        self.save()

    # recherche un emplacement vide et place l'id en paramète dans les pokemons
    def addPokemon(self, id):
        if self.pokemon1 == 0:
            self.pokemon1 = id
        elif self.pokemon2 == 0:
            self.pokemon2 = id
        elif self.pokemon3 == 0:
            self.pokemon3 = id
        elif self.pokemon4 == 0:
            self.pokemon4 = id
        elif self.pokemon5 == 0:
            self.pokemon5 = id
        self.save()

    # modifie le nom de la team
    def setName(self, name):
        self.name = name
        self.save()
