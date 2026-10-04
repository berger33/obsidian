---
id: software.testes.tranche12.000601
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

# PHPUnit 12.5: manter contratos explícitos em Data Providers

## Em uma frase
Um data provider associa conjuntos de argumentos a um método de teste e faz cada conjunto aparecer como uma execução identificável.

## Por que importa
Parâmetros variados melhoram cobertura de fronteiras sem duplicar assertions, desde que os dados venham de uma fonte legível e não dependam do estado da fixture.

## Como funciona
Marque o teste com `#[DataProvider]`, implemente o provider na forma exigida pela versão e retorne iterável de conjuntos cujos tipos e ordem correspondam à assinatura do teste.

## Exemplo
Um provider pode devolver código do país, entrada e saída esperada para verificar as regras de normalização em cada combinação.

## Limites e trade-offs
Providers são avaliados antes do ciclo de `setUp`; não use `$this` ou objetos de fixture criados para cada execução para fabricar os argumentos.

## Como verificar
Rode o teste com um conjunto que falha e confira se o relatório identifica seus dados sem tornar a linha de saída impossível de interpretar.

## Conexões
- [[phpunit-discovery-metodos-atributos]] — Veja também: PHPUnit 12.5: descobrir métodos de teste.
- [[phpunit-testwith-inline-cases]] — Veja também: PHPUnit 12.5: escolher entre `TestWith` e Data Provider.

## Fontes
- [PHPUnit 12.5 — Writing Tests](https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html) — descoberta, nomes, atributos de teste, providers e fluxo AAA; consultado em 2026-10-02.
- [PHPUnit 12.5 — Attributes](https://docs.phpunit.de/en/12.5/attributes.html) — atributos #[Test], #[DataProvider], #[TestWith], #[Depends] e configurações; consultado em 2026-10-02.
