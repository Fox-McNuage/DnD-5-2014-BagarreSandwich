# DnD 5 2014 BagarreSandwich


# Fonctionnalités prévues
Bon l'objectif c'est d'avoir sous la main pendant les sessions une interface graphique rapide à utiliser qui me permette d'estimer les longueurs sur la carte : Il faut que je puisse
1. choisir le mouvement de chaque perso/créature puis le déplacer tout en tenant compte des terrains difficiles et autres obstacles (qu'il faut donc rajouter)
2. rajouter les sorts à effet de zone que je peux placer dans la portée possible. Et si jamais ils déplacent des creatures ou modifient le terrain il faut le prendre en compte
3. la taille des perso et leur allonge, ainsi que l'impossibilité de se traverser
4. le retour en arrière : si je fais une mauvaise manip que je puisse undo.

Une interface aussi schématique que possible au final, le but n'est pas de remplacer le combat sur papier mais de simplifier les estimations à la louche de qui tu touche ou jusqu'où tu va.

##  À faire en pratique

- Ajouter une grille ? Ou justement tu veux avoir le logiciel pour t'en passer ?
- Pouvoir tracer des lignes pour les attaques à distance / juger la visiblité ?
- Proposition : au tour d'une créature, afficher fenêtre pour choisir l'action (sort, etc). Problème : soit il faut enregistrer à l'avance les capacités de chaque créature, soit re régler le sort à chaque utilisation. Autre proposition : ne pas restreindre mais afficher les infos ?

## Fait

## Remarque
J'ai écrit des remarques en commentaire du code parfois, ça se fait pas trop il me semble normalement.
- À mon sens, faut se fixer, les variables soit en anglais soit en français (je sais je clc)
- N'ajouter des trucs que si tu t'en sers immédiatement, les classes vont de toute façon évoluer (exemple : les 150 000 attributs des personnages, pour l'instant pas utilisés c'est un peu nébuleux)
- Peut être moi qui est un peu psychorigide, mais pitié gardez pas une même variable/attribut si vous changez totalement le type de l'objet c'est pas clair (Champdebataille.status)
