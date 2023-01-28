import Instance as it


class InstancesHandler():
    def __init__(self, **kwargs) -> None:
        instances_arr = kwargs.get("instances_arr", None)
        pass

    def list_instances():
        print("-list instances selected-")

    def add_instance(service_id, service_name, service_username, service_password):
        new_instance = it.Instance(
            service_id, service_name, service_username, service_password)
        print("\nservice id:", service_id, "\nservice name: ", new_instance.service_name, "\nusername: ", new_instance.service_username,
              "\npassword: ", new_instance.service_password)
        print("-add instance selected-")
        # add to instances_arr

    def remove_instance(id):
        print("instance id: ", id)
        print("-remove instance selected-")

    def modify_instance():
        print("-modify instance selected-")
