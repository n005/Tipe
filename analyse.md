## Première Analyse des fichers RINEX et NMEA:

### 1. Récupération des phases du sat. G30 (ici) (Fichier RINEX):  

![](https://github.com/n005/Tipe/blob/main/images/L1_G30.png?raw=true)

![](https://github.com/n005/Tipe/blob/main/images/L5_G30.png?raw=true)

### 2. Calcul du TEC [1]:  
* $sTEC_{L_1L_5} = \frac{1}{K}\frac{f_1^2f_5^2}{f_1^2-f_5^2}(L_1\lambda_1 - L_5\lambda_5)$:  

![](https://github.com/n005/Tipe/blob/main/images/TEC_G30.png?raw=true)

[1]: https://iopscience.iop.org/article/10.1088/1742-6596/1991/1/012025/pdf

### 3. A l'aide du fichier NMEA, calcul de la position:  

![](https://github.com/n005/Tipe/blob/main/images/Position.png?raw=true)

### 4. Evaluation de la variation:   

![](https://github.com/n005/Tipe/blob/main/images/RSD.png?raw=true)

### 5. Evaluation de l'impact des batiments sur l'amplitude de la variation de la speudo-range (ici campagne):  

![](https://github.com/n005/Tipe/blob/main/images/DSR_G30.png?raw=true)

### 6. Analyse du multipath:  

![](https://github.com/n005/Tipe/blob/main/images/MP_error.png?raw=true)  

![](https://github.com/n005/Tipe/blob/main/images/MP_dist.png?raw=true)
