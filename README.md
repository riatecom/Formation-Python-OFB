# Formation Python pour géomaticiens 🐍🌏

## Description :memo:

*Date* : 11/12/2023  
*Public* : Atelier réseau géomatique de l'Office Français de la Biodiversité  
*Lieu* : MNHN, Paris  
*Durée* : Environ 3 heures

## Support :book:

Voir la présentation : [https://riatelab.github.io/Formation-Python-OFB](https://riatelab.github.io/Formation-Python-OFB).

## Pour compiler la présentation :computer:

**Prérequis** :

- [Python](https://www.python.org)
- [Quarto](https://quarto.org)

**Étapes** :

1. Cloner le projet : `git clone https://github.com/riatelab/Formation-Python-OFB`
2. Se placer dans le dossier du projet : `cd Formation-Python-OFB`
3. Créer un environnement virtuel : `python -m venv .venv`
4. Activer l'environnement virtuel : `source .venv/bin/activate` (Linux) ou `.venv/Scripts/activate.bat` (Windows)
5. Installer les dépendances : `pip install -r requirements.txt`
6. Compiler la présentation et obtenir la sortie dans le dossier `dist` : `quarto render . --output-dir dist/` (si vous voulez recompiler à chaque modification,
   il est possible d'utiliser [watchexec](https://github.com/watchexec/watchexec) : `watchexec -w index.qmd -w images -w static -r quarto render . --output-dir dist/`).

## Licence :recycle:

Le contenu de ce dépôt est mis à disposition selon les termes de la [Licence CC BY-NC-SA 4.0 (Creative Commons - Attribution - Pas d’Utilisation Commerciale - Partage dans les Mêmes Conditions 4.0 International)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr).

## Auteurs :bust_in_silhouette:

[Matthieu Viry](https://github.com/mthh), [Ronan Ysebaert](https://github.com/rysebaert) et [Timothée Giraud](https://github.com/rcarto).
