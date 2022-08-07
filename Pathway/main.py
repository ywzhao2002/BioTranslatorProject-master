import torch
import argparse
from BioTranslator.BioConfig import BioConfig
from BioTranslator.BioLoader import BioLoader
from BioTranslator.BioTrainer import BioTrainer


def main(cfg: BioConfig):
    torch.cuda.set_device(eval(cfg.gpu_ids))
    files = BioLoader(cfg)
    trainer = BioTrainer(files, cfg)
    trainer.train(files, cfg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # choose method and dataset
    parser.add_argument('--method', type=str, default='BioTranslator', help='Specify the method to run, choose between BioTranslator, ProTranslator, TFIDF, clusDCA, Word2Vec, Doc2Vec.')
    parser.add_argument('--pathway_dataset', type=str, default='KEGG', help='The pathway dataset, choose between Reactome, KEGG and PharmGKB')
    # the dataset you want to train BioTranslator
    parser.add_argument('--dataset', type=str, default='GOA_Human', help='Specify the dataset for cross-validation, choose between GOA_Human, GOA_Mouse, GOA_Yeast, SwissProt, CAFA3.')
    # exclude the proteins in the following data from the training set
    parser.add_argument('--excludes', type=str, default=['Reactome', 'KEGG', 'PharmGKB'], help='The pathway dataset, choose between Reactome, KEGG and PharmGKB')
    # specify the dataset root dir
    parser.add_argument('--data_repo', type=str, default='./data/ProteinDataset/', help='Where you store the potein dataset, this folder should contains GOA_Human, GOA_Mouse, GOA_Yeast, SwissProt, CAFA3 folder.')
    # Specify the encoder model path, this model will be used only when you do not have embeddings in emb_path
    parser.add_argument('--encoder_path', type=str, default='../TextEncoder/Encoder/text_encoder.pth', help='The path of text encoder model')
    # please specify where you cache the go term embeddings
    parser.add_argument('--emb_path', type=str, default='embeddings/', help='Where you cache the embeddings.')
    # please specify the working space, that means, the files generated by our codes will be cached here
    parser.add_argument('--working_space', type=str, default='working_space/')
    # please specify where you choose to save the results, the results will be saved in the format of a dictionary
    parser.add_argument('--save_path', type=str, default='results/')
    # The following are parameters we used in our model
    parser.add_argument('--max_length', type=int, default=2000, help='The input sequence will be truncated by max_length.')
    parser.add_argument('--hidden_dim', type=int, default=1500, help='The dimension of the second to the last layer.')
    parser.add_argument('--features', type=str, default='seqs, description, network', help='The features you want to use to embed proteins.')
    # The follwoing are paramters used in the training process
    parser.add_argument('--lr', type=float, default=0.0003, help='Learning rate. ')
    parser.add_argument('--epoch', type=int, default=30, help='Training epochs.')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size')
    # The GPU ids
    parser.add_argument('--gpu_ids', type=str, default='1', help='Specify which GPU you want to use')

    args = parser.parse_args()
    args = args.__dict__

    cfg = BioConfig(args)
    main(cfg)

