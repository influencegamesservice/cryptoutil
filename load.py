from argparse import ArgumentParser
import enutil

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument("--encryption", '-e', required=True)
    argparser.add_argument("--key", "-k", required=True)

    return argparser.parse_args()

if __name__ == "__main__":
    args = get_option()
    plain_text = enutil.Encryption().load_encryption2plaintext(args.key, args.encryption)
    print(plain_text.decode())