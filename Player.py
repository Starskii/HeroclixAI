# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.datasets import mnist
#
#
# class Brain:
#     (x_train, y_train), (x_test, y_test) = mnist.load_data()
#
#     def get_batch(x_data, y_data, batch_size):
#         idxs = np.random.randint(0, len(y_data), batch_size)
#         return x_data[idxs, :, :], y_data[idxs]
#
#     # Python optimisation variables
#     epochs = 10
#     batch_size = 100
#     # normalize the input images by dividing by 255.0
#     x_train = x_train / 255.0
#     x_test = x_test / 255.0
#     # convert x_test to tensor to pass through model (train data will be converted to
#     # tensors on the fly)
#     x_test = tf.Variable(x_test)
#
#     # now declare the weights connecting the input to the hidden layer
#     W1 = tf.Variable(tf.random.normal([784, 300], stddev=0.03), name='W1')
#     b1 = tf.Variable(tf.random.normal([300]), name='b1')
#     # and the weights connecting the hidden layer to the output layer
#     W2 = tf.Variable(tf.random.normal([300, 10], stddev=0.03), name='W2')
#     b2 = tf.Variable(tf.random.normal([10]), name='b2')
#
#     def nn_model(x_input, W1, b1, W2, b2):
#         # flatten the input image from 28 x 28 to 784
#         x_input = tf.reshape(x_input, (x_input.shape[0], -1))
#         x = tf.add(tf.matmul(tf.cast(x_input, tf.float32), W1), b1)
#         x = tf.nn.relu(x)
#         logits = tf.add(tf.matmul(x, W2), b2)
#         return logits
#
#     def loss_fn(logits, labels):
#         cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=logits))
#         return cross_entropy
#
#     # setup the optimizer
#     optimizer = tf.keras.optimizers.Adam()
#
#     total_batch = int(len(y_train) / batch_size)
#     for epoch in range(epochs):
#         avg_loss = 0
#         for i in range(total_batch):
#             batch_x, batch_y = get_batch(x_train, y_train, batch_size=batch_size)
#             # create tensors
#             batch_x = tf.Variable(batch_x)
#             batch_y = tf.Variable(batch_y)
#             # create a one hot vector
#             batch_y = tf.one_hot(batch_y, 10)
#             with tf.GradientTape() as tape:
#                 logits = nn_model(batch_x, W1, b1, W2, b2)
#                 loss = loss_fn(logits, batch_y)
#             gradients = tape.gradient(loss, [W1, b1, W2, b2])
#             optimizer.apply_gradients(zip(gradients, [W1, b1, W2, b2]))
#             avg_loss += loss / total_batch
#         test_logits = nn_model(x_test, W1, b1, W2, b2)
#         max_idxs = tf.argmax(test_logits, axis=1)
#         test_acc = np.sum(max_idxs.numpy() == y_test) / len(y_test)
#         print(f"Epoch: {epoch + 1}, loss={avg_loss:.3f}, test set      accuracy={test_acc * 100:.3f}%")
#
#     print("\nTraining complete!")
from random import random, randint
import Game

class Player:
    _game = None
    _board = None

    def __init__(self, game, board):
        self._game = game
        self._board = board

    def make_move(self):
        if self._game.current_turn == Game.Team.RED_TEAM:
            current_team = self._board.red_team
        else:
            current_team = self._board.blue_team

        for champions in current_team:
            moves = self._game.get_available_movement(champions)
            picked_move = randint(0, len(moves)-1)
            self._game.move_champion(champions, moves[picked_move])
            attack_choices = self._game.get_targets_in_range(champions)
            if len(attack_choices) > 0:
                picked_move = randint(0, len(attack_choices) - 1)
                self._game.attack(champions, attack_choices[picked_move])

        self._game.end_turn()
