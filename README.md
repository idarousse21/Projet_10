<h1 align ="center">Explication et lancement du code</h1>

------------------------------
<h2 align = "center"> Application et Bibliothèque</h2>

<p>
    Pour employer le code, tout d'abord, installez l'application python.
<ul>
    <li>
        <a href = "https://www.python.org/downloads/">Python </a>
    </li>
</ul>
</p>
<p>
    Nous utiliserons aussi les bibliothèques python:.
<ul>
    <li>
        <a href = "https://www.djangoproject.com/">Django </a>
    </li>
    <li>
        <a href = "https://www.django-rest-framework.org/">Django REST framework</a>
    </li>
    <li>
        <a href = "https://django-rest-framework-simplejwt.readthedocs.io/en/latest/">Simple JWT</a>
    </li>
</ul>
</p>

<h2 align = "center"> Documentation de l'application </h2>
<p>
   Avant de lancer l'application je vous suggère de lire la documentation de l'API:
<ul>
    <li>
        <a href = "https://documenter.getpostman.com/view/23090595/2s8Z75Spn4">Documntation Softdesk API </a>
    </li>
</ul>

</p>

<h2 align = "center"> Lancement du code </h2>
<p>Pour commencer, vous devez lancer l'invite de commande et employer les commandes suivantes:
    <ol>
        <li>Clonez le projet:</li>
                <ul><li>git clone https://github.com/idarousse21/Projet_10 </li></ul>
            <li>Dirigez-vous sur le dossier cloné:</li>
                <ul><li>cd Projet_10 </li></ul>
            <li>Créez un environnement virtuel:</li>
                <ul><li>python -m venv env</li></ul>
            <li>Puis activation de l'environnement virtuel:</li>
                <ul><li>Sur Windows:</li></ul>
                env\Scripts\activate
                <ul><li>Sous Mac/Linus:</li></ul>
                source/env/Scripts/activate
            <li>Télécharger les bibliothèque nécessaire :</li>
                <ul><li>pip install -r requirements.txt</li></ul>
            <li>Démarrer le serveur django:</li>
                <ul><li>python manage.py runserver</li></ul>
    </ol>

<h2 align = "center"> Création de compte test </h2>
    <p>
        Pour le test de l'application 4 compte utilisateur et un compte super utilisateur ont été créer.
    </p>
    <p> 
        Identifiant/MDP
    </p>
    <ul>
        <li>
            Utilisateurs:<br/>
            test1 : openclassroom123<br/>
            test2 : openclassroom123<br/>
            admin : admin123
        </li>
    </ul>
        <p> Pour acceder a la page de l'admin:</p>
        <ul>
        <li> Taper l'url sur votre navigateur</li>
            <ul><li>http://localhost:8000/admin/</li></ul>
        </ul>
        <p>Et utiliser l'identifiant et le mot de passe du super utilisateur:</p>
        <ul>
        <li>
            Super utilisateur:<br/>
            admin : admin123
        </li>
        </ul>
    
