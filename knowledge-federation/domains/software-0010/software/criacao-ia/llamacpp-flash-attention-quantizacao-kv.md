---
id: software.criacao_ia.tranche04.000382
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
fontes: ["https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md", "https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# llama.cpp server: Flash Attention abre a porta da quantização de KV

## Em uma frase
O -fa (flash attention) tem default 'auto' e é pré-requisito recomendado para quantizar K e V (-ctk/-ctv, default f16) — o par que compra contexto maior pelo preço de precisão.

## Por que importa
A memória de KV é o gargalo de contexto em serving local: 128k de contexto em f16 é RAM que não existe em GPU de dev. Quantizar KV a 8 bits (q8_0) corta isso quase pela metade — mas a doc condiciona: os formatos de KV quantizada pedem Flash Attention ativa (-fa on), e 'auto' pode decidir por você de um jeito que o seu plano de VRAM não esperava.

## Como funciona
Para o caso 'contexto preciso caber': '-fa on -ctk q8_0 -ctv q8_0' (a doc lista q8_0 e afins como opções para as duas chaves). q8_0 é o ponto de partida conservador (a literatura de formatos llama.cpp o trata como quase-lossless para KV); q4_* entram quando o budget aperta, com avaliação própria de qualidade. Confirme no log de startup o estado decidido pelo 'auto' em -fa — a flag aceita booleano, e o explícito evita surpresas entre builds.

## Exemplo
Um servidor de 24 GB com 7B que não passava de 16k de contexto com -np 2: '-fa on -ctk q8_0 -ctv q8_0 -c 65536' fecha o plano, e a avaliação de regressão é um mini-suite de recall de documento longo, não perplexidade genérica.

## Limites e trade-offs
Quantização de KV é lossy de um jeito que importa para retrieved-context: 'quase-lossless' no papel não dispensa o teste no seu caso de uso. O suporte de -fa/quant-KV é backend-dependente (a doc registra restrições; nem todo build/CUDA/hip tem tudo). E as duas chaves são independentes: só -ctk sem -ctv dá economia parcial com assimetria de comportamento — use por decisão medida.

## Como verificar
Compare o pico de VRAM reportado no log com -ctk/-ctv off vs. q8_0 no mesmo -c: o delta é o número do plano. Rode o suite de qualidade (extrativa + recap de contexto longo) com/sem quantização e registre o delta de acerto. No build de produção, grepe a linha de config de FA no log — 'auto' resolvido como 'on' é o que você quer ver.

## Conexões
- [[llamacpp-contexto-e-batch-na-carga]] — llama.cpp server: tamanho de contexto e batch de prompt são duas alavancas separadas.
- [[llamacpp-slots-paralelos-np-cb]] — llama.cpp server: -np multiplica o contexto e -cb faz o cache caber em cada slot.

## Fontes
- [llama.cpp — tools/server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) — a seção de memória/KV com -fa auto, defaults f16 e a recomendação de -fa on com KV quantizada Consulta: 2026-10-04.
- [llama.cpp — grammars README](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) — o contraste de orçamento: constraints comem contexto/ciclo por outro caminho Consulta: 2026-10-04.
