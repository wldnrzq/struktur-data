class Map:
    def __init__(self):
        self.cities = {}
        self.roads = {}

    def add_city(self, city_name):
        if city_name not in self.cities:
            self.cities[city_name] = {}
            print(f"Kota {city_name} berhasil ditambahkan.")
        else:
            print("Kota sudah ada.")

    def add_road(self, start_city, end_city, road_name, distance):
        if start_city in self.cities and end_city in self.cities:
            if end_city not in self.cities[start_city]:
                self.cities[start_city][end_city] = distance
                self.roads[(start_city, end_city)] = road_name
                print(f"Jalan dari {start_city} ke {end_city} ({road_name}) berhasil ditambahkan.")
            else:
                print(f"Jalan dari {start_city} ke {end_city} sudah ada.")
        else:
            print("Salah satu atau kedua kota tidak ditemukan.")

    def remove_road(self, start_city, end_city):
        if (start_city, end_city) in self.roads:
            del self.roads[(start_city, end_city)]
            print(f"Jalan dari {start_city} ke {end_city} berhasil dihapus.")
        else:
            print("Jalan tidak ditemukan.")

    def display_cities(self):
        if self.cities:
            print("Kota-kota yang ada:")
            for city in self.cities:
                print("-", city)
        else:
            print("Belum ada kota yang ditambahkan.")

    def display_roads(self):
        if self.roads:
            print("Jalan-jalan yang ada:")
            for road, road_name in self.roads.items():
                print(f"- Dari {road[0]} ke {road[1]} ({road_name}), jarak: {self.cities[road[0]][road[1]]}")
        else:
            print("Belum ada jalan yang ditambahkan.")

    def dijkstra(self, start_city, end_city):
        if start_city in self.cities and end_city in self.cities:
            distances = {city: float('inf') for city in self.cities}
            distances[start_city] = 0
            visited = set()
            while True:
                current_city = min((city for city in distances if city not in visited), key=distances.get)
                visited.add(current_city)
                if current_city == end_city:
                    break
                for neighbor, distance in self.cities[current_city].items():
                    if neighbor not in visited:
                        new_distance = distances[current_city] + distance
                        if new_distance < distances[neighbor]:
                            distances[neighbor] = new_distance
            return distances[end_city]
        else:
            return "Salah satu atau kedua kota tidak ditemukan."


# Inisialisasi objek peta
my_map = Map()

# Menu utama
while True:
    print("\nMenu:")
    print("1. Tambah Kota")
    print("2. Tambah Jalan")
    print("3. Hapus Jalan")
    print("4. Tampilkan Kota-kota")
    print("5. Tampilkan Jalan-jalan")
    print("6. Temukan Jarak Terpendek antar Kota")
    print("7. Keluar")

    choice = input("Pilih menu: ")

    if choice == '1':
        city_name = input("Masukkan nama kota baru: ")
        my_map.add_city(city_name)

    elif choice == '2':
        start_city = input("Masukkan nama kota awal: ")
        end_city = input("Masukkan nama kota tujuan: ")
        road_name = input("Masukkan nama jalan: ")
        distance = float(input("Masukkan jarak antara kota (dalam kilometer): "))
        my_map.add_road(start_city, end_city, road_name, distance)

    elif choice == '3':
        start_city = input("Masukkan nama kota awal: ")
        end_city = input("Masukkan nama kota tujuan: ")
        my_map.remove_road(start_city, end_city)

    elif choice == '4':
        my_map.display_cities()

    elif choice == '5':
        my_map.display_roads()

    elif choice == '6':
        start_city = input("Masukkan nama kota awal: ")
        end_city = input("Masukkan nama kota tujuan: ")
        shortest_distance = my_map.dijkstra(start_city, end_city)
        if isinstance(shortest_distance, float):
            print(f"Jarak terpendek dari {start_city} ke {end_city} adalah {shortest_distance} kilometer.")
        else:
            print(shortest_distance)

    elif choice == '7':
        print("Terima kasih! Sampai jumpa lagi.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
