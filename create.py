from argparse import ArgumentParser
import enutil

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument("--plainstring", '-p', required=True)
    argparser.add_argument("--savekey", "-s", required=True)
    argparser.add_argument("--saveencryption", '-e', required=True)

    return argparser.parse_args()

if __name__ == "__main__":
    args = get_option()
    enutil.Encryption().create_encryptionAndkey(args.plainstring, args.savekey, args.saveencryption)