from argparse import ArgumentParser
import encryption_utility

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument("--encryptionpath", '-e', required=True)
    argparser.add_argument("--keypath", "-k", required=True)

    return argparser.parse_args()

if __name__ == "__main__":
    args = get_option()
    plain_text = enutil.Encryption().load_encryption2plaintext(args.keypath, args.encryptionpath)
    print(plain_text)