import numpy as np
# numpy非科学计数输出
np.set_printoptions(suppress=True)


def func_matrix(x, theta):
    """
    [[   1. 2104.    3.]
    [   1. 1600.    3.]    [[   0]
    [   1. 2400.    3.]  *  [   1]
    [   1. 1416.    2.]     [-580]]
    [   1. 3000.    4.]]
    预测函数矩阵化
    :param x: area和rooms生成的数组X
    :param theta: theta参数
    :return:
    """
    return x.dot(theta.T)


def func_loss(x, theta, y):
    """
    loss function
    :param x:
    :param theta:
    :param y:
    :return:
    """
    return np.mean(np.sum((func_matrix(x, theta) - y) ** 2))


def func_(x, y, theta):
    """
    loss函数求导的矩阵运算
    :param x:
    :param y:
    :param theta:
    :return:
    """
    return np.dot(x.T, (func_matrix(x, theta) - y.T))


def gradient_descent(theta, lr, epoch, x, y):
    """
    梯度下降
    :return:
    """
    for i in range(epoch):
        theta1 = func_(x, y, theta)
        theta = theta - lr * theta1.T
        print(theta)
    return theta


if __name__ == '__main__':
    """
    x是5 * 3的矩阵
    y是 1 * 5的矩阵
    theta 是 1 * 3 的矩阵
    """
    price = [400, 330, 369, 342, 540]
    area = [2104, 1600, 2400, 1416, 3000]
    rooms = [3, 3, 3, 2, 4]

    price_ = np.array(price).reshape(len(price), 1)
    area_ = np.array(area).reshape(len(area), 1)
    rooms_ = np.array(rooms).reshape(len(rooms), 1)
    # 数据矩阵化
    X = np.concatenate((np.ones(5).reshape(len(price), 1), area_, rooms_), axis=1)
    print(X)
    Y = price_.T
    print(Y)
    # theta的初始化
    theta = np.array([0, 1, -580]).reshape(1, 3)
    print(theta.T)
    lr = 0.00000001
    epoch = 100

    theta_ = gradient_descent(theta, lr, epoch, X, Y)

