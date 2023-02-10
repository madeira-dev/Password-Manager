class InstancesHandler():
    def __init__(self, instances_arr) -> None:
        self.instances_arr = instances_arr

    def list_instances(instances_arr, owner_id):
        print("")
        for instance in instances_arr:
            if owner_id == instance[0]:
                print("#########################")
                print("#")
                print("# owner id:", instance[0])
                print("# service id:", instance[1])
                print("# service name:", instance[2])
                print("# username:", instance[3])
                print("# password:", instance[4])
                print("#")
                print("#########################\n")

    def add_instance(new_instance, instances_arr):
        new_instance_tuple = (
            new_instance.owner_id, new_instance.service_id, new_instance.service_name, new_instance.service_username, new_instance.service_password)
        instances_arr.append(new_instance_tuple)
        print(f"\n->new instance for {new_instance.service_name} added<-")

    def remove_instance(instance_id, instances_arr, owner_id):
        for instance in instances_arr:
            if str(instance[0]) == str(owner_id) and str(instance_id) == str(instance[1]):
                print("inside if")
                instances_arr.remove(instance)
                print(f"->{instance[2]} instance removed<-")

    def modify_instance(service_id, instances_arr, owner_id):
        for instance in instances_arr:
            if instance[1] == service_id and owner_id == instance[0]:
                target_instance = instance
                print("target: ", target_instance)
                break

        print("""
        1. service name
        2. username
        3. password""")

        modification = int(input("type the option number to change: "))

        if modification == 1:
            new_service_name = str(input("type the new service name: "))
            for index, instance in enumerate(instances_arr):
                instance_list = list(instance)
                if instance_list[1] == service_id:
                    instance_list[2] = new_service_name
                instance = tuple(instance_list)
                instances_arr[index] = instance

        elif modification == 2:
            new_service_username = str(input("type the new username: "))
            for index, instance in enumerate(instances_arr):
                instance_list = list(instance)
                if instance_list[1] == service_id:
                    instance_list[3] = new_service_username
                instance = tuple(instance_list)
                instances_arr[index] = instance

        elif modification == 3:
            new_service_password = str(input("type the new password: "))
            for index, instance in enumerate(instances_arr):
                instance_list = list(instance)
                if instance_list[1] == service_id:
                    instance_list[4] = new_service_password
                instance = tuple(instance_list)
                instances_arr[index] = instance

        else:
            # make a proper error handling
            print("invalid number")
            return
# probably delete this search method, not using

    def search_instance(instance_id, instances_arr):
        for instance in instances_arr:
            if instance[0] == instance_id:
                searched_instance = instance
                break
        return searched_instance

    def update_db(connection, instances_arr):
        conn_cur = connection.cursor()
        conn_cur.execute("DELETE FROM instances;")
        connection.commit()

        for instance in instances_arr:
            conn_cur.execute("INSERT INTO instances VALUES (?, ?, ?, ?, ?)",
                             (instance[0], instance[1], instance[2], instance[3], instance[4]))
            connection.commit()
