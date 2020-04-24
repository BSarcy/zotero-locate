# Script de génération du fichier engines.json

Ce script compile tous les fichiers de configuration des moteurs de recherche présents dans le répertoire ../engines_json pour généere un fichier engines.json à déposer dans le répertoire locate de Zotero.

## Pré-requis : 
Ce script nécesite l'installation de python (installé par défaut sur les environnements linux)
L'écriture du moteur doit suivre une syntaxe allégée. Le générateur ajoute les informations complémentaires  
```json
{
	"title": "[nom publique de votre moteur] - obligatoire", 
	"icon": "[lien vers l'icône] - facultatif",
	"linktemplate": "[Masque pour la construction de l'url de recherche - obligatoire]"
  }
```
## Usage pour linux :

Positionnez vous sur le répertoire  engines_generator et exécuter le script generator.py
`python generator.py` 
