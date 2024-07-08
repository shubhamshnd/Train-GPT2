
# GPT-2 Training and Chatbot

This repository contains scripts to train a GPT-2 model and use it for generating answers to specific questions. The model can be trained to answer about any topic, Provided you have structured data in the mentioned format.

## Files

- `Train.py`: Script to train the GPT-2 model using a custom dataset.
- `Chat-Pretrained.py`: Script to use the pre-trained GPT-2 model for generating answers.
- `Chat-Finetuned.py`: Script to use the fine-tuned GPT-2 model for generating answers.

## Requirements

- Python 3.6+
- Transformers library from Hugging Face
- Pandas
- Datasets library from Hugging Face

## Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/shubhamshnd/Train-GPT2
    cd Train-GPT2
    ```

2. Install the required libraries:
    ```bash
    pip install transformers pandas datasets
    ```

3. Prepare your training data file named `train.txt` in the following format(example):
    ```
    Question: What is the Safe Work Load(SWL) of Sennebogen 1, 2? Answer: 20.4 T
    Question: Can you specify the Safe Work Load(SWL) of Sennebogen 1, 2? Answer: 20.4 T
    Question: Tell me the Safe Work Load(SWL) for Sennebogen 1, 2. Answer: 20.4 T
    Question: What does the Safe Work Load(SWL) of Sennebogen 1, 2 indicate? Answer: 20.4 T
    Question: Could you elaborate on the Safe Work Load(SWL) of Sennebogen 1, 2? Answer: 20.4 T
    Question: Sennebogen 1, 2's Safe Work Load(SWL)? Answer: 20.4 T
    Question: Safe Work Load(SWL) for Sennebogen 1, 2? Answer: 20.4 T
    ```

## Training the Model

To train the GPT-2 model with your data, run:
```bash
python Train.py
```
This will fine-tune the GPT-2 model using your custom dataset and save the trained model in the `gpt2-finetuned` directory.

## Using the Pre-trained Model

To use the pre-trained GPT-2 model, run:
```bash
python Chat-Pretrained.py
```
This script uses the pre-trained GPT-2 model to generate answers based on the provided questions.

## Using the Fine-tuned Model

To use the fine-tuned GPT-2 model, run:
```bash
python Chat-Finetuned.py
```
This script uses the fine-tuned GPT-2 model to generate answers based on the provided questions.

## Contact

For any questions or inquiries, please contact me at [shubhamshindesunil@gmail.com](mailto:shubhamshindesunil@gmail.com) or connect with me on [LinkedIn](https://www.linkedin.com/in/shubham-shinde-313b291b9).

---

Feel free to fork and contribute to this repository. Happy coding!
