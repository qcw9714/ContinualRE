import torch
CONFIG= {
    'learning_rate': 0.001,
    'embedding_dim': 300,
    'hidden_dim': 200,
    'batch_size': 50,
    'num_clusters': 20,
    'epoch': 3,
    'random_seed': 100,
    'task_memory_size': 20,
    'loss_margin': 0.5,
    'sequence_times': 30,
    'num_cands': 10,
    'num_steps': 1,
    'num_constrain': 10,
    'data_per_constrain': 10,
    'lr_alignment_model': 0.0001,
    'epoch_alignment_model': 10,
    'model_path': 'model.pt',
    'device': torch.device('cuda:2' if torch.cuda.is_available() else 'cpu'),
    'bert_feature_file': '../ewc/data/bert_feature/bert_feature.txt',
    'relation_file': '../ewc/data/relation.2M.list',
    'training_file': '../ewc/data/train.replace_ne.withpool',
    'test_file': '../ewc/data/test.replace_ne.withpool',
    'valid_file': '../ewc/data/valid.replace_ne.withpool',
    'glove_file': '../ewc/data/glove.6B.300d.txt',
    'is_SimQue': True,
    'is_FewRel': False
}