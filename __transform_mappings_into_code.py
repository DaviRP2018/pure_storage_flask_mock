"""
This script was used for initial code writting and shouldn't be needed anymore.

It has the capability to read JSON files inside a "mappings" folder and transform them into
initial Python files for coding
"""
import ast
import json
import os

output_file_path = "generated_resources.py"
mappings_folder = "mappings"  # change to your folder path

with open(output_file_path, "w") as output_file:
    output_file.write("from flask_restful import Resource\n\n")

    class_index = 0

    # Iterate through JSON files in the mappings folder
    for filename in os.listdir(mappings_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(mappings_folder, filename)

            with open(file_path, "r") as file:
                data = json.load(file)

            class_name = "Resource{}".format(
                "".join(
                    word.title()
                    for word in data.get("name", "nameless").split("_")
                    if not word.isnumeric()
                )
            )
            method = data["request"]["method"].lower()

            output_file.write(f"class {class_name}(Resource):\n")

            url = data["request"]["url"]
            status_code = data["response"]["status"]
            response_body = data["response"]["body"]

            output_file.write(f"    def {method}(self):\n")
            output_file.write("        # Custom code goes here\n")
            try:
                ast.literal_eval(response_body)
                output_file.write(f"        return {response_body}, {status_code}\n\n")
            except (ValueError, SyntaxError):
                output_file.write(f"        return '{response_body}', {status_code}\n\n")

            api_route = f'api.add_resource({class_name}, "{url}")\n'
            output_file.write(api_route)

            output_file.write("\n")
            class_index += 1
