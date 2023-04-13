# List
list_of_cloud = ["AWS", "Azure", "GCP", "Oracle"]
# print(list_of_cloud)
# print(list_of_cloud[1])
list_of_cloud.append("Linode")
print(list_of_cloud)

# Dictionary
dict_of_cloud = {
    "aws": "Amazon Web Services",
    "azure": "Microsoft Azure",
    "gcp": "Google Cloud Platform",
}
# print(dict_of_cloud)
# print(dict_of_cloud["gcp"])
# print(dict_of_cloud.get("azure"))
# print(dict_of_cloud.get("oracle", "Not found"))
# dict_of_cloud.update({"linode": "Linod Cloud"})
# print(dict_of_cloud)

fav_tools = {
    1: "Linux",
    2: "Git",
    3: "Docker",
    4: "Kubernetes",
    5: "Terraform",
    6: "Ansible",
    7: "Chef"
}
# print(fav_tools[3])
# print(fav_tools.get(1))
