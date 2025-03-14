# Algorithm Details

This document details the core algorithms used in the Driver Fatigue Monitoring System, including the calculation of EAR, MAR, and head pose estimation.

## 1. Eye Aspect Ratio (EAR)
### Objectif:
Mesurer l'ouverture des yeux pour détecter leur fermeture prolongée.
### Formule:
\[
EAR = \frac{\|P2 - P6\| + \|P3 - P5\|}{2 \times \|P1 - P4\|}
\]
- **P1 à P6** représentent les points clés de l'œil.
### Étapes:
1. Calculer la distance verticale entre P2 et P6.
2. Calculer la distance verticale entre P3 et P5.
3. Calculer la distance horizontale entre P1 et P4.
4. Retourner le ratio calculé.


## 2. Mouth Aspect Ratio (MAR)
### Objectif:
Mesurer l'ouverture de la bouche pour détecter les bâillements.
### Formule:
\[
MAR = \frac{\|P3 - P7\| + \|P2 - P6\|}{2 \times \|P0 - P4\|}
\]
- **P0 à P7** représentent les points clés autour de la bouche.
### Étapes:
1. Calculer la distance verticale entre P3 et P7.
2. Calculer la distance verticale entre P2 et P6.
3. Calculer la distance horizontale entre P0 et P4.
4. Retourner le ratio calculé.
### Pseudocode:


## 3. Head Pose Estimation
### Objectif:
Estimer l'orientation de la tête (pitch, yaw, roll) pour détecter les inclinaisons associées à la fatigue.
### Méthode:
- Sélectionner les points d'intérêt (bout du nez, menton, coins des yeux et de la bouche).
- Utiliser OpenCV `solvePnP` pour résoudre la correspondance entre les points 3D du modèle générique et les points 2D de l'image.
### Étapes:
1. Extraire les points 2D d'intérêt à partir des landmarks.
2. Définir les points 3D correspondants (modèle du visage).
3. Définir la matrice de la caméra et les coefficients de distorsion.
4. Appliquer `solvePnP` pour obtenir le vecteur de rotation et de translation.
5. Projeter un point 3D lointain pour visualiser la direction du nez.
### Pseudocode:


## 4. Conversion de la Matrice de Rotation en Angles d'Euler
### Objectif:
Convertir la matrice de rotation obtenue par solvePnP en angles d'Euler (yaw, pitch, roll) pour une interprétation plus intuitive.
### Étapes:
1. Calculer `sy` (pour détecter une situation singulière).
2. Si non singulier, calculer roll, pitch et yaw avec atan2.
3. Sinon, appliquer une formule alternative et fixer le yaw à 0.
### Pseudocode:


