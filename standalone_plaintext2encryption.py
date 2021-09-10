from argparse import ArgumentParser
import encryption_utility

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument("--plainstring", '-p', required=True)
    argparser.add_argument("--savekeypath", "-s", required=True)
    argparser.add_argument("--saveencryptionpath", '-e', required=True)

    return argparser.parse_args()

if __name__ == "__main__":
    args = get_option()
    encryption_utility.Encryption().create_encryptionAndkey(args.plainstring, args.savekeypath, args.saveencryptionpath)