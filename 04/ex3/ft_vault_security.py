# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/09/16 17:41:17 by laveerka        #+#    #+#               #
#  Updated: 2026/09/24 11:44:20 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def secure_archive(file_name: str, mode: str,
                   content: str | None) -> tuple[bool, str]:
    """Reading or writing while handling files using 'with'"""
    if mode[0] == "r":
        try:
            with open(file_name, "r") as f:
                lines = f.read()
                return (True, lines)
        except (FileNotFoundError, PermissionError) as e:
            return (False, str(e))
    else:
        try:
            with open(file_name, "w") as f:
                if content:
                    f.write(content)
                    return (True, content)
                else:
                    return (False, "Nothing to write")
        except (PermissionError) as e:
            return (False, str(e))


def main() -> None:
    """Main to report on file reading and writing"""
    print("=== Cyber Archives Security ===\n")
    mode = "read"
    print(f"Using 'secure_archive' to {mode} from a nonexistent file:")
    result_non_existing: tuple[bool, str] = secure_archive(
        "/not/existing/file", mode, None)
    success_0, message_0 = result_non_existing
    print(f"({success_0}, \"{message_0}\")\n")
    print(f"Using 'secure_archive' to {mode} from an inaccessible file:")
    result_inaccessible: tuple[bool, str] = secure_archive(
        "no_perm.txt", mode, None)
    success_1, message_1 = result_inaccessible
    print(f"({success_1}, \"{message_1}\")\n")
    print(f"Using 'secure_archive' to {mode} from a regular file:")
    result_regular: tuple[bool, str] = secure_archive(
        "ancient_fragment.txt", mode, None)
    success_2, message_2 = result_regular
    print(f"({success_2}, '{message_2}')\n")
    mode = "write"
    print(f"Using 'secure_archive' to {mode} previous content to a new file:")
    result_writing: tuple[bool, str] = secure_archive(
        "new_file.txt", mode, "Content successfully written to file")
    success_3, message_3 = result_writing
    print(f"({success_3}, '{message_3}')")


if __name__ == "__main__":
    main()
