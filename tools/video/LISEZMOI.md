# Vidéos Qui offre à qui (Shorts 1080x1920, 15 s)

Fabrication : captures du vrai site avec Playwright (polices locales via fonts.py, appels au backend simulés dans cap.py), puis montage image par image (gen.py + un fichier JSON de scènes), encodage ffmpeg, musique son-short.wav (mélodie originale, libre de droits).

1. Servir le site : `python3 -m http.server 8765` à la racine du dépôt.
2. Captures : adapter cap.py, images dans /tmp/v2/s/.
3. Montage : `python3 gen.py scenes.json test` (images de contrôle), puis `full`.
4. `ffmpeg -framerate 30 -i X_f/%04d.jpg -c:v libx264 -preset veryfast -crf 18 -pix_fmt yuv420p v.mp4` puis ajout de son-short.wav.
5. Copier le mp4 dans /media/ (exclu de Google par robots.txt), pousser, puis programmer sur Metricool (marque 8318595, YouTube + Facebook) avec l'adresse https://qui-offre-a-qui.fr/media/....

Règle Shorts : l'écran final affiche toujours « 🔗 Lien dans la bio » (les liens ne sont pas cliquables dans les Shorts), et le texte de la publication le rappelle aussi.

Couverture : chaque Short a une image de couverture 1080x1920 (cover.py : accroche en gros + téléphone incliné avec une capture), passée en videoThumbnailUrl à Metricool. La première image de la vidéo montre déjà l'accroche (jamais un fond vide).

## Promos partenaires (règle de Jérémy, 27 nov 2026)

À chaque promo qu'il transmet (code Awin) : PAS de Reel ni de Short (décision du 27 nov 2026).
1. Ajouter la ligne dans PROMOS (src/build.py) : marque, offre, code, date de fin, lien Awin. L'encart (accueil, guides, page Guides) et la page /codes-promo/ se mettent à jour, et le code disparaît seul après sa date de fin.
2. Faire une image (pin.py, 1000x1500) avec « valable jusqu'au … ».
3. Programmer sur Metricool : un post Facebook (type POST, image + lien cliquable https://qui-offre-a-qui.fr/codes-promo/?src=fb) et une épingle Pinterest (tableau Idées cadeaux de Noël, lien vers le guide concerné ou /codes-promo/ avec ?src=pin). Toujours écrire « Lien affilié ».
4. Sources : ?src=fb, ?src=pin ; les liens de la chaîne YouTube portent ?src=youtube. assets/track.js enregistre la source dans vcs_hits (ref = "src:..."), et chaque clic vers Awin est compté (kind = 'awin').
