---
id: software.criacao_ia.tranche04.000389
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
fontes: ["https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md", "https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# llama.cpp: JSON Schema vira GBNF — restringe a saída e não entra no prompt

## Em uma frase
O caminho estruturado do server aceita um JSON Schema (campo json_schema no sabor nativo, response_format na API OpenAI, ou -j global) convertido em grammar — com as ressalvas documentadas de versão de spec e unsupported silencioso.

## Por que importa
A assimetria com OpenAI estruturado é o ponto cego do port: lá, o schema vai no prompt (e o modelo 'vê' a forma); aqui, o schema só restringe por máscara — o modelo nunca lê a descrição. Tudo que não está na mask (semântica de campo, enum descriptions) precisa continuar no prompt, ou o modelo satisfaz a forma com conteúdo fora da intenção. E 'campos unsupported são ignorados silenciosamente' é a segunda metade do contrato.

## Como funciona
A doc do README de grammars formaliza o recorte: 'JSON Schema draft 2020-12', com o suporte declarado sobre o subconjunto que a conversão trata; additionalProperties default false (fechar extra); pattern exige âncoras ^...$ explícitas; min/max só de inteiros na conversão; $ref aninhado/remote tem os bugs que a própria página lista. No pedido, o campo json_schema é a rota por-request; -j define um default global. Para tool calls, o texto lembra a diferença: o schema de tools sim vai no prompt (a conversa de função é prompt), o de resposta não.

## Exemplo
O extrator de fatura com 'type:object, required:[total, currency], properties:{total:{type:number}...}': a forma é garantida, mas o prompt continua explicando 'total = valor com IVA, decimal point' porque a mask sozinha não diz isso ao modelo.

## Limites e trade-offs
Restrição dura ≠ modelo bom: o sampling obedece a grammar, mas a qualidade do preenchimento é do modelo — uma grammar perfeita com um 1B ruim dá JSON válido e errado. Conversões complexas (oneOf profundo, format:date-time semantics) caem no ignorado-silencioso — valide o que o produto precisa com teste, não por fé no convertor. E -j global aplica a todas as requests de um mesmo server — em multi-tenant, o default vira política; prefira por-request.

## Como verificar
Um teste de conformidade por prompt real: N saídas × schema.validate(), com asserção de 100% — o contrato da mask deve dar isso. Um campo 'description' ignorado: confirme que o modelo o vê só se estiver no prompt (o diff entre com/sem é a prova da assimetria). Uma schema com $ref aninhado: teste e registre se a sua build cai no caso conhecido da doc.

## Conexões
- [[gbnf-custo-e-armadilha-de-repeticao]] — GBNF: repetições aninhadas custam exponencialmente — e a doc dá o recheio anti-armadilha.
- [[llamacpp-samplers-ordem-fixa]] — llama.cpp: o pipeline de samplers tem ordem fixa, e cada campo do pedido é um nó dele.

## Fontes
- [llama.cpp — grammars README](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) — a seção JSON Schema: conversão, defaults, unsupported silencioso e as ressalvas específicas Consulta: 2026-10-04.
- [llama.cpp — tools/server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) — os campos json_schema/response_format e -j no server Consulta: 2026-10-04.
