
def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    h = len(X)
    w = len(X[0])

    h_out = (h - pool_size) // stride + 1
    w_out = (w - pool_size) // stride + 1

    output = []
    
    for i in range(h_out):
        row = []
        for j in range(w_out):
            r_start = i * stride
            c_start = j * stride
            max = float('-inf')
            for r in range(pool_size):
                for c in range(pool_size):
                    val = X[r_start + r][c_start + c]
                    if val > max:
                        max = val
            row.append(max)
        output.append(row)
    return output





