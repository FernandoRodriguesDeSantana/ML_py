{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyOUVCDJJteBHbSvfQUEv/T6",
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
        "<a href=\"https://colab.research.google.com/github/FernandoRodriguesDeSantana/ML_py/blob/main/first_ml_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#**My First ML Project**"
      ],
      "metadata": {
        "id": "5yZWqjXa8FWU"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Load Data**"
      ],
      "metadata": {
        "id": "qXq4FXHS8OlY"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ZkPHeh5Rt99S"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "\n",
        "df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv')\n",
        "df"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Data preparation**"
      ],
      "metadata": {
        "id": "C4mnpY4h9qAM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "###Data separation as X and Y"
      ],
      "metadata": {
        "id": "aDLazLWV9tJe"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y = df['logS']\n",
        "y"
      ],
      "metadata": {
        "id": "_KHT_6hc92bm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X = df.drop('logS', axis=1)\n",
        "X"
      ],
      "metadata": {
        "id": "av0jHY3--BTj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "###Data splitting"
      ],
      "metadata": {
        "id": "k6XhhcKh-h_Y"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)"
      ],
      "metadata": {
        "id": "x3JDNVLU-lUC"
      },
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train"
      ],
      "metadata": {
        "id": "gopKXAXICcCL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_test"
      ],
      "metadata": {
        "id": "x1Jz69KVCguK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##**Model Building**"
      ],
      "metadata": {
        "id": "NI0A0wDQDQmn"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "###Linear Regression"
      ],
      "metadata": {
        "id": "h8HTz_9qDxLO"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Training the model*"
      ],
      "metadata": {
        "id": "NtxY73srEaVO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "\n",
        "lr = LinearRegression()\n",
        "lr.fit(X_train, y_train)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "ZJ8qTQ1CD0RF",
        "outputId": "0ea981b9-da1b-4425-9d06-6039008c0328"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LinearRegression()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LinearRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LinearRegression</label><div class=\"sk-toggleable__content\"><pre>LinearRegression()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Applying the model to make a prediction*"
      ],
      "metadata": {
        "id": "bhdx8kRDEu-X"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y_lr_train_pred = lr.predict(X_train)\n",
        "y_lr_test_pred = lr.predict(X_test)"
      ],
      "metadata": {
        "id": "OcddwfAQE34A"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(y_lr_train_pred, y_lr_test_pred)"
      ],
      "metadata": {
        "id": "XQdJCfvVFJit"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y_lr_train_pred"
      ],
      "metadata": {
        "id": "ulaOW7t1FaLt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y_lr_test_pred"
      ],
      "metadata": {
        "id": "J1glFZ-CFe0I"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "*Evaluate model performance*"
      ],
      "metadata": {
        "id": "lk6GK4UYFnHN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y_train"
      ],
      "metadata": {
        "id": "fzRzB5PxFt7e"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "y_lr_train_pred"
      ],
      "metadata": {
        "id": "iRkQxvatFx_R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import mean_squared_error, r2_score\n",
        "\n",
        "lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)\n",
        "lr_train_r2 = r2_score(y_train, y_lr_train_pred)\n",
        "\n",
        "lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)\n",
        "lr_test_r2 = r2_score(y_test, y_lr_test_pred)"
      ],
      "metadata": {
        "id": "FlUoTMEEGDaa"
      },
      "execution_count": 37,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(lr_train_mse)\n",
        "print(lr_train_r2)\n",
        "print(lr_test_mse)\n",
        "print(lr_test_r2)"
      ],
      "metadata": {
        "id": "wuiqVgppG_Xd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "lr_results = pd.DataFrame(['Linear Regression', lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()\n",
        "lr_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']\n",
        "lr_results"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 81
        },
        "id": "2XhKFUZiHdxT",
        "outputId": "55cbdba0-8e97-49d4-fe54-26521a14f0ca"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "              Method Training MSE Training R2  Test MSE   Test R2\n",
              "0  Linear Regression     1.007536    0.764505  1.020695  0.789162"
            ],
            "text/html": [
              "\n",
              "\n",
              "  <div id=\"df-3e10ffcd-6407-4244-aea5-b4dbb23d030b\">\n",
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
              "      <th>Method</th>\n",
              "      <th>Training MSE</th>\n",
              "      <th>Training R2</th>\n",
              "      <th>Test MSE</th>\n",
              "      <th>Test R2</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Linear Regression</td>\n",
              "      <td>1.007536</td>\n",
              "      <td>0.764505</td>\n",
              "      <td>1.020695</td>\n",
              "      <td>0.789162</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3e10ffcd-6407-4244-aea5-b4dbb23d030b')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "\n",
              "\n",
              "\n",
              "    <div id=\"df-01f369e6-b240-42c5-9a78-7f8c93d46ac1\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-01f369e6-b240-42c5-9a78-7f8c93d46ac1')\"\n",
              "              title=\"Suggest charts.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "    </div>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "    background-color: #E8F0FE;\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: #1967D2;\n",
              "    height: 32px;\n",
              "    padding: 0 0 0 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: #E2EBFA;\n",
              "    box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: #174EA6;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "    background-color: #3B4455;\n",
              "    fill: #D2E3FC;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart:hover {\n",
              "    background-color: #434B5C;\n",
              "    box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "    filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "    fill: #FFFFFF;\n",
              "  }\n",
              "</style>\n",
              "\n",
              "    <script>\n",
              "      async function quickchart(key) {\n",
              "        const containerElement = document.querySelector('#' + key);\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      }\n",
              "    </script>\n",
              "\n",
              "      <script>\n",
              "\n",
              "function displayQuickchartButton(domScope) {\n",
              "  let quickchartButtonEl =\n",
              "    domScope.querySelector('#df-01f369e6-b240-42c5-9a78-7f8c93d46ac1 button.colab-df-quickchart');\n",
              "  quickchartButtonEl.style.display =\n",
              "    google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "}\n",
              "\n",
              "        displayQuickchartButton(document);\n",
              "      </script>\n",
              "      <style>\n",
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
              "          document.querySelector('#df-3e10ffcd-6407-4244-aea5-b4dbb23d030b button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3e10ffcd-6407-4244-aea5-b4dbb23d030b');\n",
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
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Random Forest**"
      ],
      "metadata": {
        "id": "5NFdem10IjaY"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Training the model"
      ],
      "metadata": {
        "id": "32cIGDF6I0XW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.ensemble import RandomForestRegressor\n",
        "\n",
        "rf = RandomForestRegressor(max_depth = 2, random_state = 100)\n",
        "rf.fit(X_train, y_train)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "bOe0EeR4JamN",
        "outputId": "b7d1f4d8-6c15-4f02-e8da-d592adc5e4ce"
      },
      "execution_count": 34,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RandomForestRegressor(max_depth=2, random_state=100)"
            ],
            "text/html": [
              "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestRegressor(max_depth=2, random_state=100)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestRegressor</label><div class=\"sk-toggleable__content\"><pre>RandomForestRegressor(max_depth=2, random_state=100)</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 34
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Applying the model to make a prediction"
      ],
      "metadata": {
        "id": "L2bqhKEGJAGq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "y_rf_train_pred = rf.predict(X_train)\n",
        "y_rf_test_pred = rf.predict(X_test)"
      ],
      "metadata": {
        "id": "LNzqUm-cKCQF"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Evaluate model performance"
      ],
      "metadata": {
        "id": "Anwcp0mwJOBD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import mean_squared_error, r2_score\n",
        "\n",
        "rf_train_mse = mean_squared_error(y_train, y_rf_train_pred)\n",
        "rf_train_r2 = r2_score(y_train, y_rf_train_pred)\n",
        "\n",
        "rf_test_mse = mean_squared_error(y_test, y_rf_test_pred)\n",
        "rf_test_r2 = r2_score(y_test, y_rf_test_pred)"
      ],
      "metadata": {
        "id": "JOjmjc_bLDVa"
      },
      "execution_count": 41,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "rf_results = pd.DataFrame(['Linear Regression', rf_train_mse, rf_train_r2, rf_test_mse, rf_test_r2]).transpose()\n",
        "rf_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']\n",
        "rf_results"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 81
        },
        "id": "hkyq-EvILEl1",
        "outputId": "d26c15f0-8f20-4e87-f43d-1d93af52a5e0"
      },
      "execution_count": 42,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "              Method Training MSE Training R2  Test MSE   Test R2\n",
              "0  Linear Regression     1.028228    0.759669  1.407688  0.709223"
            ],
            "text/html": [
              "\n",
              "\n",
              "  <div id=\"df-de0e97c3-3980-448b-bef6-e5ba954eac0a\">\n",
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
              "      <th>Method</th>\n",
              "      <th>Training MSE</th>\n",
              "      <th>Training R2</th>\n",
              "      <th>Test MSE</th>\n",
              "      <th>Test R2</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Linear Regression</td>\n",
              "      <td>1.028228</td>\n",
              "      <td>0.759669</td>\n",
              "      <td>1.407688</td>\n",
              "      <td>0.709223</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-de0e97c3-3980-448b-bef6-e5ba954eac0a')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "\n",
              "\n",
              "\n",
              "    <div id=\"df-32d2328d-8180-4cb6-99b0-0ddb8583b62d\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-32d2328d-8180-4cb6-99b0-0ddb8583b62d')\"\n",
              "              title=\"Suggest charts.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "    </div>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "    background-color: #E8F0FE;\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: #1967D2;\n",
              "    height: 32px;\n",
              "    padding: 0 0 0 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: #E2EBFA;\n",
              "    box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: #174EA6;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "    background-color: #3B4455;\n",
              "    fill: #D2E3FC;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart:hover {\n",
              "    background-color: #434B5C;\n",
              "    box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "    filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "    fill: #FFFFFF;\n",
              "  }\n",
              "</style>\n",
              "\n",
              "    <script>\n",
              "      async function quickchart(key) {\n",
              "        const containerElement = document.querySelector('#' + key);\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      }\n",
              "    </script>\n",
              "\n",
              "      <script>\n",
              "\n",
              "function displayQuickchartButton(domScope) {\n",
              "  let quickchartButtonEl =\n",
              "    domScope.querySelector('#df-32d2328d-8180-4cb6-99b0-0ddb8583b62d button.colab-df-quickchart');\n",
              "  quickchartButtonEl.style.display =\n",
              "    google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "}\n",
              "\n",
              "        displayQuickchartButton(document);\n",
              "      </script>\n",
              "      <style>\n",
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
              "          document.querySelector('#df-de0e97c3-3980-448b-bef6-e5ba954eac0a button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-de0e97c3-3980-448b-bef6-e5ba954eac0a');\n",
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
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Model comparison**"
      ],
      "metadata": {
        "id": "XcMKFh0HLKEl"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "df_models = pd.concat([lr_results, rf_results], axis = 0).reset_index(drop = True)\n",
        "df_models"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 112
        },
        "id": "CIQyK6pPLUhh",
        "outputId": "2a9cdb44-9eab-4f3c-9471-c00640fb0e6e"
      },
      "execution_count": 46,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "              Method Training MSE Training R2  Test MSE   Test R2\n",
              "0  Linear Regression     1.007536    0.764505  1.020695  0.789162\n",
              "1  Linear Regression     1.028228    0.759669  1.407688  0.709223"
            ],
            "text/html": [
              "\n",
              "\n",
              "  <div id=\"df-a598f932-36c6-4a12-8bcc-5908101cc742\">\n",
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
              "      <th>Method</th>\n",
              "      <th>Training MSE</th>\n",
              "      <th>Training R2</th>\n",
              "      <th>Test MSE</th>\n",
              "      <th>Test R2</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Linear Regression</td>\n",
              "      <td>1.007536</td>\n",
              "      <td>0.764505</td>\n",
              "      <td>1.020695</td>\n",
              "      <td>0.789162</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Linear Regression</td>\n",
              "      <td>1.028228</td>\n",
              "      <td>0.759669</td>\n",
              "      <td>1.407688</td>\n",
              "      <td>0.709223</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-a598f932-36c6-4a12-8bcc-5908101cc742')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "\n",
              "\n",
              "\n",
              "    <div id=\"df-5e34c3e4-fe44-4694-a21a-be601e3a50cf\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-5e34c3e4-fe44-4694-a21a-be601e3a50cf')\"\n",
              "              title=\"Suggest charts.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "    </div>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "    background-color: #E8F0FE;\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: #1967D2;\n",
              "    height: 32px;\n",
              "    padding: 0 0 0 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: #E2EBFA;\n",
              "    box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: #174EA6;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "    background-color: #3B4455;\n",
              "    fill: #D2E3FC;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart:hover {\n",
              "    background-color: #434B5C;\n",
              "    box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "    filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "    fill: #FFFFFF;\n",
              "  }\n",
              "</style>\n",
              "\n",
              "    <script>\n",
              "      async function quickchart(key) {\n",
              "        const containerElement = document.querySelector('#' + key);\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      }\n",
              "    </script>\n",
              "\n",
              "      <script>\n",
              "\n",
              "function displayQuickchartButton(domScope) {\n",
              "  let quickchartButtonEl =\n",
              "    domScope.querySelector('#df-5e34c3e4-fe44-4694-a21a-be601e3a50cf button.colab-df-quickchart');\n",
              "  quickchartButtonEl.style.display =\n",
              "    google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "}\n",
              "\n",
              "        displayQuickchartButton(document);\n",
              "      </script>\n",
              "      <style>\n",
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
              "          document.querySelector('#df-a598f932-36c6-4a12-8bcc-5908101cc742 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-a598f932-36c6-4a12-8bcc-5908101cc742');\n",
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
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 46
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Data visualization of prediction results**"
      ],
      "metadata": {
        "id": "LGS3qPR9MFn1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "\n",
        "plt.figure(figsize=(5,5))\n",
        "plt.scatter(x = y_train, y = y_lr_train_pred, alpha = 0.3)\n",
        "\n",
        "plt.plot()\n",
        "plt.ylabel('Predict LogS')\n",
        "plt.xlabel('Experimental LogS')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 482
        },
        "id": "Iw8yMWnJMKjV",
        "outputId": "1a7f6f42-3c99-4b19-8818-c5f4652931f2"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0.5, 0, 'Experimental LogS')"
            ]
          },
          "metadata": {},
          "execution_count": 55
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 500x500 with 1 Axes>"
            ],
            "image/png": "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P+HnWG5s2+YXfuEX+IVf+AX+4A/+gP/xP/4Hd9xxhxRSybyRe6QSyUmye/dufvu3f5vPf/7zXHHFFdxyyy1HCcxPfvKTWY9//OMfs3XrVjRN4+KLLyaKIsbGxtiyZcusr76+viWP/6UvfSlPPfUUGzZsOOrnL+SGwDAMoiia9dwDDzzArbfeyi//8i+zY8cO+vr62Lt376LFft555/HYY49Rr9dn/UxVVTn33HPJ5/P09va292whqXh++OGHT3js7du3zzquRHIipJBKJMfA8zxGRkZmfc1UtEZRxK/+6q9yww038Na3vpW7776bxx9/nE9+8pOzjrF//35uv/12du3axf/7f/+Pz33uc7znPe8B4JxzzuHNb34zb3nLW/ja177Gnj17ePDBB7nzzjv51re+teSf77bbbmNqaopf+ZVf4aGHHmL37t185zvf4a1vfetRwng8NmzYwPe//31GRkaYnp4GYOvWrXzta1/j0Ucf5bHHHuNNb3rTCbPYuWg2mzz66KOzvnbv3s2b3/xmbNvmlltu4cknn+Tee+/l3e9+NzfffHN7Cfvd7343d955J9/4xjfYtWsX73nPe5ienm5n5pOTk1x77bX87d/+LY8//jh79uzhq1/9Kh/72Md47Wtfu+BYJWcvcmlXIjkG3/72t2ctcQKce+657Ny5k49+9KPs27ePb37zm0CyFPrXf/3X/Mqv/ArXX389F154IQBvectbaDabXH755Wiaxnve8x5+/dd/vX28u+++mz/5kz/hve99L0NDQ3R1dXHllVdy0003Lfnn6+/v54EHHuD9738/119/PZ7nMTg4yI033oiqzv8e+5Of/CS33347n//85xkYGGDv3r186lOf4td+7dd4+ctfTldXF+9///upVCoLjvHZZ5/l4osvnvXcq171Ku655x6+853v8J73vIfLLruMVCrF61//ej71qU+1X/f+97+fkZER3vKWt6BpGr/+67/ODTfc0F5Gz2QyXHHFFXz6059m9+7dBEHAunXrePvb387v/d7vLThWydmLIsRhTW0SiWTRuPrqq7noooukDd4qIY5jzjvvPN74xjfykY98ZKXDkZxByIxUIpGckezbt4/vfve7vPKVr8TzPP7n//yf7Nmzhze96U0rHZrkDEPukUokkjMSVVX50pe+xGWXXcYrXvEKnnjiCe655x7OO++8lQ5NcoYhl3YlEolEIjkFZEYqkUgkEskpIIVUIpFIJJJTQAqpRCKRSCSngBRSiUQikUhOASmkEolEIpGcAlJIJRKJRCI5BaSQSiQSiURyCkghlUgkEonkFJBCKpFIJBLJKfD/AxIeRGAGN5o1AAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    }
  ]
}