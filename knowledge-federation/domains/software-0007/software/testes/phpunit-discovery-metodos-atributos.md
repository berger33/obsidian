---
id: software.testes.tranche12.000600
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
fontes: ["https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html", "https://docs.phpunit.de/en/12.5/attributes.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit 12.5: descobrir métodos de teste

## Em uma frase
PHPUnit descobre métodos públicos com prefixo `test` ou métodos marcados com o atributo `#[Test]`.

## Por que importa
Uma convenção consistente torna previsível quais métodos entram na suite e evita que um helper público seja executado como teste por engano.

## Como funciona
Agrupe casos na classe apropriada, mantenha `TestCase` como base e escolha entre prefixo e atributo sem misturar estilos sem motivo.

## Exemplo
Uma classe `MoneyTest` pode declarar `testAddsCurrencies()` ou usar `#[Test]` em `addsCurrencies()`, mantendo nome que descreve o comportamento verificado.

## Limites e trade-offs
Um método correto numa classe ou arquivo fora dos padrões de descoberta pode nunca ser executado, apesar de aparecer no editor como teste.

## Como verificar
Use `--list-tests` para conferir a lista descoberta e compare nomes e arquivos com a suite que a pipeline pretende executar.

## Conexões
- [[phpunit-dataprovider-contrato]] — Veja também: PHPUnit 12.5: manter contratos explícitos em Data Providers.

## Fontes
- [PHPUnit 12.5 — Writing Tests](https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html) — descoberta, nomes, atributos de teste, providers e fluxo AAA; consultado em 2026-10-02.
- [PHPUnit 12.5 — Attributes](https://docs.phpunit.de/en/12.5/attributes.html) — atributos #[Test], #[DataProvider], #[TestWith], #[Depends] e configurações; consultado em 2026-10-02.
