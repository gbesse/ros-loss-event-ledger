# ros-loss-event-ledger

## Français

Additionner les pertes ROS incrémentales sans inventer les silences.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m ros_loss_event_ledger examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Les événements rosbag2 de pertes sont incrémentaux et omettent les sujets à zéro ; ce registre additionne, déduplique par identifiant externe et refuse une couverture complète lors d’un conflit.

### Limites

Export JSON normalisé, pas d’abonnement ROS actif. Identifiants et complétude fournis par collecteur ; des pertes non observées restent inconnues.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Accumulate incremental ROS losses without inventing silent intervals.

Synthetic data; no network access or secret required.

```sh
python -m ros_loss_event_ledger examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

rosbag2 loss events are incremental and omit zero-loss topics; this ledger adds, deduplicates by external identifier and rejects complete coverage on conflict.

### Limits

Normalized JSON export, not a live ROS subscription. IDs and completeness supplied by collector; unobserved losses remain unknown.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Acumular pérdidas ROS incrementales sin inventar intervalos silenciosos.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m ros_loss_event_ledger examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Eventos de pérdida rosbag2 son incrementales y omiten temas con cero; este registro suma, deduplica por identificador externo y rechaza cobertura completa con conflictos.

### Límites

Exportación JSON normalizada, no suscripción ROS activa. Identificadores y completitud aportados por colector; pérdidas no observadas desconocidas.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/ros2/rosbag2#statistics-about-lost-messages
