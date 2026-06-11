import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """

    w = np.zeros(X.shape[1])
    b = 0

    for i in range(steps):
        y_hat = _sigmoid(X @ w.T + b)
        error = y_hat - y
        grad_w = np.mean(X.T @ error)
        grad_b = np.mean(np.sum(error))
    
        w = w - lr * grad_w
        b = b - lr * grad_b

    return w, b
    
    pass