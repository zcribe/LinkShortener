# Link shortener
A simple link shortener that:
* Takes a link input
* Generates a token for it
* Adds both to database
* Uses a redirector view to redirect provided link to original link

Obvious glaring flaws:
* Generates a new DB entry for every new entry not every new link.
* Links do not deprecate.
* Token generation is very basic.
