import os
import sys
from job import Jobs

def standalone():
    
    j = Jobs("small",hours = 1, machine_type = "gpu4", root_dir = '../')
    grids = {"name":["small"],
             "batch_size":[4],
             "size": [100],
             "dropout":[0.7],
             "learning_rate":[0.001],
             "n_epoch":[100],
             "num_layers":[2],
             "attention":[True],
             "from_vocab_size":[100],
             "to_vocab_size":[100],
             "min_source_length":[0],
             "max_source_length":[22],
             "min_target_length":[0],
             "max_target_length":[22],
             "n_bucket":[2],
             "optimizer":["adam"],
             "learning_rate_decay_factor":[1.0],
             "N":["00000"],
             "attention_style":["additive"],
             "attention_scale":[False]
    }
    
    beams = [5,10]
    
    j.generate(grids,beams)

    
def distributed():
    
    j = Jobs("small",hours = 1, machine_type = "gpu4", root_dir = '../')
    grids = {"name":["small"],
             "batch_size":[4],
             "size": [100],
             "dropout":[0.7],
             "learning_rate":[0.001,0.004],
             "n_epoch":[100],
             "num_layers":[2],
             "attention":[True],
             "from_vocab_size":[100],
             "to_vocab_size":[100],
             "min_source_length":[0],
             "max_source_length":[22],
             "min_target_length":[0],
             "max_target_length":[22],
             "n_bucket":[2],
             "optimizer":["adam"],
             "learning_rate_decay_factor":[1.0],
             "NN":["00000,11111,22222,33333"],
             "attention_style":["additive"],
             "attention_scale":[False]
    }
    
    beams = [10]
    
    j.generate(grids,beams,dist=True)

    


if __name__ == "__main__":
    standalone()
    distributed()

    

    
    
