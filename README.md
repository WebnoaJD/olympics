# Olympics

  Il s'agit d'un site factice de la billeterie des Jeux Olympiques Paris 2024, dans le cadre d'un projet étudiant

## Installation

	1. Cloner le dépot :
	   	Dans une console bash : 
			git clone https://github.com/WebnoaJD/olympics.git
			cd projet
		
	2. Créer un environnement virtuel : 
			python -m venv myenv
			source myenv/bin/activate  # Sur Windows : myenv\Scripts\activate
		
	3. Installer les dépendances :
			pip install -r requirements.txt


## Utilisation

	Executer : python manage.py runserver

## Fonctionnalités

	Carousel de photos et indications sur les JO
 	Sélection d'une épreuve et une offre associée
 	Ajout au panier
  	Créer un compte utilisateur (e-mail + mot de passe)
   	Passer un contrôle (factice) d'identité (mock d'une application comme Jumio)
    	Recevoir un lien d'activation par mail
     	Activer le lien et se connecter 
      	Procéder au paiement (factice) : pour que le paiement soit valide, entrer CVC = 999
        Accéder à ses billets avec qrcode : le qrcode est une clé générée par la concaténation d'une clé crée par l'authenticité du compte utilisateur et d'une clé crée par le succès du paiement
	Se déconnecter
       
