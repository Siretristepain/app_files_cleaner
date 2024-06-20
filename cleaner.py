import typer
from pathlib import Path

def main(extension: str = typer.Argument("txt", help="Extension des fichiers à chercher"),
        path: str = typer.Argument(Path.cwd(), help="Répertoire à partir duquel lancer la recherche"),
        delete: bool = typer.Option(False, help="Option de suppression des fichiers trouvés"),
        recursive: bool = typer.Option(False, help="Option de recherche dans les sous-répertoires")):
    
    typer.echo(f"Extension : {extension}\nDelete : {delete}\nPath: {path}\nRecursive : {recursive}")

if __name__ == '__main__':
    typer.run(main)