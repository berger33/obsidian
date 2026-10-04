---
id: software.criacao_ia.tranche04.000388
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

# GBNF: repetições aninhadas custam exponencialmente — e a doc dá o recheio anti-armadilha

## Em uma frase
A performance de uma grammar durante a geração depende da forma: repetidores aninhados como 'x? x?' explodem o custo de parse e a correção documentada é a forma plana 'x{0,N}'.

## Por que importa
A mask de logits roda um parser incremental da grammar por token candidato por passo — o trabalho do parser é função da sua escrita, não só do tamanho da saída. A doc de grammars registra o caso (repetidores adjacentes gerando caminhos combinatórios) com o issue de referência #4218 e o reescrito linear; quem trata grammar como config barata paga isso em TPS caindo conforme o prompt cresce.

## Como funciona
Regras do README aplicadas: prefira o operador de contagem explícita 'x{0,10}' a cadeias de opcionais 'x? x? ... x?'; mantenha alternância rasa (o | profundo multiplica o backtrack do parser de Earley); e use a validação de performance da própria ferramenta do repo para medir o custo da sua grammar num texto-alvo antes de produção. Quando a saída tem seções longas (JSON com arrays profundos), o custo é do modelo E do parser — dimensione contexto e timeout com isso na conta.

## Exemplo
A grammar de 'lista CSV de até 40 campos' escrita como '(campo ,){0,40}' plana sustenta o TPS; a mesma intenção como repetidores adjacentes aninhados derruba throughput na cauda da lista — o delta medido é o argumento para code review de .gbnf.

## Limites e trade-offs
Não há budget de parser por request configurável: grammar lenta é lenta para todos os tokens, e o 'travamento' de um servidor com poucas sessões longas de grammar pode parecer hang do modelo. O teste-gbnf-validator mede parsing de conformidade, não throughput por token do modelo — a medição de TPS é sua, com a grammar no campo grammar. E grammar grande demais compete com o contexto: a doc do JSON-schema abaixo lembra que só a saída é restringida — o texto da grammar não entra no prompt (mas o seu custo computacional sim).

## Como verificar
Compare TPS medido do mesmo prompt com as duas grafias (plana vs. aninhada) no seu hardware: é a quantificação da regra da doc. Um corpus de saída-alvo (10 docs) parseado pelo validador com e sem timeout documenta a conformidade. Na CI, uma asserção de tempo de parse da grammar por release do modelo — a regressão de performance de grammar entra pela porta do tokenizer às vezes.

## Conexões
- [[gbnf-sintaxe-e-root]] — GBNF: a sintaxe que construi constrangimento de tokens, e o que 'root' significa.
- [[gbnf-json-schema-nao-e-prompt]] — llama.cpp: JSON Schema vira GBNF — restringe a saída e não entra no prompt.

## Fontes
- [llama.cpp — grammars README](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md) — a seção de performance com o exemplo x?x? → x{0,N} e referência ao issue #4218 Consulta: 2026-10-04.
- [llama.cpp — tools/server README](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) — o consumo no server que transforma custo de parser em custo de serving Consulta: 2026-10-04.
