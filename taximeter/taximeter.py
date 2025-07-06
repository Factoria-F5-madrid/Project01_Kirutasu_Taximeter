import time


def taximeter():
    """
    Función para manejar y mostrar las opciones del taxímetro.
    """
    print("Welcome to the first project for F5 students: The Taximeter!")
    print("Please, choose one of the next available actions:\n'start', 'stop', 'move', 'finish', 'exit'\n")

    trip_is_active = False # Ningun viaje en marcha
    start_time = 0
    stopped_time = 0 # Reset tiempo detenido
    moving_time = 0 # Reset tiempo en movimiento
    state = None  # 'stopped' o 'moving'
    state_start_time = 0

    while True:
        command = input("Type here your command: > ").strip().lower() # Nos aseguramos que el string sea sin espacios y
        # en lowercase, para poder gestionarlo

        if command == "start":
            if trip_is_active:
                print("Error: A trip is already in progress and cannot start again at this moment.")
                continue
            trip_is_active = True # El viaje ha comenzado
            start_time = time.time()
            stopped_time = 0
            moving_time = 0
            state = 'stopped'  # Iniciamos en estado 'stopped'
            state_start_time = time.time() # Arranca el contador del total del viaje
            print("Trip started. Initial state: 'stopped'.")

        elif command in ("stop", "move"):
            if not trip_is_active:
                print("Error: No active trip. Please start first.")
                continue
            # Calcula el tiempo del estado anterior
            duration = time.time() - state_start_time # Resta el tiempo total menos el tiempo en el estado anterior (por tanto duracion es en movimiento o en parado)
            if state == 'stopped':
                stopped_time += duration # Suma la duracion al tiempo detenido total
            else:
                moving_time += duration # Suma la duracion al tiempo en movimiento total

            # Cambia el estado
            state = 'stopped' if command == "stop" else 'moving'
            state_start_time = time.time()
            print(f"State changed to '{state}'.")

        elif command == "finish":
            if not trip_is_active:
                print("Error: No active trip to finish.")
                continue
            # Agrega tiempo del último estado
            duration = time.time() - state_start_time
            if state == 'stopped':
                stopped_time += duration
            else:
                moving_time += duration

            # Calcula la tarifa total y muestra el resumen del viaje
            total_fare = calculating_fare(stopped_time, moving_time)
            print(f"\n--- Trip Summary ---")
            print(f"Stopped time: {stopped_time:.1f} seconds")
            print(f"Moving time: {moving_time:.1f} seconds")
            print(f"Total fare: €{total_fare:.2f}")
            print("---------------------\n")

            # Reset las variables para el próximo viaje
            trip_is_active = False
            state = None

        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break # detiene el bucle while, aunque se podría usar una flag para hacerla false sin "romperlo"

        else:
            print("Unknown command. Use: start, stop, move, finish, or exit.")

if __name__ == "__main__":
    taximeter()
