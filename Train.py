import json
from datasets import load_dataset
from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling

def main():
    # Load the tokenizer and model
    model_name = "gpt2"
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Add padding token to tokenizer
    tokenizer.pad_token = tokenizer.eos_token

    # Use Hugging Face Datasets to load the dataset
    datasets = load_dataset('text', data_files={'train': 'train.txt'})

    def tokenize_function(examples):
        return tokenizer(examples['text'], return_special_tokens_mask=True)

    tokenized_datasets = datasets.map(tokenize_function, batched=True, num_proc=1, remove_columns=["text"])

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,
    )

    training_args = TrainingArguments(
        output_dir="./gpt2-finetuned",
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=tokenized_datasets['train'],
    )

    trainer.train()

    # Save the model
    model.save_pretrained("gpt2-finetuned")
    tokenizer.save_pretrained("gpt2-finetuned")

if __name__ == "__main__":
    main()
