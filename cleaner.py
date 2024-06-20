import typer
from pathlib import Path
import os

def main(extension: str = typer.Argument(".txt", help="Extension des fichiers à chercher"),
        path: str = typer.Argument(Path.cwd(), help="Répertoire à partir duquel lancer la recherche"),
        delete: bool = typer.Option(False, help="Option de suppression des fichiers trouvés"),
        recursive: bool = typer.Option(False, help="Option de recherche dans les sous-répertoires")):
    
    typer.echo(f"Extension : {extension}\nDelete : {delete}\nPath: {path}\nRecursive : {recursive}")

    # Si l'utilisateur n'a pas précéde l'extension d'un '.', on l'ajoute
    if not extension.startswith('.'):
        extension = f".{extension}"

    # STRUCTURE pour faire la liste des fichiers
    #___________________________________________
    if not recursive:
        # On fait la liste des fichiers ayant l'extension souhaitée dans le répertoire souhaité
        all_files = sorted(f for f in Path(path).iterdir() if (f.is_file()) & (f.suffix == extension))
    else:
        # On fait également la liste des fichiers avec l'extension, mais on cherche aussi dans les sous-répertoire
        all_files = sorted(f for f in Path(path).rglob(f"*{extension}"))

    # STRUCTURE pour afficher la liste des fichiers trouvés
    #______________________________________________________
    if len(all_files) != 0:
        typer.secho(f"Fichiers trouvés :", underline=True)
        for file in all_files:
            typer.secho(file, fg=typer.colors.BLUE)
    else:
        typer.echo(f"Aucun fichier trouvés avec l'extension {extension}")

    # STRUCTURE pour demander la confirmation à l'utilisateur
    if delete:
        wrng_msg = typer.style("ATTENTION", bold=True, fg=typer.colors.RED)
        confirmation = typer.confirm(f"{wrng_msg}, êtes-vous sûr de vouloir supprimer tous ces fichiers?")
        if not confirmation:
            raise typer.Abort()
        
        typer.echo("Suppression des fichiers")
        for file in all_files:
            os.remove(file)
            typer.secho(f"Suppression {file}", fg=typer.colors.RED)

if __name__ == '__main__':
    typer.run(main)