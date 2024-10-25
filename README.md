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

	L'utilisateur du site peut : 

	Faire défiler un carousel de photos et indications sur les JO
 	Sélectionner d'une épreuve et une offre associée
 	Ajouter l'offre au panier
  	Créer un compte utilisateur (e-mail + mot de passe)
   	Passer un contrôle (factice) d'identité (mock d'une application comme Jumio)
    	Recevoir un lien d'activation par mail
     	Activer le lien et se connecter 
      	Procéder au paiement (factice) : pour que le paiement soit valide, entrer CVC = 999
        Accéder à ses billets avec qrcode : le qrcode est une clé générée par la concaténation d'une clé crée par l'authenticité du compte utilisateur et d'une clé crée par le succès du paiement
	Se déconnecter

 	L'administrateur du site peut : 

   	Se connecter à l'espace admin : /olympics-ticketing-admin-2024-Paris/
    	Ajouter, modifier, supprimer une épreuve (Event)
    	Ajouter, modifier, supprimer une offre (Offer) en indiquant le pourcentage de remise sur le billet unitaire et le nombre de billets auquel l'offre ouvre droit
     	Consulter un histogramme des offres vendues
      	Actualiser les images et textes (About)
        Actualiser les mentions légales (Legal)
    	
       
