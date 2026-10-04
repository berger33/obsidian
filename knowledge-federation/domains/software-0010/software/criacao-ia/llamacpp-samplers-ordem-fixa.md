---
id: software.criacao_ia.tranche04.000390
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

# llama.cpp: o pipeline de samplers tem ordem fixa, e cada campo do pedido é um nó dele

## Em uma frase
No server, os samplers pedidos por campos do request rodam numa ordem definida — penalties, dry, top_n_sigma, top_k, typ_p, top_p, min_p, xtc, temperature — não na ordem em que você os lista no JSON.

## Por que importa
Interação de parâmetros é dependente de ordem: top-k antes de temperature corta distribuição que 'esquentaria' outro conjunto; dry (repetition penalty de n-gramas por cache) antes de tudo muda o que os cortes veem. Quem porta config de outro runtime com 'os mesmos campos' obtém comportamento diferente sem erro nenhum — a ordem é a API implícita.

## Como funciona
O README do server lista a sequência do pipeline (a ordem da referência desta nota) e os campos por sampler (temperature, top_k, top_p, min_p, typical_p, penalty fields, dry_*, xtc_* etc.). Leitura operacional: configure o 'top' (top_k/top_p/min_p) sabendo que o renormaliza-mento e as interações acontecem naquela sequência; temperature por último significa que os cortes são na distribuição fria — e trocar só seu 'temperature: 0.5' não reproduz o '0.5 antes do top_p' de outro servidor. Não existe reordenação por campo no request — o que a doc expõe são os parâmetros por sampler.

## Exemplo
Dois serviços com 'top_p 0.9 + temperature 0.7': um llama.cpp, outro com ordem invertida — as amostras divergem de estilo com o mesmo seed; o time marca a diferença no contrato de qualidade do produto em vez de procurar bug no prompt.

## Limites e trade-offs
A ordem documentada pode mudar entre releases da ferramenta — o README é a fonte da sua build, não desta nota. Campos sem valor explícito assumem defaults próprios do backend (a doc lista por sampler); em port, setar explicitamente o que importa bate menos com upgrade. E sampling com grammar ativa é outro grafo de interação (a mask vem antes de tudo que corta): o resultado é a composição dos dois sistemas, e testar um não testa o outro.

## Como verificar
Um suite de golden-samples: mesmos seeds, mesmo prompt, N requests com configs variadas — diff de distribuição de tokens (top-1 match, entropia amostrada) contra um reference run seu. Uma request com campo de sampler desconhecido: observe o comportamento (ignore vs. 4xx) e registre — é o que a doc diz sobre extras? teste, não assuma. Na subida de versão do build, rode o suite e trate diff como review item.

## Conexões
- [[gbnf-json-schema-nao-e-prompt]] — llama.cpp: JSON Schema vira GBNF — restringe a saída e não entra no prompt.

## Fontes
- [llama.cpp — tools/server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) — a tabela de campos de sampling com a ordem do pipeline documentada Consulta: 2026-10-04.
- [llama.cpp — grammars README](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) — o componente que precede os samplers na mesma request Consulta: 2026-10-04.
