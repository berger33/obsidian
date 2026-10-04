---
id: software.criacao_ia.tranche04.000391
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
fontes: ["https://huggingface.co/docs/transformers/main_classes/text_generation", "https://huggingface.co/docs/transformers/internal/generation_utils"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Transformers: os None da GenerationConfig são herança, não desatenção

## Em uma frase
A GenerationConfig deixa os parâmetros não-definidos como None e os resolve contra o config do modelo na geração — o objeto que viaja com o checkpoint, não o default global da biblioteca.

## Por que importa
Times que setam 'GenerationConfig(temperature=0.7)' e colhem comportamento diferente do esperado esquecem o outro lado: o que você não define vem do modelo (generation_config.json salvo junto dele). E o modelo pode ter um generation_config authorado pelo uploader — temperatura 0.7 sua vs. defaults do checkpoint é uma mistura de camadas invisível sem leitura do estado resolvido.

## Como funciona
A página do classe documenta o mecanismo: campos None são preenchidos por '_get_default_generation_params'-style resolution na entrada de generate() (a referência interna lista a rota). Para debug, leia o config resolvido de fato (o atributo do modelo/model.generation_config após a carga) e compare com o seu objeto. Para publicar um preset intencional, use 'model.generation_config.save_pretrained()' — o arquivo generation_config.json passa a ser o default de quem carregar o checkpoint, e from_pretrained(model_id) o recupera.

## Exemplo
Um finetuner que queria 'temperatura do modelo base + max_new_tokens nosso' faz 'GenerationConfig(max_new_tokens=512)' e deixa o resto None — recebe exatamente a semântica de herança; e o postmortem de 'mudou o sampling após merge' é sempre ler o json do checkpoint.

## Limites e trade-offs
Herança tem precedência definida (explícito > generation_config.json > defaults da classe) — mas campos deprecados e renomeados entre versões bagunçam a leitura do json alheio; valide com asserções, não com print. Um generation_config.json podado no merge de LoRA (comum) apaga a camada do base silenciosamente. E defaults de 'max new tokens' sem config limitam a saída (nota separada do max 20).

## Como verificar
Depois de from_pretrained, um assert de 'model.generation_config.to_dict()' contra um snapshot esperado (por release de modelo) pega mudanças de herança no CI. Carregue o mesmo checkpoint com e sem o GenerationConfig explícito e diff a saída de uma geração com seed. Publique um preset e confirme que outro processo o lê de volta.

## Conexões
- [[hf-max-new-tokens-vs-max-length]] — Transformers: max_new_tokens é o budget relativo; max_length é o absoluto que te morderá.

## Fontes
- [Transformers — Generation (text_generation)](https://huggingface.co/docs/transformers/main_classes/text_generation) — a classe GenerationConfig com a resolução de defaults e os métodos de save/load Consulta: 2026-10-04.
- [Transformers — generation utils (referência interna)](https://huggingface.co/docs/transformers/internal/generation_utils) — as funções de resolução de config usadas por generate() Consulta: 2026-10-04.
