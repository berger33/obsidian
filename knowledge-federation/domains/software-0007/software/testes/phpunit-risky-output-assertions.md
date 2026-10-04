---
id: software.testes.tranche12.000608
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://docs.phpunit.de/en/12.5/risky-tests.html", "https://docs.phpunit.de/en/12.5/configuration.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit 12.5: interpretar testes marcados como risky

## Em uma frase
PHPUnit pode classificar como arriscados testes sem assertions úteis ou que produzem saída, conforme verificações habilitadas.

## Por que importa
Um teste que roda sem validar resultado ou imprime acidentalmente pode parecer verde e ainda fornecer pouco sinal confiável para CI.

## Como funciona
Ative checagens de output e testes sem assertions de forma deliberada, avalie warnings e use `--fail-on-risky` quando a política do projeto exigir que o status afete o código de saída.

## Exemplo
Um teste de endpoint que só envia request sem verificar response pode ser sinalizado como inútil, enquanto um `print` de depuração pode violar a política de output.

## Limites e trade-offs
Marcar `DoesNotPerformAssertions` indiscriminadamente suprime o sinal de teste arriscado; o atributo não substitui uma verificação observável de comportamento.

## Como verificar
Introduza um caso vazio e um caso que imprime texto para conferir a configuração efetiva e a reação do job quando recebe `--fail-on-risky`.

## Conexões
- [[phpunit-random-seed-repro]] — Veja também: PHPUnit 12.5: reproduzir falhas por ordem aleatória.
- [[phpunit-size-time-budget]] — Veja também: PHPUnit 12.5: classificar tamanhos e limites de duração.

## Fontes
- [PHPUnit 12.5 — Risky Tests](https://docs.phpunit.de/en/12.5/risky-tests.html) — testes sem assertions, output e critérios de risco; consultado em 2026-10-02.
- [PHPUnit 12.5 — Configuration](https://docs.phpunit.de/en/12.5/configuration.html) — precedência entre defaults, XML e opções da linha de comando; consultado em 2026-10-02.
