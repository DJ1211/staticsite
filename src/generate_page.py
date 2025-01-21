import os
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            title = line[1:]
            return title.strip()
    raise Exception("Error: No h1 title found in markdown")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not os.path.exists(from_path):
        raise Exception(f"Source file at {from_path} not found")
    with open(from_path) as file:
        content_data = file.read()
        html_node = markdown_to_html_node(content_data)
        html_string = html_node.to_html()
        title = extract_title(content_data)
    
    if not os.path.exists(template_path):
        raise Exception(f"Template file at {template_path} not found")
    with open(template_path) as file:
        template_data = file.read()
        print(f"Replacing Title with {title}")
        template_data = template_data.replace("{{ Title }}", title)
        print(f"Replacing content with {html_string[:50]}")
        template_data = template_data.replace("{{ Content }}", html_string)

    directory = os.path.dirname(dest_path)
    os.makedirs(directory, exist_ok=True)    
    
    with open(dest_path, 'w') as output_file:
        output_file.write(template_data)
        print(f"Page successfully generated and written to {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    directory_list = os.listdir(dir_path_content)
    for item in directory_list:
        if os.path.isfile(os.path.join(dir_path_content, item)):
            if item.endswith(".md"):
                from_path = os.path.join(dir_path_content, item)
                dest_item = item.replace(".md", ".html")
                dest_path = os.path.join(dest_dir_path, dest_item)
                generate_page(from_path, template_path, dest_path)
            else:
                print(f"{item} is not a markdown file")
        else:
            new_dir_path_content = os.path.join(dir_path_content, item)
            new_dest_dir_path = os.path.join(dest_dir_path, item)
            generate_pages_recursive(new_dir_path_content, template_path, new_dest_dir_path)
