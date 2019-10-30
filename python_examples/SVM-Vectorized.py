# Source is from https://mlxai.github.io/2017/01/06/vectorized-implementation-of-svm-loss-and-gradient-update.html


def svm_loss_naive(W, X, y, reg):
  """
  Structured SVM loss function, naive implementation (with loops).

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  dW = np.zeros(W.shape) # initialize the gradient as zero

  # compute the loss and the gradient
  num_classes = W.shape[1]
  num_train = X.shape[0]
  loss = 0.0
  for i in xrange(num_train):
    scores = X[i,:].dot(W)
    correct_class_score = scores[y[i]]
    for j in xrange(num_classes):
      if j == y[i]:
        continue
      margin = scores[j] - correct_class_score + 1
      if margin > 0:
        loss += margin
        dW[:,y[i]] -= X[i,:]
        dW[:,j] += X[i,:]

  # Averaging over all examples
  loss /= num_train
  dW /= num_train

  # Add regularization
  loss += 0.5 * reg * np.sum(W * W)
  dW += reg*W

  return loss, dW
