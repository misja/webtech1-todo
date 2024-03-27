# Routes

## General

- homepage met uitleg GET
- contactgegevens / over ons (optioneel) GET
- login GET/POST

## Movies

http://localhost/movies?page=2&lang=nl GET


- overzicht van alle films (met optioneel filters?)

/movies GET

- detailpagina van enkele film GET

/movies/<int:movie_id> GET
/movies/<str:movie_slug> GET

- film toevoegen POST

/movies POST

- film aanpassen POST

/movies/<int:movie_id>/edit GET/POST

- film verwijderen GET

/movies/<int:movie_id>/delete GET

## Users

- overzicht van alle users (met optioneel filtering)
- registreren
- individuele gegevens opvragen
- updaten van gegevens
- gebruiker verwijderen

## Users / Movies

* persoonlijke favorieten




/ -> /submit

/submit -> /