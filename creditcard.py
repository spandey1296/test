{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "zMXA-QWQvms5"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "app = pd.read_csv('/content/application_record (1).csv')\n",
        "crecord = pd.read_csv('/content/credit_record.csv')"
      ],
      "metadata": {
        "id": "o-0vBpXjyNMj"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "app.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tzEbdYKC2BP7",
        "outputId": "c3c62e88-455b-4ebb-9b23-89764f365d81"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 438557 entries, 0 to 438556\n",
            "Data columns (total 18 columns):\n",
            " #   Column               Non-Null Count   Dtype  \n",
            "---  ------               --------------   -----  \n",
            " 0   ID                   438557 non-null  int64  \n",
            " 1   CODE_GENDER          438557 non-null  object \n",
            " 2   FLAG_OWN_CAR         438557 non-null  object \n",
            " 3   FLAG_OWN_REALTY      438557 non-null  object \n",
            " 4   CNT_CHILDREN         438557 non-null  int64  \n",
            " 5   AMT_INCOME_TOTAL     438557 non-null  float64\n",
            " 6   NAME_INCOME_TYPE     438557 non-null  object \n",
            " 7   NAME_EDUCATION_TYPE  438557 non-null  object \n",
            " 8   NAME_FAMILY_STATUS   438557 non-null  object \n",
            " 9   NAME_HOUSING_TYPE    438557 non-null  object \n",
            " 10  DAYS_BIRTH           438557 non-null  int64  \n",
            " 11  DAYS_EMPLOYED        438557 non-null  int64  \n",
            " 12  FLAG_MOBIL           438557 non-null  int64  \n",
            " 13  FLAG_WORK_PHONE      438557 non-null  int64  \n",
            " 14  FLAG_PHONE           438557 non-null  int64  \n",
            " 15  FLAG_EMAIL           438557 non-null  int64  \n",
            " 16  OCCUPATION_TYPE      304354 non-null  object \n",
            " 17  CNT_FAM_MEMBERS      438557 non-null  float64\n",
            "dtypes: float64(2), int64(8), object(8)\n",
            "memory usage: 60.2+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "crecord.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-SR9umdj2Jp3",
        "outputId": "3396d23d-b031-4033-922b-04658299be61"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 1048575 entries, 0 to 1048574\n",
            "Data columns (total 3 columns):\n",
            " #   Column          Non-Null Count    Dtype \n",
            "---  ------          --------------    ----- \n",
            " 0   ID              1048575 non-null  int64 \n",
            " 1   MONTHS_BALANCE  1048575 non-null  int64 \n",
            " 2   STATUS          1048575 non-null  object\n",
            "dtypes: int64(2), object(1)\n",
            "memory usage: 24.0+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "app['ID'].nunique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IT0fQ2xs2oh8",
        "outputId": "39242954-53da-4dae-9a97-19b20bd6b605"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "438510"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "crecord['ID'].nunique()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nUz2xd8r24Z2",
        "outputId": "7359b0a0-aeb4-4918-f1ef-8b244f012f58"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "45985"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(set(crecord['ID']).intersection(set(app['ID']))) #checking how many records match in two datasets"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rEBskAvN3JWO",
        "outputId": "4fb658e7-7793-42da-dc08-66bbee514b00"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "36457"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.heatmap(app.isnull()) #occupation_type has many null values"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 399
        },
        "id": "NwR6OLME4qIF",
        "outputId": "bb16605f-a7b4-433e-ce65-950b004a0891"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<AxesSubplot:>"
            ]
          },
          "metadata": {},
          "execution_count": 8
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXkAAAFtCAYAAADiRBqwAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/NK7nSAAAACXBIWXMAAAsTAAALEwEAmpwYAABqWUlEQVR4nO2dedxtY9nHvz9TZidlCkWGSqaMSUVEk4gyy1R5KwpFaNCgesuQlFIayJsMKZKMiUiUeRYnxKGIUobCOef3/nHd+5z17LP3Wmvv9Txn7+c599dnf6y91rrvde99nn2te133df0u2SaTyWQyE5O5Bj2ATCaTyYwd2chnMpnMBCYb+Uwmk5nAZCOfyWQyE5hs5DOZTGYCk418JpPJTGDGhZGX9FZJf5I0WdKhgx5PJpPJjBeG3shLmhv4FvA2YDVgZ0mrDXZUmUwmM/pI+qGkRyXd1uW4JH0jTXhvkbROVZ9Db+SBDYDJtu+1/RxwOrDNgMeUyWQyY8HJwFtLjr8NWCW99gFOqOpwPBj5ZYEHC++npH2ZTCYzobB9BfCPklO2AU5xcA0wSdIyZX3OM5oDHBSS9iHuamjuxdada66FBjyiTCYzHpj63ENq2sfzj91bWxtmviVW+h+SrUqcaPvEHi7XbdL7124NxoORfwhYvvB+ubRvBulLOhFgnvmWzWI8mUxm9jF9Wu1Ti7ZqdjEe3DXXAqtIWlHSfMBOwLkDHlMmk8kEnl7/1ZzKSW87Qz+Ttz1V0n7ARcDcwA9t3z7gYWUymVHkPw9f2XfbBV7yhlEcSR9MHxXjXZdzgf0knQ5sCPzLdldXDYwDIw9g+3zg/EGPI5PJjA0DN9QN8OjM0AGQdBqwKfBiSVOAzwLzxnX8HcIOvh2YDDwD7FXV57gw8plMZmIzrmfy06aOWle2d644bmDfXvrMRj6TyWSa0MPC6yBoZOQlLQ+cAiwFmAgHOk7S4sAZwArA/cAOtv8paTHgx8BL07WPtn1S6utI4B3EYvAlwP4ulK2SdC7wcturNxlzJpMZPgY+G2/CKLprxoKm0TVTgY/bXg14LbBvkhw4FLjU9irApek9xGPGHbbXIvxOx0iaT9LrgI2BNYHVgfWBTVoXkbQd8FTDsWYymczoM316/dcAaDSTT6u6f03bT0q6kwjM34Yw4gA/Ai4HDiFm+4tIErAwkdk1Ne2fH5gPELHQ8AiApIWBjxEJBGc2GW8mkxlOxrNPfjQXXseCUfPJS1oBeA3wB2CpQljP3wh3DsDxRAjQw8AiwI6Ob+hqSZcRNwwBx9u+M7U5AjiGWEnOZDITkEEb6kYMaIZel1Ex8mm2/TPgANv/jol6YNuSWr71twA3AZsBKwGXSLoSWBJ4FRHYT9r/BuBJYCXbB6abSLfrF2UNyLIGmUxmtjHt+UGPoJTGRl7SvISBP9X2z9PuRyQtY/uvSTzn0bR/L+AraUF1sqT7gFcS/vdrbD+V+rwA2Igw8utJuj+NdUlJl9vetDiGLGuQyWQGxpC7axotvCbf+g+AO21/rXDoXGCPtL0H8Iu0/QCweWq7FPAK4N60fxNJ86SbxiapzxNsv8T2CsDrgbvbDXwmk8kMlIm88EpExLwXuFXSTWnfJ4GvAGdKeh/wF2CHdOwI4GRJtxK+90NsPybpLMKFcyuxCHuh7V82HFsmkxknjOeF12GfyTeNrvkdYaw7sXmH8x8GtuywfxrwPxXXup8Ir8xkMpnhYU5YeM1kMpkmDHw23gBPn/gLr3MD1wEP2d4qKUYeQETPLGH7sXTewcCuheu+Kh3/h6RJwPeJmbqBvW1fLWlt4DtEDP1U4MO2/9h0zJlMZrgY1+6aIZ/Jj4ae/P7AnYX3VwFvJnzxM7B9lO21ba8NHAb81narzNVxhB/+lcBahf6OBD6f2hye3mcymczwMHv15HumqXbNcoTezJeIrFRs35iOlTXdGTgtnbcY8EZgz9T+OeC5dJ6BRdP2YkQSVSaTmWAMfDbehIksUAZ8HfgEkb1aC0kLEtXI90u7VgT+DpwkaS3gekKc7GnC7XORpKOJp47XNRxvJpPJjC5DHl3Tt7tG0lbAo7av77HpO4GrCq6aeYB1gBNsvwZ4mpmCZh8CDrS9PHAgEZPfaSz7SLpO0nXTpz/d60fJZDKZ/hnyOPkmPvmNga1TNurpwGaSflyj3U4kV01iCjDF9h/S+7MIow+RSNXKov0psEGnDm2faHs92+tlSYNMJjNbmTa1/msA9O2usX0YsYCKpE2Bg2zvVtYm+d83AWacZ/tvkh6U9ArbfyLi6+9Ihx9O519OJEvd0+94M5nM8JKja8aOUY+Tl/RRwk+/NHCLpPNtvz8d3ha4OPnbi3wEOFXSfITMQatu4QeA4yTNA/yXJEKWyWQmFgM31A2IXM7hRYXiSxOCLFCWyWTqMvW5h0rDAOvwn8t/WNvmLLDp3o2v1ys54zWTyWSaMFGjawAkTZJ0lqS7JN0paSNJR6X3t0g6O2Wzts5fU9LVkm6XdKuk+dP+yyX9SdJN6bVk2v8xSXekvi6V9LJGnzaTyWRGmwkcXQOdM1UvAVa3vSZwNzMXZ+chinh/0ParifKARdGHXVsZsbZb+vM3Auulvs4iZ7xmMplhY8ija5rEybcyVX8Akalq+wnbF9tufZprmFntaUvgFts3p/Mfd8WKhe3LbLfK/hX7ymQymeFgyGUNmszki5mqN0r6vqT2IPW9gQvS9qqAJV0k6QZJn2g796TkqvmMOmsivK/QVyaTyQwHQ+6uabLw2spU/YjtP0g6jshU/QyApE8RypGnFs5/PbA+UZT7UknX276UcNU8JGkRopTge4FTWheStBuwHhEzPwu5xmsmM77JcfJjR5OZfNdMVUl7AlsRxtuF86+w/VhywZzfOt/2Q+n/TwI/oZDZKunNwKeArW0/22kgOeM1k8kMjInqrrH9N+BBSa9IuzYH7pD0ViIZauuCPx3gImANSQumRdhN0vnzSHoxzCgKvhVwW3r/GuC7qa9HyWQymWFjyBdem8bJd8pUvRZ4AXBJcq1fY/uDtv8p6WvpuIHzbf8q+fEvSgZ+buDXwPdS/0cBCwM/TX09YHvrhmPOZDJDxsBdLk0YcndN0xqvNxG+8iIrl5z/YyKMsrjvaWDdLue/ucn4MplMZswZ8mSonPGayWQyTZjIM/lMJpOZ4xlyI99U1uDAJFFwm6TTJM0v6QeSbk5SBGdJWjidu6ekvxekC96f9r8sxc3flPr6YKH/+SSdKOnuJJXw7mYfN5PJZEYZu/5rAPQ9k5e0LPBRYDXb/5F0JlEQ5EDb/07nfI0o8/eV1OwM2/u1dfVXYCPbz6Ybwm2SzrX9MBE6+ajtVSXNBSze73gzmczwMq7j5KcOJmqmLk3dNfMAC0h6HlgQeLhg4AUsQETSdCUV7m7xAkY+XewNvDKdNx14rOF4M5nMEDJwQ92EibrwmjJUjwYeAP5DFAO5GEDSScDbiQpPHy80e7ekNxLCZQfafjCdvzzwKyIy52DbDxfUK49Ilaf+DOxn+5F+x5zJZIaTcT2TH0WffMozOo4IJ/++7a+0HX8p8CNgUjrnUNvnl/XZRKDshcA2hIbNS4CFkvwAtvdK++4EdkxNfgmskBQlL0kDJZ3/YNq/MrCHpKWIG9BywO9trwNcDRzdZSy5kHcmkxkMo+STlzQ38C3gbcBqwM6SVms77dPAmbZfQ7jHv101vCbumjcD99n+exrgz4HXkeLgbU+TdDqR/XqS7ccLbb9PB9ngNIO/DXgDoWHzDCMLeb+v00BsnwicCLkyVCYzHhn4bLwJozeT3wCYbPtegGQ/t2FmzWsI9/eiaXsxog52KU2M/APAayUtSLhrNgeuk7Sy7cnJJ781cFca8DK2/5rabk3M8pG0HPB4Wrx9ISFidqxtS/oloTv/G0YW+M5kMhOIOcVdUxRTTJyYJqkAywIPFo5NATZs6+JzwMWSPgIsREy2S2nik/+DpLOAGwi1yRuJ2fRvJC0KCLgZ+FBq8lFJW6dz/wHsmfa/CjhGklObo23fmo4dAvyfpK8TssatAt+ZTGYCMXBD3QBPq1/Iu+h16JOdgZNtHyNpI8I+rp4CUzrSVNbgs8Bn23Zv3OXcw0hVotr2XwKs2aXNX4jCJJlMZgIzp8zkK3gIWL7wfrm0r8j7gLcC2L46lVB9MdBVwDFnvGYymYEzcEPdhNELobwWWEXSioRx3wnYpe2cBwjX9cmSXgXMT3g5ulLLyEv6ISEB/Kjt1dO+xYEzgBWA+4EdbP+z0GZ9IiJmJ9tnFfYvSvjWz7G9X/Lp/xRYCZgG/NL2oencFxDFQ9YFHgd2tH1/nTFnMpnxw/ieyY9OrIftqZL2I2TZ5wZ+aPt2SV8ArrN9LhGS/j1JBxKLsHsWanZ0pG4I5cmkR4QChwKX2l4FuDS9B2aEAn0VuLhDX0cAV7TtOzoVA38NsLGkt6X97wP+aXtl4NjUZyaTyQwPo1j+z/b5tle1vZLtL6V9hycDj+07bG9sey3ba7dyk8qoNZO3fYWkFdp2b0NEvkDEvF9OLJRC6Mz/jCj1NwNJ6wJLAReSJIpTYZHL0vZzkm5gZsHubYjVZIjKU8dLUtWdK5PJjC8GPhtvQg8Lr4OgiUDZUoWQyL8RxrulabMtcELx5KQ9cwxwULcOU5brO4knAyiEFNmeCvwLeFGDMWcymczoMoELec8gxbS3ZtdfBw6xPT1Vc2rxYaIa1JS2/QCkkoCnAd9oJQPUJRfyzmQyA2OUfPJjRRMj/0grwUnSMswM4VkPOD0Z8hcDb5c0FdgIeIOkDxMl/eaT9FRrkZWIHb3H9tcL12iFFE1JN4HFiAXYEeSM10xmfDOuF14nqkAZcC6wByEjvAfwCwDbK7ZOkHQycJ7tc4BzCvv3BNYrRNF8kTDg7+9yjauB9wC/yf74TCYzVEyEmbyk04hF1hdLmkIkQH0FOFPS+4C/ADv0M4Aka/ApQv7ghvQEcLzt7wM/IDK6JhNZsjv1c41MJpMZKzzklaE00SbG2V2TyWTqMvW5h2ZdIOyRp7+4W22bs9Cnf9z4er2SM14zmUymCUPurqkVQinph5IeTTLArX1Hpbqrt0g6u1XkQ9IKkv5TqOX6nUKbC1P919slfSclTSFpcUmXSLon/f+FbddfX9JUSe8ZlU+dyWQyo8WQh1A2yXi9BFg9Ffu4m5HiY39O2Vhr2/5gYf8OttcCVgeWALZP+/vNns1kMpnBMt31XwOglpG3fQWx8Fncd3FKUAK4hplZqmX9/DttzgPMx8z6r9sws1LUj4B3FZq1sme7qqxlMpnMwPD0+q8BMFo++b0JsbIWK0q6Efg38GnbM4JgJV1EVEC5gJAqgOrs2TfRJpGQyWQmDuM6Tn7IffKNjbykTxGFQE5Nu/4KvNT240mr5hxJr27N4m2/JWkgnwpsRrh9ZlAze7Z9DDnjNZMZxwzcUDfAU4dbu6aRkU9JTVsBm7eSlGw/Czybtq+X9GdgVeC6Vjvb/5X0C8JNcwk9Zs+m5CoK/eWM10wmMxiGfCbft0CZpLcSRbq3TkqSrf1LFKJmXg6sAtwraeFkwFs6Ne8g1X9lZmYrtGXP2l7B9gqEa+fD7QY+k8lkBspE8Ml3yXg9DHgBcEmaaV+TImneCHxB0vPAdOCDtv8haSng3FQIZC5CXrgVXjkq2bOZTGZ8kn3yY0fOeM1kMnMso5Hx+uQB76xtcxb5+i9zxmsmk8mMKybywmsmk8mMBtldM3b0Xci7cOzjwNHAErYfS/s2JcIf5wUes71JWT+S1ib88/MT4Zgftv1HSYsBPwZemsZ6tO2T+vysmUxmSBm4oW7CkBv5JrIGSFoe2BJ4oLBvEvBtIurm1cyULujaD3Ak8HnbawOHp/cA+wJ3JCmETYFjJM1Xc8yZTCYz5tiu/RoEfcsaJI4lwiiLo98F+LntB1LbGXIEJf0YWDRtLwY8XNi/iCJ8Z+HUduqszTOZTGZADLl2Td8+eUnbAA/ZvrktG3VVYF5JlwOLAMfZPqWiuwOAiyQdTdx4Xpf2H0/E0D+c+trRHvJaW5lMZs5iyN01fRl5SQsCnyRcNZ36XBfYHFgAuFrSNbbvLunyQ8CBtn8maQeiItSbgbcANxHyBysRMflXFoTOWuPJsgaZTGYgeOpwzzv7ncmvBKwItGbxyxGl+zYApgCP234aeFrSFcBahBxxN/YA9k/bPwW+n7b3Ar6SJBMmS7oPeCXwx2LjLGuQyYxvxnd0zWAvX0VfRt72rcCSrfeS7icKcz+WNGmOT9IF8wEbEr77Mh4GNgEuJ2bt96T9DxBPBFemjNlXAPf2M+ZMJjO8DNxQN8ATwV3TSdbA9g86nWv7TkkXArcQ97jv276top8PAMelG8N/Sa4X4AjgZEm3AiIUKR/r65NmMpnMWDDkRj7LGmQymTmW0ZA1eGLHN9W2OZPOuCzLGmQymTmP8eyTH3Z3TWWcfKci3mn/R1Ih79slHZn27Voo4H2TpOkpmxVJ60q6VdJkSd9Ise9IOqNw/v2Sbkr7t5B0fWpzvaTNRvvDZzKZTFM81bVfg6DOTP5kIl59Rqy7pDcRBT/Wsv2spCUBbJ9KqhAlaQ3gHNs3pWYnEL73PwDnE5mvF9jesdDvMcC/0tvHgHfafljS6sBFwLL9fcxMJpMZI8Z7dI3tKySt0Lb7Q0RoY6sCVKci2zsDpwOkYiGL2r4mvT+FKNZ9QevkNLPfgYiuwfaNhb5uBxaQ9ILWNTOZzMRh0C6XJgx7ema/PvlVgTdI+hIRDXOQ7WvbztmRmO1DzMCnFI5NYdZZ+RuAR2zfw6y8G7ghG/hMZmIynn3y434mX9JuceC1wPpEVaeXt+q8StoQeKYVOlmTnYHT2ndKejXwVTpn17bOyRmvmcw4ZuCGugHDPpPvt8brFEKEzLb/SNzLXlw4vhMjDfZDRFZsi+XSPmBGzdftgDOKF5G0HHA2sLvtP3cbjO0Tba9ne71s4DOZzOzEU+u/qpD0Vkl/SgEqh3Y5ZwdJd6Sgl59U9dmvkT8HeFO64KpEZmtLS34uwrd+eutk238F/i3ptcn3vjupWHfizcBdtme4dJJk8a+AQ21f1ec4M5lMZkwZrTrekuYGvgW8DVgN2FnSam3nrELU1944SbkfUDW+OiGUpwFXA6+QNCUV2/4h8PIUVnk6sEfLVUMU8n7Qdrv8wIcJTZrJwJ8pLLoy68wfYD9gZeDwQojlkmQymcwQMVpGHtgAmGz7XtvPEbZ1m7ZzPgB8y/Y/oWvQywjqRNfs3OXQbl3Ov5zw1bfvvw5YfZYGcWzPDvu+CHyxanyZTCYzUFw/ibW4fpg4MQksQgSjPFg4NoXQ/iqyaurnKmBu4HO2Lyy7Zs54zWQymQb0svBaVMztk3mAVQgNsOWAKyStYfuJbg36yniVtLaka5IL5bokMYykgwuuldskTZO0eDq2f9p3u6QDCn19TtJDhXZvLxxbU9LVqc2tkubv+SvJZDKZMcTTVftVwUPA8oX3IwJUElOAc20/b/s+QsJ9lbJO+8p4ZWZN1guSUT4S2NT2UcBRAJLeSRQC+UfKWP0A4XN6DrhQ0nm2J6f+jrV9dPGiKeLmx8B7U/WpFwHP1xhvJpMZZ4znOPnp00ZNc+xaYBVJKxLGfSeinGqRc4hw85MkvZhw35TKr/eb8dqtJmuRYtz7q4A/2H4GQNJviZDJIzu0a7ElcIvtm9M4Hq8aayaTGZ8M2lA3YbTi5G1PlbQfIeEyN/BD27dL+gJwne1z07EtJd0BTAMOrrKNtaSGk5E/z/bq6f2r0sVEqslq+y+F8xckHitWTjP5VxEhkxsB/wEuTYP+iKTPAXsC/wauAz5u+5/JpbMuUZxkCeB022U3BSBLDWcymfqMhtTwg+tvXtvmLH/tpbNdarjfOPlWTdblgQOJmqxF3glcZfsfEIVEiKzVi4ELibqt09K5JxDlBNcG/gock/bPA7we2DX9f1tJm/c53kwmkxkT7PqvQdCvkd8D+Hna/inhay8yS9y77R/YXtf2G4F/kmq+2n7E9jTb04HvFfqaAlxh+7Hk5jkfWKfTYCTtkxaAr5s+/ek+P1Imk8n0ziguvI4J/YZQdqvJiqTF0rERcfSSlrT9qKSXEv7416b9y6SMWIBtgVYUz0XAJ5Lr57nUZ8dasbmQdyYzvskLr2NHpZFXh7qsdK/JCmGoL7bdPqX+WSFCZt9CXOeRqbCIgfuB/wFIfvmvESvOBs63/as+PmMmkxlyBm2omzCoGXpdco3XTCYzxzIaC69/Xv0ttW3OSrddlGu8ZjKZzHhi2KWGs5HPZDIDZ1z75HvQrhkEdXzyyxPZrksRvvETbR+X5ArOAFYgfOk7JD/6YkSm6ktT/0fbPin1dSTwDiKq5xJg/4J6JZLOBV5eiMfveI3GnzqTyQwVgzbUTfCQG/k6IZRTiQSl1YiImH2TxvGhwKW2VyGSm1oC9/sCd9hei1iwPUbSfJJeB2wMrEmoUa5PRMwAIGk74Km2a3e7RiaTyQwF06ep9msQVBp523+1fUPafhK4k5DE3Ab4UTrtR0RhbojZ/iKpOMjCwD+IG4WB+YkCIy8A5gUeAZC0MPAxZpUW7naNTCaTGQomVJx8kjd4DfAHYKlCfPvfCHcOhJjZuUQs/SLAjinR6WpJlxFZrQKOT5mwAEcQma7PtF2y2zUymUxmKBh2n3ztjNc02/4ZcIDtfxePJb96y7f+FkK24CWEVMHxkhaVtDIhVLYc8SSwmaQ3pBj5lWyfXXb9tmu0jy1nvGYymYFgq/ZrENQy8pLmJQz8qbZbcgaPSFomHV8GaJWh2ouZRb4nA/cBrySSpK6x/ZTtp4jyfxul13qS7gd+B6wq6fKKa4wgF/LOZDKDYtxr1yTf+g+AO21/rXDoXELDhvT/VmHuB4DNU9ulgFcQescPAJtImifdNDZJfZ5g+yW2VyCEyO62vWnFNTKZTGYomG7Vfg2COj75jYH3ArdKuint+yTwFeDMVNj7L8AO6dgRwMmSbiV874fYfkzSWYTOza2E2+VC27+suHa3a2QymcxQMD3LGsxesqxBJpOpy2jIGly33Ltq25z1ppyTZQ0ymUxmPDHuk6EkLS/pMkl3pILa+6f9R0m6S9Itks6WNCntn0/SSanw9s2SNk37FykU675J0mOSvp6OfSz1f4ukSyW9rG0Mi0qaIun40f34mUwm04yJ4JNvZbzeIGkR4HpJlxCyBIeluoRfBQ4DDiFkiLG9hqQlgQskrZ8SqdZudSrpemYWHrkRWM/2M5I+RNR+3bEwhiOAK5p80EwmM7yMZ+2aYfcP1ynk/VcigQnbT0q6E1jW9sWF064B3pO2VwN+k85/VNITwHrAH1snS1qVqN16ZTrvsra+diucuy6RBHVh6ieTyUwwBm2omzBter8F9mYPTTJei+xNCIkB3AxsnYqNLE8U416egpEnygOe4c6rvu8jYuiRNBeRCbsb8OZexprJZMYP43kmP+RKw/WNfLeMV0mfIlw6p6ZdPyQyW68jwh5/z8yi3S12IsIy26+xGzFbbwmXfZioCDUlwvW7jm0fUnUqzb0YOSEqkxlfDNpQN8EM98JrLSPfJeMVSXsCWwGbt2bltqcCBxbO+T2paHd6vxYwj+3r267xZuBTwCa2n027NwLeIOnDhNjZfJKesj1CjTLXeM1kMoNi+pBbnDp68h0zXiW9FfgEYZSfKexfkIi/f1rSFsBU23cUutwZOK3tGq8Bvgu81fYM6QLbuxbO2ZNYnM1yw5nMBGN8u2vG/0y+W8brNwjJ4EuSK+Ua2x8kFlQvkjQdeIhZ3TI7AG9v23cUMVP/aerrAdtb9/xpMpnMuGTQhroJw+6uyRmvmUxmjmU0Ml4vXmqn2jZny0dOzxmvmUwmM54Y9uiaJhmvn5P0UCGD9e2FNodJmizpT5LeUtg/SdJZKVP2Tkkbpf2LS7pE0j3p/y9M+xeT9MuUOXu7pL1G/yvIZDKZ/pnew2sQNMl4BTjW9tHFkxX1X3cCXk0UDvm1pFVtTwOOI9Qn3yNpPmDB1KxVy/Urkg5N7w9hZr3Yd0paAviTpFNtP9fsY2cymWFiPC+8DrtPvu+M15Im2wCnpzDI+yRNBjaQdAfwRmDP1NdzwHOFNpum7R8BlxNGvlu92EwmM4EYtKFuwpArDTfKeN0Y2E/S7kTi08dt/5O4AVxTaDYl7fsP8HfgpBQrfz2wv+2n6b1ebCaTmUCM55n8RAihBGbNeJV0AiEcZmYW4t674lrrAB+x/QdJxxFumc8UT7JtSe31YjcDViLCNa9srzGbyWTGN4M21E1oT+cfNvqu8Wr7EdvT0sz6e8AG6fSHCK2aFsulfVOAKbZbujdnEUYfeq8X2z6+XMg7k8kMhOlS7dcg6LvGa8soJ7YFbkvb5wI7SXqBpBWBVYA/2v4b8KCkV6TzNgfuKLTppV7sCHIh70wmMyjcw2sQNMl43VnS2sTY7wf+B8D27ZLOJAz4VGDfFFkD8BHg1BRZcy8xU4ce68X291EzmUxm9Bn2RcKc8ZrJZOZYRiPj9bSX7Frb5uz88Kml10uaYMcBcwPft/2VLue9m3B5r2/7urI+c8ZrJpPJNGDaKEXXSJob+BawBbGGea2kc9sEHkn5Svsza12Pjgx3SZNMJpMZcqar/quCDYDJtu9NeUSnEzlE7RwBfBX4b53x1ZEaXh44hYhdN3Ci7eMknUEshAJMAp6wvbakF5EeI4CTbe/Xoc9zgZfbXj29Xwv4DpHwdD+wawrT3ILw189HJE4dbPs3dT5YJpMZP4zvOPn6FAscJU5M9TAg8okeLBybAmzY1n4dYHnbv5J0cJ1r9i1rYHtGoW1JxwD/Sm//S8S+r55eI5C0HfBU2+7vAwfZ/q2kvYGDUx+PAe+0/bCk1YGLKM+2zWQymdlKL4uAxQJHvZLKoX6NpBpQlyayBnekC4uIhtksnfM08DtJK3cY5MLAx4g72ZmFQ6sCV6TtSwhj/hnbNxbOuR1YQNILCpWjMpnMBGDQs/EmjKKsQbccoxaLEBPny1PdjaWBcyVtXbb4OhqFvN8APGL7nhpdtDJjn2nbfzvhezoH2J6RH7TFu4EbsoHPZCYec4q7poJrgVVSftFDhNDjLq2Dtv8FvLj1XtLlhAdkdKJruhXypkM5vy7t1wZWsn1gulkU2Rv4hqTPEIlRz7W1fTWx0LBll75zIe9MZhwzaEPdhGmjNJO3PVXSfoQnY27ghynv6AvAdbbP7affpoW85wG2A9at0c1GwHqS7k/XXVLS5bY3tX0XyYBLWhV4R+EaywFnA7vb/nOnjnMh70xmfJNn8oHt84Hz2/Yd3uXcTev02Xch78SbgbtsT6nqx/YJwAmpzxWA81qDlLSk7UfTwsKniUgbJE0CfgUcavuqOh8ok8mMPwZtqJsw7BmvfcsapDvOTnRw1aTZ+qLAfJLeBWzZHtDfxs6S9k3bPwdOStv7ASsDh0tq3c22tP1oeweZTGb8Mp5n8sPuOsiyBplMZo5lNGQNjnvpbrVtzv4P/DgX8s5kMnMe43kmP+7dNSUZrz1nqUq6EFgmXfdKkkJlt+zZ1GZN4LuE+2c6IchTK503k8mMDwZtqJsw7EVDmhTy7idLdYd0IxAhfbA9UQ+2Y/Zsit75MfBe2zcnyYTnR+FzZzKZzKgw7DVeKwXKbP/V9g1p+0mglfHanqX67nTOjbYfTvtnZKmmY634+nmImf4IX1Yhe7a1mLslcIvtm1P7xwva9JlMJjNwpvfwGgRNMl77ylKVdBGhtnYBMZsv0p49uyrg1GYJYtZ/ZC9jzmQyw8949skPe6RHk0LefWWp2n6LpPmBUwm9m0sKh9uzZ+cBXk8oWj4DXCrpetuXtl0rZ7xmMuOYQRvqJkwfcjPfd8ZrkyxV2/+V9AviSeCS1KZT9uwU4IpWyT9J5xPFvy9t6y9nvGYy45jxPJMfdv9x3xmvvWappieBRWz/NRn0dxARNi06Zc9eBHxC0oLEk8ImwLF9fdJMJjO0DNpQN2Hch1DSvZD3Kr1kqRKFuM9Ni7BzAZeRbgyJWbJnbf9T0tcIdTYD59v+Vf2Pl8lkxgPjeSY/7NE1OeM1k8nMsYxGxuunV9ilts354v0/yRmvmUwmM54Y9lllNvKZTCbTgGH3yVcmQ0maX9IfJd0s6XZJn0/795M0WZIlFauVbCPpFkk3SbpO0uvT/rUlXZ36uEVSMctVkr4k6W5Jd0r6aGH/N9J1blEUsc1kMpmhYRqu/RoEdWbyzwKb2X4qhVL+TtIFwFXAecDlbedfCpxr20l35kzglUSc++6275H0EkIe4SLbTxCFaZcHXml7uqQlU19vA1ZJrw0JPfoR1cszmcz4Z1wvvA706tXUKeRt4Kn0dt70cqvIdiooWzz/qcLbhUguK9t3F855WNKjRBbrE8CHgF1sT0/HW3rx2wCnpDFcI2mSpGVScfFMJjNBGLShbsKwJ0NVumsAJM2dwicfBS6x/YeK87eVdBcRL793h+MbENo1rUSplYAdk3vnAkmrpP3LAg8Wmk5hpthZJpPJDBz38BoEtYy87WlJ+nc5YIOkLll2/tm2Xwm8CziieEzSMsD/AXu1Zu7AC4D/2l4P+B7ww14+hKR90g3iuunTn+6laSaTyTRi2AXKahn5Fsl/fhnw1prnXwG8vLUwK2lRYnb/KdvXFE6dQiRUQcghrJm2H2Kk8NlyaV/7dU60vZ7t9bJuTSaTmZ2M+4VXSUsAz9t+QtICwBaE8Fi381cG/pwWXtchZumPS5qPMOCn2G5XnzwHeBNwHyFd0PLfnwvsJ+l0YsH1X9kfn8lMPMb3wutw++TrRNcsA/xI0tzEzP9M2+elMMdPAEsDt0g63/b7CXnh3SU9D/wH2DEZ/B2ANwIvkrRn6ntP2zcRlaROlXQgscj7/nT8fODtwGQiOmevxp84k8kMHYM21E0YbhOfZQ0ymcwQMKiZ/GjIGvzPCtvXtjnfvf+nWdYgk8nMeYznmfy4j5NPBT6uIHzr8wBn2f6spB8A6xHqkncTrpenCu3eTVR+Wt/2dak+61lEAZCTbe/X4VrnAi+3vXrb/o8DRwNLtLTlM5nMxGE8++Q95A6bJhmvB7ZqtiY54P0I3zqp4Pf+RJnAFv8lCn2vnl4jkLQdM5OuivuXJ6SKH+jhc2UymXHEoA11EwYVNVOXOoW8XZihFzNeWwZewAKMXH84gojA+W+hn6dt/664r0UqKPIx4IsdhnAsscA73N9kJpOZI5kQcfLdMl4lnQT8jdCm+Wbatw6wfI/FPY4AjiEiaIrX3QZ4yPbNPfSVyWQys43pdu3XIGiU8Wp7L+AlwJ2ELMFcwNeAj9cdgKS1gZVsn922f0GiAtXhndq1nZszXjOZzEAYdlmDnqJrUkJUK+P1trRvWkpW+gSRtbo6cHkSLluaKPm3te3runS7EbCepPvTeJaUdDnwEWBF4ObU13LADZI2sP23tnHlQt6ZzDhmPC+8jvtkqC4Zr0dKWtn25OST35oowv0voKgtfzlwUImBx/YJhIQwklYAzrO9aTrckhwm3QTWy9E1mczEY9CGugkTIbpmloxXQn/myqRFI+BmQi64lGSoFwXmk/QuYEvbd/Q39Ewmkxk8U8e7kbd9C/CaDoc2rtF207b3K1Scfz8dwivrtM1kMplBMOwz+Z5UKDOZTCYzktEMoZT0Vkl/SiVPD+1w/GOS7kjlUC+V9LKqPpvUeD1Z0n2KWq43pSgZJG0q6V+F/YcX+ur4ASSdmvbfJumHKekKSYtJ+mXh2lmgLJPJDBW2a7/KSC7xbxFlT1cDdpa0WttpNxJrk2sSCgJHVo2vScYrwMEdZIMBrrS9VZcPsAWhH3+tpHOTT/5UYLd06k8IFcoTgH2BO2y/My0A/0nSqbafqzHuTCaTGXNGMbpmA2Cy7XsBUtTiNsCMdUvblxXOv4aZdrMrfdd4rT3smXT9ALbPb50k6Y9EuCTpOoukCJ6FgX8AU/u4diaTGWLGcwhlL7IGkvYB9insOjGFgEPncqcblnT3PuCCkuNA8xqvX0q+oWMlvaDQZKPkYrlA0qtLPsCIeq3pSeG9wIVp1/HAq4CHgVuB/QslAzOZTGbgTMe1X8Uqdul1YvUVZkXSboRA5FFV5zbJeD2MkDNYH1gcOCSdfgPwMttrEVIH5/Qw9m8DV9hu3dbfAtxEZNWuDRyfwjZHkDNeM5nMoBgtnzw1y51KejPwKWBr289Wddp3xqvto9PuZ5OGzUHpnH8Xzj9f0rcVNV5LP4CkzwJLAP9TOGcv4CvJZTRZ0n3EjeWPbePKGa+ZzDhm0C6XJoyia+FaYBVJKxK2cSdgl+IJkl4DfJewwY/W6bROdM0Skial7VbG612Slkn7BLyLJHMgaem0D0kbpGs8XvwAinqvOxE1XJH0fmLWvnObO+YBYPN0zlLAK4B763ywTCaTmR24h/9K+7GnEpLtFxF6YGfavl3SFyRtnU47ilif/GmKXjy3anxNarz+JkW8iHCpfDCd/x7gQ5KmEjVed0oz8amSWh9gbuCHtm9Pbb4D/AW4Ot0ffm77C4Q65cmSbk3XOSTLGmQymWFiNLVrUhDK+W37Di9sv7nXPnON10wmM8cyGjVe37TcFrVtzmVTLsk1XjOZTGY8MeyyBtnIZzKZTAMGVQykLk1kDa4sSBc8LOmctL9M1mD/JF1wu6QDCvu3T/umS1qvsH8LSddLujX9f7PR/PCZTCbTlIlQNKSjrIHtGTFPkn4G/KLQppOswerAB4jM1+eACyWdZ3syEZmzHREaVOQx4J22H07tL6ItgSqTyYx/xnPG67AXDem7kHfreEpO2ozqpKdXAX+w/UwKFfotYdixfaftP3W49o22H05vbwcWaMuszWQymYHSS8brIKjlk0/hk9cDKwPfKsgaQMTIX1pMgiLJGhByBAelUMnbCBmEFxGhlW8HulaM6sC7gRvqZHhlMpnxxaBn402YNuRKK7WMvO1pwNopKepsSavbvi0d3hn4fuH0lqzBU5LeTszwV7F9p6SvAhcDTxOx9dPqXD/p33wV2LLL8RmiP5p7Meaaa6E63WYymSFhPLtrhj26pqeiIbafAFqFvElyBRsQ5QBb5/y75d5Jgf3zpvOw/QPb69p+I/BP4O6qa0paDjgb2N32n7uMa4boTzbwmUxmdjKK2jVjQr+FvL+aDr+HKLz938L5SwOP2HabrAGSlrT9qKSXEv7411ZcexJxAznU9lU9f7pMJjMuGPRsvAnDvvDat6xBOrYT8JW287vJGgD8LPnknwf2TU8GSNqWUKxcAviVpJtsv4XQcVgZOLwQirllXWGeTCaTGWuGXTUgyxpkMpk5ltGQNVhz6Y1q25xb/nZ1ljXIZDKZ8cREznjdTNINKYP1R5LmKbTZNGW73i7pt2nfKwpZsDdJ+ncr61XSWpKuTpmtv1ShMIikNdOx29Px+Uf9W8hkMpk+GS2p4bGi0l2TtOEXKma8AgcCZwCb275b0heAv9j+QVos/T0hav9Aa7G1rc+5CVH8DW3/RdK1RDz9byXtDaxo+zPpxnED8F7bNyd//hMppLMj2V2TyWTqMhrumlctuUFtm3Pno3+c7e6afjNepwHP2W6FQF5CJCtBVDL5ue0HUvtOi6SbA3+2/Zf0flXgig59bQncYvvm1NfjZQY+k8lkZjfDPpPvq5A3UX5vnoKY2HuYWdpvVeCFki5PomK7d+hyJ+C0wvvbgW3S9vZtfVnSRck19ImanyuTyWRmC9Pt2q9B0Fchb+DVhKE+VtIfgSeZmb06D7Au8A6ipN9nJK3a6ktR+m9r4KeFS+wNfFjS9cAihIBZq6/XA7um/28rafP28SkX8s5kMgNimqfXfg2CpoW83wAgaUti1g0wBXjc9tPA05KuANZiZnbr2wgNmkcK/d5FkixIN4R3FPq6olXyT9L5wDrApW3jyoW8M5nMQBj3sgbqXsh7ybTvBcAhRJ1WCMnh10uaR9KCwIZEUdoWOzPSVUOhr7mATxf6ughYQ9KCaRF2E+COPj5nJpPJjAn29NqvQdCkkPdRkrZK+06w/RsI2WBJFwK3ANOB77fEzCQtRNwk/qftGjtL2jdt/xw4KfX1T0lfA64l5I3Pt/0rMpnMhGI8C5QNu6xBznjNZDJzLKMRQvnSxdeobXMe+MetOeM1k8nMeeSZ/NhRW2o4hVHeKOm89H4/SZMluSUlnPYfXMhqvU3SNEmLp2OTJJ0l6S5Jd0raKO1fW9I1qc11Sb0SBd9I17lF0jqj+/EzmUymGdOmT6/9GgS9zOT3JxZQW5IDVwHnAZcXT7J9FHAUgKR3Agfa/kc6fBxwoe33pFDKBdP+I4HP275AUWjkSGBTIhJnlfTaEDgh/T+TyUwgBj0bb8K4j66BGYU73kGhAlSqv3p/RdMZkTSSFgPeCPwgtX+uJTVMLKq2bh6LEWUDIRKkTklZt9cAkyQtU2fMmUwmMzsY90VDEl8HPkEkKtUihU++ldCEB1gR+DtwkqS1iJqx+6d4+gOAiyQdTdx4XpfaLAs8WOh2Str317rjyGQymbFk2H3ydSpDbQU8avt6SZv20Pc7gasKrpp5iESmj9j+g6TjgEOBzwAfItw6P5O0AzHbf3PdCynXeM1kxjXjeeF12CMU68zkNwa2Tr7y+YFFJf3Y9m4V7dr1aaYAU2z/Ib0/izDyAHsQPn8IuYOWW+ghZurYQMgqPNR+oZzxmsmMbwZtqJswqAXVutRRoTzM9nK2VyAM92+qDHzyv29CZL+2+vkb8KCkV6RdmzMze/XhdD7AZsA9aftcYPcUZfNa4F+2s6smk8kMDdNx7dcg6DtOXtJHCT/90sAtks63/f50eFvg4uRvL/IR4NQUWXMvsFfa/wHguCRd8F+S6wU4H3g7MBl4pnB+JpPJDAXD7q7JGa+ZTGaOZTQyXhdecMXaNuepZ+7LGa+ZTCYznhj2OPls5DOZTKYBw17IOxv5TCaTacD0AUkI1yUb+UwmM3BynHwg6a2E/MvchEz7V9qOvwA4hai+9ziwY5XyQG2Bskwmk8nMymjJGqSaHd8iNLtWI+psrNZ22vuAf9peGTgW+GrV+LKRz2QymQa4h1cFGwCTbd9r+zngdEK/q8g2wI/S9lnA5pLKI3Z6uQtNhBewz3hqO97Gm9sO9zVz28G+iByg6wqvfQrH3kO4aFrv3wsc39b+NmC5wvs/Ay8uu+acOJPfp/qUoWo73sab2w73NXPbAWL7RNvrFV4njvU150Qjn8lkMsNIHa2uGeckhYDFiAXYrmQjn8lkMsPBtcAqklZM0i87EfpdRc4lBB0h3Du/cfLbdGNODKFs8ng0iLbjbby57XBfM7cdUmxPlbQfcBERQvlD27dL+gJwne1zCRn2/5M0GfgHcSMoZcJp12QymUxmJtldk8lkMhOYbOQzmUxmApONfCaTyUxgspGfzUjauOL4orNrLHWQdMagx5ApR9LRgx5DL0h6ScXxrr8BSS8d/RFNbCa8kZe0h6QbJD2dXtdJ2r1Bf5MkfarinLkl7SzpIEmrp31bSfo9cHzFJW6UVLli3uGah5e8PtNrfwU2qrju1wvb+7cdO7mi7WaF7RXbjm3XyyAlvUjStpLWrXHumYXtr7Ydu7ii7cfKXjXH+RFJ30qv/SS9qKpdBTtUXLPv73k0/40KXFNx/PLCNS5tO3ZOWUNJH5C0StqWpJMk/VvSLZLW6Wew450JbeQl7QEcAHwceAmwLFGycH9J761ou7ykEyWdJ+n9khaSdAxwN7BkxaV/ALwfeBHwDUk/Bo4GjrT9moq2mwE7SrpE0soV5xZ5usPLhKDRIT300ytvLGzv0XZszYq2xRnoz9qOfbqsYfp3ad1AlyHSvfcmwssOqLjuKoXtLdqOLVHRdpHC66C294tUjPlVaZzrEn9H9wDrA7dKemXFdUu7rjje9/fcsG03qsZbPL54j233B+5P2zsTf4MrAh8j1B3nOCZ6nPyHgG09UorzN5LeTYj//F9J21OA3xJ/2G8ldCZuAtZ0FCUvY7103nRJ8wN/A1ayXZqZBmD7L8C2kt4GXCXpWmB64fjWXdod09qWtAjxx7438TmP6dSmcH63GY6AeSuGrC7bdShrW9XXirZvS9t7AZfY3j199quAr5e0LYsbLo0ptv35GQOU3lV8X4MjgP1tn1ncmf4evwS8u1tDSe3GbsYhejOavX7PTdp2oypu212267Sdavv5tL0VcEr63f1a0pE9jHHCMNGN/KLuoLVs+/4avu/FbX8ubV8kaXtgV7tWhYDnWufZ/q+ke+sY+BaSXkHMEq8kpEdrVSVIhuBjwK6EUt06tv9Zo2nZTeCuirZzSXoh8VTY2m79+OeuaNvkx/x8YXtz4HsAtp+UVPV9LSjpNcSYF0jbLWO5QEXbXsbYzhq23zNLJ/bPJH25ou316XqdDOvzHfaNuESX7U7vR6WtpG92OS5gUsU1l0yuLxW2W22rnrSmpye7fxJ/F18qHOvl33bCMNGN/H/6PAZAm8F6HFisJetp+x8lTV8p6ZZWN8BK6b2iqbu6MSR9hZATPdD2hVVjLLQ7CtiOyO5bw/ZTddvaflNJv1Uz+cUIA9T6nm4odl3R9uWSzk1tW9uk9yt2bwbAg5I+AkwB1gEuTONdgOqnj78BX+uw3Xo/Vjzd5zFsV30fZTT5nvtte12fxyBu2It02Ab4fkXbw1P/cwPn2r4dQNImwL0VbSckEzrjVdIzwOROh4CX216opO39xAy608zJtl9e0vZlZeNKLplubS8F3mH7v2V9dGg3HXgWmMpI49q6sdSO2kk3ss2AXYCtbC/Vy1h6uM4mZcdt/7ak7ZLAF4BlgG/ZvjjtfxOwru0xiTiRdCszv9+Vmfn3VecGPoWRN5QZh4ADbC/f4Virbemioe0buh1r+D333bYpkl5s+7E+2s0DLFJ8ipW0EIDt0pvpRGSiG/m+je1YIOn1wM629y055wbbA4kCkPRawrC/i1jw2peYDXV1+SRj+0nC4N0CfMX2v3u45tqp7e227+x78D2Qoi+OSte9FTjIdrvaX7e2TW7gn61o29W/L+my8qberOT4bEfSLyl5kuu2tpTabgWcRLihpgM72P59w/FsAXzCdvtC+4RnQhv5JkjazfaP0/bGtq8qHNvPdlUoZOvc1xCGc3vgPuDntr9Zcn5fRl7SZrZ/k7ZXtH1f4dh2tn9e0vbLaXwPAKcBZxOCSJUuAkkXEu6aK4iFrkVs71lzzIcDu6X2GwL/a/t7Ndu2GxEDjwGXtf7dStpeSSysXwFsDWxku1Y4oKSLbW9Z59xhId0guv3QbXvz0W7b8OnhFsKw3yVpQyIqrbS/QtvNgO8Q0XTnEOXxTiKelr5U9juYqExoIy/pSbov/pS6MIrGtt3wVhliSasS4Vs7E4bnDGK2WDoLTG2fIIxPR7rNgBqO91EipO/rwC9tP5sWi7u6pAptb7a9Vt1rtbW9HVjf9jOKWPELba9fs22nH/3ixE3jHtuHlrS9yfbafY75xhphsN3anml7h7T9VduHFI5V3jzSU8TTth9LT12vJ8rFnVPRrlPuwGuJcOJHy77zJm279Lc8sJPto0rO6envt63tjcCBwNVErdQfA4fWnZRNRCb0wqvt0rjlCpqEjt1FRMZsZXsygKQDa17371SEPHahyXiXIeLFdwa+nmZvC0iax/bUygu3RdQU31csUD9r+5l03uOSaudtdJsJpoXB64GuRh6YvxBRAyMjbEr928Tie9dZf8VMsT0+v5i/UBo1kp569gAs6XTgzUTS0DskbWr7gJIxXV/oZxPgM8D8wAdtX1B23SZtC+2WIJ4UdyZm2GdXNClG1Mzy3nandY3CYV+ets+R9NCcbOBhghv5hjQJO9uO0Hm+LLkzTqfa0LZ4ssSAHU3E7neiyXiXTZE8F0p6AeF2WQB4SNKltncpadseXQMzI2wMlD0NtEdrrFR4X+q37Ybtaaqoa0zniJrWexOLzt1YjPh+Oi7IA2VGvu/4fOLv6VXAgoRbben0BDQPkb9RiqS3EMlLzxJuizIff+O2inyF7QhX5arE97Ki7eVqXLI9oqb9fRmT2m7C8xTfZ3dNZgaFyBwBKzEyiqI0MqfQx0JEOOTOhOE4BTi7FQnSpc3Pu/mHJT1gu6N2R8HNI+ANzHT5CHi97ReWXLPj47Ail+Bdtk8paTu37WndjpfR0G/bKTnohcDuwMq2dy1pu2gvi8NtbfteGJd0F/G3MBfhRtgFZsTn/9j2q+pct91lVMMddy3xpHAU4cYYQUVkTl9tJf0H+CNxc/idbffgAnyt7Srpg25tT6Z8DWHvfvodz2Qj34XRjsxJLoz3EP7IrgtdFX086C5hdg0NZhM/803Ah2zPYgBqtD0EOLqfm4Sk+xiZHNRaeL0c+GKZEZf0Z+BTtk/v47pdvytJL7X9QEnbyymPOCnLV7iXSJATcCRwcOsQsTC5Up/XtUsic/ptq5CW2AlYiFjMP4PISq5j5G8gSuF9wva/qs7PlJONfAWSJjHTl3p3nT86SesDL273WUp6O/BI0c/ZoW1Z+vrNNR932/scER3U4fijhEupI7Y/WtJ2Q+CbwM3Ej7JOhm2r7fHE4uG+ZePr0najfm4sqe3LiEXmhYkbVKdcim5tVydcB8sCV9h+VNKaxBrAG7rdhFPbJk8QJ5Udt71XP/2ONZJeThj7nYnf0WeJp9m7S9rMBXwU+DBwhO0y+ZH2tl9vrU9I2t/2cYVjJ7tm5NdEIhv5LiTf9HeJmPH7CCP7MmLR6IO2nytp+xtgr/bZfjIuJ1XMnNpnqCNwl7BGSXMTaoTLElEqtynijT8JLFA2U5f0FyJTsCO2f9TtWGov4IPETPMCRmrtdL1BpLbrEMqcdwIntLUtcyM0zidQ6AOdTMwaK/WBUpujCJ/8TUSc/UWEGN3/At91SRJbkyeIpijyGfYFXp123U4kkT06lm3b+lmdcFHtYLtSfE/SaoSLaC5m/ibsMYqKm6jkhdfufJpIj1/e9pMwYzHpW0SEQZl87yKd3Dm2/yLpxWUX7WbEa/ADYHnCD/oNSQ8TQmmHuiLEDni8ypBXsDihpvh3YhG2ltYOhCGX9ElCCG4lZroGqhZA+xXHisZ96gMB7wBe49AkeiHwILC6O2gkdWAzInrpffT4BJHGvDrhpika26Nt31rRbmPgJ8QNrbW+si7wR0m7Vjzl9d22HYeg3CfTq5T0HR0KfIq4odSdjZZFmc2Z2M6vDi9CEnbBDvsXBm6raDu5n2MlbVYibiq3V4x3rrQ9P/AE8KKa/V/T4Hv6IPDn9H/12HZJQgn0KmCtHts+AZzb7VXR9ivEk8Nb+/i8N7S9v7GPPt4GPAKc18OYtyGkifcm5HPXTNv3ANtU/fsSN6b2/WsDfxiLtsCTwL8LryeL/6+45u+JG8vSfXy3NxML8C8qbC+eXjf3+3c+nl95Jt+d6U4x3EVsPyWpalbxa0lfAj7t9JeXXBqfB35T5+KK6jk7Eo+3axDugLJiIn0rX9p+raT5CPXK4izxJ7afrWi+MZEx2tOje+IawuDu3vqeeqDffAKIp47XuEd9oEQx7BNgxV7CPhs8QXwB2MIjnxhuSa7BX6RXNxa1fWP7Tts3pafTMvpteymwNBE6ebpLFqQ7cLrtb/RwfpEmgnkTkmzku2ONTPIpUvXD/Dihljc5RZ8ArEWo472/rKGkfYhFqmWBM4miH79wtW55E+XLVwG/JGbUrUXhTYFPSdra9h0l1311nwYe4E7bJ/bZtms+QQ1e2KeBh5hRF6l9o9FMhdGPuWYiUYF53F02u1LzX9IL3bYonhb5qxLQ+mpr+12SFiNi5b+nqKtwBmHAyxLkAPYE+jLytlfop91EJhv57nRK8mlROiNwKN3tnCILZsyMbY+QOpX0aicp1ALHE4tNu9i+Lp1XZwbSNca6BscTPuJL2sb3ZmK22TW0ryHLNGh7f/uOlJewHRGm+o4GfXelwY0FQiF0bcJwrp72Ta55w5naKUQzLeZXZSUfC1ws6SBmzmzXJXRdjh2rto5ItJMk/Yh4Cv0G4Uosy1htjCJBbJptK2QUNiS+55vG8rrDSo6uGSCdVvsVGi6tFPClidn8ni4JzWtrP4neQz7vst2x/JykO12epNMk/LKVHNQtkqhMXqDVx3zEYuguwFuIBdyf2/5lSZsn6EMfKLUtSg13alv2xDQv8EXi6ewvxOdenhDQ+pRnVjTq1PZdRHz8l5n5tLUesTh5iKv1a7Yi9GaK7rijyr6npm0lvY74930D8DvgDNtX1rjeVGAWVyn1oms+QNyAniIqcR1M3JxeA/zQ9le7tZ2oZCPfBVVUhe/Rx9jtGje6PLRxOcIvvzORVHK27Y6RCQ1DPu8mCo0827Z/fuBW26t0btks/FIhIHctXZ6WXB5quiXxvWwJXEa4Ar5Z53Fd0j2UuM3KZutqJjV8LBFjf6BnRmwtStRR/Y/t/SvGvRbhCmwZ2zuI6Jqby9oNAkU9hieICcBvaHvaKLuBV/0uKq57O5F7sQixuP4yh6DbgsC1tl9d2sEEJBv5LhRmbEUDZCLFe0nbVaXt6lyjF3W9VQk3xBe6HD+C0In5oGcN+fyL7a4hn5I+TSgL7tsyUpJWIB6vr+t2zV4/Q4e2TX7M04nFyz2dZJVVP21+VOOlU1js41WLx+nmsmr7eSnH4a6ym2nD8XUrxQdUPm311VbNsmyb/F3MaKtZFVL77nc8k33yXbC9RvF9MnqHEOp/VfU4+0bSJ2wfmba3t/3TNJ6708y6G9sCGxQjghz1Tj9MRLF0NfK2vyhpP+DKNOOBKEd3tEu07xNdnxCKdFl/aMI6hJ/314qU/9Oprinb4v46J0naosM6xWuJiKB/EO6A/wNeTNS33d3lJRvd6UbgEFWrukGcW3a8IqqnWG7v80TWaV36amt70x6u0c5P65wk6TDb/9u2u6UoOhcwn0bW7y37/UxcPARxnMP8IvzbJxOPfu8H5h3FvmeJT6cQh82sMdk3lPR1S8mxWyvGsV1hexEimWu0v8dZxg5sWbPtzyqOv46QVniYyLjdZwzHfB3hItqeKBb92rT/lVTEzBNFLHbvsH83quPk/074lg8G3ghsUnz18JlKxzhabQmJi9b29m3HvjyG/z6XE+67jq/RuO54e+WZfBdS9MOnCP/nkcD7XFNIq64/3/ZrOzXvst3p/YhuG4R8fpokkevk6hkDZhmXS9Q425jFBaNCkQ1HabjfS9qfeNLaiSho3pRO3+U8nllP9gtOaomOKkZV/e0L/FzS3oxcPF2AeBIrY2lmav7vAvwKOM29Px018c/20nYn4ncDcBgjZ+dvpUbWaw06/U1tOgr9Tiiyke/OzUTK+q+ADYANij9il2uy/IoSfz7lbgV32e70vkjfIZ+zidE2LrMU2XAkg12cXqNBp+sWb5j/qXH+zINRR3ZDRYm61gLg+bYvlfRuIjKoW9tpQFHzf2fgckmf93AWxWhSxKYus3zfKinoAnOmnnw28t15H30aJjfz568l6d/ED2GBtA0VPkWXRJVIWrbimsVEqhFNqUikGiBNKjQ1oa9/n7ax/YZZM5+PpcTIw4wIqncQBn4FYmH87KrraWYZzE5jtstDEvtt2+9kpRc63SzOIsTjbupwjikv6jIhyUa+C7ZP7nYsJVtUImkVwuWzIZEZ+VGXxEKn6zaO2unA1UCZC+k+4J1jcN0itRZou9Dpx7wY/Vdoqsv9s3Rc89+nU5ZoVZOK/k4BVgfOBz7vEPuqhRuUwWzQtvHNsAadFmhbVdnWJKQeTnOPQnATjRxC2QVJv7P9+rT9f7bfWzhWVYmn3Z9/Wl1/fkmfk4gQxy/10bZrsZF0/Eb3H7K2m+0fp+0RuvWS9hsNV4KkLdv99w1DNxcFlrJ9T3q/PeEXB7jI9iONBtzH+FRS9Ssdn05EPMHImXCd2fj8hIDcysAtRFJQZe3epm1r9t9JMqFr3gXxWY+o0W+rKtuOhFjZp9wsW3nckmfy3SmW92tPoKjyKfbtz1ekYX+GKHh8DlFV5wtEWbuf1Bv6LFTdyWvJxUraw7MmN32MKGUHEeFSNGx7E5IJ3fq7rGRsdqqg1WWBtolf92hC6fCe9P5/iaicBYhInQ826LvFLOMryZYVsFRZZ7arNGZa1+j0BPEj4Hkir+DtxN9zaeLVKLWtw6WM/JuBmTezIgsS0W0vIkJXq/gv8C9C+fJlzKnhk2QjX0aZYawymk3qSJ5CFOv+GRGFcB3hX1zD9t+6NSpJWhEwqeyCtverObb9iR99e/+dtju9b+egDvteS6TQV4mevbf4RiEH8UbgAZdU3kqsD/xP4f2Ttj+S+vldRdu6dPq32GqU+i6jk9FcrbVOJOkHRM2BujRpW4dOETIzRN9SQt/+xG/qdCoE4dKi9k7E5OrXwHFOGlBzKtnId2eSpG2JpIpJhUU+Ef7gMm4mtKv78YUtbvtzafui5ErYNUWOlFH2hzxaf+RVkTs9LbAVjbGiRu1niBnXB12t0vgVSYc6KmAtQ8SQX0eob55o++slbedp+7cp3jAmVVy3bxxFY95FuD5utX3RGFym07/RjHUg21NrhHqOVts6dPwbUahcfoyQv/4RsE7NNY5fE26l3wEvAHaXtPuMi1VUKpuIZCPfnd8CWxe2iwuTXcWtEt8ndMevJ9wCVwFX141Bb4t3f5yIJBGAu8i0dnCjjAWdfpCtyJyivDHpfR2JgbcQcfrPAl+yfVnNsaxYWHzciygSvXua+V1F1HDtxnRJS7eejFr9pCik2lWtKujkrvk24e74PXCEpA3q+Jd7pNO/UWsRtDWu1kJopT+/Ydu+UJRY3I7IdVjD9lM9NN+b4QgZHhrywusYkeQBNiB8vK8jXAR/A66y/eGSdvcThqabaFdHwynpl5RrjJQWs6hDpwVaNRPsupaIdz+KiABqb1smYnWT7bXT9qXA95xqpxaPdWm7G+EC+DhwY9q9DuGr/4ZLCkenf9fnW1FSiiIgbyf0gX5eOG/x9huypNuICljTUj9X2l6327X6oeGCdK8RQY3bdvmbmk7c9KfS4yJzxbXmGc1F4/FCnsl3QaEAuYLt36X3HyNK/0FUTCoNy3JoyFyeDNkfiApKuxN+9rJ2K9QcX7sWzNF12jVklgXaMiNeg6cJSdj3pNeIrimv8fqgpI8AUwgDfSGApAWI2rxdsf1jSY8Rsr+tRfXbgMNruIkuJHIo7pG0MnFzOhXYStL6tg9L1+j0xPVcK8rK9jOtp7NRpkmfnfz5o9I2PSW1wk8fLhjbzdvPrbvI3OU6XaPiiPWEOa6Qd57Jd0HSacCpts9L7/9EPD4uCLzS9q4lbXchZu9rEzOSlqG/umzxtMfxjZqSoqSv2z4gbe9v+7jCsZNt71nStpUsM2MXM5NnxuRxPl13SSLqaBmi0HNLauBNwLq2x+SmJ+nWwkLkEcQayr4KXfvr3ZYI19b2GaA1ORBRu3cyM7+r2kln3YxmpyeIHvpsEko7oq2kwwidpy+k9w8Q0sPzAT/yrMJinfp8E4WbsO3LexlH+2+kyecbz+SZfHde0TLwiWdaq/6SqgoffBf4E/Ad4Arbd4/B+EbM2ErC84DyYhZEVEqLPYDjCu+rDE+TWp4tY70vIwtSfMsVJQXT8VlCHZNPf4ZfX9I3W5EzhX1N4rCL3/FmhKsJ288lN0MZfVfvajeaxBPEEySjSYSBdl2zqcloSk9sTxQLafG47dcoZJV/SxpvJ9IN7OdEGGRrcX779JS2rUMeou446h6bsGQj3532uNriY+WLK9pOImq6vg74XPLb/pX4YV7tSGtvSvsfbCs8T0R8/tt76KssDLJ8EA1qeUramIj9P5kIHYUoLfdHSbu6kFjVgI077OsUh70Q4YapisO+RdLRwENElEzrCWJS1UAaurb6NpqDwlEGs8Vxad+0ZKzLOB44wW1Z5ylK5tvMWme3SJOouAlJNvLdeVLSqq1ZeMtgSXolUBolk/yuN6TX8ZKWIn6kBxAuhlGXLigaEEnP9mhQ5koRPXMVtlvGvnKs7r+W5zHAu2zfWNh3rqSziaehDXv4DLVx5zjsvagRhw18IJ2/AiGV3NLvX42KdZGmrq0GRrNsTPN5ZtWwJv789rYLS5q3tUDdMtgK/Z0qF95qtmdR5bR9iqRPVbRtEhU3IclGvjufBc6T9CVGFjD+JBUZf5LWZGZUzeuIR+rfExmhozE7hWZaMO20K1gWo1oqH3E1ay3PbV2jliewaJuBjwvaNyXjO2Y0iMP+KFHfdIRMhZPccUXbJq6tvo2mpMPdobpXegL7BbBp2jXLImiHNnUXUM8CvquQtngmtV2ImKWfVXGZjguvkuaiYtJhe6+Kvuc48sJrCQoNmmIB49uIH3ipOJSkGwhj/nsiZLL2j1l91paVVFyEPZXQHJ8xuyoLR2yCmtXyvBN4XbtxTQb49+5SXLzH8XUK0SvGYX/LPcRhSzqeqCG6bz/upIJrayfiaaeua+vLxA2ik9H8Wyuqp0vbi4n6pp8q7FsKuIgoel5W3rGvBdTkRvoSIUXwF5hRtPyHhI5M11BGRS3chYEDWk8v6bMeC/zX5bIgH+t2DMB21dPlhCMb+YZ0WtgrHJuf8NsCTLb93xr99VVbVqED0w27vKZmaZROhaG+nHL9mbLr7kO4Pw5i5NPSVwkhrO+WtN3R9hll407n7dnBt9soDjt9X8cT1cJOoJBAVfdmmmalLdfWl6uMT0OjOT8xe77b9scU6qgXEOUdv1Nx3RuANxSM7Y3FtQCncMWS9gsw8jfwH0lLuUQETtK8xBrDnm2f9UfAJ11elH46IQNyAfFvPMKNZPvzZeOdiGQj35BOoYwKKeIvE9l3xT/Sk4gfZKnccFtfKzBTi/4brq652jPph3Eb8FhrV+FwqaEehWtvxcinpduJp6VfVrQ7j3A3ftj2vWM1vpLrb0roCxWjmiq/qw6urTNqurZa7Xs2mqndvMRTw7OEC/EA23W06NvDEGfcNCVd75rJXGlh+t3EE+arbL+kRpviZ/1zYf2jrM1axPf7VsIFeRpwqedgQ5eNfEO6GPljiVqpBzpJGSjkbY8G/mO7UsVPs2rR/6js5qDI4pTbsjUlvReYZrurgqWkA4hkpH8Rbpeze3Rh9BUG2RSFDsz/EhE67TPqru6P5A7qSkXbJYl/j5cTN5ibexjv/fTp2urQ1yRqGs2CC2Ne4oZ6JYVFyLKnCEl3A69u/9tLawG32V6lpO0CRCTMLsBriN/Eu4iw4q7hphql6k6FG+qbgUNslxZDn6hkI9+QLkb+HmDV9tlDesS9q+KH0ZcWvaQ/AJu3G+fky7yizoxL0ssJF8I2xBPIl23fVNGmGAbZimlel4i3Lw2DVHflTKCemFSauV1BFNUuzqi76uZIuo9ZXWKFy1a2/V9CRqH933d929eWtL2cPl1bqX2/RvOzZf2WuTD6XQuQ9BPiaeViZt7UJttesWwsqe1J5cN1pcqrpCWAHYiotueBzzjV453TyNE1zelmKGb5MTvC3aruqv1q0c/bafZt++n0qF6J7Xsl/YLQVX8vsCozy6h1o0kYZN/qmGkm+WniCWRXj0xcK6WOoSlhA9t/L4xjNWK2uDMxS1+v5Lqb9nvRNqP5TWYazcur2lYY8YW6HUt8hlgLeEBS+1rAZ0rarUbceO8E7qz5t9/il3Vn6+0oiqTvQCxqnwXsMNZPlMNONvJ9oJFCR8d1OOUOSbvbPqWt3W7AXRXd96tFv4CkhTwylroVBz5fWcO2GfyDxMzry7bbC1V3okkY5Ctsf7LGNTpxC+ETX6d9nKqusvQy4AlHfD+K9Pl3EeX+vlW2sGf772mdpGXYnyeKUqxn+/6yAUv6hO0j0/b2tn9aOPbliu+iidFshT4uA9ziyM5dksjb2JMoUNOR9BR5qKTP02EtAOi4FmB7bUVOyc7ArxVaQYvUWT8gbt79lm/8PrG+9BfgLcCWbZOkxkJ9443srumCmpX/a6Vl/4eZLoz1iBlyaVq2pLXpQ4te0kFErPIHnRKhkjH6FnC57aNK2k4njOYviEo6I65d4bPtOwyy6nssQ9Jqtu/ocqyq3OEfiH+Hh9P3/WvCBbMmoTD5/pK2VxNx6acToY/3SLqvphtixuftsKBZ+V0UjOaOxCL5K4DVayy6HkC4ACcTGuvfJiKYTgGOtP3XqrEX+ppEjwuoqd26aew7AFNsv67k3CZ/F5uUHfccWAIwz+S703f5v2TEN1RUqWm1Pd/2pSM66SzP2pcWve2jJT0FXCGppZb5FPAV2yeUtSWycFuGfeGyEztwLHBxusm0h0EeW9F2bo3Mrh1B2QJoNwPfOlxx3QVsP5y2dyPCNY9RhDXeVNH2EWBZolzfEkQJwbo35CZVtLB9F5Gk99mC0bxWUqnRBPYhnpr+ocjDuBvY2NUVtGJgJWsBddqnsV8PXC/pYEbKM3SiVaNglqFQIeRW14hL+pntd9c5d7yTjXx3GgsdOTRqynRqZpFntb2eRmrRfxT4P0mVWvSOmOfvtNwknW4M6lCn1TMrUfWM7RMlPUzovbya+G7uAL7oijBI4JWMzLQd0TUlRUfUPelFVN+oitfbDGjJA09XhfqvR2r1fC5FQU1SFACpKo3XdxWtDuPoxWj+t3XDtP2ApD/1YOD7XgvoMm5L+jFQlvR3HyPlCMaCyoI2E4Vs5LszSWMvdNRtBtuXFn2hfdmsv1OdViS9jTB2q6VdtwNftX1+jeudB9Re+Cxwh/uXfi3z93daJynyG0lnEqJxLyTdiBVlBCvlIpIv/yRCr2dJwn1yrKSXlrmJmFllqVhhifS+r0LTNY3mcpK+UXi/TPF9yWI+NFwL6ELVU8tzbibmVoc5xk+djXx3ZofQ0Sx/aOquRf96j44WfaeydB8gClt/gpkRL+sRdVSXs31i185CImCy27JTJf0PUaLv0L4GWbFAVxYxUoMDCMO8DPG9tmLAlyZ813XHuEQMxd8EvqnqKlm1hOm6uPFKm1QcP7jtfa1ZPDReQO3abcXxWcJuJa1EuIt2st3uPs2UkBdeB0inBSaFUuGYadF3ueYdhLFrL1f3IuB3trvqoKe1g/XaF4qTf/sW26uXtB0hOdDLol7bzHQWKmanfaPw53wW2I+ZYllTgW+6RAOmx2v0tPBYFU3Udu7CAO6tbmqxfa0FVHUvRylgM9tVoZtIeglxM94FWINYHP+57Vv7GXtb3zc2eIocV+SZfAkKHfh9CN8xxCPriaNoeDvNwCYxtlr0na6pToucth+v8lEDL+gUCZT821UL1Cc3WNSrPRttR7NK/pqIVrmMyIx8vKT5gYT7bH3b96X+Xg6cIOlA21WLzbWG2GHMZUbzRZUdSh8i3HELpfdPEe64b/cysB7WAspkl6skmfchbiTLAmcSOv+/aPj01s4ho9jXUJNn8l2QtBERBnkiETUiwgh9ANjOPWTPqUGpNo3Uol+x2yO/pO1cI4FE0vG292vb9wdgH7el6CuySb9ne4OS/q4FdrF9T9v+VYhs3a7JQWqQFTnapCifPYlw0O1LzrsR2ML2Y237lwAuHo3ZYZenrb5DAyV9mpg07Oek85NuTMcBf7D9xT7H2fUJIq1P9FQlrND2OWJS83Hb16V997okE7nQtlNUDtSIzJmoZCPfBUkXEDOdy9v2bwIcavttJW37rm+p7lr0VxPRNR2zRBvGFr+ekCc+iZFx/XsAuzkVM+/S9m1E1MUX29oeRohgdV24lXQTsbB9ChFzPqWHH3OpDon7THqp+h4l3dbNBVV2rOkYGhrNPwFruU0FNT1F3Wx71T777ZqPoJE5AT2FKyY34fbEbH5pYja/Z8WidqvtTcQTz0+AXxK5KjOYDQu6Q0d213RnpU5hYrZ/K6nrQmSiSam2k4mFpwuAT/f7w+4F27+TtAEhMrZn2n0H8NqqxV7bFyiEwg4GWpLLtwPvrvKdNlzU24jIzj2NWJhuUtUIAIX8Q9Vvoiz6ZrQKuXT6LOeQwm17NZrEDHYWmWtH1mpVXdrSfkuOFT9DT+GKyV3WCgdejvDLP6JIvDvbJZnBbX9TPyH+jn9CPGV1lWOeyGQj352yMMRONUJH4D5LtRVmP/MDKysEy+po0fedQJJcDS+yfXjb/tUkTXNBq6XLmG8jZv094/4TfJYGtkjn70Jo/Zxm+/aqa6qzyuELCWNSVbWoFQY5S7dUhEEq8h+eb0XzpPWWtwN/aXO1darQ1LfRBB6StLlnTcbbjFjvKRtzv2sBZTkBlaSJw8rArY5yjcdIWpWQ3yil7W9qR+JJ8aukoutzGtld0wVJjxJ+4lkOEaJHS5W0bSLP2pcWvaTbKSneXfaYKul04Nu2r2jb/wbgQ7Z3KWl7EuXKiu/r1rakTxGFKmqFqqbvdWfiR/x528dXnN+ucmjgcUL+4Ve9jrcukq4A3ueQQlgZ+CPhJlsN+KPLqzt1lUSocd1XE5IVv2OkS21jYJuyG2O/awGSphGTIRFyHi0t+MrCLJK+TSTW/Z644f3Sdllx9fb2yxI3g22JGP8z6VE+eyKRjXwXJJXOTN2WNdrWtkmptr606JuEhEm6rtsCaZWfWVInt8HyRBTK3LaXK2nbKMY+Gfd3EAZ+BeBcQqKgqzbQIJF0q+010vYRwOK295U0H3B961iXtn0bzdR+fuKJpxVjfgdwatUTYpO1gH6RdBuxhjAtPf1c6frFSX5L/H7OJATsRkRKuSLQYUJiO78qXkSa/MI9nD838BUiLO96Ijrn78Qj4zwVbe8h3Xw79HlPSbvjG3y+P/VzrMO5Lye0d+4GPgTMV3H+9V0+61zEE09Z21PS9/pFQqSr18/8NiJM87H0+i3w9jH+O7qlsH0VIdHcen/zGF73AGD9qr+9Lm1vKGz/bCy/n07X7PS+ou39hCzCfcC9hdd9wL2zY/zD9so++RL6jS12n/KsM5u7Hy36ayXtXtLpKd2OAZMlvd1tkTApcqaytF5a6Po0EWJ6FKGEWWeRq+8Ye0JY7GlCpuGjhdPruAP6zvBtyC2SjgYeIv4uLk7jmTRG12uxHLEu9EpFDeFWkfnfu3pm22QtoF+K60sCVkrv6wiUrTAbxjeuyEa+C4XY4k3dFlusiG+vjC126Jzfmn7EuygkC15FiX43/WvRd4tH35pIKikz8gcAv5K0AyN9thsBW5W0Q9JPCdXJYwgXzTRg0ZbRrTAi/5G0ijvH2Jdq2dueq+x4BQcya4bvb9JN7XdEbsRY8AHiprQCsKVn1ixdjYoEoSbYPggguYXWI/6u9wJOlPSE7dXKmnfZHku6Zlj3g+ZwSYTsk+9C09hi9V+qrW8t+kIfAnYlsvruAL5ku1uSSKvNC9JYW/7324GftH/+Du3up1B2j5EzP7u8lF7fMfZd+luIWGzb2fY7Ss67012kGsqONUXSIcDRrlHOcYyuvxhx4944/X8SEb2yV0mbRmsBg0JjKIkw3shGvguS7nKXghdlx9LxxpmcGqlFf4draNGnyJw9gYOAa4D/tf2nutccBClE9GBG3lyOqvtjTLPTdxA/5rcQi20/d4nMsRpk+DZB0vHA64F9XVL7dgyueyLxt/QkkVNwDXBN+9/PsKAGshOaVRLhTEISYbZnUQ8L2V3TnW6xxZtTEVvMKMizukctekn7Eq6AS4G3uqIUXRHNLGzdZSheqaRtaSif7RsqjvcVYy9pS+LHvCXx4z+F0JPpOist8HGiDm3HDN9ex1IX2/ul7+t4RWLPCcD0wvHS76oBLyUqQt1DrAdMITKwhxLbs8hIa6bsxHeIZMNuHE9kh+/imZIIc/RMNs/ku9Aktji176tUWw/ju9GFkElF5uKjRBRPp8XMsmSo9qSWuQiVwYOIyIau2ZWSLisZpm1vVtK2PdFmxozN9o9L+m193iuJdPeWUFgtSYR07tLAhxkZUvgtj46cc9W1NyWeOG6l4Ooq+65G4ZoiPmtLLmN14B+E6N1nx+q6o01VjoAaSCJMVLKR70JKVlkaWJWRhuBPwF9t/7mHvmrXt+yhz/YaoasQJekebDt1eSI2f3KNPucC3ku4T24iinmXldnrZbxb2L6kbV+nRJvFidn0PS6Jk1fUZt2J+EHfS7jFDrddquk+SBQFRo4holQ+3O4umk1jWI6YqLyOWFR/ke1Js3sc/aCQnbi+bMLSdn5LEmFnIkLubPdfOH7cko18FySdBxzW7huWtAZh/HouT5ZmU7UzOSv6ajfyfY83/Xj2JqJOfkfUha28KTQZb8W5cxM/5rVrnv864of8buBm4sdcVuikOIMecYgxVCpMbrH/Jfz+7fr769u+doyu+1FmzuCfJ4VPptetZYEAg0DlshO/c4luv6T9nDKeJb269cStJIlQ1naiko18FyRda3v9LsdmZC720W/tAg8V/bS7a/oer6QpROGLrwOzZDe6hoRxr+Otcf5NZUZeBWnl1iJ0ehJ5M/Fj3rukbWu2L0LzZoQchMdIqVDSEi7oAElajbg57Qw84RJZ5obX/RopNt521/WkTov5g0ANZCfUQP5hopIXXrszqeRYqchYBT2pJaqLFj2zilhNKummary/Jn5Ia6VXERMhnU3pVOpw8Q7nvZCoZ1slNPbpwrguBdZJM9KL06v7QApGXNKzY2XUO1z375JWYKZhfx54GVFZ6/4xvG63ouftzFJYfhDUXDyvQ2Nl0olANvLduU7SB2x/r7hT0vtpUJWIioQStWnRE5ECT5C06EkyxZ41yajv8dres+7gR5nrGRlb35qxXUbIIpShLttDi6SrgUWJ9YN3O4TK7htLA98jQ/E9qpmm0SRJ2xLBA4u2u35G46l0vJGNfHcOAM6WtCsjo2vmIxJuutIhamTGIapLtfWrRd9kvKUzPdtfqxhzHe7v0G+T2OUFJL2G+DHPn7ZnGKmycMS2sM8FemnbkEeI+O2lgCWIkMZh8pcOy1g2IyQn2vkecAtQZuR/S2R5Q2gTFdeiRuupdFyRffIVSHoThUQd16ix2iVqZAYuL9XWvqC6p1Oxa0nXu0KNr8/xlobQuaS2pqRP2D4ybW9v+6eFY1+uimZIIW+7MLKO7mkur7PaNHSz77ZNUWSdbke4a1Yh3Gxvsf3HsbpmXYbFh63y6lu3exSkCSTt4RIl2YlENvJjgJqVautbi36skXSY20oXli101YhpfhWR8HURcCPMqKO7BbCZo/hD0zHPEro5O9rW7H9JImJkJ+Clg47l7nVxfAzH0Xfd4B6uMRQ3tNlBE5GnTHfOaW1I+lmPbc8CvqvQ0W71sRCR6VdVtWis6ZRpWOYbr/LxHgHsb3tP28fZ/rrtPYgygl9qMM4iXx1Q21IU1bhs+5u2NybkDmYLkpaV9NL0KrpsO1WkGgSHAxdI2lPSGum1FxEJdXhF27oMxfrD7CAb+bGhiTzrZ4jM1QckXS/pBsKf/Wg6Nkg6/TDKVAqrHhPXsH3mLB3aP2Omy6kpTX7Mo2oIFHxOUcv2buBuSX+XdPhYRvhIOkxS0TheDZxHRCEd3NrZYTF/INi+gBDzexNR8/hkYFNisbon0bqyy4xSP0NPXngdG/qWZ3UzLfqxptNnadU8FbGI2ap/WlnzlPJauZV1dGvS5Mc82obgQCLbdH3PlGJ4OXCCpANtHzvK12vRpLD8bEdRxeqR9FRX3L+EpPldXe+41mVGoY9xQTbyY0OZ4bNryLO6Py36sWaWH4btuTudWJMlu0T2iIg+mWi8F9jC9mOtHbbvVdQKuBgYKyOP+ywsPyC+AVzIrJEwrycE6bqG1xaT5CqYbSqggyYb+TGgoeFDJVr0jQfX+XozUsEr+Gn7ji4JTTOocAF8j/hsnfh+jfHU4f4Bte3EvEUD3yIlSc07ytcqsrCkeVuL+YVorRcQcfvDxrq292nfaftsSVXFeopJcl2xvV+/gxt3eAhqEObXzBfwE0Jk7AdElMncwH1jfM3aNTQ7tJ1OSCEUa2nOqLE5hmP+RGF7+7ZjXx6rtmP1PTf5N6hx3S8DPwQWLOxbCDiJqDkwZn9bfY73zn6OjfX3OF5feeF1+JhFi57hXiT6BjHeCwk99pfbXjG9ShedJZ1Z2P5q27FSaQIi7LDFYW3H3jqGbZuwlqR/d3g9SVQvGiuGeTG/E49KmqVwi6T1CSntMl4p6ZYOr1s1s27sHEV21wwZttfWTC36X6dIjEUkLeVR0qLvwJqFdYMilWsItg+QJCL64b3AN5OBPsFpcbGEYsz/FkS5whZVPvkmoZtN2vaNG7rxGlx3mBfzO3EwcKakkxmZvb07I2/QnbiPkVmuczzZyA8hjiSgzwKf1Uwt+msljYoWfQdudYMkGMdz8mWSbiR+hEcQKfvfK21Y/oRS9fTSJHSzSdtxi4dzMX8WbP8xzeQ/zsyqYX8GNrT9aEXz5zybBOfGC9nIDzm2rweul3QwI8PghoKUqLUNkbm5BLHota7rZfwuWNCfKWrItIpGl9EkdLNJ23HJ7F7Mb0JK0DqIqHHQ+jvaNA7pU27LBm9jjomaqUuWNRhHaJS06Dv0+0nbX+6z7dPErP10OghuuSScrUJDBttv6mdMmZFoFArLz04kHUvchA60/WTatyhwNPAf2/uXtN2Dkqcx26eM8nCHnmzkxxGSHvQY6JtI+kbZcdsfLWl7MuVFwLsW76hLJw2ZJqGbDcM+xx2SbiKelk4BTrc9RT3Uw53dSLoHWNVtxiklb93lEv0mSd/scmhrYFnbc5z3Ihv5ccQYzuSfA24jih4/TNvio/tU6xutxeJOYlKKQt6tilYwcswuM2BN2o5XNMaF5UcTSXfbXrXXYx3OFbArsaB/B/Al23NchM0cd1cbdtRMi75fliFS33ckDN8ZwFm2n+i1o7So927C9ztai3qdIl6+QWibXAWcRtT+rDtjadJ2XDKAxfwm3CFp93bXSsoMrlQmTT79PQm//jXAe2z/aSwGOh7IM/khQw206Efp+ssRETIfAw6x/X812nRd1PMoFInuNJNP+1uhmzsDGxA+5zqhm43aThTSdzAqheVHE0XJy58D/2FkCOUCwLa2Hyppuy+wP1HK8KsenqpbAyMb+SFDDbToR+Ha6xBGbwvix3WM7Tsq2oz5ol43I184PomZoZufdFsJxIq++247ERgrF+BoIGkzoFUg5A7bl9ZoM51I8vo7HZ6Iba85qoMcB2R3zfBxDqmYsqSf2X73WF9Q0heAdxBZtqcDh3lmwfAqZsnQlTTaM4f723c0Cd1sGPY50RhaNUZHVbPKymZtvIIor/hg2/7lgb+NxrjGG3kmP2SoUJ1Hs6lST5r93Ac8k3a1/igETLe9VkX7vhb11KB0YMPQzb7bTjSGeSbfD5LOIyYpt7btX4PQJZrjsmGzkR8yVFJObwyv+bJOu4nZz2G2395DX+sSvvntgdJFvbLPWsNFczJ9hm7OjrDPYaJiMX8z2wvN5iGNGZKutb1+l2O32h5LjaChJLtrho/GWvS9UkwDT1mnLSN9H9BT+cJChu5BVGfo9q0hY3vPrp2GHsuYtB2nHN3nsfHIpJJjw6idP+ZkIz9kDELEStKqhLtlZ8LdcgbxlFeZcaqRZeU6URa5MWoaMk1CN8co7HOYuG8OWm+4TtIH2hfQJb2fmZE6cxTZXZNp+eSvBN5ne3LaVysjUtLHO+xeCHgf8CLbC5e0nUaU+Wtp1bTWBATMb7u0kEaT0M2xDvscJtrcYrNlMX9QpCexs4HnGBl+OR8RfjnHLb5mI59B0ruIMMKNCV3404Hv9xoGKWkRIkb5fUT27DGuVg3siyahm+NNy6Upg1jMHzSS3sTMYvC3p0idOZLsrslg+xzgnEJo4QFE/dUTgLNtlxbwSFowHyNSyH8ErGP7n1XXbagh0yR0c3aEfQ4TfReWH6/YvgwoFcCbU8gz+UxHJL2QJHVge/OS844CtgNOBL5l+6kertFIQ6aJHst40nJpSoVbbEwW8zPDQzbymUYkQ/0sYaiLf0yVBkTS1xklDZleQjdHs20mM+xkI58ZKKOtIdNEj2VYtVwymSZkn3xmoKSZe8+lA5uEbjYM+8xkxhXZyGcGRkMNmac77JsRugl8YYzaZjLjiuyuyQyM0dKQaRK6OTvDPjOZQZBn8plB8lPCsL8ivYqYmNl3pd/QzaZtM5nxRDbymYHRREOmLXRzjR5DN/tum8mMN7K7JjM0tGvI2O6qIdMwdLPvtpnMeCMb+cxAmZM0ZDKZQTDXoAeQmXNJGjJ3E+UGvwmsAPzT9uXZwGcyo0M28plBMouGDHOItkomM7vIRj4zMGyvDexAuGh+Lel3wCITtHBHJjMQsk8+MzRkDZlMZvTJRj4zdGQNmUxm9Mhx8pmBkTVkMpmxJ8/kMwOjSenATCZTj2zkM0NB1pDJZMaG7K7JDJSsIZPJjC3ZyGcGRtaQyWTGnuyuyQyMrCGTyYw92chnMpnMBCZnvGYymcwEJhv5TCaTmcBkI5/JZDITmGzkM5lMZgLz/1VEKCJIAMUcAAAAAElFTkSuQmCC\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.heatmap(crecord.isnull())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 288
        },
        "id": "buS2FlG_5ELQ",
        "outputId": "e45f44d7-dfb9-49b6-ee17-18845e505fa3"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<AxesSubplot:>"
            ]
          },
          "metadata": {},
          "execution_count": 9
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "app = app.drop_duplicates('ID', keep='last')"
      ],
      "metadata": {
        "id": "dv_Eq8f_9pzD"
      },
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "app.drop('OCCUPATION_TYPE', axis=1, inplace=True)"
      ],
      "metadata": {
        "id": "BDnX_NZc-PMG"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ot = pd.DataFrame(app.dtypes == 'object').reset_index()"
      ],
      "metadata": {
        "id": "9peTeaoL-2u0"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ot"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 582
        },
        "id": "ZOyWNOisOI7w",
        "outputId": "0e56f8ae-8116-48ce-8aec-96c6aefc3758"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                  index      0\n",
              "0                    ID  False\n",
              "1           CODE_GENDER   True\n",
              "2          FLAG_OWN_CAR   True\n",
              "3       FLAG_OWN_REALTY   True\n",
              "4          CNT_CHILDREN  False\n",
              "5      AMT_INCOME_TOTAL  False\n",
              "6      NAME_INCOME_TYPE   True\n",
              "7   NAME_EDUCATION_TYPE   True\n",
              "8    NAME_FAMILY_STATUS   True\n",
              "9     NAME_HOUSING_TYPE   True\n",
              "10           DAYS_BIRTH  False\n",
              "11        DAYS_EMPLOYED  False\n",
              "12           FLAG_MOBIL  False\n",
              "13      FLAG_WORK_PHONE  False\n",
              "14           FLAG_PHONE  False\n",
              "15           FLAG_EMAIL  False\n",
              "16      CNT_FAM_MEMBERS  False"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-4b88434c-5e00-4f21-b92b-46a9aa30f4d6\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>index</th>\n",
              "      <th>0</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>ID</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>CODE_GENDER</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>FLAG_OWN_CAR</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>FLAG_OWN_REALTY</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>CNT_CHILDREN</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>AMT_INCOME_TOTAL</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>NAME_INCOME_TYPE</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>NAME_EDUCATION_TYPE</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>NAME_FAMILY_STATUS</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>NAME_HOUSING_TYPE</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>DAYS_BIRTH</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>DAYS_EMPLOYED</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>FLAG_MOBIL</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>FLAG_WORK_PHONE</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>FLAG_PHONE</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>FLAG_EMAIL</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>CNT_FAM_MEMBERS</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-4b88434c-5e00-4f21-b92b-46a9aa30f4d6')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-4b88434c-5e00-4f21-b92b-46a9aa30f4d6 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-4b88434c-5e00-4f21-b92b-46a9aa30f4d6');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "object_type = ot[ot[0] == True]['index']"
      ],
      "metadata": {
        "id": "UQbWd7PxB4zb"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "object_type"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HN0gR-C7B6hB",
        "outputId": "bac34130-a585-4534-c264-20e919edc9b8"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1            CODE_GENDER\n",
              "2           FLAG_OWN_CAR\n",
              "3        FLAG_OWN_REALTY\n",
              "6       NAME_INCOME_TYPE\n",
              "7    NAME_EDUCATION_TYPE\n",
              "8     NAME_FAMILY_STATUS\n",
              "9      NAME_HOUSING_TYPE\n",
              "Name: index, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numtype = pd.DataFrame(app.dtypes != 'object').reset_index().rename(columns = {0: 'yes/no'})"
      ],
      "metadata": {
        "id": "YQ3hV_7RDcdI"
      },
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "numtype"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 582
        },
        "id": "RvzLa_9RMpVJ",
        "outputId": "532a67a6-7801-4668-a821-8532fa3c1b21"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "                  index  yes/no\n",
              "0                    ID    True\n",
              "1           CODE_GENDER   False\n",
              "2          FLAG_OWN_CAR   False\n",
              "3       FLAG_OWN_REALTY   False\n",
              "4          CNT_CHILDREN    True\n",
              "5      AMT_INCOME_TOTAL    True\n",
              "6      NAME_INCOME_TYPE   False\n",
              "7   NAME_EDUCATION_TYPE   False\n",
              "8    NAME_FAMILY_STATUS   False\n",
              "9     NAME_HOUSING_TYPE   False\n",
              "10           DAYS_BIRTH    True\n",
              "11        DAYS_EMPLOYED    True\n",
              "12           FLAG_MOBIL    True\n",
              "13      FLAG_WORK_PHONE    True\n",
              "14           FLAG_PHONE    True\n",
              "15           FLAG_EMAIL    True\n",
              "16      CNT_FAM_MEMBERS    True"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-1b20293b-9409-4350-9e7f-942eb76c16a2\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>index</th>\n",
              "      <th>yes/no</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>ID</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>CODE_GENDER</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>FLAG_OWN_CAR</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>FLAG_OWN_REALTY</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>CNT_CHILDREN</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>AMT_INCOME_TOTAL</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>NAME_INCOME_TYPE</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>NAME_EDUCATION_TYPE</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>NAME_FAMILY_STATUS</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>NAME_HOUSING_TYPE</td>\n",
              "      <td>False</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>DAYS_BIRTH</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>DAYS_EMPLOYED</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>FLAG_MOBIL</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>FLAG_WORK_PHONE</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>FLAG_PHONE</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>FLAG_EMAIL</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>CNT_FAM_MEMBERS</td>\n",
              "      <td>True</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-1b20293b-9409-4350-9e7f-942eb76c16a2')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-1b20293b-9409-4350-9e7f-942eb76c16a2 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-1b20293b-9409-4350-9e7f-942eb76c16a2');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "numtype = numtype[numtype['yes/no'] == True]['index']"
      ],
      "metadata": {
        "id": "mOtP49EANkc_"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "numtype"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7CxOna6SN3Pe",
        "outputId": "1b996e68-8409-4202-c96c-190712db124d"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0                   ID\n",
              "4         CNT_CHILDREN\n",
              "5     AMT_INCOME_TOTAL\n",
              "10          DAYS_BIRTH\n",
              "11       DAYS_EMPLOYED\n",
              "12          FLAG_MOBIL\n",
              "13     FLAG_WORK_PHONE\n",
              "14          FLAG_PHONE\n",
              "15          FLAG_EMAIL\n",
              "16     CNT_FAM_MEMBERS\n",
              "Name: index, dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import LabelEncoder\n",
        "le = LabelEncoder()\n",
        "for x in app:\n",
        "  if app[x].dtypes == 'object':\n",
        "    app[x] = le.fit_transform(app[x])"
      ],
      "metadata": {
        "id": "EQZjF34oOfX5"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "app"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 487
        },
        "id": "gawWFD4KS0wV",
        "outputId": "72974b77-d46d-4e6c-acf2-e3aed540f985"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "             ID  CODE_GENDER  FLAG_OWN_CAR  FLAG_OWN_REALTY  CNT_CHILDREN  \\\n",
              "0       5008804            1             1                1             0   \n",
              "1       5008805            1             1                1             0   \n",
              "2       5008806            1             1                1             0   \n",
              "3       5008808            0             0                1             0   \n",
              "4       5008809            0             0                1             0   \n",
              "...         ...          ...           ...              ...           ...   \n",
              "438552  6840104            1             0                1             0   \n",
              "438553  6840222            0             0                0             0   \n",
              "438554  6841878            0             0                0             0   \n",
              "438555  6842765            0             0                1             0   \n",
              "438556  6842885            0             0                1             0   \n",
              "\n",
              "        AMT_INCOME_TOTAL  NAME_INCOME_TYPE  NAME_EDUCATION_TYPE  \\\n",
              "0               427500.0                 4                    1   \n",
              "1               427500.0                 4                    1   \n",
              "2               112500.0                 4                    4   \n",
              "3               270000.0                 0                    4   \n",
              "4               270000.0                 0                    4   \n",
              "...                  ...               ...                  ...   \n",
              "438552          135000.0                 1                    4   \n",
              "438553          103500.0                 4                    4   \n",
              "438554           54000.0                 0                    1   \n",
              "438555           72000.0                 1                    4   \n",
              "438556          121500.0                 4                    4   \n",
              "\n",
              "        NAME_FAMILY_STATUS  NAME_HOUSING_TYPE  DAYS_BIRTH  DAYS_EMPLOYED  \\\n",
              "0                        0                  4      -12005          -4542   \n",
              "1                        0                  4      -12005          -4542   \n",
              "2                        1                  1      -21474          -1134   \n",
              "3                        3                  1      -19110          -3051   \n",
              "4                        3                  1      -19110          -3051   \n",
              "...                    ...                ...         ...            ...   \n",
              "438552                   2                  1      -22717         365243   \n",
              "438553                   3                  1      -15939          -3007   \n",
              "438554                   3                  5       -8169           -372   \n",
              "438555                   1                  1      -21673         365243   \n",
              "438556                   1                  1      -18858          -1201   \n",
              "\n",
              "        FLAG_MOBIL  FLAG_WORK_PHONE  FLAG_PHONE  FLAG_EMAIL  CNT_FAM_MEMBERS  \n",
              "0                1                1           0           0              2.0  \n",
              "1                1                1           0           0              2.0  \n",
              "2                1                0           0           0              2.0  \n",
              "3                1                0           1           1              1.0  \n",
              "4                1                0           1           1              1.0  \n",
              "...            ...              ...         ...         ...              ...  \n",
              "438552           1                0           0           0              1.0  \n",
              "438553           1                0           0           0              1.0  \n",
              "438554           1                1           0           0              1.0  \n",
              "438555           1                0           0           0              2.0  \n",
              "438556           1                0           1           0              2.0  \n",
              "\n",
              "[438510 rows x 17 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-d0826e09-e603-45eb-a64c-072d62adbaa8\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>ID</th>\n",
              "      <th>CODE_GENDER</th>\n",
              "      <th>FLAG_OWN_CAR</th>\n",
              "      <th>FLAG_OWN_REALTY</th>\n",
              "      <th>CNT_CHILDREN</th>\n",
              "      <th>AMT_INCOME_TOTAL</th>\n",
              "      <th>NAME_INCOME_TYPE</th>\n",
              "      <th>NAME_EDUCATION_TYPE</th>\n",
              "      <th>NAME_FAMILY_STATUS</th>\n",
              "      <th>NAME_HOUSING_TYPE</th>\n",
              "      <th>DAYS_BIRTH</th>\n",
              "      <th>DAYS_EMPLOYED</th>\n",
              "      <th>FLAG_MOBIL</th>\n",
              "      <th>FLAG_WORK_PHONE</th>\n",
              "      <th>FLAG_PHONE</th>\n",
              "      <th>FLAG_EMAIL</th>\n",
              "      <th>CNT_FAM_MEMBERS</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5008804</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>427500.0</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>4</td>\n",
              "      <td>-12005</td>\n",
              "      <td>-4542</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>5008805</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>427500.0</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>4</td>\n",
              "      <td>-12005</td>\n",
              "      <td>-4542</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5008806</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>112500.0</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>-21474</td>\n",
              "      <td>-1134</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>5008808</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>270000.0</td>\n",
              "      <td>0</td>\n",
              "      <td>4</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>-19110</td>\n",
              "      <td>-3051</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5008809</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>270000.0</td>\n",
              "      <td>0</td>\n",
              "      <td>4</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>-19110</td>\n",
              "      <td>-3051</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>438552</th>\n",
              "      <td>6840104</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>135000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>4</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>-22717</td>\n",
              "      <td>365243</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>438553</th>\n",
              "      <td>6840222</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>103500.0</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>-15939</td>\n",
              "      <td>-3007</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>438554</th>\n",
              "      <td>6841878</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>54000.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>5</td>\n",
              "      <td>-8169</td>\n",
              "      <td>-372</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>438555</th>\n",
              "      <td>6842765</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>72000.0</td>\n",
              "      <td>1</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>-21673</td>\n",
              "      <td>365243</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>438556</th>\n",
              "      <td>6842885</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>121500.0</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>-18858</td>\n",
              "      <td>-1201</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>2.0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>438510 rows × 17 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-d0826e09-e603-45eb-a64c-072d62adbaa8')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-d0826e09-e603-45eb-a64c-072d62adbaa8 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-d0826e09-e603-45eb-a64c-072d62adbaa8');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 21
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "fig, ax= plt.subplots(nrows= 3, ncols = 3, figsize= (14,6))\n",
        "\n",
        "sns.scatterplot(x='ID', y='CNT_CHILDREN', data=app, ax=ax[0][0], color= 'orange')\n",
        "sns.scatterplot(x='ID', y='AMT_INCOME_TOTAL', data=app, ax=ax[0][1], color='orange')\n",
        "sns.scatterplot(x='ID', y='DAYS_BIRTH', data=app, ax=ax[0][2])\n",
        "sns.scatterplot(x='ID', y='DAYS_EMPLOYED', data=app, ax=ax[1][0])\n",
        "sns.scatterplot(x='ID', y='FLAG_MOBIL', data=app, ax=ax[1][1])\n",
        "sns.scatterplot(x='ID', y='FLAG_WORK_PHONE', data=app, ax=ax[1][2])\n",
        "sns.scatterplot(x='ID', y='FLAG_PHONE', data=app, ax=ax[2][0])\n",
        "sns.scatterplot(x='ID', y='FLAG_EMAIL', data=app, ax=ax[2][1])\n",
        "sns.scatterplot(x='ID', y='CNT_FAM_MEMBERS', data=app, ax=ax[2][2], color= 'orange')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 416
        },
        "id": "-gCTRNbvS2Sy",
        "outputId": "be0a37d8-6d3e-4cb4-c5c5-8ad98b4cc1ba"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<AxesSubplot:xlabel='ID', ylabel='CNT_FAM_MEMBERS'>"
            ]
          },
          "metadata": {},
          "execution_count": 22
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1008x432 with 9 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "There are outliers in 3 columns.\n",
        "\n",
        "1.CNT_CHILDREN\n",
        "2.AMT_INCOME_TOTAL\n",
        "3.CNT_FAM_MEMBERS"
      ],
      "metadata": {
        "id": "hU_42AreWx5f"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "q_hi = app['CNT_CHILDREN'].quantile(0.999)\n",
        "q_low = app['CNT_CHILDREN'].quantile(0.001)\n",
        "app = app[(app['CNT_CHILDREN']>q_low) & (app['CNT_CHILDREN']<q_hi)]"
      ],
      "metadata": {
        "id": "kzvsaVGpWICP"
      },
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "q_hi = app['AMT_INCOME_TOTAL'].quantile(0.999)\n",
        "q_low = app['AMT_INCOME_TOTAL'].quantile(0.001)\n",
        "app= app[(app['AMT_INCOME_TOTAL']>q_low) & (app['AMT_INCOME_TOTAL']<q_hi)]"
      ],
      "metadata": {
        "id": "ZeXncy-KXF6d"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "q_hi = app['CNT_FAM_MEMBERS'].quantile(0.999)\n",
        "q_low = app['CNT_FAM_MEMBERS'].quantile(0.001)\n",
        "app= app[(app['CNT_FAM_MEMBERS']>q_low) & (app['CNT_FAM_MEMBERS']<q_hi)]"
      ],
      "metadata": {
        "id": "FP0pGB7YXH2F"
      },
      "execution_count": 25,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "fig, ax= plt.subplots(nrows= 3, ncols = 3, figsize= (14,6))\n",
        "\n",
        "sns.scatterplot(x='ID', y='CNT_CHILDREN', data=app, ax=ax[0][0], color= 'orange')\n",
        "sns.scatterplot(x='ID', y='AMT_INCOME_TOTAL', data=app, ax=ax[0][1], color='orange')\n",
        "sns.scatterplot(x='ID', y='DAYS_BIRTH', data=app, ax=ax[0][2])\n",
        "sns.scatterplot(x='ID', y='DAYS_EMPLOYED', data=app, ax=ax[1][0])\n",
        "sns.scatterplot(x='ID', y='FLAG_MOBIL', data=app, ax=ax[1][1])\n",
        "sns.scatterplot(x='ID', y='FLAG_WORK_PHONE', data=app, ax=ax[1][2])\n",
        "sns.scatterplot(x='ID', y='FLAG_PHONE', data=app, ax=ax[2][0])\n",
        "sns.scatterplot(x='ID', y='FLAG_EMAIL', data=app, ax=ax[2][1])\n",
        "sns.scatterplot(x='ID', y='CNT_FAM_MEMBERS', data=app, ax=ax[2][2], color= 'orange')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 416
        },
        "id": "83kDEqi-Y2u3",
        "outputId": "ad23df31-f2b9-4fba-97b3-70844a763d69"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<AxesSubplot:xlabel='ID', ylabel='CNT_FAM_MEMBERS'>"
            ]
          },
          "metadata": {},
          "execution_count": 26
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1008x432 with 9 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "crecord['Months from today'] = crecord['MONTHS_BALANCE']*-1\n",
        "crecord = crecord.sort_values(['ID','Months from today'], ascending=True)\n",
        "crecord"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "XD9Bl3tXZA41",
        "outputId": "5a6c385f-f78c-48b9-8c7b-008e5bfc3486"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "              ID  MONTHS_BALANCE STATUS  Months from today\n",
              "0        5001711               0      X                  0\n",
              "1        5001711              -1      0                  1\n",
              "2        5001711              -2      0                  2\n",
              "3        5001711              -3      0                  3\n",
              "4        5001712               0      C                  0\n",
              "...          ...             ...    ...                ...\n",
              "1048570  5150487             -25      C                 25\n",
              "1048571  5150487             -26      C                 26\n",
              "1048572  5150487             -27      C                 27\n",
              "1048573  5150487             -28      C                 28\n",
              "1048574  5150487             -29      C                 29\n",
              "\n",
              "[1048575 rows x 4 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-f5bf85d3-f0f5-422f-8d32-6392f658d501\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>ID</th>\n",
              "      <th>MONTHS_BALANCE</th>\n",
              "      <th>STATUS</th>\n",
              "      <th>Months from today</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5001711</td>\n",
              "      <td>0</td>\n",
              "      <td>X</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>5001711</td>\n",
              "      <td>-1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5001711</td>\n",
              "      <td>-2</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>5001711</td>\n",
              "      <td>-3</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5001712</td>\n",
              "      <td>0</td>\n",
              "      <td>C</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048570</th>\n",
              "      <td>5150487</td>\n",
              "      <td>-25</td>\n",
              "      <td>C</td>\n",
              "      <td>25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048571</th>\n",
              "      <td>5150487</td>\n",
              "      <td>-26</td>\n",
              "      <td>C</td>\n",
              "      <td>26</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048572</th>\n",
              "      <td>5150487</td>\n",
              "      <td>-27</td>\n",
              "      <td>C</td>\n",
              "      <td>27</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048573</th>\n",
              "      <td>5150487</td>\n",
              "      <td>-28</td>\n",
              "      <td>C</td>\n",
              "      <td>28</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1048574</th>\n",
              "      <td>5150487</td>\n",
              "      <td>-29</td>\n",
              "      <td>C</td>\n",
              "      <td>29</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>1048575 rows × 4 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-f5bf85d3-f0f5-422f-8d32-6392f658d501')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-f5bf85d3-f0f5-422f-8d32-6392f658d501 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-f5bf85d3-f0f5-422f-8d32-6392f658d501');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "crecord['STATUS'].value_counts() "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "meO1SAvNoX60",
        "outputId": "fe36daf9-3bed-445f-e0ab-17915029e3f9"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "C    442031\n",
              "0    383120\n",
              "X    209230\n",
              "1     11090\n",
              "5      1693\n",
              "2       868\n",
              "3       320\n",
              "4       223\n",
              "Name: STATUS, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "crecord['STATUS'].replace({'C': 0,'X': 0}, inplace=True)\n",
        "crecord['STATUS'] = crecord['STATUS'].astype('int') \n",
        "crecord['STATUS'] = crecord['STATUS'].apply(lambda x:1 if x>=2 else 0)\n",
        "# replacing the value C and X with 0 as it is the same type\n",
        "# 1,2,3,4,5 are classified as 1 because they are the same type"
      ],
      "metadata": {
        "id": "WMPRUdEUrGdM"
      },
      "execution_count": 29,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "crecord['STATUS'].value_counts(normalize=True)\n",
        "# the data is oversampled for the labels\n",
        "# 0 are 99%\n",
        "# 1 are only 1% in the whole dataset"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MMrVZBaGtYhy",
        "outputId": "e3f20644-c6e6-4fdb-b588-dc93775d5121"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    0.99704\n",
              "1    0.00296\n",
              "Name: STATUS, dtype: float64"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "crecordgb = crecord.groupby('ID').agg(max).reset_index()\n",
        "crecordgb"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "JUgtov_jup-o",
        "outputId": "fd691188-7d24-4202-cb65-26367c9ede24"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "            ID  MONTHS_BALANCE  STATUS  Months from today\n",
              "0      5001711               0       0                  3\n",
              "1      5001712               0       0                 18\n",
              "2      5001713               0       0                 21\n",
              "3      5001714               0       0                 14\n",
              "4      5001715               0       0                 59\n",
              "...        ...             ...     ...                ...\n",
              "45980  5150482             -11       0                 28\n",
              "45981  5150483               0       0                 17\n",
              "45982  5150484               0       0                 12\n",
              "45983  5150485               0       0                  1\n",
              "45984  5150487               0       0                 29\n",
              "\n",
              "[45985 rows x 4 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-1cfb87af-1079-40af-a825-01e81f4514d9\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>ID</th>\n",
              "      <th>MONTHS_BALANCE</th>\n",
              "      <th>STATUS</th>\n",
              "      <th>Months from today</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5001711</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>5001712</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>5001713</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>21</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>5001714</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>14</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5001715</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>59</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>45980</th>\n",
              "      <td>5150482</td>\n",
              "      <td>-11</td>\n",
              "      <td>0</td>\n",
              "      <td>28</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>45981</th>\n",
              "      <td>5150483</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>17</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>45982</th>\n",
              "      <td>5150484</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>12</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>45983</th>\n",
              "      <td>5150485</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>45984</th>\n",
              "      <td>5150487</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>29</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>45985 rows × 4 columns</p>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-1cfb87af-1079-40af-a825-01e81f4514d9')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-1cfb87af-1079-40af-a825-01e81f4514d9 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-1cfb87af-1079-40af-a825-01e81f4514d9');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = app.join(crecordgb.set_index('ID'), on='ID', how='inner')\n",
        "df.drop(['MONTHS_BALANCE', 'Months from today'], axis=1, inplace=True)\n",
        "df.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 270
        },
        "id": "knFjIGaL9T3L",
        "outputId": "400bb367-cb20-4a4b-f9a8-844a97aedaeb"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "         ID  CODE_GENDER  FLAG_OWN_CAR  FLAG_OWN_REALTY  CNT_CHILDREN  \\\n",
              "29  5008838            1             0                1             1   \n",
              "30  5008839            1             0                1             1   \n",
              "31  5008840            1             0                1             1   \n",
              "32  5008841            1             0                1             1   \n",
              "33  5008842            1             0                1             1   \n",
              "\n",
              "    AMT_INCOME_TOTAL  NAME_INCOME_TYPE  NAME_EDUCATION_TYPE  \\\n",
              "29          405000.0                 0                    1   \n",
              "30          405000.0                 0                    1   \n",
              "31          405000.0                 0                    1   \n",
              "32          405000.0                 0                    1   \n",
              "33          405000.0                 0                    1   \n",
              "\n",
              "    NAME_FAMILY_STATUS  NAME_HOUSING_TYPE  DAYS_BIRTH  DAYS_EMPLOYED  \\\n",
              "29                   1                  1      -11842          -2016   \n",
              "30                   1                  1      -11842          -2016   \n",
              "31                   1                  1      -11842          -2016   \n",
              "32                   1                  1      -11842          -2016   \n",
              "33                   1                  1      -11842          -2016   \n",
              "\n",
              "    FLAG_MOBIL  FLAG_WORK_PHONE  FLAG_PHONE  FLAG_EMAIL  CNT_FAM_MEMBERS  \\\n",
              "29           1                0           0           0              3.0   \n",
              "30           1                0           0           0              3.0   \n",
              "31           1                0           0           0              3.0   \n",
              "32           1                0           0           0              3.0   \n",
              "33           1                0           0           0              3.0   \n",
              "\n",
              "    STATUS  \n",
              "29       0  \n",
              "30       0  \n",
              "31       0  \n",
              "32       0  \n",
              "33       0  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-6326778b-987d-4dce-8e06-c40762aa06a1\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>ID</th>\n",
              "      <th>CODE_GENDER</th>\n",
              "      <th>FLAG_OWN_CAR</th>\n",
              "      <th>FLAG_OWN_REALTY</th>\n",
              "      <th>CNT_CHILDREN</th>\n",
              "      <th>AMT_INCOME_TOTAL</th>\n",
              "      <th>NAME_INCOME_TYPE</th>\n",
              "      <th>NAME_EDUCATION_TYPE</th>\n",
              "      <th>NAME_FAMILY_STATUS</th>\n",
              "      <th>NAME_HOUSING_TYPE</th>\n",
              "      <th>DAYS_BIRTH</th>\n",
              "      <th>DAYS_EMPLOYED</th>\n",
              "      <th>FLAG_MOBIL</th>\n",
              "      <th>FLAG_WORK_PHONE</th>\n",
              "      <th>FLAG_PHONE</th>\n",
              "      <th>FLAG_EMAIL</th>\n",
              "      <th>CNT_FAM_MEMBERS</th>\n",
              "      <th>STATUS</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>29</th>\n",
              "      <td>5008838</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>405000.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>-11842</td>\n",
              "      <td>-2016</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3.0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>30</th>\n",
              "      <td>5008839</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>405000.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>-11842</td>\n",
              "      <td>-2016</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3.0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>31</th>\n",
              "      <td>5008840</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>405000.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>-11842</td>\n",
              "      <td>-2016</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3.0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>32</th>\n",
              "      <td>5008841</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>405000.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>-11842</td>\n",
              "      <td>-2016</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3.0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>33</th>\n",
              "      <td>5008842</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>405000.0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>-11842</td>\n",
              "      <td>-2016</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>3.0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-6326778b-987d-4dce-8e06-c40762aa06a1')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-6326778b-987d-4dce-8e06-c40762aa06a1 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-6326778b-987d-4dce-8e06-c40762aa06a1');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AIVFbUBmA1zu",
        "outputId": "af1b8679-b756-499a-d7a4-696fa1ff66d9"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "Int64Index: 9516 entries, 29 to 434805\n",
            "Data columns (total 18 columns):\n",
            " #   Column               Non-Null Count  Dtype  \n",
            "---  ------               --------------  -----  \n",
            " 0   ID                   9516 non-null   int64  \n",
            " 1   CODE_GENDER          9516 non-null   int64  \n",
            " 2   FLAG_OWN_CAR         9516 non-null   int64  \n",
            " 3   FLAG_OWN_REALTY      9516 non-null   int64  \n",
            " 4   CNT_CHILDREN         9516 non-null   int64  \n",
            " 5   AMT_INCOME_TOTAL     9516 non-null   float64\n",
            " 6   NAME_INCOME_TYPE     9516 non-null   int64  \n",
            " 7   NAME_EDUCATION_TYPE  9516 non-null   int64  \n",
            " 8   NAME_FAMILY_STATUS   9516 non-null   int64  \n",
            " 9   NAME_HOUSING_TYPE    9516 non-null   int64  \n",
            " 10  DAYS_BIRTH           9516 non-null   int64  \n",
            " 11  DAYS_EMPLOYED        9516 non-null   int64  \n",
            " 12  FLAG_MOBIL           9516 non-null   int64  \n",
            " 13  FLAG_WORK_PHONE      9516 non-null   int64  \n",
            " 14  FLAG_PHONE           9516 non-null   int64  \n",
            " 15  FLAG_EMAIL           9516 non-null   int64  \n",
            " 16  CNT_FAM_MEMBERS      9516 non-null   float64\n",
            " 17  STATUS               9516 non-null   int64  \n",
            "dtypes: float64(2), int64(16)\n",
            "memory usage: 1.4 MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X = df.iloc[:,1:-1]\n",
        "y = df.iloc[:,-1]"
      ],
      "metadata": {
        "id": "9jXEIfwQBz9_"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)"
      ],
      "metadata": {
        "id": "llpTxVoyD9_b"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import MinMaxScaler\n",
        "mms = MinMaxScaler()\n",
        "X_scaled = pd.DataFrame(mms.fit_transform(X_train), columns=X_train.columns)\n",
        "X_test_scaled = pd.DataFrame(mms.fit_transform(X_test), columns=X_test.columns)"
      ],
      "metadata": {
        "id": "zHHQqIqcEgOD"
      },
      "execution_count": 37,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from imblearn.over_sampling import SMOTE\n",
        "oversample = SMOTE()\n",
        "X_balanced, y_balanced = oversample.fit_resample(X_scaled, y_train)\n",
        "X_test_balanced, y_test_balanced = oversample.fit_resample(X_test_scaled, y_test)"
      ],
      "metadata": {
        "id": "huzoQL3vJIPF"
      },
      "execution_count": 39,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y_train.value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vf3DNXTHJMvb",
        "outputId": "c1ede45b-661f-408a-a06e-0bc88796880f"
      },
      "execution_count": 40,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    6554\n",
              "1     107\n",
              "Name: STATUS, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_balanced.value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HYgX1reJLEAV",
        "outputId": "cdfd4bce-b74f-478a-e31c-0f3acb495e63"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    6554\n",
              "1    6554\n",
              "Name: STATUS, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_test.value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7pHvbidQLI_7",
        "outputId": "ef8341c2-7024-4e81-f8ca-9ae3dde84175"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    2811\n",
              "1      44\n",
              "Name: STATUS, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_test_balanced.value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "J1ktL3BFLPFE",
        "outputId": "c8057dc5-c5f9-457d-d868-84cda0702bb1"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    2811\n",
              "1    2811\n",
              "Name: STATUS, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 43
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.neighbors import KNeighborsClassifier\n",
        "from sklearn.svm import SVC\n",
        "from sklearn.tree import DecisionTreeClassifier\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from xgboost import XGBClassifier"
      ],
      "metadata": {
        "id": "e9_s_yBTLR97"
      },
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "classifiers = {\n",
        "    \"LogisticRegression\" : LogisticRegression(),\n",
        "    \"KNeighbors\" : KNeighborsClassifier(),\n",
        "    \"SVC\" : SVC(),\n",
        "    \"DecisionTree\" : DecisionTreeClassifier(),\n",
        "    \"RandomForest\" : RandomForestClassifier(),\n",
        "    \"XGBoost\" : XGBClassifier()\n",
        "}\n"
      ],
      "metadata": {
        "id": "d8JABoFjMmqq"
      },
      "execution_count": 45,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "train_scores = []\n",
        "test_scores = []\n",
        "\n",
        "for key, classifier in classifiers.items():\n",
        "    classifier.fit(X_balanced, y_balanced)\n",
        "    train_score = classifier.score(X_balanced, y_balanced)\n",
        "    train_scores.append(train_score)\n",
        "    test_score = classifier.score(X_test_balanced, y_test_balanced)\n",
        "    test_scores.append(test_score)\n",
        "\n",
        "print(train_scores)\n",
        "print(test_scores)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D4jBAizdM9Db",
        "outputId": "d00e0a18-6681-4f29-cbc5-6f65f620d20e"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0.6000152578577967, 0.9829111992676228, 0.9205065608788526, 0.9953463533719866, 0.9953463533719866, 0.9949649069270674]\n",
            "[0.6204197794379225, 0.7532906438989684, 0.7757025969405905, 0.811632870864461, 0.8358235503379581, 0.9212024190679473]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        " XGBoost model is performing best on the train set as well as test set with 92% accuracy."
      ],
      "metadata": {
        "id": "pdGGF6v8NmeV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "xgb = XGBClassifier()\n",
        "model = xgb.fit(X_balanced, y_balanced)\n",
        "prediction = xgb.predict(X_test_balanced)"
      ],
      "metadata": {
        "id": "cWLypPIvNgOo"
      },
      "execution_count": 47,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import classification_report\n",
        "print(classification_report(y_test_balanced, prediction))\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "i6aLb2kjN8Vg",
        "outputId": "e61461cc-6d6b-49d3-d64c-be20943cb81f"
      },
      "execution_count": 48,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.87      0.99      0.93      2811\n",
            "           1       0.99      0.85      0.92      2811\n",
            "\n",
            "    accuracy                           0.92      5622\n",
            "   macro avg       0.93      0.92      0.92      5622\n",
            "weighted avg       0.93      0.92      0.92      5622\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "EV1VMS9aOErR"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}