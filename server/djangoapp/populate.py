from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(
            CarMake.objects.create(
                name=data['name'],
                description=data['description']
                ))

    # Create CarModel instances with the corresponding CarMake instances
    c0 = car_make_instances[0]
    c1 = car_make_instances[1]
    c2 = car_make_instances[2]
    c3 = car_make_instances[3]
    c4 = car_make_instances[4]
    car_model_data = [
      {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": c0},
      {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": c0},
      {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": c0},
      {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": c1},
      {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": c1},
      {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": c1},
      {"name": "A4", "type": "SUV", "year": 2023, "car_make": c2},
      {"name": "A5", "type": "SUV", "year": 2023, "car_make": c2},
      {"name": "A6", "type": "SUV", "year": 2023, "car_make": c2},
      {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": c3},
      {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": c3},
      {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": c3},
      {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": c4},
      {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": c4},
      {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": c4},
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data['name'],
            car_make=data['car_make'],
            type=data['type'],
            year=data['year']
            )
