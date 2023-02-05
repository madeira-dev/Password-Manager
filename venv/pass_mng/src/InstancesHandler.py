class InstancesHandler():
    def __init__(self, instances_arr) -> None:
        self.instances_arr = instances_arr

    def list_instances(instances_arr, owner_id):
        print("#########################")
        for instance in instances_arr:
            if owner_id == instance[0]:
                print("#owner id:", instance[0])
                print("#service id:", instance[1])
                print("#service name:", instance[2])
                print("#username:", instance[3])
                print("#password:", instance[4])

    def add_instance(new_instance, instances_arr):
        new_instance_tuple = (
            new_instance.owner_id, new_instance.service_id, new_instance.service_name, new_instance.service_username, new_instance.service_password)
        instances_arr.append(new_instance_tuple)

    def remove_instance(instance_id, instances_arr, owner_id):
        for instance in instances_arr:
            if instance[1] == instance_id and owner_id == instance[0]:
                instances_arr.remove(instance)

    def modify_instance(service_name, instances_arr, owner_id):
        for instance in instances_arr:
            if instance[2] == service_name and owner_id == instance[0]:
                target_instance = instance
                print("target: ", target_instance)
                break

        print("""which field you want to change?
        1. service name
        2. username
        3. password""")

        modification = int(input("type the option number: "))

        if modification == 1:
            new_service_name = str(input("type the new service name: "))
            tmp_target = list(target_instance)
            tmp_target[1] = new_service_name
            print("tmp_target: ", tmp_target)
            target_instance = tuple(tmp_target)
            print("target updated: ", target_instance)

        elif modification == 2:
            new_service_username = str(input("type the new username: "))
            tmp_target = list(target_instance)
            tmp_target[2] = new_service_username
            target_instance = tuple(tmp_target)

        elif modification == 3:
            new_service_password = str(input("type the new password: "))
            tmp_target = list(target_instance)
            tmp_target[3] = new_service_password
            target_instance = tuple(tmp_target)

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
