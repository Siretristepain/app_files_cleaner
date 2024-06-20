# app_files_cleaner

Projet d'application en ligne de commande via le module typer permettant de chercher des fichiers d'une extension donnée et de les supprimer.

## Cahier des charges

- Je souhaite une commande 'run' qui me permette de chercher les fichiers d'une extension donnée dans le dossier courant et ses sous-dossiers.

- Je voudrais que je puisse ajouter un chemin optionnel à ma commande 'run', auquel cas elle aurait le même comportement mais à partir du dossier spécifié.

- Je souhaiterais pouvoir passer en option --delete/--no-delete pour supprimer ou non les fichiers trouvés. Il y aurait une étape de confirmation dans le cas --delete.

- Je voudrais une commande 'search' pour aller chercher directement les fichiers d'une extension donnée.

- Je souhaiterais aussi une commande 'delete' qui supprimerait directement les fichiers d'une extension donnée (avec confirmation).
