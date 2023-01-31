# Etudes des système GNSS des smartphones.
J'ai choisi ce sujet car il permet de comprendre à la fois les phénomènes physiques et le traitement numérique, deux domaines qui m'intéressent particulièrement, et également de tenter de résoudre une problématique de positionnement par satellites de plus en plus cruciale avec l'arrivée massive d'appareils connectés (IoT).

Ce sujet se rapporte à la ville car, en plus de l'impact de l'urbanisation sur les signaux, la précision des systèmes GNSS (Global Navigation Satellite System) doit devenir de plus en plus importante (par exemple pour les voitures autonomes ou pour faciliter la navigation dans un environnement complexe).
## Positionnement thématique (ETAPE 1) 

*INFORMATIQUE (Technologies informatiques); SCIENCES INDUSTRIELLES(Électronique); PHYSIQUE(Physique Interdisciplinaire).*

## Mots-clés (ETAPE 1)  (ANGLAIS)
* GNSS (Global Navigation Satellite System),  
* Ionosphere,
* Dual-Band GNSS,
* Programming,
* Modelization,

## Mots-clés (ETAPE 1) 
* Système de positionnement par satellites,
* Ionosphère,
* GNSS bi-bande,
* Programmation,
* Modélisation,


## Bibliographie commentée 

