/**
 *  depuis toute les routes non ajax
 * redirigie après le choix du pokemons dans la box de recherche
 */
function selectSearch() {
    var select = document.getElementById('searchBoxSelect');
    window.location.href = '/pokemon/' + select.value;
}

/**
 * depuis toute les routes non ajax
 * ouvre et ferme la box de recherche
 */
function opencloseSearchBox() {
    var box = document.getElementById('searchBox');
    if (box.classList.contains('searchBox--hidden')) {
        box.classList.remove('searchBox--hidden');
        box.classList.add('searchBox--show');
    } else {
        box.classList.remove('searchBox--show');
        box.classList.add('searchBox--hidden');
    }
}

/**
 * depuis la route teamsID
 * ouvre et ferme la box d'ajout d'un pokemon
 * si l'id du pokemon est à 0
 * sinon ferme supprime le pokemon de la teams
 * @param id = id du pokemon
 * @param idTeam = id de la team en cours
 */
function opencloseUpdatePokemonBox(id, idTeam) {
    if (id === 0) {
        var box = document.getElementById('addPokemonBox');
        if (box.classList.contains('searchBox--hidden')) {
            box.classList.remove('searchBox--hidden');
            box.classList.add('searchBox--show');
        } else {
            box.classList.remove('searchBox--show');
            box.classList.add('searchBox--hidden');
        }
    } else {

        /**
         * fait une requête ajax qui appele la route updateTeam
         * reload au succes
         */
        var xhttp = new XMLHttpRequest();
        xhttp.open("GET", "/updateTeam/?id=" + id + "&idTeam=" + idTeam, true);

        xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        xhttp.onload = function () {
            if (xhttp.status === 200) {
                location.reload();
            }
            if (xhttp.status === 400) {
                alert('the request was not successful')
            }
        }
        xhttp.send();
    }
}

/**
 * depuis la route teamsID
 * apres l'ouverture de la box d'ajout d'un pokemon donc id = 0
 * permet d'ajouter un pokemon a la team
 * @param idTeam = id de la team en cour
 */
function addPokemon(idTeam) {
    /**
     * fait une requête ajax qui appele la route updateTeam
     * reload au succes
     */
    var select = document.getElementById('addPokemonBoxSelect');
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/addTeam/?id=" + select.value + "&idTeam=" + idTeam, true);

    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhttp.onload = function () {
        if (xhttp.status === 200) {
            location.reload();
        }
        if (xhttp.status === 400) {
            alert('the request was not successful')
        }
    }
    xhttp.send();
}

/**
 * depuis la route teamsID
 * modifie le nom de la team en ajax
 * @param idTeam = id de la team en cour
 */
function updateName(idTeam) {
    /**
     * fait une requête ajax qui appele la route updateTeam
     */
    var select = document.getElementById('nameTeam');
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/nameTeam/?value=" + select.value + "&idTeam=" + idTeam, true);

    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhttp.onload = function () {
        if (xhttp.status === 200) {
        }
        if (xhttp.status === 400) {
            alert('the request was not successful')
        }
    }
    xhttp.send();
}

/**
 * depuis la route teamsID
 * supprime la team en base de données
 * @param idTeam = id de la team en cour
 */
function deleteTeam(idTeam) {
    /**
     * fait une requête ajax qui appele la route updateTeam
     * renvoie sur team aux succès
     */
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/deleteTeam/?idTeam=" + idTeam, true);

    xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xhttp.onload = function () {
        if (xhttp.status === 200) {
            window.location.href = '/teams';
        }
        if (xhttp.status === 400) {
            alert('the request was not successful')
        }
    }
    xhttp.send();
}