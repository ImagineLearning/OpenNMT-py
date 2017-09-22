import sys

def optim():
    sys.argv.extend(["-data", "/Users/juanjose.lopez/imagine-learning/OpenNMT-py/weights/tester.p",
                     # "-loss_func", "datum_weighted",
                    "-epochs", "1"
                     ])
    import train
    train.main()

def prepro():
    sys.argv.extend(["-train_src", "/Users/juanjose.lopez/imagine-learning/OpenNMT-py/data/src-train.txt",
                     "-train_tgt", "/Users/juanjose.lopez/imagine-learning/OpenNMT-py/data/tgt-train.txt",
                     "-valid_src", "/Users/juanjose.lopez/imagine-learning/OpenNMT-py/data/src-val.txt",
                     "-valid_tgt", "/Users/juanjose.lopez/imagine-learning/OpenNMT-py/data/tgt-val.txt",
                     "-train_dw", "/Users/juanjose.lopez/imagine-learning/OpenNMT-py/data/dw-train.txt",
                     "-valid_dw", "/Users/juanjose.lopez/imagine-learning/OpenNMT-py/data/dw-val.txt",
                     "-save_data", "/Users/juanjose.lopez/imagine-learning/OpenNMT-py/weights/tester.p",

                   ])
    import preprocess
    preprocess.main()

if __name__ == "__main__":
    optim()
    # prepro()