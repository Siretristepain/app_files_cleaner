import typer
from pathlib import Path

def main(extension: str = typer.Argument(".txt", help="Extension des fichiers à chercher"),
        path: str = typer.Argument(Path.cwd(), help="Répertoire à partir duquel lancer la recherche"),
        delete: bool = typer.Option(False, help="Option de suppression des fichiers trouvés"),
        recursive: bool = typer.Option(False, help="Option de recherche dans les sous-répertoires")):
    
    typer.echo(f"Extension : {extension}\nDelete : {delete}\nPath: {path}\nRecursive : {recursive}")

    # Si l'utilisateur n'a pas précéde l'extension d'un '.', on l'ajoute
    if not extension.startswith('.'):
        extension = f".{extension}"


    # On fait la liste des fichiers ayant l'extension souhaitée dans le répertoire souhaité
    all_files = sorted(f for f in Path(path).iterdir() if (f.is_file()) & (f.suffix == extension))

    typer.echo(f"{all_files}")

if __name__ == '__main__':
    typer.run(main)