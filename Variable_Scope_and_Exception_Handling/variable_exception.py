class LocationManager:
    def __init__(self):
        self.countries = {}

    def create(self):
        while True:
            country = input("Enter a country name (must not be blank): ").strip()
            if not country:
                print("Country name cannot be blank. Please try again.")
                continue
            if country not in self.countries:
                self.countries[country] = {"states": {}}
            print(f"Country '{country}' added successfully.")

            while True:
                state = input("Enter a state name (must not be blank): ").strip()
                if not state:
                    print("State name cannot be blank. Please try again.")
                    continue

                while True:
                    print("Available countries:", list(self.countries.keys()))
                    country_association = input(f"Associate state '{state}' with a country: ").strip()
                    if country_association not in self.countries:
                        print("Invalid country. Please select a valid country from the list.")
                    else:
                        self.countries[country_association]["states"][state] = {"cities": []}
                        break

                print(f"State '{state}' added to {country_association}.")
                another_state = input("Do you want to enter another state? Y/N: ").strip().upper()
                if another_state != 'Y':
                    break

            while True:
                city = input("Enter a city name (must not be blank): ").strip()
                if not city:
                    print("City name cannot be blank. Please try again.")
                    continue

                while True:
                    print(f"Available states for association: {list(self.countries[country_association]['states'].keys())}")
                    state_association = input(f"Associate city '{city}' with a state: ").strip()
                    if state_association not in self.countries[country_association]["states"]:
                        print("Invalid state. Please select a valid state from the list.")
                    else:
                        self.countries[country_association]["states"][state_association]["cities"].append(city)
                        break

                print(f"City '{city}' added to state '{state_association}'.")
                another_city = input("Do you want to enter another city? Y/N: ").strip().upper()
                if another_city != 'Y':
                    break

            another_country = input("Do you want to enter another country? Y/N: ").strip().upper()
            if another_country != 'Y':
                break

    def update(self):
        while True:
            print("1. Update Country")
            print("2. Update State")
            print("3. Update City")
            choice = input("Select an option (1, 2, or 3): ").strip()
            
            try:
                if choice == '1':
                    self.update_country()
                elif choice == '2':
                    self.update_state()
                elif choice == '3':
                    self.update_city()
                else:
                    print("Invalid choice. Please select a valid option.")
                    continue
            except Exception as e:
                print(f"Error: {e}")
            break

    def update_country(self):
        print("Available countries:", list(self.countries.keys()))
        country_to_update = input("Select a country to update: ").strip()
        if country_to_update in self.countries:
            new_name = input(f"Enter a new name for country '{country_to_update}': ").strip()
            self.countries[new_name] = self.countries.pop(country_to_update)
            print(f"Country '{country_to_update}' updated to '{new_name}'.")
        else:
            print(f"Country '{country_to_update}' not found.")

    def update_state(self):
        country = input("Enter the country name to update state: ").strip()
        if country in self.countries:
            print("Available states:", list(self.countries[country]["states"].keys()))
            state_to_update = input("Select a state to update: ").strip()
            if state_to_update in self.countries[country]["states"]:
                new_state = input(f"Enter a new name for state '{state_to_update}': ").strip()
                self.countries[country]["states"][new_state] = self.countries[country]["states"].pop(state_to_update)
                print(f"State '{state_to_update}' updated to '{new_state}'.")
            else:
                print(f"State '{state_to_update}' not found.")
        else:
            print(f"Country '{country}' not found.")

    def update_city(self):
        country = input("Enter the country name to update city: ").strip()
        if country in self.countries:
            state = input("Enter the state name to update city: ").strip()
            if state in self.countries[country]["states"]:
                print("Available cities:", self.countries[country]["states"][state]["cities"])
                city_to_update = input("Select a city to update: ").strip()
                if city_to_update in self.countries[country]["states"][state]["cities"]:
                    new_city = input(f"Enter a new name for city '{city_to_update}': ").strip()
                    self.countries[country]["states"][state]["cities"].remove(city_to_update)
                    self.countries[country]["states"][state]["cities"].append(new_city)
                    print(f"City '{city_to_update}' updated to '{new_city}'.")
                else:
                    print(f"City '{city_to_update}' not found.")
            else:
                print(f"State '{state}' not found.")
        else:
            print(f"Country '{country}' not found.")

    def delete(self):
        while True:
            print("1. Delete Country")
            print("2. Delete State")
            print("3. Delete City")
            choice = input("Select an option (1, 2, or 3): ").strip()

            try:
                if choice == '1':
                    self.delete_country()
                elif choice == '2':
                    self.delete_state()
                elif choice == '3':
                    self.delete_city()
                else:
                    print("Invalid choice. Please select a valid option.")
                    continue
            except Exception as e:
                print(f"Error: {e}")
            break

    def delete_country(self):
        print("Available countries:", list(self.countries.keys()))
        country_to_delete = input("Select a country to delete: ").strip()
        if country_to_delete in self.countries:
            confirm = input(f"Are you sure you want to delete country '{country_to_delete}' and all its states and cities? Y/N: ").strip().upper()
            if confirm == 'Y':
                del self.countries[country_to_delete]
                print(f"Country '{country_to_delete}' deleted along with all states and cities.")
            else:
                print("Deletion aborted.")
        else:
            print(f"Country '{country_to_delete}' not found.")

    def delete_state(self):
        country = input("Enter the country name to delete state: ").strip()
        if country in self.countries:
            print("Available states:", list(self.countries[country]["states"].keys()))
            state_to_delete = input("Select a state to delete: ").strip()
            if state_to_delete in self.countries[country]["states"]:
                confirm = input(f"Are you sure you want to delete state '{state_to_delete}' and all its cities? Y/N: ").strip().upper()
                if confirm == 'Y':
                    del self.countries[country]["states"][state_to_delete]
                    print(f"State '{state_to_delete}' deleted along with all its cities.")
                else:
                    print("Deletion aborted.")
            else:
                print(f"State '{state_to_delete}' not found.")
        else:
            print(f"Country '{country}' not found.")

    def delete_city(self):
        country = input("Enter the country name to delete city: ").strip()
        if country in self.countries:
            state = input("Enter the state name to delete city: ").strip()
            if state in self.countries[country]["states"]:
                print("Available cities:", self.countries[country]["states"][state]["cities"])
                city_to_delete = input("Select a city to delete: ").strip()
                if city_to_delete in self.countries[country]["states"][state]["cities"]:
                    confirm = input(f"Are you sure you want to delete city '{city_to_delete}'? Y/N: ").strip().upper()
                    if confirm == 'Y':
                        self.countries[country]["states"][state]["cities"].remove(city_to_delete)
                        print(f"City '{city_to_delete}' deleted.")
                    else:
                        print("Deletion aborted.")
                else:
                    print(f"City '{city_to_delete}' not found.")
            else:
                print(f"State '{state}' not found.")
        else:
            print(f"Country '{country}' not found.")

def main():
    location_manager = LocationManager()

    while True:
        print("\n1. Create")
        print("2. Update")
        print("3. Delete")
        print("4. Exit")

        try:
            choice = input("Select an option (1, 2, 3, or 4): ").strip()

            if choice == '1':
                location_manager.create()
            elif choice == '2':
                location_manager.update()
            elif choice == '3':
                location_manager.delete()
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                print("Invalid input. Please select a valid option.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
