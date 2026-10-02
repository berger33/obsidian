---
id: software.testes.tranche11.000507
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-11.md"
fontes: ["https://xunit.net/docs/running-tests-in-parallel", "https://xunit.net/docs/config-xunit-runner-json"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# xUnit: entender paralelismo por collection antes de aumentar threads

## Em uma frase
No modo collections, testes de uma collection não rodam em paralelo entre si, mas collections distintas podem concorrer.

## Por que importa
Aumentar workers pode acelerar teste independente e também expor race em banco, arquivos ou variável estática compartilhada.

## Como funciona
Separe testes por recurso compartilhado, proteja estado necessário e ajuste paralelismo do runner com medição.

## Exemplo
Duas classes da mesma collection usam servidor único; classe sem dependência roda junto em collection separada.

## Limites e trade-offs
Modo e algoritmos disponíveis dependem da versão do framework e do runner; configuração de assembly não é configuração universal.

## Como verificar
Observe tempo, sobreposição e integridade de dados com paralelismo ligado e desligado.

## Conexões
- [[xunit-async-lifetime-teardown]] — Veja também: xUnit: escolher lifecycle async compatível com versão.
- [[xunit-outputhelper-saida-associada]] — Veja também: xUnit: associar diagnóstico ao teste com ITestOutputHelper.

## Fontes
- [xUnit.net — Running Tests in Parallel](https://xunit.net/docs/running-tests-in-parallel) — coleções, modos de paralelismo, limites e escopo de runner; consultado em 2026-10-02.
- [xUnit.net — Configuration Files](https://xunit.net/docs/config-xunit-runner-json) — opções de runner, execução paralela e configuração por assembly; consultado em 2026-10-02.
