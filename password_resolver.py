import argparse
import os

def get_all_environ_dict():
    """
    Get all environment variables as dict.
    
    Returns
    -------
    dict<str, str>
        key: env key (ALL UPPERCASE)
        value: env value
    """
    ret = {}
    for key in os.environ:
        ret[key] = os.environ[key]
    return ret


def main(hint_str):
    """
    Main method
    
    Parameters
    ----------
    hint_str : str
        password hint string
    """
    env_dict = get_all_environ_dict()
    for key in env_dict:
        try:
            exec(f"{key} = \"{env_dict[key]}\"")
        except SyntaxError:
            continue
    exec(f"print({hint_str})")


if __name__ == "__main__":
    # Configure argument parser
    parser = argparse.ArgumentParser(description="Get your password depends on environment variables")
    parser.add_argument("arg1", help="String you want to convert to correct password", type=str)
    args = parser.parse_args()

    main(args.arg1)
