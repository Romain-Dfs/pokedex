import random

import requests
from django.http import HttpResponse
from django.template import loader

from .models import Teams


# affiche les 151 premier pokemon
def index(request):
    # récupre la liste des pokemon
    pokemonList = requestAPI("https://pokeapi.co/api/v2/pokemon?limit=151")
    if "ERROR" in pokemonList:
        return returnTemplateError(pokemonList['ERROR'])
    else:
        # récupère les données des pokémon
        pokemonArray = []
        for pokemon in pokemonList['results']:
            pokemonData = requestAPI(pokemon['url'])
            if "ERROR" in pokemonData:
                return returnTemplateError(pokemonData['ERROR'])
            else:
                pokemonArray.append(pokemonData)

        # envoie les données du pokemon aux données pour le template
        data = {'results': pokemonArray}

        # récupère la liste de tout les pokemon pour l'options de recherche
        data['searchPokemon'] = retDataSearchPokemon()

        # affiche le template avec les data
        template = loader.get_template('index.html')
        return HttpResponse(template.render(data))


# affiche un pokemon suivant son id
def pokemonID(request, id):
    # récupère le pokemon depuis l'api
    pokemonData = requestAPI('https://pokeapi.co/api/v2/pokemon/' + str(id))
    if "ERROR" in pokemonData:
        return returnTemplateError(pokemonData['ERROR'])
    else:
        data = pokemonData
        # modifie le poids du pokemon pour l'affiche en kg
        data['weight'] = str(float(data['weight']) / 10)

        # récupère des données supplémentaire sur le pokemone
        pokemonSpecie = requestAPI('https://pokeapi.co/api/v2/pokemon-species/' + str(id))
        if "ERROR" in pokemonSpecie:
            return returnTemplateError(pokemonSpecie['ERROR'])
        else:
            # récupère sont groupes d'oeufs
            data['egg_groups'] = pokemonSpecie['egg_groups'][0]['name']
            # recupère la description des abillitées du pokemon
            dataAbilities = []
            for ability in pokemonData['abilities']:
                pokemonAbilitie = requestAPI(ability['ability']['url'])
                if "ERROR" in pokemonAbilitie:
                    return returnTemplateError(pokemonAbilitie['ERROR'])
                else:
                    # récupère la description en anglais
                    for effect_entry in pokemonAbilitie['effect_entries']:
                        if (effect_entry['language']['name'] == "en"):
                            dataAbilities.append({'name': ability['ability']['name'], 'effect': effect_entry['effect']})
                    data['dataAbilities'] = dataAbilities

            # récupère la liste de tout les pokemon pour l'options de recherche
            data['searchPokemon'] = retDataSearchPokemon()
            # affiche le template avec les data
            template = loader.get_template('pokemonID.html')
            return HttpResponse(template.render(data))


# affiche tout les teams
def teams(request):
    data = {'teams': Teams.objects.all}
    data['searchPokemon'] = retDataSearchPokemon()
    template = loader.get_template('teams.html')
    return HttpResponse(template.render(data))


# affiche la ta team de manière plus détailler
# id en paramètre est l'id de la team
def teamsID(request, id):
    # si l'id en paramètre est 0 on est sur une crétion de team
    # on va donc créer une nouvelle team
    # sinon on récupère avec son id
    if id != int(0):
        team = Teams.objects.get(pk=id);
    else:
        team = Teams(name='', pokemon1=0, pokemon2=0, pokemon3=0, pokemon4=0, pokemon5=0)
        team.save()
        # récupère le nouvell id de la team créer
        id = team.id
    # initialise les variable envoyé au front
    data = {
        'name': str(team),
        'idteam': str(id)
    }
    # récupère tout les pokemons
    pokemons = team.getPokemon()
    # pour tout les pokémons va récupère les datas depuis l'api
    for key in pokemons:
        if pokemons[key] != 0:
            pokemonData = requestAPI('https://pokeapi.co/api/v2/pokemon/' + str(pokemons[key]))
            if "ERROR" in pokemonData:
                return returnTemplateError(pokemonData['ERROR'])
            else:
                data[key] = pokemonData
                data[key]['weight'] = str(float(data[key]['weight']) / 10)
        # si l'id du pokemon égale à 0 alors le pokemone n'exite pas on créais un pokemon vide
        else:
            data[key] = {
                'name': 'unknown',
                'types': [
                    {
                        'slot': 1,
                        'type': {
                            'name': 'unknown'
                        }
                    }
                ],
                'sprites': {
                    'front_default': '/static/dist/img/pngegg.png'
                },
                'height': '',
                'weight': '0',
                'abilities': [
                    {
                        'ability': {
                            'name': 'unknown'
                        }
                    }
                ],
                'id': 0
            }

    # récupère la liste de tout les pokemon pour l'options de recherche
    data['searchPokemon'] = retDataSearchPokemon()

    # affiche le template avec les data
    template = loader.get_template('teamsID.html')
    return HttpResponse(template.render(data))


