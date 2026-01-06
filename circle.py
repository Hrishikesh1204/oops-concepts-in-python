{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNatJf/0N/gh/D/uJRBgQ1O",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Hrishikesh1204/oops-concepts-in-python/blob/main/circle.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GlfD9wjvCVLo",
        "outputId": "0b7d863b-6d99-443e-8d03-a3d8dc68d4d4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1962.5\n",
            "157.0\n"
          ]
        }
      ],
      "source": [
        "class circle:\n",
        "    def __init__(self, radius):\n",
        "        self.radius = radius\n",
        "\n",
        "    def area(self):\n",
        "        return 3.14 * self.radius ** 2\n",
        "\n",
        "    def perimeter(self):\n",
        "        return 2 * 3.14 * self.radius\n",
        "\n",
        "c1 = circle(25)\n",
        "print(c1.area())\n",
        "print(c1.perimeter())"
      ]
    }
  ]
}