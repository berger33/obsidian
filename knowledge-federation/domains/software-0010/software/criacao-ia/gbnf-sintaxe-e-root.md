---
id: software.criacao_ia.tranche04.000387
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

# GBNF: a sintaxe que construi constrangimento de tokens, e o que 'root' significa

## Em uma frase
Uma grammar GBNF é regras 'nome ::= sequência' (nomes minúsculos com traço) sobre terminais de texto e tokens especiais; a regra 'root' define exatamente qual string é aceita como saída inteira.

## Por que importa
Constrained decoding não é 'dica ao modelo' — é mask de logits: cada token do passo é aceito só se um próximo estado da grammar existir. Isso torna a gramática um contrato de parser: se root não casa com a forma completa da saída, o modelo pode gerar uma string válida por partes e inválida no todo — ou travar no fim do contexto sem fechar a regra.

## Como funciona
Os blocos da doc: repetição (*, +, ?, {m}, {m,n}), ranges ([a-z], [^...] para negação), alternância com |, e a escape <[token_id]> para forçar um único token do vocabulário (o caso 'e.g. \n como token único'). # começa comentário de linha. 'root ::= ws "{" ...' etc: a saída tem que cobrir root inteira — whitespace explícito na grammar, senão o modelo 'não pode' emiti-lo. No server, a grammar entra pelo campo grammar (sabor nativo) — e a doc do server documenta o caminho, mantendo o arquivo fora do prompt.

## Exemplo
Uma resposta 'apenas número inteiro positivo': 'root ::= [1-9][0-9]*' — o modelo não consegue emitir texto, espaço ou zero-líder, porque a grammar não tem caminho neles; e o caso de teste do zero-líder vira asserção no seu suite.

## Limites e trade-offs
GBNF não é regex cheia nem contexto-free arbitrário: é uma classe com a restrição de parse em tempo de geração — e o desempenho depende de como você escreve (nota do próximo tópico). <[token]> é fragile ao tokenizer (o id não é o mesmo entre modelos; a doc cobre o conceito, a manutenção não). E root obrigatoriamente consome a saída: strings 'de fora' (preamble, markdown) não têm como escapar do constrangimento a não ser que a grammar as aceite.

## Como verificar
Valide a grammar com as ferramentas do próprio repo (gbnf-validator/test-gbnf-validator — a seção de ferramentas do README) antes de subir para o server. Rode o teste adversarial clássico: prompt que implora por texto fora do contrato (o modelo deve ser incapaz — a máscara é dura). Uma suite de 'N amostras × conformidade por regex' é o teste de regressão de grammar.

## Conexões
- [[llamacpp-servidor-sem-auth-na-rede]] — llama.cpp server: não é um servidor de produção exposto — e as três chaves que aproximam.
- [[gbnf-custo-e-armadilha-de-repeticao]] — GBNF: repetições aninhadas custam exponencialmente — e a doc dá o recheio anti-armadilha.

## Fontes
- [llama.cpp — grammars README](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) — referência da sintaxe (repetições, ranges, tokens, comentários) e do conceito de root Consulta: 2026-10-04.
- [llama.cpp — tools/server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) — o campo grammar e o consumo no server Consulta: 2026-10-04.
