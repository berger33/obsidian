---
id: software.testes.fuzzing-libfuzzer.000001
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-01
validade: volatil
status: candidata
revisao_humana: aprovada
revisor: usuario-da-sessao
data_revisao_humana: 2026-10-02
fontes: ["https://llvm.org/docs/LibFuzzer.html", "https://source.android.com/docs/security/test/libfuzzer"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
aliases: [Fuzzing, Coverage-guided fuzzing, libFuzzer]
lote: software-testes-2000-0001
---

# Fuzzing guiado por cobertura com libFuzzer

## Em uma frase
Fuzzing guiado por cobertura muta entradas para exercitar novos caminhos de execução e revelar falhas que entradas fixas podem não atingir.

## Por que importa
Parsers, decodificadores e bibliotecas que aceitam dados não confiáveis podem falhar diante de entradas malformadas, inesperadas ou de fronteira. Um fuzzer pode explorar grandes espaços de entrada e, com sanitizers, ajudar a expor crashes, acessos inválidos e outros defeitos. O resultado depende da qualidade do alvo, instrumentação, corpus e condições de execução.

## Como funciona
O libFuzzer é um motor in-process guiado por cobertura. Ele chama repetidamente uma função-alvo com arrays de bytes, acompanha código alcançado por instrumentação e muta entradas do corpus para buscar novas execuções. O alvo deve tolerar entradas vazias, enormes ou inválidas, evitar encerrar o processo e ser tão determinístico e rápido quanto possível. Um corpus inicial variado pode melhorar a exploração de formatos estruturados; entradas que alcançam novos caminhos podem ser incorporadas ao corpus.

## Exemplo
Um parser de imagens pode ser exposto por um alvo que recebe bytes, tenta decodificá-los e retorna sem efeitos permanentes. O corpus inicial pode conter imagens pequenas válidas e inválidas. Rodar com AddressSanitizer pode tornar acessos de memória incorretos observáveis e produzir uma entrada que reproduz um crash.

## Limites e trade-offs
Fuzzing não prova ausência de defeitos e não substitui testes de propriedades, exemplos de regressão ou análise de segurança. A exploração pode ficar presa se o alvo for lento, não determinístico ou exigir entradas estruturadas que o corpus não representa. A documentação atual do LLVM informa que os autores originais migraram o desenvolvimento ativo para Centipede; verifique estado, versão do Clang e ferramentas suportadas antes de iniciar um projeto novo.

## Como verificar
Confirme que o binário está instrumentado e que o alvo não mantém estado contaminado entre chamadas. Execute com corpus reproduzível e limite de tempo definido no CI; valide que um crash gera artefato preservado e reproduzível. Revise cobertura alcançada, corpus e relatórios dos sanitizers, e teste o corpus como regressão após corrigir cada falha.

## Conexões
- [[property-based-testing-hypothesis]] — ambos exploram dados, mas fuzzing pode usar feedback de cobertura da execução.
- [[shrinking-contraexemplos-hypothesis]] — simplificar a entrada que reproduz a falha facilita diagnóstico.
- [[testes-hermeticos-dependencias]] — alvos determinísticos e isolamento tornam sessões de fuzzing mais reproduzíveis.

## Fontes
- [LLVM — libFuzzer](https://llvm.org/docs/LibFuzzer.html) — arquitetura, alvo, corpus e estado atual do projeto; acesso em 2026-10-01.
- [Android Open Source Project — Fuzz with libFuzzer](https://source.android.com/docs/security/test/libfuzzer) — escrita, execução e instrumentação de fuzzers; acesso em 2026-10-01.
