# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/16 17:41:12 by laveerka        #+#    #+#               #
#  Updated: 2026/09/20 16:13:53 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def read_file(file_name: str) -> str | None:
    try:
        f = open(file_name, "r")
        print("---\n")
        content = f.read()
        print(content)
        print("\n---")
        f.close()
        print(f"File '{file_name}', closed.\n")
        return content
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file_name}': {e}")
        return None


def transform_data(content: str) -> str:
    print("Transform data:\n---\n")
    lines = content.split("\n")
    tagged = [line + "#" for line in lines]
    return "\n".join(tagged)


def save_data(tagged: str) -> None:
    file_name = input("Enter new file name (or empty): ")
    if file_name:
        print(f"Saving data to '{file_name}'")
        f = open(file_name, "w")
        f.write(tagged)
        f.close()
        print(f"Data saved in file '{file_name}'")
    else:
        print("Not saving data.")


def main():
    args = sys.argv
    if len(args) == 2:
        print("==== Cyber Archives Recovery ===")
        file_name = args[1]
        print(f"Accessing file '{file_name}'")
        content = read_file(file_name)          
        if content:
            tagged = transform_data(content)
            print(f"{tagged}")
            print("\n---")
            save_data(tagged)
    else:
        print("Usage: ft_ancient_text.py <file>")

if __name__== "__main__":
    main()
