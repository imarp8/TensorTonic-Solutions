import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here

    # pe_encoded = np.zeros(seq_len, d_model)

    components = []
    for pos in range(seq_len):
        rows = []
        for d in range(d_model):
            if d%2 == 0:
                comp = np.sin(pos / (base ** (2*(d//2)/d_model)))
                rows.append(comp)
            elif d%2 != 0:
                comp = np.cos(pos / (base ** (2*(d//2)/d_model)))
                rows.append(comp)
        components.append(rows)

    return np.array(components)
    
    pass