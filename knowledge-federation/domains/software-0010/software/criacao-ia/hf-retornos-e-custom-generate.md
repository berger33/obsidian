---
id: software.criacao_ia.tranche04.000400
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://huggingface.co/docs/transformers/main_classes/text_generation", "https://huggingface.co/docs/transformers/kv_cache"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Transformers: past_key_values no retorno e generate custom por repositório

## Em uma frase
return_dict_in_generate abre as saídas estruturadas (past_key_values para continuação, scores para rerank) — e o campo custom_generate abre o pipeline para geradores alternativos versionados no hub, com o contrato de confiança explícito.

## Por que importa
Duas camadas de 'saída da caixa preta': continuar uma conversa sem recomputar KV, e trocar o algoritmo de geração sem forkar a lib. A primeira é performance de agente (o cache que os loops de tool-use rejeitam todo dia por não saber do parâmetro); a segunda é o canário de supply-chain — código Python do hub rodando no seu generate() exige trust_remote_code e requirements.txt próprios, com o aviso explícito da doc sobre pins quebrados.

## Como funciona
Para dict: 'return_dict_in_generate=True' retorna GenerateOutput (sequences, past_key_values, scores quando output_scores=True); a rota de continuação realimenta o cache cortando o que passou — as páginas descrevem os campos e a limitação de que past é formato de cache interno (não contrato estável entre versões). Para custom: 'generation_config.custom_generate' aponta o módulo/repositório (ex.: 'unbabel-comet/...') e a doc descreve o formato (generate.py + requirements.txt) com a ressalva de ImportError por pins incompatíveis; exige trust_remote_code na carga.

## Exemplo
Um orquestrador multi-turno guarda 'past_key_values' por sessão e reaproveita no próximo turno com o delta de prompt; o reranker de melhor-de-n usa os 'scores' por passo do mesmo dict — duas features do mesmo retorno que o preset default escondia.

## Limites e trade-offs
past_key_values é formato de cache interno (a própria doc de kv_cache explica por que não o trate como API de dados — o layout muda com cache_implementation e versão); serializar para 'estado de sessão' é unsupported. output_scores triplica memória nos passos (um vocab por passo — budget). E custom_generate é execução de código de terceiros: o trust_remote_code que habilita é a decisão de segurança, não um toggle de conveniência — audite o repositório como dependência de runtime.

## Como verificar
Um teste de paridade de continuação: gerar A, continuar com past vs. regerar A+B do zero, comparar a saída (a diferença é o que o cache não-carregado te custaria). No dict, assert de shape de past por modo de cache (dynamic vs static respondem diferente — o teste fixa a expectativa). Para custom_generate: um CI que roda o gerador externo como dependência versionada (pinned commit), não como 'latest'.

## Conexões
- [[hf-assisted-decoding-especifico]] — Transformers: decodificação assistida — draft por modelo, n-gram, medusa ou ensemble.

## Fontes
- [Transformers — Generation (text_generation)](https://huggingface.co/docs/transformers/main_classes/text_generation) — GenerateOutput (past_key_values, scores) e o campo custom_generate com contrato de requirements Consulta: 2026-10-04.
- [Transformers — KV cache](https://huggingface.co/docs/transformers/kv_cache) — o que past_key_values é por dentro, e por que não é formato estável Consulta: 2026-10-04.
