# Guides du site Qui offre à qui. Chaque guide : slug, titre, description, date, corps HTML.
# Liens Amazon : écrire {AMZ:mots clés} ; build.py le remplace par une recherche Amazon avec l'identifiant quioffreaqui-21.
# Règles : vouvoiement, aucun tiret long ni demi-cadratin, aucun prix précis inventé, aucun avis inventé.

def idee(titre, texte, kw):
    return f'<div class="idee"><b>{titre}</b><span>{texte}</span><a class="btn s petit" href="{{AMZ:{kw}}}" rel="sponsored nofollow noopener" target="_blank">Voir les modèles</a></div>'

PAGES = [
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
<p>Avec notre <a href="/">outil gratuit</a>, vous entrez les prénoms et chacun reçoit un lien privé avec le nom de la personne à gâter, sans inscription.</p>
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
<p>Sur <a href="/">Qui offre à qui</a> : entrez les prénoms, ajoutez les exclusions si besoin, et chacun reçoit son lien privé.</p>
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
<p>Utilisez notre <a href="/">outil de tirage gratuit</a> : il gère les exclusions (couples, frères et sœurs) et envoie un lien privé à chacun.</p>
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
<p>Le tirage avec des papiers pliés a ses limites : quelqu'un tire son propre nom, les absents ne peuvent pas participer, et il faut recommencer. Avec un <a href="/">tirage au sort en ligne</a>, chaque participant reçoit un lien privé qui n'affiche que son propre résultat. Personne ne voit les autres tirages, pas même l'organisateur, et les exclusions sont respectées automatiquement.</p>
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
<p>Avec le télétravail, il est rare que toute l'équipe soit présente le jour du tirage. Avec <a href="/">Qui offre à qui</a>, l'organisateur entre les prénoms, lance le tirage et envoie à chacun son lien privé par messagerie. Personne ne voit les résultats des autres.</p>
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
]
