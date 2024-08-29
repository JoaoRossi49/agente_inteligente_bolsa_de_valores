import matplotlib.pyplot as plt


BBAS3 = [27.93,27.47,27.12,26.55,26.19,26.3,26.65,26.2,26.16,26.37,26.55,26.95,27.16,27.12,26.89,26.87,26.98,27.14,27.11,27.19,27.31,27.04,26.95,26.83,26.48,26.61,26.2,26.29,26.73,26.85,26.71,26.45,26.36,26.71,26.7,26.71,26.89,26.81,26.61,26.39,26.27,26.08,26.45,26.45,26.72,26.54,27.51,27.21,27.18,27.65,27.29,27.23,27.15,27.12,27.32,27.32,27.41,27,27.08,26.94,27.5,27.9,27.92,27.69,27.68,27.65,28.01,27.83,27.62,27.14,28.38,28.29,28.38,28.22,27.71,27.42,27.55,27.55,27.38,27.5,27.6,27.39,27.71,27.93,27.97,27.91,28.23,28.5,28.87,28.8,29.19,28.95,28.5,28.39,28.19,28.08,28.04,28.31,27.99,27.97,27.82,27.7,27.82,28.22,27.92,28.01,28.65,28.35,28.48,28.8,28.41,28.7,28.98,29.26,28.83,28.63,28.75,28.72,29.16,29.1,28.76,28.48,28.84,29.09,29.02,28.84,28.32,28.56,28.56,28.18,28.65,29.09,29.17,28.55,28.25,28.26,27.63,27.52,27.66,27.88,27.69,27.73,27.67,27.19,27.37,27.09,27.4,27.35,27.51,26.98,26.82,26.64,26.68,27.09,26.86,26.54,26.83,26.8,27.11,26.85,26.89,26.65,26.57,26.53,26.85,26.75,26.73,26.1,25.93,25.7,26.48,26.48,26.2,25.78,26.35,26.35,26.45,26.4,25.65,25.61,25.24,24.79,24.81,24.73,24.56,24.39,24.26,24.08,24.08,23.97,24.06,23.71,24.74,24.43,24.16,23.99,23.18,23.15,23.21,23.37,23.98,23.49,23.49,23.6,23.63,23.71,23.52,23.64,23.85,23.38,23.45,23.23,23.27,23.39,22.48,22.41,22.24,22.53,22.59,22.81,22.11,21.91,22.23,22.36,22.32,22.84,22.64,22.68,22.77,22.69,22.63,22.65,22.53,22.18,22.24,22.4,22.48,47.49,22.55,22.4,22.75,23.09,22.96,22.32,22.61,22.91,22.81,22.26,22.34,22.26,22.05,21.86,21.98,22.2,21.96,21.85,21.97,22.12,22.16,22.28,22.24,22.14,22.53,22.11,21.85,22.31,22.12,22.24,22.69,22.42,22.18,22.57,22.49,22.3,22.45,22.24,22.6,22.93,23.36,22.91,23.26,23.41,23.56,23.1,23.4,23.19,23.47,23.91,23.85,23.84,24.31,23.56,23.57,23.14,23.31,22.84,22.73,22.97,22.17,21.14,21.15,20.9,20.84,20.41,20.36,20.4,20.22,20.26,20.38,20.37,20.3,19.83,20.09,19.71,19.72,19.69,20.28,20.18,20.26,19.85,19.6,19.66,43.3,19.73,19.25,19.03,19.09,19.56,19.49,19.47,19.63,19.81,19.85,19.67,19.9,19.86,19.82,19.48,19.49,18.22,17.81,17.8,17.86,17.93,17.64,17.84,17.8,17.48,17.28,17.16,17.15,16.98,17.17,17.12,16.92,17.02,17.32,17.13,17.11,17.25,17.35,17.69,18.08,17.9,17.5,17.11,16.92,17.63,18.22,18.05,18.3,18.67,18.52,18.99,18.8,18.59,18.42,18,17.9,17.55,17.65,17.24,17.48,17.38,17.49,17.83,18.05,18.09,17.81,18.01,18.02,17.54,17.63,17.77,17.34,16.95,16.72,15.79,15.81,15.77,15.87,15.65,15.39,15.54,15.33,14.66,14.47,14.75,15.4,15.37,15.1,15.62,15.64,15.27,15.13,14.99,14.61,14.45,14.17,13.78,14.13,14.83,15.35,15.37,15.57,15.61,15.45,15.81,15.46,15.48,15.47,15.28,15.01,15.37,15.12,14.94,15.09,14.74,14.79,15.12,15.61,15.23,15.58,15.89,16.32,16.25,16.84,16.59,16.25,15.87,16.65,16.55,16.34,16.94,17.24,19.16,18.7,17.86,17.8,16.93,16.79,16.89,16.77,17.18,17.44,17.4,17.09,16.82,17.78,16.52,16.44,16.53,16.53,16.66,17.47,17.68,17.37,17.49,17.23,16.9,17.09,17.26,17.25,17.49,17.27,16.81,16.88,17.73,18.12,18.03,17.76,18.03,18.08,17.72,17.8,17.39,17.69,17.34,17.16,17.48,17.9,18.06,17.97,18.44,17.45,16.71,16.57,16.3,15.8,15.51,15.22,15.12,14.92,15.04,15.14,14.86,14.77,14.71,14.49,14.59,14.49,14.49,14.11,13.91,13.63,13.65,13.8,13.75,13.98,13.85,13.65,13.74,13.81,13.86,13.95,13.83,13.9,13.85,13.57,13.65,13.74,13.79,14.38,14.27,14.23,14.01,14.01,14.34,14.58,14.6,14.73,14.84,15.02,15.24,15.22,15.19,14.97,15.37,15.54,15.59,15.68,15.72,15.08,14.55,14.64,14.85,14.44,14.31,14.33,13.98,13.68,13.84,13.8,13.76,14.12,13.72,13.45,13.54,13.87,13.89,13.83,14.15,14.04,14.33,14.35,14.88,14.35,14.34,14.27,14.3,14.21,13.96,13.71,13.64,14.01,14.14,14.15,14.23,14.31,14.25,14.39,14.4,14.24,14.31,14.03,13.75,13.78,13.65,13.47,13.62,13.54,13.82,14,13.25,13.15,13.73,14.09,14.09,13.94,13.72,14.17,14.1,13.97,14.27,13.99,13.99,13.91,13.28,13.22,12.78,12.64,12.75,12.61,12.76,12.78,12.7,12.91,12.93,12.86,12.78,12.61,12.73,12.41,12.35,12.35,12.28,12.17,12.06,12.04,11.74,11.55,11.44,11.39,11.34,11.32,11.23,11.42,11.41,11.42,11.47,11.53,11.59,11.57,11.61,11.68,11.65,12.01,12.44,12.48,12.69,12.69,12.8,12.61,12.9,12.84,13.02,12.68,12.66,12.33,12.54,12.13,12.11,12.53,11.91,11.69,11.22,11.28,11.3,11.38,11.55,11.71,11.73,11.96,11.43,11.45,11.38,11.13,11.4,11.32,11.07,11.23,11.33,11.34,11.46,11.23,11.58,12.09,11.9,12.51,12.27,11.89,11.95,11.93,12.03,11.78,11.9,11.88,11.34,11.48,11.22,11.43,11.36,11.6,11.35,11.44,11.41,11.15,10.88,11.24,11.45,11.26,11.35,11.44,11.19,11.15,10.96,11.44,11.24,11.27,11.76,11.75,11.67,11.78,11.61,11.77,11.81,11.44,11.34,11.32,11.24,11.19,11.24,11.26,11.35,11.6,11.71,12.02,12.13,11.77,11.98,12.16,12.23,12.07,12.35,12.55,12.37,12.31,12.13,12.19,12.37,12.25,12.04,12.13,12.28,12.47,12.38,12.44,12.13,12.16,12,12.19,12.26,12.13,12.26,12.37,12.46,12.55,12.94,12.91,12.91,13.19,13.3,13.32,13.64,13.54,13.59,13.44,13.48,13.52,13.78,13.87,13.57,13.37,12.9,12.72,12.74,12.69,12.52,12.32,12.49,12.4,12.37,12.26,12.06,11.89,11.68,11.68,11.38,11.46,11.37,11.23,10.95,10.97,11.01,11.16,11.11,11.11,11.36,11.16,11.29,11.28,11.19,11.29,11.11,11.16,11.11,11.1,11.08,11.08,10.95,10.92,11.01,11.08,11.22,11.23,11.42,11.52,11.17,11.12,11.08,10.93,11.13,11.55,11.51,11.41,11.51,11.2,11.17,11.25,11.21,11.16,10.82,10.9,11.42,11.21,10.82,10.8,10.4,10.47,11.01,11.31,11.35,10.6,11.99,12.22,12.26,12.4,12.47,12.43,12.6,12.45,12.48,12.57,12.62,12.52,12.6,12.44,12.69,12.34,12.05,12.38,12.56,12.69,12.98,13.2,13.34,13.77,13.8,14.52,14.38,14.62,14.54,13.96,13.67,13.82,14.26,14.38,14.46,14.3,14.07,13.89,14.37,14.48,14.46,14.33,14.15,14.1,13.86,13.18,13.36,13.37,13.18,12.91,12.8,12.75,12.41,12.68,12.74,12.95,12.99,12.65,12.55,12.68,12.56,12.53,12.35,12.04,11.92,12.44,12.52,11.91,11.11,11.18,11.05,10.97,10.86,11.28,11.34,11.94,12.2,12.21,12.26,11.75,11.66,11.15,11.03,11.32,11.24,11.31,11.31,11.38,10.86,10.94,11.01,10.82,10.85,10.79,10.84,11.11,11.04,11.08,10.99,11.23,11.25,11.42,11.71,11.69,11.65,11.79,11.62,11.81,12.06,12.08,12.33,12.26,12.07,12.06,11.86,12.12,11.89,11.78,12.07,12.15,11.81,11.7,11.69,11.74,11.58,11.89,11.85,12.09,12.16,12.34,12.22,12.31,11.94,11.93,12.31,12.03,12.47,12.88,12.55,12.51,12.16,12.31,12.61,12.72,12.65,12.7,12.32,12.43,12.31,12.11,12.23,12.17,12.21,11.92,12.42,12,11.88,11.85,11.52,11.98,11.4,11.83,11.54,12.01,11.91,12.16,12.32,12.36,12,11.85,11.95,12.26,12.82,13.04,12.61,12.52,12.45,11.76,11.39,11.05,11.03,11.07,11.03,11.29,10.21,10.48,9.79,9.55,9.82,9.37,9.55,9.15,9.43,9.77,9.71,9.41,9.67,9.96,9.95,10.21,10.59,10.44,9.2,8.71,10.05,10.34,10.39,10.6,10.32,10.62,10.82,10.83,10.62,10.65,10.45,9.98,9.14,9.68,9.57,9.99,10.39,10.12,10.92,10.4,9.29,7.93,8.81,9.16,9.53,11.42,10.89,13.07,11.2,12.9,14.12,13.41,15.08,15.37,16.33,16.32,16.81,16.7,16.32,16.12,17.39,17.38,17.56,17.51,17.35,17.61,17.96,18.24,18.13,17.35,17.52,17.51,17.81,17.05,17.23,17.15,17.6,17.48,17.92,17.77,17.95,18.19,17.22,17.09,17.6,17.71,17.47,17.39,17.72,17.81,17.62,18.04,18.42,18.58,18.73,18.98,19.01,18.66,18.72,18.8,18.58,18.04,18.08,17.89,17.29,16.91,17.15,17.28,16.84,16.87,17.12,17.06,17.13,17.28,17.03,16.7,16.83,16.76,16.66,16.19,16.4,16.46,16.2,15.99,16.07,16.24,16.05,16.32,16.5,16.41,16.65,16.65,16.76,16.66,16.75,16.82,17.26,16.99,17.04,16.67,16.52,16.62,16.55,16.21,16.09,15.68,15.72,15.5,15.72,15.8,15.51,15.44,15.02,15.3,15.93,15.82,15.16,15.7,15.89,15.83,15.96,15.9,16.01,16.51,16.59,16.33,16.77,16.52,16.29,16.46,16.76,16.68,17.09,17.38,17.17,16.49,15.94,15.57,15.87,16.07,15.67,15.3,15.42,15.55,15.62,16.21,16.3,15.42,15.44,15.75,15.79,15.8,16.37,16.18,16.75,16.8,16.68,16.7,16.48,16.79,16.79,16.95,17.19,17.37,17.22,17.26,18.02,17.7,17.91,17.9,18.13,17.83,17.83,17.8,17.9,18.32,18.68,18.92,18.94,19,18.7,18.31,18.55,18.57,18.52,18.49,18.09,18.26,18.22,18.08,17.78,17.38,17.39,17.71,17.99,18.16,17.8,17.97,18.12,17.67,18.17,17.88,17.79,17.83,17.57,17.59,17.36,17.03,16.78,16.75,16.75,15.85,15.26,15.53,16.03,16.3,16.46,17.07,17.37,17.22,16.84,16.8,17.04,16.94,16.91,16.8,16.79,16.71,16.44,16.78,16.45,16.62,16.06,16.28,15.95,15.9,16.42,16.61,16.49,16.74,16.71,16.62,16.42,16.6,16.74,16.58,16.34,15.79,16.72,16.33,16.22,17.15,17.52,17.92,18.31,18.45,18.29,18.43,18.15,18.26,17.71,17.11,17.17,17.41,17.17,17.61,17.81,17.72,18.01,17.85,17.77,18.29,18.21,18.39,18.37,17.48,17.88,16.85,17.36,17.34,17.22,18.34,17.82,17.49,17.4,16.97,16.76,16.22,16.43,16.51,16.18,16.21,16.29,16.43,16.37,16.53,16.72,16.34,16.28,16.04,16.08,16.27,16.38,16.38,16.31]


def get_cotacoes():
    x = [i for i in range(len(BBAS3))]
    y = list(reversed(BBAS3))
    return x, y