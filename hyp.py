EPOCHS = 800
LR = 0.0001
HIDDEN_LIST = [ [125, 250, 250, 125],
                [250, 500, 500, 250],
                [500, 1000, 1000, 500],
                [125, 250, 500, 250, 125],
                [250, 500, 1000, 500, 250],
                [125, 250, 500, 500, 250, 125],
                [250, 500, 1000, 1000, 500, 250] ]

CLASS_FREQ = [410, 3090, 4037, 3259, 4197]

# NUM_FOLDS = [5, 10]
# ONE_HOT
# DATA_AUG