from textnode import TextNode, TextType
from htmlnode import HTMLNode
import os
import shutil

def main():
    def copy_to_public(source, dest):
        if os.path.exists(dest):
            print(f"Deleting existing {dest}")
            shutil.rmtree(dest)
        
        if not os.path.exists(dest):
            print(f"Creating new {dest}")
            os.mkdir(dest)
        
        copy_items(source, dest)


    def copy_items(source, dest):
        list = os.listdir(source)
        for item in list:
            if os.path.isfile(os.path.join(source, item)):
                print(f"Copying {item} from {source} to {dest}")
                shutil.copy(os.path.join(source, item), dest)
            else:
                print(f"Making directory {item} at {dest}")
                os.mkdir(os.path.join(dest, item))
                new_dest = os.path.join(dest, item)
                new_source = os.path.join(source,item)
                copy_items(new_source, new_dest)
            


    source = "./static"
    dest = "./public"

    copy_to_public(source, dest)

if __name__ == "__main__":
    main()