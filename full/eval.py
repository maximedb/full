import torch
import transformers
from typing import List, Optional


default_follow_ups = [
    "Not really relevant here.",
    "You're really confusing."
    "You're really boring.",
    "What are you trying to say?",
    "You don't seem interested."
]


class FULL:
    def __init__(self, model_name: str = "facebook/blenderbot-400M-distill", device: Optional[str] = None, sep_token: str ="\t", follow_ups: List[str] = [], lookback: int = 50):
        assert lookback > 0, "Lookback should be larger than 0"
        cuda_available = torch.cuda.is_available()
        if device is None and cuda_available:
            device = "cuda"
        elif device is None:
            device = "cpu"
        elif device == "cuda" and not cuda_available:
            raise RuntimeError("CUDA not available, please specify another device")
        self.model = transformers.AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(model_name, add_prefix_space=True, truncation_side="right")
        self.device = device
        self.model = self.model.to(device)
        self.sep_token = sep_token
        self.lookback = lookback
        if len(follow_ups) > 0:
            assert all([isinstance(follow_up, str) for follow_up in follow_ups])
            self.follow_ups = follow_ups
        else:
            self.follow_ups = default_follow_ups

    def _compute_conditional_loss(self, encoder_inputs, decoder_inputs):
        inputs = self.tokenizer(encoder_inputs, truncation=True, return_tensors="pt") # /!\ truncation side should be right!
        with self.tokenizer.as_target_tokenizer():
            decoder_inputs =  self.tokenizer(decoder_inputs, truncation=True, return_tensors="pt")
        inputs["labels"] = decoder_inputs["input_ids"]
        encoder_outputs = None
        with torch.no_grad():
            outputs = self.model(
                input_ids=inputs["input_ids"].to(self.device),
                labels=inputs["labels"].to(self.device),
                encoder_outputs=encoder_outputs,
                return_dict=True
            )
            encoder_outputs = outputs.encoder_last_hidden_state
        return torch.exp(outputs["loss"]).item()

    def evaluate_turn(self, conversation: List[str], response: str):
        assert isinstance(conversation, list), "the conversation should be a list"
        assert len(conversation) > 0, "the conversation should have at least one turn"
        assert all([isinstance(turn, str) for turn in conversation]), "all turns in a conversation should be str"
        assert isinstance(response, str), "response should be a string"
        assert len(response), "response should be non empty"
        conversation = conversation[-self.lookback:] + [response]
        score = self._evaluate(conversation)
        return score

    def evaluate_dialog(self, conversation: List[str]):
        assert isinstance(conversation, list), "the conversation should be a list"
        assert len(conversation) > 0, "the conversation should have at least one turn"
        assert all([isinstance(turn, str) for turn in conversation]), "all turns in a conversation should be str"
        conversation = conversation[-self.lookback:]
        score = self._evaluate(conversation)
        return score

    def _evaluate(self, conversation: List[str]):
        str_conversation = self.sep_token + self.sep_token.join(conversation)
        scores = []
        for follow_up in self.follow_ups:
            cnd_loss = self._compute_conditional_loss(str_conversation, follow_up)
            scores.append(cnd_loss) 
        return sum(scores) / len(scores)