# requête ajax pour supprimer un pokemon d'une team d'une équipe
# il faut envoyé avec l'attribue idTeam et id (id du pokemon a supprimer) en paramètre
# la méthode post ne fonctionnais pas a cause d'un token de djongo
def updateTeams(request):
    if request.method == 'GET':
        id = request.GET.get('id');
        idTeam = request.GET.get('idTeam');
        team = Teams.objects.get(pk=idTeam)
        team.deletePokemon(int(id))
        return HttpResponse(status=200)
    return HttpResponse(status=400)


# requête ajax pour ajouter un pokemon d'une team d'une équipe
# il faut envoyé avec l'attribue idTeam et id (id du pokemon a ajouter) en paramètre
# la méthode post ne fonctionnais pas a cause d'un token de djongo
def addTeams(request):
    if request.method == 'GET':
        id = request.GET.get('id');
        idTeam = request.GET.get('idTeam');
        team = Teams.objects.get(pk=idTeam)
        team.addPokemon(int(id))
        return HttpResponse(status=200)
    return HttpResponse(status=400)


# requête ajax pour modifier le nom d'une équipe
# il faut envoyé avec l'attribue idTeam et value (le nouveau nom) en paramètre
# la méthode post ne fonctionnais pas a cause d'un token de djongo
def nameTeam(request):
    if request.method == 'GET':
        value = request.GET.get('value');
        idTeam = request.GET.get('idTeam');
        team = Teams.objects.get(pk=idTeam)
        team.setName(value)
        return HttpResponse(status=200)
    return HttpResponse(status=400)


# requête ajax pour supprimé une équipe
# il faut envoyé avec l'attribue idTeam en paramètre
# la méthode post ne fonctionnais pas a cause d'un token de djongo
def deleteTeam(request):
    if request.method == 'GET':
        idTeam = request.GET.get('idTeam');
        team = Teams.objects.get(pk=idTeam)
        team.delete()
        return HttpResponse(status=200)
    return HttpResponse(status=400)


# permet de requete une api et de renvoie les data en json
# si la requête n'aboutie pas renvoie une erreur
def requestAPI(url):
    request = requests.get(url)
    if request.status_code == 200:
        return request.json()
    else:
        return {'ERROR': 'API \"' + str(url) + '\" not working'}


# affiche la page d'erreur
def returnTemplateError(strError):
    template = loader.get_template('error.html')
    #renvoie un nombre aléatoire pour afficher l'image d'un pokemon aléatoire
    data = {'ERROR': strError, 'pokemon': random.randint(1, 151)}
    return HttpResponse(template.render(data))


# retourne la liste des 151 premier pokemons sous la forme suivante
# {'id':'','name':''}
def retDataSearchPokemon():
    # requpère les données depuis l'api puis check s'il y pas eut un erreur avec l'api
    pokemon_list = requestAPI("https://pokeapi.co/api/v2/pokemon?limit=151")
    if "ERROR" in pokemon_list:
        return returnTemplateError(pokemon_list['ERROR'])
    else:
        # remplie le dictonaire avec l'id car celui-ci n'est pas données avec l'api
        ret_pokemon_list = []
        i = 1
        for pokemon in pokemon_list['results']:
            ret_pokemon_list.append({'id': int(i), 'name': str(pokemon['name'])})
            i += 1
        return ret_pokemon_list
