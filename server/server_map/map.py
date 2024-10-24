class Map:
    def __init__(self, locations: list, connections: list):
        self.locations = locations
        self.connections = connections

    def add_new_location(self, unique_name, name, data):
        self.locations.append([unique_name, name, data])

    def add_new_connection(self, unique_name, first_location, second_location, data):
        first_location_exist = False
        second_location_exist = False

        for connection in self.connections:
            if connection[0] == unique_name:
                return False, "Error: this connection already exist"

        if first_location == second_location:
            return False, "Error: same locations"

        for location in self.locations:
            if location[0] == first_location:
                first_location_exist = True
            if location[0] == second_location:
                second_location_exist = True

        if not first_location_exist and second_location_exist:
            return False, "Error: one or both locations dont exist"

        self.connections.append([unique_name, first_location, second_location, data])
        return True, "Successfully added new connection"

    def find_location(self, location_unique_name):
        location_exist = False
        location_id = None
        location = []

        for index, i in enumerate(self.locations):
            if i[0] == location_unique_name:
                location_exist = True
                location = i
                location_id = index
                break

        return location_exist, location_id, location

    def find_connection(self, connection_unique_name):
        connection_exist = False
        connection_id = None
        connection = []

        for index, i in enumerate(self.locations):
            if connection_unique_name == i[0]:
                connection_exist = True
                connection = i
                connection_id = index
                break

        return connection_exist, connection_id, connection

    def edit_location_data(self, location_unique_name, new_data):
        result, id, location = self.find_location(location_unique_name)
        if not result:
            return False, None
        self.locations[id][2] = new_data
        return True, id

    def edit_connection_data(self, connection_unique_name, new_data):
        result, id, connection = self.find_connection(connection_unique_name)
        if not result:
            return False, None
        self.connections[id][3] = new_data
        return True, id

    def find_all_location_connections(self, location_unique_name):
        result, id, location = self.find_location(location_unique_name)
        if not result:
            return False, []

        connections = []
        for connection in self.connections:
            if (connection[1] == location_unique_name) or (connection[2] == location_unique_name):
                connections.append(connection)

        return True, connections
