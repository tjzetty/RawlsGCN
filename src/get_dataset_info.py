# from dataloading import load_data

# adj, features, labels, idx_train, idx_val, idx_test, sens, sens_idx = load_data('credit')

# features_shape = features.shape
# nfeat = features_shape[0]  # Number of input features

# labels_shape = labels.shape
# nclass = labels_shape[0]  # Number of output classes

# print("Number of input features: {}".format(nfeat))
# print("Number of output classes: {}".format(nclass))

from dataloading import load_data

adj, features, labels, idx_train, idx_val, idx_test, sens, sens_idx = load_data('twitter')

print(adj)
print("Shape of features:", features.shape)
print("Shape of labels:", labels.shape)

if len(labels.shape) > 1:
    nclass = labels.shape[1]  # Number of output classes
    print("Number of output classes:", nclass)
else:
    print("Error: labels do not have multiple classes.")
