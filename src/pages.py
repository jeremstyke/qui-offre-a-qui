# Guides du site Qui offre à qui. Chaque guide : slug, titre, description, date, corps HTML.
# Liens Amazon : écrire {AMZ:mots clés} ; build.py le remplace par une recherche Amazon avec l'identifiant quioffreaqui-21.
# Règles : vouvoiement, aucun tiret long ni demi-cadratin, aucun prix précis inventé, aucun avis inventé.

def idee(titre, texte, kw):
    return f'<div class="idee"><b>{titre}</b><span>{texte}</span><a class="btn s petit" href="{{AMZ:{kw}}}" rel="sponsored nofollow noopener" target="_blank">Voir les modèles</a></div>'

PAGES = [
{
"slug": "idee-cadeau-5-euros",
"title": "Idée cadeau à 5 € : 15 petites idées qui font plaisir",
"desc": "Un tout petit budget de 5 € pour un Père Noël secret, une classe ou un club ? 15 idées de petits cadeaux utiles, gourmands ou rigolos.",
"date": "2026-11-26",
"body": """
<p>Avec <strong>5 €</strong>, on est sur le petit cadeau symbolique, idéal pour une classe, un club, une grande équipe ou un Père Noël secret entre ados. Le but n'est pas d'impressionner, mais de faire sourire. Voici des idées qui y arrivent.</p>
<h2>Les petites douceurs</h2>
<div class="idees">
""" + idee("Sucettes ou bonbons originaux", "Toujours un succès", "bonbons originaux") + idee("Sachets de chocolat chaud", "Pour une pause réconfortante", "chocolat chaud sachet") + idee("Biscuits de Noël", "À partager ou à garder", "biscuits noel") + """
</div>
<h2>Les petits objets utiles</h2>
<div class="idees">
""" + idee("Baume à lèvres", "Indispensable quand il fait froid", "baume levres") + idee("Petit carnet", "Pour les listes et les idées", "petit carnet") + idee("Porte-clés original", "Un clin d'œil qui sert tous les jours", "porte cle original") + idee("Stylos colorés", "Pour le bureau ou l'école", "stylos couleur") + """
</div>
<h2>Les petits cadeaux rigolos</h2>
<div class="idees">
""" + idee("Chaussettes fantaisie", "Drôles et utiles en hiver", "chaussettes fantaisie") + idee("Mini jeu de cartes", "Pour une pause ou un trajet", "mini jeu de cartes") + idee("Autocollants amusants", "Pour personnaliser un ordinateur ou un carnet", "stickers") + idee("Balle anti-stress", "Le gadget qui sert vraiment", "balle anti stress") + """
</div>
<h2>Les petites attentions cocooning</h2>
<div class="idees">
""" + idee("Bougie chauffe-plat parfumée", "Une ambiance douce en un instant", "bougies chauffe plat parfumees") + idee("Sachets de thé ou tisane", "Pour un moment de calme", "assortiment tisane") + idee("Masque visage en tissu", "Un petit moment de soin", "masque visage tissu") + idee("Mini plante grasse", "Un peu de vert sans entretien", "mini plante grasse") + """
</div>
<h2>Réussir un cadeau à 5 €</h2>
<ul>
<li><strong>Misez sur l'emballage</strong> : un joli papier et un petit mot donnent de la valeur au cadeau.</li>
<li><strong>Le fait maison marche très bien</strong> à ce budget : biscuits, sablés, bougie.</li>
<li><strong>Regroupez des petites choses</strong> : un sachet de thé et des biscuits font un vrai petit colis.</li>
</ul>
<h2>Questions fréquentes</h2>
<h3>5 €, ce n'est pas trop peu pour un Père Noël secret ?</h3>
<p>Non, c'est un budget courant dans les classes, les clubs ou les grandes équipes. Tout le monde peut participer, c'est ce qui compte.</p>
<h3>Que trouver à 5 € pour un enfant ?</h3>
<p>Des bonbons originaux, un porte-clés, des autocollants ou un mini jeu de cartes font plaisir aux plus jeunes.</p>
<h3>Comment organiser le tirage pour une classe ou un club ?</h3>
<p>Avec notre <a href="/">tirage au sort gratuit</a>, vous entrez les prénoms et vous envoyez son lien à chaque participant ou à ses parents.</p>
"""},
{
"slug": "idee-cadeau-10-euros",
"title": "Idée cadeau à 10 € : 15 idées pour un Père Noël secret",
"desc": "Un budget de 10 € pour votre Père Noël secret ou un échange entre collègues ? 15 idées de cadeaux utiles ou drôles qui font vraiment plaisir.",
"date": "2026-11-26",
"body": """
<p>Dix euros, c'est le budget le plus courant pour un <strong>Père Noël secret</strong> entre collègues ou dans une grande famille. Le piège, c'est le gadget qu'on oublie dans un tiroir. Voici des idées qui restent abordables tout en étant vraiment utilisées.</p>
<h2>Les idées utiles du quotidien</h2>
<div class="idees">
""" + idee("Mug isotherme", "Pour le café du bureau qui reste chaud", "mug isotherme") + idee("Chaussettes douillettes", "Un classique d'hiver qui sert vraiment", "chaussettes chaudes hiver") + idee("Carnet élégant", "Pour les listes, les idées ou le travail", "carnet de notes a5") + idee("Gourde pliable", "Légère, elle se glisse dans un sac", "gourde pliable") + idee("Câble de charge solide", "Celui qu'on finit toujours par chercher", "cable charge tresse") + """
</div>
<h2>Les idées gourmandes</h2>
<div class="idees">
""" + idee("Assortiment de thés", "Pour découvrir de nouveaux parfums", "coffret the") + idee("Chocolat chaud à préparer", "Parfait pour une soirée d'hiver", "chocolat chaud cadeau") + idee("Épices à cuisiner", "Pour celui ou celle qui aime cuisiner", "coffret epices") + """
</div>
<h2>Les idées qui font rire</h2>
<div class="idees">
""" + idee("Jeu de cartes d'apéro", "Pour animer la prochaine soirée", "jeu de cartes apero") + idee("Puzzle de bureau", "Un casse-tête pour la pause", "casse tete bois") + idee("Bonnet de Noël lumineux", "Pour la photo de groupe", "bonnet noel lumineux") + """
</div>
<h2>Les idées douceur et cocooning</h2>
<div class="idees">
""" + idee("Bougie parfumée", "Une ambiance chaleureuse à la maison", "bougie parfumee") + idee("Baume à lèvres de soin", "Indispensable quand il fait froid", "baume levres") + idee("Bouillotte", "Le petit confort des soirées d'hiver", "bouillotte") + idee("Masque de nuit", "Pour mieux dormir ou voyager", "masque de nuit soie") + """
</div>
<h2>Comment bien choisir avec 10 €</h2>
<ul>
<li><strong>Visez l'utile plutôt que le gadget</strong> : un objet qui sert tous les jours marque plus qu'une blague qui fait rire une minute.</li>
<li><strong>Pensez à la personne</strong> : sa boisson préférée, ses loisirs, son trajet. Une petite attention ciblée vaut mieux qu'un objet passe-partout.</li>
<li><strong>Soignez l'emballage</strong> : à petit budget, un joli papier et un mot écrit à la main changent tout.</li>
<li><strong>Respectez le budget</strong> : dépasser met mal à l'aise ceux qui ont joué le jeu.</li>
</ul>
<h2>Questions fréquentes</h2>
<h3>Quel cadeau offrir à 10 € à un collègue qu'on connaît peu ?</h3>
<p>Restez neutre et utile : un mug isotherme, un assortiment de thés ou un carnet. Évitez les cadeaux trop personnels comme les parfums.</p>
<h3>Peut-on offrir un cadeau fait maison ?</h3>
<p>Oui, c'est souvent très apprécié : biscuits, confiture, bougie. Prévenez simplement le groupe si vous craignez les allergies.</p>
<h3>Comment organiser le tirage au sort ?</h3>
<p>Avec notre <a href="/">outil gratuit</a>, vous entrez les prénoms et chacun reçoit par e-mail le nom de la personne à gâter, sans inscription.</p>
"""},
{
"slug": "idee-cadeau-15-euros",
"title": "Idée cadeau à 15 € : 15 idées pour un échange réussi",
"desc": "Un budget de 15 € pour votre Père Noël secret, un échange entre collègues ou entre amis ? 15 idées de cadeaux utiles, gourmands ou drôles.",
"date": "2026-11-26",
"body": """
<p><strong>15 €</strong>, c'est le budget juste au-dessus du petit cadeau symbolique : assez pour offrir un objet de qualité, sans mettre personne mal à l'aise. Voici des idées classées par type de personne.</p>
<h2>Pour les amateurs de boissons chaudes</h2>
<div class="idees">
""" + idee("Coffret de thés", "Pour découvrir de nouveaux parfums", "coffret the") + idee("Mug double paroi", "Élégant et garde la chaleur", "mug double paroi verre") + idee("Mousseur à lait", "Pour un cappuccino maison", "mousseur a lait electrique") + """
</div>
<h2>Pour les joueurs</h2>
<div class="idees">
""" + idee("Jeu de cartes d'ambiance", "Pour animer une soirée", "jeu de cartes ambiance") + idee("Jeu de dés rapide", "Il tient dans une poche", "jeu de des") + idee("Quiz de culture générale", "Pour les repas de famille", "jeu quiz culture generale") + """
</div>
<h2>Pour le confort de la maison</h2>
<div class="idees">
""" + idee("Bougie parfumée", "Une ambiance cocooning", "bougie parfumee") + idee("Chaussettes en laine", "Bien au chaud tout l'hiver", "chaussettes laine") + idee("Guirlande lumineuse", "Pour une déco douce", "guirlande lumineuse") + """
</div>
<h2>Pour le bureau ou le télétravail</h2>
<div class="idees">
""" + idee("Carnet de qualité", "Pour noter idées et rendez-vous", "carnet de notes a5") + idee("Support d'ordinateur", "Meilleure posture devant l'écran", "support ordinateur portable") + idee("Plante facile", "Un peu de vert sans effort", "plante interieur facile") + """
</div>
<h2>Pour les gourmands</h2>
<div class="idees">
""" + idee("Chocolats de qualité", "Un classique qui plaît", "chocolats coffret") + idee("Pâte à tartiner originale", "Pour les petits-déjeuners", "pate a tartiner") + idee("Coffret d'épices", "Pour cuisiner autrement", "coffret epices") + """
</div>
<h2>Bien choisir avec 15 €</h2>
<ul>
<li><strong>Un seul bel objet</strong> plutôt que plusieurs petites choses.</li>
<li><strong>Utile ou gourmand</strong> : ce sont les cadeaux qu'on garde ou qu'on partage.</li>
<li><strong>Commandez tôt</strong> en décembre pour être livré avant l'échange.</li>
</ul>
<h2>Questions fréquentes</h2>
<h3>15 €, c'est trop pour un Secret Santa au bureau ?</h3>
<p>Non, c'est un budget courant entre collègues, souvent entre 10 et 20 €. L'essentiel est que tout le monde le respecte.</p>
<h3>Quel cadeau à 15 € pour un homme ?</h3>
<p>Un mug double paroi, un jeu de cartes, un support d'ordinateur ou un coffret de chocolats restent des valeurs sûres.</p>
<h3>Comment organiser le tirage ?</h3>
<p>Avec notre <a href="/">tirage au sort gratuit</a>, chacun reçoit par e-mail le nom de la personne à gâter.</p>
"""},
{
"slug": "idee-cadeau-50-euros",
"title": "Idée cadeau à 50 € : 15 idées pour un vrai beau cadeau",
"desc": "50 € pour un cadeau de Noël, d'anniversaire ou un échange en famille ? 15 idées de cadeaux de qualité, high-tech, cuisine, loisirs et bien-être.",
"date": "2026-11-26",
"body": """
<p>Avec <strong>50 €</strong>, on entre dans le vrai beau cadeau : celui qu'on utilise pendant des années. C'est le budget des échanges en famille proche ou des cadeaux d'anniversaire. Voici des idées qui valent la dépense.</p>
<h2>High-tech</h2>
<div class="idees">
""" + idee("Écouteurs sans fil", "Pour la musique et les appels", "ecouteurs sans fil") + idee("Enceinte Bluetooth étanche", "Pour la salle de bain ou l'extérieur", "enceinte bluetooth etanche") + idee("Liseuse ou étui de liseuse", "Pour les grands lecteurs", "etui liseuse") + """
</div>
<h2>Cuisine</h2>
<div class="idees">
""" + idee("Appareil à raclette", "Pour les soirées d'hiver entre amis", "appareil raclette") + idee("Couteau de cuisine de qualité", "L'outil qu'on garde des années", "couteau de chef") + idee("Machine à pop-corn", "Pour les soirées film", "machine pop corn") + """
</div>
<h2>Maison et confort</h2>
<div class="idees">
""" + idee("Plaid chauffant", "Le confort absolu en hiver", "plaid chauffant") + idee("Lampe de lecture", "Une lumière agréable pour le soir", "lampe de lecture led") + idee("Diffuseur d'ambiance", "Pour une maison qui sent bon", "diffuseur huiles essentielles") + """
</div>
<h2>Loisirs</h2>
<div class="idees">
""" + idee("Jeu de société expert", "Des heures de jeu entre amis", "jeu de societe strategie") + idee("Coffret LEGO adulte", "Pour se détendre en construisant", "lego adulte") + idee("Kit de dessin complet", "Pour se lancer ou progresser", "kit dessin complet") + """
</div>
<h2>Bien-être</h2>
<div class="idees">
""" + idee("Pistolet de massage", "Pour détendre les muscles", "pistolet de massage") + idee("Coussin chauffant", "Idéal pour le dos et la nuque", "coussin chauffant") + idee("Coffret soin", "Un moment pour soi", "coffret soin") + """
</div>
<h2>Bien choisir avec 50 €</h2>
<ul>
<li><strong>Vérifiez les avis réels</strong> et la marque : à ce prix, la qualité doit suivre.</li>
<li><strong>Pensez à l'usage</strong> : un cadeau utilisé chaque semaine vaut mieux qu'un objet de déco.</li>
<li><strong>Gardez le ticket cadeau</strong> pour un éventuel échange.</li>
</ul>
<h2>Questions fréquentes</h2>
<h3>Quel cadeau à 50 € pour quelqu'un qui a déjà tout ?</h3>
<p>Un consommable haut de gamme ou un objet de confort, comme un plaid chauffant ou un appareil à raclette pour les repas à plusieurs.</p>
<h3>Peut-on fixer 50 € pour un Père Noël secret ?</h3>
<p>Oui, en famille proche ou entre amis qui le souhaitent. Entre collègues, un budget plus modeste évite les malaises.</p>
<h3>Comment faire le tirage au sort ?</h3>
<p>Utilisez notre <a href="/">outil gratuit</a> : prénoms, e-mails, exclusions, et chacun reçoit son résultat en secret.</p>
"""},
{
"slug": "idee-cadeau-100-euros",
"title": "Idée cadeau à 100 € : 15 idées pour un cadeau qui marque",
"desc": "100 € pour un cadeau de Noël en famille, un cadeau commun ou un anniversaire important ? 15 idées utiles et durables : high-tech, cuisine, maison, loisirs.",
"date": "2026-11-26",
"body": """
<p>Avec <strong>100 €</strong>, on offre un cadeau qui compte : un objet de qualité qu'on garde des années. C'est souvent le budget d'un cadeau commun à plusieurs (un Secret Santa entre collègues qui se cotisent, un cadeau des enfants aux parents) ou d'un échange en famille très proche. Voici des idées qui valent vraiment ce prix.</p>
<h2>High-tech</h2>
<div class="idees">
""" + idee("Casque à réduction de bruit", "Pour les trajets et le télétravail", "casque reduction de bruit") + idee("Liseuse", "Des milliers de livres dans la poche", "liseuse") + idee("Montre connectée", "Sport, sommeil et notifications", "montre connectee") + """
</div>
<h2>Cuisine</h2>
<div class="idees">
""" + idee("Friteuse sans huile", "L'appareil qu'on utilise tous les jours", "friteuse sans huile") + idee("Machine à café à capsules ou à grain", "Pour les amateurs de bon café", "machine a cafe") + idee("Cocotte en fonte", "Pour les plats mijotés pendant des années", "cocotte fonte") + """
</div>
<h2>Maison et confort</h2>
<div class="idees">
""" + idee("Couverture lestée", "Pour un sommeil plus apaisé", "couverture lestee") + idee("Lampe d'ambiance connectée", "Des couleurs qui changent selon l'humeur", "lampe connectee") + idee("Ensemble de linge de lit de qualité", "Le confort qu'on remarque chaque soir", "parure de lit percale") + """
</div>
<h2>Loisirs</h2>
<div class="idees">
""" + idee("Grand coffret LEGO", "Des heures de construction", "lego adulte") + idee("Appareil photo instantané", "Des souvenirs imprimés tout de suite", "appareil photo instantane") + idee("Jumelles de qualité", "Pour la nature, la randonnée et les oiseaux", "jumelles 8x42") + """
</div>
<h2>Bien-être</h2>
<div class="idees">
""" + idee("Fauteuil ou coussin de massage", "Pour le dos après une longue journée", "coussin de massage shiatsu") + idee("Coffret parfum", "Un cadeau qu'on choisit avec soin", "coffret parfum") + idee("Lampe de luminothérapie", "Pour garder le moral en hiver", "lampe luminotherapie") + """
</div>
<h2>Bien choisir avec 100 €</h2>
<ul>
<li><strong>Misez sur l'usage quotidien</strong> : à ce prix, le cadeau doit servir souvent, pas rester dans un placard.</li>
<li><strong>Vérifiez la marque et les avis réels</strong> avant d'acheter, et comparez plusieurs modèles.</li>
<li><strong>Pensez au cadeau commun</strong> : à quatre personnes à 25 €, on offre quelque chose de bien plus marquant que quatre petits cadeaux.</li>
<li><strong>Gardez le ticket cadeau</strong> pour un échange éventuel.</li>
</ul>
<p>Pour un budget plus serré, voyez nos <a href="/idee-cadeau-50-euros/">idées à 50 €</a> ou nos <a href="/idee-cadeau-30-euros/">idées à 30 €</a>.</p>
<h2>Questions fréquentes</h2>
<h3>100 €, ce n'est pas trop pour un Père Noël secret ?</h3>
<p>Entre collègues, oui en général. En famille proche, entre adultes qui le souhaitent, ou pour un cadeau commun, c'est un budget courant. L'important est que tout le monde soit d'accord avant le tirage.</p>
<h3>Quel cadeau à 100 € pour quelqu'un qui a déjà tout ?</h3>
<p>Un objet de meilleure qualité que celui qu'il possède déjà (casque, machine à café, linge de lit) ou une expérience à vivre.</p>
<h3>Comment organiser un cadeau commun à plusieurs ?</h3>
<p>Fixez le montant de chacun, choisissez une personne qui achète, et faites le tirage au sort en ligne sur notre <a href="/">outil gratuit</a> si chacun doit offrir à quelqu'un d'autre.</p>
"""},

{
"slug": "idee-cadeau-20-euros",
"title": "Idée cadeau à 20 € : 15 idées qui font vraiment plaisir",
"desc": "Budget de 20 € pour un Père Noël secret, un anniversaire ou un échange entre amis ? 15 idées de cadeaux utiles, gourmands ou originaux.",
"date": "2026-11-26",
"body": """
<p>Avec <strong>20 €</strong>, on passe du petit clin d'œil au vrai cadeau. C'est le budget idéal pour un échange en famille ou entre amis, à condition de bien cibler la personne. Voici des idées classées par profil.</p>
<h2>Pour la personne qui aime son confort</h2>
<div class="idees">
""" + idee("Plaid tout doux", "Pour les soirées canapé de l'hiver", "plaid polaire doux") + idee("Chaussons confortables", "Le cadeau qu'on porte tous les jours", "chaussons confortables") + idee("Lampe veilleuse", "Une lumière douce pour la chambre", "lampe veilleuse deco") + """
</div>
<h2>Pour la personne gourmande</h2>
<div class="idees">
""" + idee("Coffret de cafés du monde", "Pour varier les plaisirs du matin", "coffret cafe") + idee("Kit cocktail", "Pour jouer au barman entre amis", "kit cocktail") + idee("Livre de recettes rapides", "Des idées pour cuisiner en semaine", "livre recettes rapides") + """
</div>
<h2>Pour la personne qui aime jouer</h2>
<div class="idees">
""" + idee("Jeu de société d'ambiance", "Rapide à expliquer, parfait en groupe", "jeu de societe ambiance") + idee("Jeu de cartes de stratégie", "Pour les parties à deux", "jeu de cartes 2 joueurs") + idee("Puzzle 1000 pièces", "Pour les longues soirées d'hiver", "puzzle 1000 pieces") + """
</div>
<h2>Pour la personne connectée</h2>
<div class="idees">
""" + idee("Support de téléphone", "Pratique au bureau ou en cuisine", "support telephone bureau") + idee("Batterie externe", "Pour ne plus tomber en panne", "batterie externe") + idee("Ampoule connectée", "Une ambiance qui change en un clic", "ampoule connectee") + """
</div>
<h2>Pour la personne qui aime prendre soin d'elle</h2>
<div class="idees">
""" + idee("Coffret bain", "Un moment de détente à la maison", "coffret bain") + idee("Brosse démêlante", "Simple et très utile", "brosse demelante") + idee("Diffuseur d'huiles essentielles", "Pour une ambiance apaisante", "diffuseur huiles essentielles") + """
</div>
<h2>Nos conseils pour un cadeau réussi à 20 €</h2>
<ul>
<li><strong>Demandez une liste d'envies</strong> : quelques indices évitent les doublons et les déceptions.</li>
<li><strong>Un bel objet simple plutôt que trois petits</strong> : à ce budget, la qualité se voit.</li>
<li><strong>Gardez le ticket cadeau</strong> : il permet d'échanger sans gêne.</li>
</ul>
<h2>Questions fréquentes</h2>
<h3>20 €, c'est un bon budget pour un Père Noël secret ?</h3>
<p>Oui, c'est un budget très courant : assez pour un vrai cadeau, sans mettre personne en difficulté.</p>
<h3>Comment savoir ce qui fera plaisir ?</h3>
<p>Observez ses habitudes : boisson préférée, loisirs, trajet. Une liste d'envies partagée dans le groupe aide aussi beaucoup.</p>
<h3>Où organiser le tirage gratuitement ?</h3>
<p>Sur <a href="/">Qui offre à qui</a> : entrez les prénoms, ajoutez les exclusions si besoin, et chacun reçoit son résultat par e-mail.</p>
"""},
{
"slug": "idee-cadeau-30-euros",
"title": "Idée cadeau à 30 € : 15 idées pour gâter sans se ruiner",
"desc": "30 € pour un cadeau de Noël, d'anniversaire ou un échange en famille ? 15 idées de cadeaux de qualité, classées par profil, pour viser juste.",
"date": "2026-11-26",
"body": """
<p>À <strong>30 €</strong>, vous pouvez offrir un objet de qualité qui dure. C'est le budget des échanges en famille et des cadeaux d'anniversaire entre amis proches. Voici des idées qui sortent de l'ordinaire.</p>
<h2>High-tech utile</h2>
<div class="idees">
""" + idee("Petite enceinte Bluetooth", "Pour la musique partout", "enceinte bluetooth portable") + idee("Écouteurs filaires de qualité", "Un bon son sans recharge", "ecouteurs intra") + idee("Réveil lumineux", "Pour se lever en douceur l'hiver", "reveil lumineux") + """
</div>
<h2>Cuisine et gourmandise</h2>
<div class="idees">
""" + idee("Moulin à épices électrique", "Pour les amateurs de cuisine", "moulin epices electrique") + idee("Gaufrier compact", "Des goûters maison en quelques minutes", "gaufrier") + idee("Coffret apéritif", "À partager entre amis", "coffret aperitif") + """
</div>
<h2>Maison et déco</h2>
<div class="idees">
""" + idee("Plaid en laine", "Chaud et élégant sur un canapé", "plaid laine") + idee("Cadre photo original", "Pour un souvenir à mettre en valeur", "cadre photo multivues") + idee("Plante facile en pot", "Un peu de vert qui dure", "plante interieur facile") + """
</div>
<h2>Loisirs et bien-être</h2>
<div class="idees">
""" + idee("Jeu de société familial", "Pour les réunions de fêtes", "jeu de societe famille") + idee("Tapis de yoga", "Pour bouger à la maison", "tapis de yoga") + idee("Coffret de peinture", "Pour se lancer dans l'aquarelle", "coffret aquarelle") + """
</div>
<h2>Pour les petits et les ados</h2>
<div class="idees">
""" + idee("Jeu de construction", "Créatif et sans écran", "jeu de construction enfant") + idee("Lampe d'ambiance pour chambre", "Les ados adorent", "lampe led chambre ado") + idee("Livre illustré", "Un cadeau qui accompagne longtemps", "livre illustre enfant") + """
</div>
<h2>Bien choisir un cadeau à 30 €</h2>
<ul>
<li><strong>Privilégiez la qualité</strong> : un seul bel objet marque plus qu'un panier de petites choses.</li>
<li><strong>Vérifiez les avis réels</strong> sur la fiche produit avant d'acheter.</li>
<li><strong>Pensez à la livraison</strong> : en décembre, commandez au moins une semaine avant l'échange.</li>
</ul>
<h2>Questions fréquentes</h2>
<h3>Quel cadeau à 30 € pour une personne qui a déjà tout ?</h3>
<p>Misez sur le consommable de qualité (gourmandises, coffret apéritif) ou sur une activité à partager, comme un jeu de société.</p>
<h3>Peut-on se mettre à plusieurs pour un cadeau ?</h3>
<p>Oui, dans un échange classique chacun offre à une seule personne, mais rien n'empêche de réunir plusieurs budgets pour un cadeau commun.</p>
<h3>Comment faire le tirage au sort ?</h3>
<p>Utilisez notre <a href="/">outil de tirage gratuit</a> : il gère les exclusions (couples, frères et sœurs) et envoie son résultat à chacun par e-mail.</p>
"""},
{
"slug": "pere-noel-secret-famille",
"title": "Père Noël secret en famille : règles, budget et idées",
"desc": "Organiser un Père Noël secret en famille : un seul cadeau chacun, le bon budget, les exclusions entre couples, les enfants, et des idées pour tous les âges.",
"date": "2026-11-26",
"body": """
<p>Dans une grande famille, acheter un cadeau pour chacun coûte vite cher et prend un temps fou. Le <strong>Père Noël secret en famille</strong> règle le problème : chaque adulte offre un seul cadeau, à une personne tirée au sort, et tout le monde repart gâté.</p>
<h2>Pourquoi passer au Père Noël secret en famille</h2>
<ul>
<li><strong>Moins de dépenses</strong> : un cadeau soigné au lieu de dix petits cadeaux vite oubliés.</li>
<li><strong>Moins de stress</strong> : une seule personne à qui penser, et plus de temps pour bien choisir.</li>
<li><strong>Plus de surprise</strong> : le jour J, chacun essaie de deviner qui l'a gâté.</li>
</ul>
<h2>Les règles qui marchent en famille</h2>
<ul>
<li><strong>Un budget identique pour tous</strong>, souvent entre 20 et 50 € en famille proche.</li>
<li><strong>Des exclusions entre conjoints</strong> : ils s'offrent déjà un cadeau, autant qu'ils tirent quelqu'un d'autre.</li>
<li><strong>Les enfants à part</strong> : beaucoup de familles gardent les cadeaux habituels pour les petits et réservent le tirage aux adultes et aux ados.</li>
<li><strong>Une liste d'envies</strong> de quelques idées par personne, partagée dans le groupe de la famille.</li>
</ul>
<h2>Faire le tirage quand la famille est dispersée</h2>
<p>C'est souvent là que le chapeau et les papiers ne suffisent plus : les cousins vivent loin, les grands-parents ne sont pas là au moment du tirage. Avec <a href="/">Qui offre à qui</a>, vous entrez les prénoms, cochez les couples à séparer, et chacun reçoit son résultat par e-mail. C'est prêt en 2 minutes, sans compte et gratuitement.</p>
<h2>Des idées pour tous les âges</h2>
<div class="idees">
""" + idee("Plaid chauffant", "Pour les grands-parents frileux", "plaid chauffant") + idee("Jeu de société familial", "À ouvrir le soir même", "jeu de societe famille") + idee("Cadre photo numérique", "Pour partager les photos de famille", "cadre photo numerique") + idee("Lampe d'ambiance", "Les ados adorent", "lampe led chambre ado") + idee("Coffret gourmand", "Une valeur sûre pour les adultes", "coffret gourmand") + idee("Livre de recettes", "Pour les cuisiniers de la famille", "livre de recettes") + """
</div>
<p>Pour aller plus loin, consultez nos sélections <a href="/idee-cadeau-20-euros/">à 20 €</a>, <a href="/idee-cadeau-30-euros/">à 30 €</a> et <a href="/idee-cadeau-50-euros/">à 50 €</a>.</p>
<h2>Le jour de l'échange</h2>
<p>Posez tous les cadeaux sous le sapin avec seulement le prénom du destinataire. Ouvrez-les un par un, du plus jeune au plus âgé par exemple : chacun tente de deviner son Père Noël secret avant la révélation.</p>
<h2>Questions fréquentes</h2>
<h3>Faut-il inclure les enfants dans le tirage ?</h3>
<p>C'est au choix. Beaucoup de familles gardent les cadeaux classiques pour les enfants et font le tirage entre adultes et ados.</p>
<h3>Comment éviter que deux conjoints se tirent ?</h3>
<p>Ajoutez une exclusion dans notre outil : ces deux personnes ne pourront pas se tirer l'une l'autre.</p>
<h3>Quel budget pour un Père Noël secret en famille ?</h3>
<p>Entre 20 et 50 € en général. Choisissez un montant que tout le monde peut suivre sans difficulté.</p>
"""},
{
"slug": "secret-santa-a-distance",
"title": "Secret Santa à distance : l'organiser en ligne simplement",
"desc": "Organiser un Secret Santa ou un Père Noël secret à distance : tirage au sort en ligne sans compte, envoi des cadeaux par la poste et échange en visio.",
"date": "2026-11-26",
"body": """
<p>Télétravail, famille éclatée, amis dans d'autres villes : il est de plus en plus rare que tout le monde soit réuni pour tirer les noms au sort. Bonne nouvelle, un <strong>Secret Santa à distance</strong> s'organise très bien en ligne, du tirage jusqu'à l'ouverture des cadeaux.</p>
<h2>Étape 1 : le tirage au sort en ligne</h2>
<p>Sur <a href="/">Qui offre à qui</a>, l'organisateur entre les prénoms, le budget et la date, puis lance le tirage. Chaque participant reçoit son résultat par e-mail et découvre à qui il offre un cadeau. Pas de compte, et c'est gratuit.</p>
<h2>Étape 2 : se mettre d'accord sur la livraison</h2>
<ul>
<li><strong>Livraison directe</strong> : chacun fait livrer le cadeau chez son destinataire. Il faut alors connaître son adresse : demandez-la discrètement à l'organisateur.</li>
<li><strong>Livraison au bureau</strong> : pratique entre collègues, les cadeaux attendent à l'accueil.</li>
<li><strong>Dépôt chez l'organisateur</strong> : il redistribue tout le jour de la rencontre.</li>
</ul>
<h2>Étape 3 : l'ouverture en visio</h2>
<p>Fixez un créneau de 30 minutes en visio. Chacun ouvre son cadeau devant la caméra et tente de deviner son Père Noël secret : c'est souvent le meilleur moment de l'échange.</p>
<h2>Les pièges à éviter</h2>
<ul>
<li><strong>Commander trop tard</strong> : en décembre, comptez au moins une semaine de livraison.</li>
<li><strong>Oublier un budget clair</strong> : les frais de port ne doivent pas faire exploser le montant prévu.</li>
<li><strong>Les produits fragiles ou périssables</strong> : préférez ce qui voyage bien.</li>
</ul>
<h2>Des idées qui voyagent bien</h2>
<div class="idees">
""" + idee("Coffret de thés", "Léger et facile à envoyer", "coffret the") + idee("Carnet de qualité", "Plat et sans risque de casse", "carnet de notes a5") + idee("Chaussettes douillettes", "Rentrent dans une enveloppe", "chaussettes chaudes hiver") + idee("Jeu de cartes", "Petit format, grand plaisir", "jeu de cartes ambiance") + """
</div>
<p>Retrouvez aussi nos idées <a href="/idee-cadeau-10-euros/">à 10 €</a> et <a href="/idee-cadeau-20-euros/">à 20 €</a>, et nos conseils pour un <a href="/cadeau-secret-santa-collegue/">Secret Santa entre collègues</a>.</p>
<h2>Questions fréquentes</h2>
<h3>Peut-on faire un Secret Santa entièrement en ligne ?</h3>
<p>Oui : tirage en ligne, cadeaux livrés à domicile ou au bureau, et ouverture en visio.</p>
<h3>Comment connaître l'adresse de la personne tirée ?</h3>
<p>Demandez-la à l'organisateur, ou faites livrer au bureau ou chez l'organisateur pour garder le secret.</p>
<h3>Les participants doivent-ils s'inscrire ?</h3>
<p>Non : avec Qui offre à qui, ils reçoivent leur résultat par e-mail et l'ouvrent d'un clic, sans compte.</p>
"""},
{
"slug": "regles-pere-noel-secret",
"title": "Père Noël secret : règles, déroulement et astuces",
"desc": "Comment fonctionne un Père Noël secret ? Les règles simples, le budget, le tirage au sort, la remise des cadeaux et nos astuces pour que tout se passe bien.",
"date": "2026-11-26",
"body": """
<p>Le <strong>Père Noël secret</strong>, aussi appelé Secret Santa, permet d'offrir un seul cadeau au lieu d'en acheter pour tout le monde. Chaque participant tire au sort une personne à gâter, sans que celle-ci sache de qui viendra le cadeau. Voici comment l'organiser simplement.</p>
<h2>Le principe en 4 étapes</h2>
<ol>
<li><strong>On réunit les participants</strong> : famille, collègues, amis, club.</li>
<li><strong>On fixe un budget commun</strong>, le même pour tous.</li>
<li><strong>On fait le tirage au sort</strong> : chacun découvre en secret à qui il offre un cadeau.</li>
<li><strong>On échange les cadeaux</strong> le jour prévu, et chacun essaie de deviner qui l'a gâté.</li>
</ol>
<h2>Les règles à fixer avant le tirage</h2>
<ul>
<li><strong>Le budget</strong> : 10, 20 ou 30 € sont les montants les plus fréquents. L'important est que tout le monde le respecte.</li>
<li><strong>La date et le lieu de l'échange</strong> : repas de fêtes, pot au bureau, soirée entre amis.</li>
<li><strong>Les exclusions</strong> : par exemple, deux conjoints qui ne doivent pas se tirer l'un l'autre.</li>
<li><strong>Le thème, si vous le souhaitez</strong> : fait maison, livres, cadeaux rigolos, tout à moins de 10 €.</li>
<li><strong>Les listes d'envies</strong> : quelques idées par personne aident beaucoup ceux qui connaissent peu leur destinataire.</li>
</ul>
<h2>Faire le tirage sans papier ni chapeau</h2>
<p>Le tirage avec des papiers pliés a ses limites : quelqu'un tire son propre nom, les absents ne peuvent pas participer, et il faut recommencer. Avec un <a href="/">tirage au sort en ligne</a>, chaque participant reçoit son propre résultat par e-mail. Personne ne voit les autres tirages, pas même l'organisateur, et les exclusions sont respectées automatiquement.</p>
<h2>Le jour de l'échange</h2>
<ul>
<li>Déposez les cadeaux au même endroit, avec seulement le prénom du destinataire.</li>
<li>Ouvrez-les un par un : c'est le moment où chacun essaie de deviner son Père Noël secret.</li>
<li>Révélez ou non les identités, selon ce que le groupe préfère.</li>
</ul>
<h2>Nos astuces pour que tout se passe bien</h2>
<ul>
<li><strong>Ne fixez pas un budget trop élevé</strong> entre collègues : tout le monde n'a pas les mêmes moyens.</li>
<li><strong>Prévoyez un petit cadeau de secours</strong> si quelqu'un oublie ou ne peut pas venir.</li>
<li><strong>Lancez le tirage au moins deux semaines avant</strong> pour laisser le temps de commander.</li>
</ul>
<h2>Besoin d'idées ?</h2>
<p>Consultez nos sélections par budget : <a href="/idee-cadeau-10-euros/">idées à 10 €</a>, <a href="/idee-cadeau-20-euros/">à 20 €</a> et <a href="/idee-cadeau-30-euros/">à 30 €</a>, ou nos idées pour un <a href="/cadeau-secret-santa-collegue/">Secret Santa entre collègues</a>.</p>
<h2>Questions fréquentes</h2>
<h3>Quelle différence entre Père Noël secret et Secret Santa ?</h3>
<p>Aucune : Secret Santa est le nom anglais du même jeu.</p>
<h3>À partir de combien de personnes peut-on jouer ?</h3>
<p>Dès 3 personnes, mais le jeu est plus amusant à partir de 5 ou 6.</p>
<h3>Et si quelqu'un tire son propre nom ?</h3>
<p>Avec notre outil, c'est impossible : le tirage exclut automatiquement chaque personne d'elle-même.</p>
"""},
{
"slug": "cadeau-secret-santa-collegue",
"title": "Secret Santa entre collègues : idées cadeaux et règles",
"desc": "Organiser un Secret Santa au bureau : quel budget, quelles règles, quels cadeaux pour un collègue qu'on connaît peu, et les pièges à éviter.",
"date": "2026-11-26",
"body": """
<p>Le <strong>Secret Santa entre collègues</strong> est une façon simple de fêter la fin d'année au travail, sans que chacun achète un cadeau à toute l'équipe. Encore faut-il trouver un cadeau pour quelqu'un qu'on ne connaît parfois que de vue. Voici les règles qui marchent et des idées sans risque.</p>
<h2>Les règles qui évitent les malaises</h2>
<ul>
<li><strong>Un budget modeste et identique</strong> : 10 à 15 € suffisent, pour que personne ne soit gêné.</li>
<li><strong>La participation reste libre</strong> : personne ne doit se sentir obligé.</li>
<li><strong>Pas de cadeau trop personnel</strong> : ni parfum, ni vêtement intime, ni humour qui pourrait blesser.</li>
<li><strong>Une date claire</strong> pour l'échange, au pot de fin d'année par exemple.</li>
</ul>
<h2>Les cadeaux sans risque pour un collègue</h2>
<div class="idees">
""" + idee("Mug isotherme", "Pour le café qui refroidit pendant les réunions", "mug isotherme") + idee("Carnet et stylo élégants", "Toujours utiles au bureau", "carnet stylo cadeau") + idee("Plante de bureau facile", "Un peu de vert sans entretien", "plante bureau facile") + idee("Coffret de thés", "Pour la pause de l'après-midi", "coffret the") + idee("Support de téléphone", "Pratique pour les visios", "support telephone bureau") + idee("Chocolats de qualité", "Un classique qui plaît presque à tous", "chocolats coffret") + """
</div>
<h2>Les cadeaux un peu plus fun</h2>
<div class="idees">
""" + idee("Casse-tête de bureau", "Pour s'occuper pendant une pause", "casse tete bois") + idee("Mini jeu de société", "Pour les pauses déjeuner", "jeu de cartes rapide") + idee("Lampe USB originale", "Pour égayer un bureau", "lampe usb bureau") + """
</div>
<h2>Organiser le tirage au bureau</h2>
<p>Avec le télétravail, il est rare que toute l'équipe soit présente le jour du tirage. Avec <a href="/">Qui offre à qui</a>, l'organisateur entre les prénoms, lance le tirage, et chacun reçoit son résultat par e-mail. Personne ne voit les résultats des autres.</p>
<h2>Pour aller plus loin</h2>
<p>Retrouvez nos <a href="/regles-pere-noel-secret/">règles complètes du Père Noël secret</a> et nos idées <a href="/idee-cadeau-10-euros/">à 10 €</a> ou <a href="/idee-cadeau-20-euros/">à 20 €</a>.</p>
<h2>Questions fréquentes</h2>
<h3>Quel budget pour un Secret Santa au travail ?</h3>
<p>Entre 10 et 15 € en général. Fixez-le avant le tirage et demandez à chacun de le respecter.</p>
<h3>Que faire si un collègue ne veut pas participer ?</h3>
<p>Rien de spécial : la participation doit rester libre. Il suffit de ne pas l'ajouter au tirage.</p>
<h3>Peut-on faire un Secret Santa à distance ?</h3>
<p>Oui : le tirage se fait en ligne, et chacun envoie son cadeau par la poste ou le dépose au bureau.</p>
"""},
{
"slug": "jeu-ange-gardien",
"title": "Jeu de l'ange gardien : règles, idées et tirage en ligne",
"desc": "Le jeu de l'ange gardien pour un EVJF, un mariage, une colo ou un séminaire : les règles, 30 idées d'attentions et le tirage au sort gratuit en ligne.",
"date": "2026-11-26",
"outil": "/?t=ange#outil",
"outil_txt": "Faire mon tirage d'ange gardien",
"body": """
<p>Le <strong>jeu de l'ange gardien</strong> est un tirage au sort secret, comme le Père Noël secret, mais sans date de remise de cadeau. Chacun tire le nom d'une personne du groupe et devient son ange gardien pendant toute la durée de l'événement : il lui fait de petites attentions en cachette, sans se faire démasquer. À la fin, chacun essaie de deviner qui veillait sur lui. C'est simple, ça crée du lien et ça fait beaucoup rire.</p>
<h2>Les règles du jeu en 4 étapes</h2>
<ol>
<li><strong>Le tirage au sort</strong> : chaque participant reçoit en secret le nom de son protégé. Personne ne doit se tirer lui-même, et l'idéal est que même l'organisateur ignore les résultats pour pouvoir jouer.</li>
<li><strong>La durée</strong> : un week-end d'EVJF, une semaine de colo, trois jours de séminaire, ou tout un mois pour une équipe de travail. Annoncez clairement la date de fin.</li>
<li><strong>Les attentions</strong> : petits mots, services rendus, douceurs, défis gentils. Le but est de faire plaisir, jamais de mettre mal à l'aise.</li>
<li><strong>La révélation</strong> : au dernier repas ou à la dernière réunion, chacun tente de deviner son ange gardien, puis on révèle tout.</li>
</ol>
<p>Avec le tirage en ligne, chacun reçoit le nom de son protégé par e-mail. Il n'y a pas de papiers à cacher ni de risque de tirer son propre nom, et l'organisateur peut participer comme les autres.</p>
<h2>Où jouer à l'ange gardien ?</h2>
<ul>
<li><strong>EVJF et EVG</strong> : parfait pour souder un groupe d'amies qui ne se connaissent pas toutes. La future mariée peut jouer ou recevoir plusieurs anges.</li>
<li><strong>Mariage</strong> : entre témoins et demoiselles d'honneur pendant les préparatifs, ou entre invités sur un week-end.</li>
<li><strong>Colonies de vacances et camps scouts</strong> : un classique pour créer de l'entraide entre enfants qui ne se connaissent pas.</li>
<li><strong>Séminaires et équipes de travail</strong> : une semaine d'ange gardien améliore l'ambiance, surtout dans une équipe récente.</li>
<li><strong>Associations, retraites, groupes de jeunes</strong> : le jeu fonctionne partout où un groupe vit quelques jours ensemble.</li>
</ul>
<h2>Idées d'attentions gratuites</h2>
<ul>
<li>Un petit mot d'encouragement glissé dans un sac ou sous une porte.</li>
<li>Un café ou un thé préparé comme il l'aime, posé à sa place.</li>
<li>Un service rendu : ranger son plateau, garder sa place, porter son sac.</li>
<li>Un dessin ou un poème anonyme.</li>
<li>Une chanson qu'il aime demandée à la soirée.</li>
<li>Un compliment transmis par une autre personne, pour brouiller les pistes.</li>
</ul>
<h2>Petites attentions à offrir</h2>
<p>Si vous voulez ajouter un petit cadeau, restez sur des budgets de 2 à 10 € : l'intérêt est dans le geste, pas dans le prix.</p>
<div class="idees">
""" + idee("Bonbons ou chocolats", "La douceur qui marche à tous les coups", "bonbons assortiment") + idee("Carte à message", "Pour un mot doux anonyme", "cartes a message") + idee("Petit carnet", "Avec un premier message déjà écrit", "petit carnet") + idee("Baume à lèvres", "Utile en week-end comme en colo", "baume levres") + idee("Masque pour les yeux", "Pour les nuits courtes d'EVJF", "masque de nuit") + idee("Mini bougie parfumée", "Une attention cocooning", "mini bougie parfumee") + """
</div>
<h2>Les pièges à éviter</h2>
<ul>
<li><strong>Les attentions trop voyantes</strong> : tout le monde devinerait tout de suite. Variez les moments et les complices.</li>
<li><strong>Les blagues qui vexent</strong> : un ange gardien protège, il ne piège pas.</li>
<li><strong>Le déséquilibre</strong> : rappelez à mi-parcours que chacun doit penser à son protégé, pour que personne ne soit oublié.</li>
<li><strong>Le tirage raté</strong> : avec des papiers, quelqu'un finit toujours par tirer son propre nom. Le tirage en ligne règle le problème.</li>
</ul>
<p>Vous organisez plutôt un échange de cadeaux ? Voyez nos <a href="/regles-pere-noel-secret/">règles du Père Noël secret</a> et nos <a href="/idee-cadeau-5-euros/">idées de cadeaux à 5 €</a>, parfaites aussi pour un ange gardien.</p>
<h2>Questions fréquentes</h2>
<h3>Combien de temps dure le jeu de l'ange gardien ?</h3>
<p>Le temps de l'événement : un week-end pour un EVJF, une semaine pour une colo ou un séminaire. Au-delà d'un mois, l'enthousiasme retombe souvent.</p>
<h3>Faut-il offrir un cadeau à son protégé ?</h3>
<p>Non. Les attentions gratuites suffisent largement. Si le groupe veut des cadeaux, fixez un petit budget commun, par exemple 5 €.</p>
<h3>Peut-on jouer à distance ?</h3>
<p>Oui : messages, cartes postales, playlist partagée ou petit colis. Le tirage se fait en ligne et chacun reçoit le nom de son protégé par e-mail.</p>
"""},
]
