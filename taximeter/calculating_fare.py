def calculating_fare(secs_stopped, secs_moving):
    """
    Este metodo/funcion calcula la tarifa total en euros.
    - Stopped: 0.02 €/s
    - Moving: 0.05 €/s
    """
    fare = secs_stopped * 0.02 + secs_moving * 0.05
    print(f"El importe total a abonar es de: {fare} €")
    return fare
