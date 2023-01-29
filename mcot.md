# Etudes des système GNSS des smartphones.
Depuis l'arrivé massive des appareils connectés (IoT), je me suis questionné sur leurs systèmes permettant leurs inter-connexions, les enjeux sont nombreux,
fiabilité, sécurité, éco-conception etc... Mon objectif est donc d'évaluer les performances en Ville des systèmes GNSS des smartphones, et d'évaluer les sources
d'incertitudes.

## Positionnement thématique (ETAPE 1) 

*INFORMATIQUE (Technologies informatiques); SCIENCES INDUSTRIELLES(Électronique); PHYSIQUE(Physique Interdisciplinaire).*

## Mots-clés (ETAPE 1) 
* GNSS,  
* Ionosphere,
* Dual-Band GNSS,
* Programation,
* Modélisation,


## Bibliographie commentée 

Le système GNSS (Global Navigation Satellite System) est un système de géolocalisation qui utilise des satellites en orbite autour de la Terre pour permettre à des appareils sur le sol de déterminer leur position, leur vitesse et l'heure avec une très grande précision. Les systèmes GNSS les plus connus sont le GPS (Global Positioning System) des États-Unis, le GLONASS (Global Navigation Satellite System) de la Russie, le Galileo de l'Union Européenne et le BeiDou de la Chine.
Le concept de GNSS a été développé dans les années 1950, mais le premier système opérationnel, le GPS, n'a été mis en place qu'au début des années 1980. Au départ, le GPS était principalement utilisé par l'armée américaine, mais il est rapidement devenu accessible au grand public grâce à la diffusion de récepteurs portables et intégrés dans les téléphones mobiles et les voitures. [3]
Au fil des ans, les systèmes GNSS ont connu de nombreuses améliorations et ont été utilisés dans de nombreuses applications, allant de la navigation routière à la localisation de véhicules autonomes en passant par la météorologie et la cartographie. Ils sont également utilisés dans de nombreuses autres industries, comme l'agriculture, les transports, la construction et l'exploration pétrolière. [5]
Les systèmes de Les systèmes de géolocalisation (GNSS) sont de plus en plus présents dans les "villes intelligentes" (smarts cities), et doivent fournir des solutions aux problèmes de stationnement, d'intervention d'urgence et pour les véhicules autonomes [6], par exemple. Pour répondre à ces exigences, de nombreux appareils de géolocalisation ont été déployés et leur nombre a explosé, car presque tout le monde possède un smartphone avec des capteurs GNSS (4,8 millions de puces actives pour smartphone en 2018, selon Ericsson [7]). Cependant, ces derniers semblent peu précis par rapport aux niveaux requis pour ce type d'application dans les villes intelligentes.
Le système étudié sera celui de la géolocalisation par satellite (GNSS, global navigation satellite systems), les sources d'incertitudes sont nombreuses, liées soit au matériel, soit à l'environnement [1], les premières études sur le système GNSS ont été rendues possibles grâce à l'ouverture aux données brutes du système Android par Google en 2016. Avant cela, seules quelques études peu fournies ont pu être réalisées. La précision était de 3 mètres dans les meilleures conditions, et presque 10 mètres dans les pires. En 2016, Yoon et al. [2] ont réalisé une géolocalisation par GNSS différentielle et ont obtenu une augmentation de la précision de 30 à 60%. Jusqu'en mai 2018, les smartphones étaient limités par leur conception et ne pouvaient recevoir qu'une fréquence d'un satellite à la fois. Cependant, Xiaomi a lancé en 2018 un smartphone "dual-band", permettant ainsi l'étude de l'influence de la ionosphère, de réduire l'impact du multipath, etc., et ainsi d'augmenter la précision du système GNSS. En 2019, une étude de Umberto et al. sur l'évaluation des observations de GNSS à double fréquence à partir d'un smartphone Android Xiaomi Mi 8 et analyse des performances de positionnement [4], m'on permis de connaître les démarches nécessaires pour la réalisation de ce TIPE.

## Problématique retenue 
Quels solutions pourrait contribuer significativement à réduire le nombre d'appareils GNSS utilisés permettant une solution plus écologique pour des 
villes intelligentes et durables ?

## Objectifs du TIPE 
1. Etude du GPS, fonctionnement rapide
2. Impact de la ionopshere et des corrections possibles
3. Etude du multipath, dilution géométrique, GPS à double fréquences, et C/N0
4. Comparaison Ville / campagne de la précision.
5. Ouverture, solution possible (SBAS, DGNSS etc.)


## Références bibliographiques (ETAPE 1) 
[1]: https://www.geologie.ens.fr/~ecalais/teaching/geopositionnement-gnss
1: https://www.geologie.ens.fr/~ecalais/teaching/geopositionnement-gnss

[2]: https://www.mdpi.com/1424-8220/16/6/910
2: https://www.mdpi.com/1424-8220/16/6/910

[3]: https://en.wikipedia.org/wiki/Satellite_navigation
3: https://en.wikipedia.org/wiki/Satellite_navigation

[4]: https://www.researchgate.net/publication/330411991_Assessment_of_Dual_Frequency_GNSS_Observations_from_a_Xiaomi_Mi_8_Android_Smartphone_and_Positioning_Performance_Analysis
4: https://www.researchgate.net/publication/330411991_Assessment_of_Dual_Frequency_GNSS_Observations_from_a_Xiaomi_Mi_8_Android_Smartphone_and_Positioning_Performance_Analysis

[5]: https://gssc.esa.int/navipedia/index.php/Category:Applications
5 : https://gssc.esa.int/navipedia/index.php/Category:Applications

[6]: https://gssc.esa.int/navipedia/index.php/Autonomous_Driving
6: https://gssc.esa.int/navipedia/index.php/Autonomous_Driving

[7}: https://www.iotjournaal.nl/wp-content/uploads/2018/06/ericsson-mobility-report-june-2018.pdf
https://www.iotjournaal.nl/wp-content/uploads/2018/06/ericsson-mobility-report-june-2018.pdf

## DOT
1. Compréhension d'un système GNSS,
2. Compréhension de l'impact liée aux perturbation (ionosphere et multipath)
3. Etude et mesure à des signaux, traitement
4. Analyse et conclusion
