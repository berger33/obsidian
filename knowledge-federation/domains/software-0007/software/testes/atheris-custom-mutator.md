---
id: software.testes.tranche23.001758
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
fontes: ["https://github.com/google/atheris/blob/master/README.md", "https://github.com/google/fuzzing/blob/master/docs/structure-aware-fuzzing.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Mutators custom: ensinar a gramática sem ensinar gramática

## Em uma frase
A seção Structure-aware Fuzzing do README oficial admite a limitação do modelo — mutação pura em dados complexos morre na porta ("inputs will be rejected early, resulting in low coverage") — e a resposta são os custom mutators do libFuzzer, expostos como parâmetro custom_mutator de atheris.Setup; dentro dele, chama-se atheris.Mutate(data, len) (equivalente ao LLVMFuzzerMutate) para reutilizar a mutação nativa sobre a representação descompactada, compactando o resultado de volta.

## Por que importa
O exemplo documentado (comprimir/descomprimir + verificar 'FU') é quantificado na página: rodando o exemplo com --no_mutator o log congela em cov: 2, corp: 1/1b por milhões de execuções, e o mesmo exemplo com o mutator grava NEWs em ~3 execuções e encontra o RuntimeError em segundos — a doc usa seu próprio benchmark para mostrar a diferença entre fuzzer cego e fuzzer informado.

## Como funciona
O motor sinaliza a troca no stderr — "found LLVMFuzzerCustomMutator... Disabling -len_control by default" — e a seção anuncia que custom crossovers também são aceitos no Setup, com um arquivo de teste exemplo no repo (custom_crossover_fuzz_test.py), mais um caminho pronto para Protocol Buffers via libprotobuf-mutator com bindings próprias (atheris_libprotobuf_mutator, na pasta contrib).

## Exemplo
Antes de escrever um mutador custom, rode o exemplo custom_mutator_example.py da seção uma vez com e outra sem a flag: os dois logs lado a lado são a decisão de investimento mais barata que a página oferece.

## Limites e trade-offs
A seção recomenda implicitamente o padrão try/except no mutador (decompress falhou, devolve b'Hi') — mutadores custom são código seu dentro do hot path do motor; um mutador lento vira o gargalo da campanha inteira, e a página não impõe contrato de performance sobre ele. O repositório google/fuzzing foi arquivado e marcado somente-leitura pelo dono em 27/12/2025, conforme aviso na própria página — o documento de referência permanece acessível, mas não receberá correções.

## Como verificar
Confirme a subseção Structure-aware Fuzzing do README oficial: a citação do exemplo do LibFuzzer docs, o bloco CustomMutator, a linha INITED versus a linha NEW do log e os parágrafos de crossover e protobuf.

## Conexões
- [[atheris-fuzzeddataprovider]] — Veja também: FuzzedDataProvider: bytes viram tipos sem parser de fita.
- [[atheris-ossfuzz-native]] — Veja também: Integração com OSS-Fuzz e o caso dos módulos nativos.

## Fontes
- [Atheris — README oficial](https://github.com/google/atheris/blob/master/README.md) — definição, instalação, instrumentação, API e mutators custom; consultado em 2026-10-03.
- [google/fuzzing — Structure-aware fuzzing](https://github.com/google/fuzzing/blob/master/docs/structure-aware-fuzzing.md) — doc de custom mutators usada como referência pelo README; consultado em 2026-10-03.
