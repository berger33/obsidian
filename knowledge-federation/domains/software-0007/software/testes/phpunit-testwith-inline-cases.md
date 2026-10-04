---
id: software.testes.tranche12.000602
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
fontes: ["https://docs.phpunit.de/en/12.5/attributes.html", "https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit 12.5: escolher entre `TestWith` e Data Provider

## Em uma frase
O atributo `#[TestWith]` permite associar dados inline ao teste, enquanto `#[DataProvider]` mantém datasets maiores em um método nomeado.

## Por que importa
Colocar poucas linhas junto da assertion facilita leitura local; separar tabelas extensas evita que detalhes de entrada ocupem o corpo principal do teste.

## Como funciona
Use `TestWith` para casos curtos e estáveis e extraia provider quando a tabela exigir preparação, nomes ou reutilização que mereçam referência própria.

## Exemplo
Um teste de normalização pode declarar duas strings simples por atributos; uma matriz maior de moedas pode ficar em provider com conjuntos nomeados.

## Limites e trade-offs
Dados inline também podem esconder o propósito de uma linha se os valores forem opacos, e compartilhar provider não significa que as suites têm a mesma intenção.

## Como verificar
Leia a falha produzida por cada caso e confirme que a origem do valor está clara sem buscar em uma fixture global.

## Conexões
- [[phpunit-dataprovider-contrato]] — Veja também: PHPUnit 12.5: manter contratos explícitos em Data Providers.
- [[phpunit-depends-retorno]] — Veja também: PHPUnit 12.5: usar `Depends` para transferir resultado.

## Fontes
- [PHPUnit 12.5 — Attributes](https://docs.phpunit.de/en/12.5/attributes.html) — atributos #[Test], #[DataProvider], #[TestWith], #[Depends] e configurações; consultado em 2026-10-02.
- [PHPUnit 12.5 — Writing Tests](https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html) — descoberta, nomes, atributos de teste, providers e fluxo AAA; consultado em 2026-10-02.
