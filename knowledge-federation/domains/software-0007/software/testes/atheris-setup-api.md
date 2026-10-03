---
id: software.testes.tranche23.001756
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-23.md"
fontes: ["https://github.com/google/atheris/blob/master/README.md", "https://llvm.org/docs/LibFuzzer.html#options"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# A API de três faces: Setup, Fuzz e o internal_libfuzzer

## Em uma frase
A seção API do README oficial especifica as assinaturas centrais: Setup(args, test_one_input, internal_libfuzzer=None) — onde args são os strings de processo (tipicamente sys.argv) que podem ser modificados in-place para remover os argumentos consumidos pelo fuzzer (a lista de flags é a da documentação do libFuzzer, linkada), test_one_input precisa receber exatamente um bytes, e internal_libfuzzer diz se o libFuzzer vem do Atheris ou de uma lib externa, auto-determinado quando não especificado, com a instrução explícita: fuzzing de Python puro, deixe como True.

## Por que importa
A separação Setup e Fuzz — reconhecida na página como quase redundante ("in many cases Setup() and Fuzz() could be combined") — é justificada funcionalmente: você frequentemente quer o motor consumindo a argv antes do setup do seu código; é a mesma razão de flags -atheris_runs conviverem com as flags nativas do libFuzzer.

## Como funciona
O Fuzz() documenta a não-return ("This function does not return") — o harness termina ali; o processamento de exceção que encerra o processo é o motor reportando, não seu main.

## Exemplo
Escreva um harness que imprime a argv residual entre Setup e Fuzz: as flags do libFuzzer consumidas devem ter sumido da lista, materializando a frase "this argument list may be modified in-place".

## Limites e trade-offs
A página define a semântica, não a lista completa de flags aceitas — o contrato dos argumentos consumidos é da doc do libFuzzer (linkada como referência), então opções novas do LLVM podem passar sem suporte até a release seguinte do Atheris.

## Como verificar
Confirme as três subseções de API Setup, Fuzz e a frase da modificação in-place no README oficial; valide o link da llvm.org/docs/LibFuzzer.html#options referenciado.

## Conexões
- [[atheris-coverage-viz]] — Veja também: Ver cobertura linha a linha com coverage.py e -atheris_runs.
- [[atheris-fuzzeddataprovider]] — Veja também: FuzzedDataProvider: bytes viram tipos sem parser de fita.

## Fontes
- [Atheris — README oficial](https://github.com/google/atheris/blob/master/README.md) — definição, instalação, instrumentação, API e mutators custom; consultado em 2026-10-03.
- [LLVM — LibFuzzer documentation](https://llvm.org/docs/LibFuzzer.html#options) — lista de flags consumidas pelo Setup, referenciada pelo README; consultado em 2026-10-03.
