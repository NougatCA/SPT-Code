
import torch
from torch.nn import CrossEntropyLoss, MSELoss
import torch.nn.functional as f

from transformers import BartForConditionalGeneration, BartConfig
from transformers.models.bart.modeling_bart import BartClassificationHead, shift_tokens_right
from transformers.modeling_outputs import Seq2SeqLMOutput, Seq2SeqSequenceClassifierOutput

from tqdm import tqdm
import numpy as np
import logging

import enums
from .utils import inputs_to_cuda

logger = logging.getLogger(__name__)


class BartForClassificationAndGeneration(BartForConditionalGeneration):

    def __init__(self, config: BartConfig, mode=None):
        super(BartForClassificationAndGeneration, self).__init__(config)
        self.mode = None
        if mode:
            self.set_model_mode(mode)

        # classification head
        self.classification_head = BartClassificationHead(
            config.d_model,
            config.d_model,
            config.num_labels,
            config.classifier_dropout,
        )
        self.model._init_weights(self.classification_head.dense)
        self.model._init_weights(self.classification_head.out_proj)

    def set_model_mode(self, mode):
        assert mode in [enums.MODEL_MODE_GEN, enums.MODEL_MODE_CLS, enums.MODEL_MODE_SEARCH]
        self.mode = mode
        logging.info(f'BART mode switched to {mode}')

    def forward(
            self,
            input_ids=None,
            attention_mask=None,
            decoder_input_ids=None,
            decoder_attention_mask=None,
            head_mask=None,
            decoder_head_mask=None,
            cross_attn_head_mask=None,
            encoder_outputs=None,
            past_key_values=None,
            inputs_embeds=None,
            decoder_inputs_embeds=None,
            labels=None,
            use_cache=None,
            output_attentions=None,
            output_hidden_states=None,
            return_dict=None,
            neg_nl_input_ids=None,
            neg_nl_attention_mask=None
    ):
        assert self.mode, 'It is required to specific a mode for BART before the model is passed through'

        if self.mode == enums.MODEL_MODE_SEARCH:
            return self.forward_search(input_ids=input_ids,
                                       attention_mask=attention_mask,
                                       decoder_input_ids=decoder_input_ids,
                                       decoder_attention_mask=decoder_attention_mask,
                                       head_mask=head_mask,
                                       decoder_head_mask=decoder_head_mask,
                                       cross_attn_head_mask=cross_attn_head_mask,
                                       encoder_outputs=encoder_outputs,
                                       past_key_values=past_key_values,
                                       inputs_embeds=inputs_embeds,
                                       decoder_inputs_embeds=decoder_inputs_embeds,
                                       labels=labels,
                                       use_cache=use_cache,
                                       output_attentions=output_attentions,
                                       output_hidden_states=output_hidden_states,
                                       return_dict=return_dict,
                                       neg_nl_input_ids=neg_nl_input_ids,
                                       neg_nl_attention_mask=neg_nl_attention_mask)

        elif self.mode == enums.MODEL_MODE_GEN:

            return self.forward_gen(input_ids=input_ids,
                                    attention_mask=attention_mask,
                                    decoder_input_ids=decoder_input_ids,
                                    decoder_attention_mask=decoder_attention_mask,
                                    head_mask=head_mask,
                                    decoder_head_mask=decoder_head_mask,
                                    cross_attn_head_mask=cross_attn_head_mask,
                                    encoder_outputs=encoder_outputs,
                                    past_key_values=past_key_values,
                                    inputs_embeds=inputs_embeds,
                                    decoder_inputs_embeds=decoder_inputs_embeds,
                                    labels=labels,
                                    use_cache=use_cache,
                                    output_attentions=output_attentions,
                                    output_hidden_states=output_hidden_states,
                                    return_dict=return_dict)

        elif self.mode == enums.MODEL_MODE_CLS:
            return self.forward_cls(input_ids=input_ids,
                                    attention_mask=attention_mask,
                                    decoder_input_ids=decoder_input_ids,
                                    decoder_attention_mask=decoder_attention_mask,
                                    head_mask=head_mask,
                                    decoder_head_mask=decoder_head_mask,
                                    cross_attn_head_mask=cross_attn_head_mask,
                                    encoder_outputs=encoder_outputs,
                                    past_key_values=past_key_values,
                                    inputs_embeds=inputs_embeds,
                                    decoder_inputs_embeds=decoder_inputs_embeds,
                                    labels=labels,
                                    use_cache=use_cache,
                                    output_attentions=output_attentions,
                                    output_hidden_states=output_hidden_states,
                                    return_dict=return_dict)

    def forward_gen(
            self,
            input_ids=None,
            attention_mask=None,
            decoder_input_ids=None,
            decoder_attention_mask=None,
            head_mask=None,
            decoder_head_mask=None,
            cross_attn_head_mask=None,
            encoder_outputs=None,
            past_key_values=None,
            inputs_embeds=None,
            decoder_inputs_embeds=None,
            labels=None,
            use_cache=None,
            output_attentions=None,
            output_hidden_states=None,
            return_dict=None
    ):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        if labels is not None:
            if decoder_input_ids is None:
                decoder_input_ids = shift_tokens_right(
                    labels, self.config.pad_token_id, self.config.decoder_start_token_id
                )

        outputs = self.model(
            input_ids,
            attention_mask=attention_mask,
            decoder_input_ids=decoder_input_ids,
            encoder_outputs=encoder_outputs,
            decoder_attention_mask=decoder_attention_mask,
            head_mask=head_mask,
            decoder_head_mask=decoder_head_mask,
            cross_attn_head_mask=cross_attn_head_mask,
            past_key_values=past_key_values,
            inputs_embeds=inputs_embeds,
            decoder_inputs_embeds=decoder_inputs_embeds,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        lm_logits = self.lm_head(outputs[0]) + self.final_logits_bias

        masked_lm_loss = None
        if labels is not None:
            loss_fct = CrossEntropyLoss()
            masked_lm_loss = loss_fct(lm_logits.view(-1, self.config.vocab_size), labels.view(-1))

        if not return_dict:
            output = (lm_logits,) + outputs[1:]
            return ((masked_lm_loss,) + output) if masked_lm_loss is not None else output

        return Seq2SeqLMOutput(
            loss=masked_lm_loss,
            logits=lm_logits,
            past_key_values=outputs.past_key_values,
            decoder_hidden_states=outputs.decoder_hidden_states,
            decoder_attentions=outputs.decoder_attentions,
            cross_attentions=outputs.cross_attentions,
            encoder_last_hidden_state=outputs.encoder_last_hidden_state,
            encoder_hidden_states=outputs.encoder_hidden_states,
            encoder_attentions=outputs.encoder_attentions,
        )

    def forward_representation(
            self,
            input_ids=None,
            attention_mask=None,
            decoder_input_ids=None,
            decoder_attention_mask=None,
            head_mask=None,
            decoder_head_mask=None,
            cross_attn_head_mask=None,
            encoder_outputs=None,
            past_key_values=None,
            inputs_embeds=None,
            decoder_inputs_embeds=None,
            labels=None,
            use_cache=None,
            output_attentions=None,
            output_hidden_states=None,
            return_dict=None):

        outputs = self.model(
            input_ids,
            attention_mask=attention_mask,
            decoder_input_ids=decoder_input_ids,
            decoder_attention_mask=decoder_attention_mask,
            head_mask=head_mask,
            decoder_head_mask=decoder_head_mask,
            cross_attn_head_mask=cross_attn_head_mask,
            encoder_outputs=encoder_outputs,
            inputs_embeds=inputs_embeds,
            decoder_inputs_embeds=decoder_inputs_embeds,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        hidden_states = outputs[0]  # last hidden state

        eos_mask = input_ids.eq(self.config.eos_token_id)

        if len(torch.unique(eos_mask.sum(1))) > 1:
            raise ValueError("All examples must have the same number of <eos> tokens.")
        sentence_representation = hidden_states[eos_mask, :].view(hidden_states.size(0), -1,
                                                                  hidden_states.size(-1))[
                                  :, -1, :
                                  ]
        return sentence_representation, outputs

    def forward_cls(
            self,
            input_ids=None,
            attention_mask=None,
            decoder_input_ids=None,
            decoder_attention_mask=None,
            head_mask=None,
            decoder_head_mask=None,
            cross_attn_head_mask=None,
            encoder_outputs=None,
            past_key_values=None,
            inputs_embeds=None,
            decoder_inputs_embeds=None,
            labels=None,
            use_cache=None,
            output_attentions=None,
            output_hidden_states=None,
            return_dict=None
    ):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict
        if labels is not None:
            use_cache = False

        if input_ids is None and inputs_embeds is not None:
            raise NotImplementedError(
                f"Passing input embeddings is currently not supported for {self.__class__.__name__}"
            )

        outputs = self.model(
            input_ids,
            attention_mask=attention_mask,
            decoder_input_ids=decoder_input_ids,
            decoder_attention_mask=decoder_attention_mask,
            head_mask=head_mask,
            decoder_head_mask=decoder_head_mask,
            cross_attn_head_mask=cross_attn_head_mask,
            encoder_outputs=encoder_outputs,
            inputs_embeds=inputs_embeds,
            decoder_inputs_embeds=decoder_inputs_embeds,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        hidden_states = outputs[0]  # last hidden state

        eos_mask = input_ids.eq(self.config.eos_token_id)

        if len(torch.unique(eos_mask.sum(1))) > 1:
            raise ValueError("All examples must have the same number of <eos> tokens.")
        sentence_representation = hidden_states[eos_mask, :].view(hidden_states.size(0), -1,
                                                                  hidden_states.size(-1))[
                                  :, -1, :
                                  ]
        logits = self.classification_head(sentence_representation)

        loss = None
        if labels is not None:
            if self.config.num_labels == 1:
                # regression
                loss_fct = MSELoss()
                loss = loss_fct(logits.view(-1), labels.view(-1))
            else:
                loss_fct = CrossEntropyLoss()
                loss = loss_fct(logits.view(-1, self.config.num_labels), labels.view(-1))

        if not return_dict:
            output = (logits,) + outputs[1:]
            return ((loss,) + output) if loss is not None else output

        return Seq2SeqSequenceClassifierOutput(
            loss=loss,
            logits=logits,
            past_key_values=outputs.past_key_values,
            decoder_hidden_states=outputs.decoder_hidden_states,
            decoder_attentions=outputs.decoder_attentions,
            cross_attentions=outputs.cross_attentions,
            encoder_last_hidden_state=outputs.encoder_last_hidden_state,
            encoder_hidden_states=outputs.encoder_hidden_states,
            encoder_attentions=outputs.encoder_attentions,
        )

    def forward_search(
            self,
            input_ids=None,
            attention_mask=None,
            decoder_input_ids=None,
            decoder_attention_mask=None,
            head_mask=None,
            decoder_head_mask=None,
            cross_attn_head_mask=None,
            encoder_outputs=None,
            past_key_values=None,
            inputs_embeds=None,
            decoder_inputs_embeds=None,
            labels=None,
            use_cache=None,
            output_attentions=None,
            output_hidden_states=None,
            return_dict=None,
            neg_nl_input_ids=None,
            neg_nl_attention_mask=None
    ):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        code_representation, code_outputs = self.forward_representation(input_ids=input_ids,
                                                                        attention_mask=attention_mask,
                                                                        # decoder_input_ids=None,
                                                                        # decoder_attention_mask=decoder_attention_mask,
                                                                        # head_mask=head_mask,
                                                                        # decoder_head_mask=decoder_head_mask,
                                                                        # cross_attn_head_mask=cross_attn_head_mask,
                                                                        # encoder_outputs=encoder_outputs,
                                                                        # past_key_values=past_key_values,
                                                                        # inputs_embeds=inputs_embeds,
                                                                        # decoder_inputs_embeds=None,
                                                                        # labels=None,
                                                                        use_cache=use_cache,
                                                                        # output_attentions=output_attentions,
                                                                        # output_hidden_states=output_hidden_states,
                                                                        return_dict=return_dict)
        nl_representation, nl_outputs = self.forward_representation(input_ids=decoder_input_ids,
                                                                    attention_mask=decoder_attention_mask,
                                                                    # decoder_input_ids=None,
                                                                    # decoder_attention_mask=None,
                                                                    # head_mask=head_mask,
                                                                    # decoder_head_mask=decoder_head_mask,
                                                                    # cross_attn_head_mask=cross_attn_head_mask,
                                                                    # encoder_outputs=encoder_outputs,
                                                                    # past_key_values=past_key_values,
                                                                    # inputs_embeds=inputs_embeds,
                                                                    # decoder_inputs_embeds=None,
                                                                    # labels=None,
                                                                    use_cache=use_cache,
                                                                    # output_attentions=output_attentions,
                                                                    # output_hidden_states=output_hidden_states,
                                                                    return_dict=return_dict)

        neg_nl_representation, neg_nl_outputs = self.forward_representation(input_ids=neg_nl_input_ids,
                                                                            attention_mask=neg_nl_attention_mask,
                                                                            use_cache=use_cache,
                                                                            return_dict=return_dict)

        pos_sim = f.cosine_similarity(code_representation, nl_representation)
        neg_sim = f.cosine_similarity(code_representation, neg_nl_representation)

        loss = (0.413 - pos_sim + neg_sim).clamp(min=1e-6).mean()
        return loss

        # if not return_dict:
        #     output = (code_representation,) + code_outputs[1:]
        #     return ((loss,) + output) if loss is not None else output
        #
        # return Seq2SeqSequenceClassifierOutput(
        #     loss=loss,
        #     logits=code_representation,
        #     past_key_values=code_outputs.past_key_values,
        #     decoder_hidden_states=code_outputs.decoder_hidden_states,
        #     decoder_attentions=code_outputs.decoder_attentions,
        #     cross_attentions=code_outputs.cross_attentions,
        #     encoder_last_hidden_state=code_outputs.encoder_last_hidden_state,
        #     encoder_hidden_states=code_outputs.encoder_hidden_states,
        #     encoder_attentions=code_outputs.encoder_attentions,
        # )

    def evaluate_search(self,
                        query_dataloader: torch.utils.data.dataloader.DataLoader,
                        codebase_dataloader: torch.utils.data.dataloader.DataLoader,
                        metrics_prefix: str):

        self.set_model_mode(enums.MODEL_MODE_CLS)
        self.eval()

        # embed query and codebase
        with torch.no_grad():
            logger.info('(1/3) Embedding search queries')
            query_vectors = []
            ref_urls = []
            for _, batch in enumerate(tqdm(query_dataloader)):
                urls = batch.pop('urls')
                ref_urls += urls
                batch = inputs_to_cuda(batch)
                representation, outputs = self.forward_representation(**batch)  # representation: [B, H]
                representation = representation.cpu().numpy()   # [B, H]
                query_vectors.append(representation)
            query_vectors = np.vstack(query_vectors)    # [len_query, H]

            logger.info('(2/3) Embedding candidate codes')
            code_vectors = []
            code_urls = []
            for _, batch in enumerate(tqdm(codebase_dataloader)):
                urls = batch.pop('urls')
                code_urls += urls
                batch = inputs_to_cuda(batch)
                representation, outputs = self.forward_representation(**batch)
                representation = representation.cpu().numpy()
                code_vectors.append(representation)
            code_vectors = np.vstack(code_vectors)  # [len_code, H]

            # calculate MRR
            logger.info('(3/3) Calculating metrics')
            scores = []
            ranks = []
            can_urls = []
            can_sims = []
            for query_vector, ref_url in tqdm(zip(query_vectors, ref_urls), total=len(query_vectors)):
                sims = []
                for code_vector, code_url in zip(code_vectors, code_urls):
                    sim = f.cosine_similarity(torch.from_numpy(code_vector).unsqueeze(0),
                                              torch.from_numpy(query_vector).unsqueeze(0))
                    sims.append((code_url, sim.item()))
                sims.sort(key=lambda item: item[1])

                sims = sims[:1000]
                can_urls.append(sims[0][0])
                can_sims.append(sims[0][1])

                rank = -1
                for index, (url, sim) in enumerate(sims):
                    if url == ref_url:
                        rank = index + 1
                ranks.append(rank)
                score = 1 / rank if rank != -1 else 0
                scores.append(score)

        self.train()
        self.set_model_mode(enums.MODEL_MODE_SEARCH)

        results = {f'{metrics_prefix}_mrr': np.mean(scores),
                   f'{metrics_prefix}_ranks': ranks,
                   f'{metrics_prefix}_ref_urls': ref_urls,
                   f'{metrics_prefix}_can_urls': can_urls,
                   f'{metrics_prefix}_can_sims': can_sims}
        return results