Le système GNSS (Global Navigation Satellite System) est un système de géolocalisation qui utilise des satellites en orbite autour de la Terre pour permettre à des appareils sur le sol de déterminer leur position, leur vitesse et l'heure avec une très grande précision. Les systèmes GNSS les plus connus sont le GPS (Global Positioning System) des États-Unis, le GLONASS (Global Navigation Satellite System) de la Russie, le Galileo de l'Union Européenne et le BeiDou de la Chine.
Le concept de GNSS a été développé dans les années 1950, mais le premier système opérationnel, le GPS, n'a été mis en place qu'au début des années 1980.
Au départ, le GPS était principalement utilisé par l'armée américaine, mais il est rapidement devenu accessible au grand public grâce à la diffusion de récepteurs portables et intégrés dans les téléphones mobiles et les voitures. [1]  
Au fil des ans, les systèmes GNSS ont connu de nombreuses améliorations et ont été utilisés dans de nombreuses applications, allant de la navigation routière à la localisation de véhicules autonomes en passant par la météorologie et la cartographie. Ils sont également utilisés dans de nombreuses autres industries, comme l'agriculture, les transports, la construction et l'exploration pétrolière. [2]  
Les systèmes de Les systèmes de géolocalisation (GNSS) sont de plus en plus présents dans les "villes intelligentes" (smarts cities), et doivent fournir des solutions aux problèmes de stationnement, d'intervention d'urgence et pour les véhicules autonomes, par exemple [3]. Pour répondre à ces exigences, de nombreux appareils de géolocalisation ont été déployés et leur nombre a explosé, car presque tout le monde possède un smartphone avec des capteurs GNSS (4,8 millions de puces actives pour smartphone en 2018, selon Ericsson [4]). Cependant, ces derniers semblent peu précis par rapport aux niveaux requis pour ce type d'application dans les villes intelligentes.  
Le système étudié sera celui de la géolocalisation par satellite (GNSS, global navigation satellite systems), les sources d'incertitudes sont nombreuses, liées soit au matériel, soit à l'environnement [5], les premières études sur le système GNSS ont été rendues possibles grâce à l'ouverture aux données brutes du système Android par Google en 2016. Avant cela, seules quelques études peu fournies ont pu être réalisées. La précision était de 3 mètres dans les meilleures conditions, et presque 10 mètres dans les pires. En 2016, Yoon et al. [6] ont réalisé une géolocalisation par GNSS différentielle et ont obtenu une augmentation de la précision de 30 à 60%. Jusqu'en mai 2018, les smartphones étaient limités par leur conception et ne pouvaient recevoir qu'une fréquence d'un satellite à la fois.  
Cependant, en 2018, Xiaomi a lancé un smartphone équipé d'un système "dual-band" (deux signaux GNSS à deux fréquences différentes reçus d'un même satellite), ce qui a permis d'étudier l'influence de la ionosphère (couche de l'atmosphère ionisée), de réduire l'impact du multipath (interférence générée lorsqu'un signal arrive à l'antenne par différentes voies), etc. et ainsi d'augmenter la précision du système GNSS. En 2019, une étude de Umberto et al. sur l'évaluation des observations GNSS à double fréquence réalisées avec un smartphone Android Xiaomi Mi 8, ainsi que l'analyse de ses performances de positionnement [7], m'ont permis de mieux comprendre les étapes nécessaires pour la réalisation de ce TIPE. Pour étudier plus particulièrement l'impact de l'urbanisation sur ces systèmes.

## Problématique retenue 
Comment peut-on réduire l'impact de l'urbanisation sur les systèmes GNSS pour améliorer la précision de la géolocalisation par satellite ?

## Objectifs du TIPE 
1. Etude du GPS, fonctionnement rapide
2. Impact de la ionopshere et des corrections possibles
3. Etude du multipath, dilution géométrique, GPS à double fréquences, et C/N0
4. Comparaison Ville / campagne de la précision.
5. Ouverture, solution possible (SBAS (systèmes d'optimisation de la précision par satellite), DGNSS (GNSS Différentiel) etc.)


## Références bibliographiques (ETAPE 1) 

Wikipédia, Géo positionnement par satellite.  

[1]: https://en.wikipedia.org/wiki/Satellite_navigation
1: https://en.wikipedia.org/wiki/Satellite_navigation

ESA, Application du GNSS  

[2]: https://gssc.esa.int/navipedia/index.php/Category:Applications
2: https://gssc.esa.int/navipedia/index.php/Category:Applications

ESA, Conduite autonome  

[3]: https://gssc.esa.int/navipedia/index.php/Autonomous_Driving
3: https://gssc.esa.int/navipedia/index.php/Autonomous_Driving

Ericsson, Mobility Report  

[4]: https://www.iotjournaal.nl/wp-content/uploads/2018/06/ericsson-mobility-report-june-2018.pdf
4: https://www.iotjournaal.nl/wp-content/uploads/2018/06/ericsson-mobility-report-june-2018.pdf

ENS, Cours de géo positionnement par satellite  

[5]: https://www.geologie.ens.fr/~ecalais/teaching/geopositionnement-gnss
5: https://www.geologie.ens.fr/~ecalais/teaching/geopositionnement-gnss

Donghwan Yoon, Changdon Kee, Jiwon Seo and Byungwoon Park, Position Accuracy Improvement by Implementing the
DGNSS-CP Algorithm in Smartphones, MDPI Sensors 2016  

[6]: https://www.mdpi.com/1424-8220/16/6/910
6: https://www.mdpi.com/1424-8220/16/6/910

Umberto Robustelli, Valerio Baiocchi and Giovanni Pugliano, Assessment of Dual Frequency GNSS Observations
from a Xiaomi Mi 8 Android Smartphone and
Positioning Performance Analysis, MDPI Electronics 2019  

[7]: https://www.researchgate.net/publication/330411991_Assessment_of_Dual_Frequency_GNSS_Observations_from_a_Xiaomi_Mi_8_Android_Smartphone_and_Positioning_Performance_Analysis
7: https://www.researchgate.net/publication/330411991_Assessment_of_Dual_Frequency_GNSS_Observations_from_a_Xiaomi_Mi_8_Android_Smartphone_and_Positioning_Performance_Analysis


## DOT
1. Compréhension d'un système GNSS,
2. Compréhension de l'impact liée aux perturbation (ionosphere et multipath)
3. Etude et mesure à des signaux, traitement
4. Analyse et conclusion
