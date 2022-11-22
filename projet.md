# Recherche général du sujet:

Système connecté (IoT):
    Réseau LoraWAN
    Système P2P
    POCSAG

### (Problème, fluidification routière ville:)

    Géoloc:
     MLAT (TDOA):
        Système de secours (localisation d'une source)
        Onde sonore également. (arXiv:1910.10661v3)
     (github.com/gsongsong/mlat)
    
    Classic triangulation:
        Service livraison par drone (Amazon, google). DGAC (loisir drone)
        (DOI: 10.1016/j.ijcip.2019.100310)
            Comment gérer un service complet de livraison?
            (DOI: 10.1016/j.trc.2021.103506)
    http://www.snastro.org/media/J-LC_GPS.PDF
    https://en.wikipedia.org/wiki/GPS_signals#Coarse/acquisition_code
    https://fr.wikipedia.org/wiki/Filtre_de_Kalman
    http://www.aholme.co.uk/GPS/Main.htm
    
            

### Optimisation du trafic routier & limitation de la pollution personnel:  
   #### Ville saturé et trafic:  (DOI: 10.1016/j.procs.2020.03.092)
        
    Qualité de l'air :
        Véhicule moins polluante:
            Électrique ? (Gestion des bornes ?)

Energie lié à la ville:
    Production plus écologique, vers une transition durable:
        Nucléaire ?
        SMR (Small modular reactors ?)
     (https://www-sciencedirect-com.ezproxy.uca.fr/search?qs=Small%20modular%20reactors)

Pollution sonore:
    Radar “sonore”

Pollution des sources sonores.  
http://www.allier.gouv.fr/IMG/pdf/n145_carte_type_a_lden.pdf

Gestion des vehicules electrique et des flux (suivi automatique de ligne)

### Santé d'internet:  
https://internethealthreport.org/2019/le-pouvoir-des-villes/?lang=fr

---

https://reseau-orpheon.fr/le-reseau-orpheon/le-positionnement-gps-gnss/

http://cnig.gouv.fr/wp-content/uploads/2018/02/methodes_travail_reseau_GNSS_130219.pdf

https://www.geologie.ens.fr/~ecalais/teaching/geopositionnement-gnss/m2_geopositionnement_2.pdf
https://hal.archives-ouvertes.fr/hal-03189905/document

---
# La géolocalistion:

## Problématique:
* Les Internet of Things (IoT) se doivent de pouvoir accèder à leur géolocalistion précise dans la ville. (Eg: tracker par exemple pour animaux, pour objets, etc).

### Etude:
* Sytème de géolocalisation par satellite, et optimisation de la précision (du signal, de la géoloc, résitance aux perturbation etc...)

---

# Historique des recherches:
## Avant le 30/03/2022:
* Recherches entre différents sujets
* Recherches général autour des systèmes de géoloc
* Recherches autour du signal et des référentiel utilisé (traitement et sync) (cf. l_58, doc ENS)

## Le 30/03/2022:
#### Questions:
* Stabilité du signal en TX et shift deviation, en RX
* Débruitage du signal en RX cf. [1]
* Correction de la précision cf. [2]
* Filtrage des signaux cf.[3]

## Le 04/04/2022:
#### Recherche sur le débruitage du signal :
* Application aux ondelettes cf. [4]
* Voir le fichier EURONAV.2017.7954204.pdf & le cf. [5]
#### Synthèse:
Le débruitage du signal GPS se fait assez numériquement (utilisation d'ondelettes, et des décomposition en modes empiriques),
difficillement expérimentable, et comparable. Je vais chercher d'avantage des thèse sur le sujet, sinon il faudra m'orienter sur autre chose 
(par exemple, les moyen de correction, ou bien les erreurs due aux conditions atmosphèriques, ou sur le signal lui même).

## Le 13/04/2022:
#### Recherche complémentaire sur le traitement du signal :
* Thèse à propos (+/- in french !) cf. [6] & [7] & [8]

#### Recherche de sujets annexes:
* Synchronisation des récepteurs GPS
* Correction atomsphériques cf. [2]
* Correction par l'usage du GPS dit différentiel (utilisation base aux sol) cf. [9]

#### Idées complémentaires:
* Modélisation numérique de perturbation atmosphérique et analyse de solution pour réduire la perte de précision liée.
* Création d'un système simplifiée GPS (GNSS) pour étudier la synchronisation GPS et les algorithmes de correlation utilisé. cf. [1] & [2] & wikipedia English on GPS signals.
* Implémentation d'un débruitage numérique (NB: Comment obtenir des donnés exploitables ?)

#### Réception d'un signal GPS:
* Quartz générant un signal similaire à celui du GPS reçu, correlation avec le signal réel (signal à autocorrélation très faible), calcul du différence de temps. Ce delta t, correspond à au temps satellite récepteur GPS et également le temps du au manque important de précision du quartz du récepteur GPS.

## Le 27/04/2022:
#### Corrections atmosphériques, voir [11], [12], [13], [14]

## Le 02/05/2022:
#### Lecture du document sur l'ionosphere [13]:
* Différents modèle de l'ionosphere: 
    * International Reference Ionosphere (IRI), simple, peu efficace quand perturbation.
    * IPIM Irap Plasmasphere Ionosphere Model, plus complexe et fonctionne lors de vents solaires (choix du doctorant)
* Différents modèles de propagation des ondes:
    * Equations paraboliques (Maxwell)(Equation d'ondes)
    * Optique géométrique (Tracé de rayons) (choix du doctorant)

#### GPS simulation, correlation et synchronisation
* Mise en place d'un test simple
* Système de correlation
* Synchronisation temporelle [15] (navigation equations) (https://electronics.stackexchange.com/questions/551458/how-does-the-4th-satellite-in-gps-know-the-time-offset)
* Etude de la dilution géométrique et/ou temporelle

## Le 11/05/2022
#### Debut d'un script sur la modélisation d'une orbite kepleriene
Cf [16], thèse sur la résolution des équations GNSS

## Le 16/05/2022
#### Avancement sur le programme

## Le 25/05/2022
#### Finition du programme sur les orbites de keplers
Ajustement de l'équation sur l'anomalie vrai cf.[17]

## Le 13/06/2022
#### Le programme est fini. Les orbites de kepler sont parfaitement modélisée, plusieurs piste pour la suite:
* Création d'un système de résolution par la technique des moindres carrées [16],
* Etude des perturbations atm [13] & [12]
* Recherche d'un sujet expérimentale, (lampe mercure). [18]
    * Ionosphère:
        * Ondes ralenties
        * Polarisation
        * Réfraction
    * Traitement du signal (elec & autom):
        * Reception & filtre
        * Quatz

## Le 22/06/2022
#### Impact de l'ionosphere sur le GPS: (GNSS):  
Etude des SID cf.[19], [32]  
Lien entre SID et erreur GNSS, cf.[20]  
Expérience possible cf.[21]  

## Le 13/09/2022
### GNSS et Total electron content (TEC)  
D'après le concours [E3A](https://github.com/n005/Tipe/blob/draft/2020-Concours%20e3a-Physique%20et%20Chimie-PC-enonce-2.pdf), il existe un lien entre la différence de temps de deux signaux et le TEC.  
Plus d'info, cf *"Bidaine_2009_TECGPS_IRST.pdf"* [22]  
Calcul du TEC par smartphone, dual-band cf [23] et [24]  
Intéret du dual band: [25]  **(Ce choix de parcours semble peu documenté dans la littérature scientifique, à creuser !)**, documentation supplémentaire: [26], [27],        [28], [29], [30], [31]  
Lien du CEA sur l'ionosphere (peut servir d'introduction) cf. [26]

### Partie expérimentale:
**Deux expérience possibles:**
* Etude qualitive du lien entre variation de la permitivité de l'ionosphere (SID) aux ondes très basse fréquences et la précision du signal GPS:
    * Mesure du niveau de signaux d'émetteur suffisament loin pour ne pas recevoir le signal directement (eg: DHO38 ou  le DCF77) 
    * Matériel:
        * Une antenne voir [ici](https://sidstation.loudet.org/antenna-fr.xhtml) pour la création
        * Un recepteur GNSS (GPS) pour les mesures de position
        * Un recepteur RTL-SDR en direct sampling pour la reception très basse fréquence (Vérification du rapport signal/bruit sur ces signaux)
        * Un raspberry ou autre carte éléctronique permettant une veille des mesures sur plusieurs jours.
* Etude quantitative de la différence de TEC
    * Mesure de différence entre deux bandes de signaux à l'aide d'un smartphone, voir concours [E3A](https://github.com/n005/Tipe/blob/draft/2020-Concours%20e3a-Physique%20et%20Chimie-PC-enonce-2.pdf), [23] et [24]  

## Le 20/09/2022
Réalisation d'une tentative très basse fréquence (126kHz) avec un RLT-SDR, réussi !  
Tentative d'analyser de fichiers RINEX prélevé dans le WeekEnd à l'aide d'un Xiaomi Mi 8
Prochaine étape: Construction d'un cadre basse fréquence.  

# Le 27/09/2022
Réalisation et exploitation des résultat RINEX (plotting sous Python).
Recherche sur le matériel permettant la construction de l'antenne.

# Le 04/10/2022
Finalisation d'un prototype d'antenne, réalisation d'un filtre dit: "notch 50Hz", puis "FM notch filters" 

# Le 11-12-13/11/2022
Creation de protocole d'analyse des données, comparaison du multipath en ville/campagne, TEC, utilisation de teqc et RTKlib

# Le 15/11/2022
MCOT (cf. mcot.md)

# Le 22/11/2022
Utilisation et modification pour le logiciel GnssLogger

--- 
# Sources & références:
[1]: http://www.snastro.org/media/J-LC_GPS.PDF
1: http://www.snastro.org/media/J-LC_GPS.PDF

[2]: https://www.geologie.ens.fr/~ecalais/teaching/geopositionnement-gnss
2: https://www.geologie.ens.fr/~ecalais/teaching/geopositionnement-gnss

[3]: http://www.aholme.co.uk/GPS/Main.htm
3: http://www.aholme.co.uk/GPS/Main.htm

[4]: https://hal.inria.fr/hal-01361007/document
4: https://hal.inria.fr/hal-01361007/document

[5]: https://onlinelibrary.wiley.com/doi/10.1002/navi.300
5: https://onlinelibrary.wiley.com/doi/10.1002/navi.300

[6]: https://oatao.univ-toulouse.fr/7579/1/al_bitar.pdf
6: https://oatao.univ-toulouse.fr/7579/1/al_bitar.pdf

[7]: https://tel.archives-ouvertes.fr/tel-01589215/document
7: https://tel.archives-ouvertes.fr/tel-01589215/document

[8]: http://recherche.ign.fr/labos/lareg/pdf/Theses/these_stephane_durand_2003.pdf
8: http://recherche.ign.fr/labos/lareg/pdf/Theses/these_stephane_durand_2003.pdf

[9]: https://reseau-orpheon.fr/le-reseau-orpheon/le-positionnement-gps-gnss/
9: https://reseau-orpheon.fr/le-reseau-orpheon/le-positionnement-gps-gnss/

[10]: https://gssc.esa.int/navipedia/index.php/Main_Page
10: https://gssc.esa.int/navipedia/index.php/Main_Page   
(Bible de l'Esa sur les systèmes GNSS) 

[11]: https://www.unoosa.org/pdf/icg/2017/CRASTE-LF/1_02.pdf
11: https://www.unoosa.org/pdf/icg/2017/CRASTE-LF/1_02.pdf

[12]: https://www.unoosa.org/pdf/icg/2017/CRASTE-LF/1_03.pdf
12: https://www.unoosa.org/pdf/icg/2017/CRASTE-LF/1_03.pdf

[13]: https://tel.archives-ouvertes.fr/tel-02979322/document
13: https://tel.archives-ouvertes.fr/tel-02979322/document

[14]: https://reseau-orpheon.fr/le-reseau-orpheon/travailler-dans-les-zones-difficiles/
14: https://reseau-orpheon.fr/le-reseau-orpheon/travailler-dans-les-zones-difficiles/

[15]: https://www.researchgate.net/profile/Helio-Kuga/publication/43655015_Real_time_estimation_of_GPS_receiver_clock_offset_by_the_Kalman_filter/links/0912f506d94444dda9000000/Real-time-estimation-of-GPS-receiver-clock-offset-by-the-Kalman-filter.pdf?origin=publication_detail
15: https://www.researchgate.net/profile/Helio-Kuga/publication/43655015_Real_time_estimation_of_GPS_receiver_clock_offset_by_the_Kalman_filter/links/0912f506d94444dda9000000/Real-time-estimation-of-GPS-receiver-clock-offset-by-the-Kalman-filter.pdf?origin=publication_detail

[16]: https://tel.archives-ouvertes.fr/tel-01871943/document
16: https://tel.archives-ouvertes.fr/tel-01871943/document

[17]: https://en.wikipedia.org/wiki/True_anomaly
17: https://en.wikipedia.org/wiki/True_anomaly

[18]: https://fr.wikipedia.org/wiki/Ionosph%C3%A8re
18: https://fr.wikipedia.org/wiki/Ionosph%C3%A8re

[19]:https://sidstation.loudet.org/antenna-fr.xhtml
19: https://sidstation.loudet.org/antenna-fr.xhtml

[20]: https://www.researchgate.net/profile/Serdjo-Kos/publication/236721806_Ionospheric_monitoring_by_correlation_between_GPS_positioning_performance_and_SID_monitor_observables/links/00b4951921da9b9d67000000/Ionospheric-monitoring-by-correlation-between-GPS-positioning-performance-and-SID-monitor-observables.pdf?origin=publication_detail
20: https://www.researchgate.net/profile/Serdjo-Kos/publication/236721806_Ionospheric_monitoring_by_correlation_between_GPS_positioning_performance_and_SID_monitor_observables/links/00b4951921da9b9d67000000/Ionospheric-monitoring-by-correlation-between-GPS-positioning-performance-and-SID-monitor-observables.pdf?origin=publication_detail

[21]: https://cedarscience.org/sites/default/files/meetings/2018/IRRI-10-Han.pdf
21: https://cedarscience.org/sites/default/files/meetings/2018/IRRI-10-Han.pdf

[22]: https://www.researchgate.net/publication/224588328_Measuring_Total_Electron_Content_with_GNSS_Investigation_of_two_different_techniques
22: https://www.researchgate.net/publication/224588328_Measuring_Total_Electron_Content_with_GNSS_Investigation_of_two_different_techniques

[23]: https://www.researchgate.net/publication/344626243_Quality_analysis_of_dual-frequency_smartphone-based_ionospheric_TEC_measurements_what_can_be_achieved
23: https://www.researchgate.net/publication/344626243_Quality_analysis_of_dual-frequency_smartphone-based_ionospheric_TEC_measurements_what_can_be_achieved

[24]: https://iopscience.iop.org/article/10.1088/1742-6596/1991/1/012025/pdf
24: https://iopscience.iop.org/article/10.1088/1742-6596/1991/1/012025/pdf

[25]: https://www.sport-passion.fr/test-materiel/explication-et-interet-GPS-double-frequence.php
25: https://www.sport-passion.fr/test-materiel/explication-et-interet-GPS-double-frequence.php

[26]: http://www-dase.cea.fr/public/dossiers_thematiques/atmosphere-ionosphere_perturbations_et_couplages/description.html
26: http://www-dase.cea.fr/public/dossiers_thematiques/atmosphere-ionosphere_perturbations_et_couplages/description.html

[27]: https://onlinelibrary.wiley.com/doi/full/10.1002/navi.448
27: https://onlinelibrary.wiley.com/doi/full/10.1002/navi.448

[28]: https://www.euspa.europa.eu/newsroom/news/test-your-android-device-s-satellite-navigation-performance
28: https://www.euspa.europa.eu/newsroom/news/test-your-android-device-s-satellite-navigation-performance

[29]: https://www.geospatialworld.net/blogs/advantages-of-dual-frequency-gnss-in-smartphones/
29: https://www.geospatialworld.net/blogs/advantages-of-dual-frequency-gnss-in-smartphones/

[30]: https://www.researchgate.net/publication/267369446_Real-Time_Multipath_Estimation_for_Dual_Frequency_GPS_Ionospheric_Delay_Measurements
30: https://www.researchgate.net/publication/267369446_Real-Time_Multipath_Estimation_for_Dual_Frequency_GPS_Ionospheric_Delay_Measurements

[31]: https://mdpi-res.com/d_attachment/remotesensing/remotesensing-13-02295/article_deploy/remotesensing-13-02295-v2.pdf?version=1623739530
31: https://mdpi-res.com/d_attachment/remotesensing/remotesensing-13-02295/article_deploy/remotesensing-13-02295-v2.pdf?version=1623739530

[32]: https://www.researchgate.net/publication/312877237_An_SDR-based_Study_of_Multi-GNSS_Positioning_Performance_During_Fast-developing_Space_Weather_Storm
32: https://www.researchgate.net/publication/312877237_An_SDR-based_Study_of_Multi-GNSS_Positioning_Performance_During_Fast-developing_Space_Weather_Storm
