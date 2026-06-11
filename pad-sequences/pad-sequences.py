import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    
    # Deciding on max length
    if max_len is None:
        max_len = max((len(seq) for seq in seqs), default=0)

    # padding based on max_len
    L = []

    for seq in seqs:
        seq = seq[:max_len]
        seq = seq + [pad_value] * (max_len - len(seq))
        L.append(seq)
        
    return np.array(L)
        # L = []
        # for j in range(seqs.shape[0]):
        #     while len(seqs[j]) < max_len:
        #         seqs[j].append(pad_value)
        #     L.append(seqs[j])

    return np.array(L)

        
    pass