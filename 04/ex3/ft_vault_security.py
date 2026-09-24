# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/16 17:41:17 by laveerka        #+#    #+#               #
#  Updated: 2026/09/24 09:54:03 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def secure_archive(file_name: str, mode: str, content: str | None):
    if mode[0] == "r":
        with open(file_name, mode[0]) as f:
            lines = f.read()
            print(lines)
    else:
        with open(file_name, mode[0]) as f:
            
    return (True, "true")


def main():
    print("=== Cyber Archives Security ===\n")
    mode = "read"
    print(f"Using 'secure_archive' to {mode} from a nonexistent file:")
    result: tuple(bool, str) = secure_archive("/not/existing/file", mode, None)
    
    mode = "write"
    print(f"Using 'secure_archive' to {mode} previous content to a new file:")
        

if __name__ == "__main__":
    main()
