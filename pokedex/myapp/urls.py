from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), # affiche la liste des 151 premier pokemons
    path('pokemon/<int:id>', views.pokemonID, name="pokemonId"), # affiche un pokemon suiffant son id
    path('teams', views.teams, name="teams"), #affiche tout les teams enregristrer
    path('teams/<int:id>', views.teamsID, name="teamsId"), # affiche la teams suivant sont id
    path('updateTeam/', views.updateTeams, name="updateTeam"), # requete ajax supprime l'id du pokemon de la team
    path('addTeam/', views.addTeams, name="addTeams"), # requete ajax ajoute l'id du pokemon de la team
    path('nameTeam/', views.nameTeam, name="nameTeam"), # requete ajax modifier le nom de la team
    path('deleteTeam/', views.deleteTeam, name="deleteTeam"), # requete ajax supprime la team suivant son id
]
