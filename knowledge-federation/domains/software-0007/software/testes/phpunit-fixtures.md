---
id: software.testes.tranche18.001200
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-18.md"
fontes: ["https://docs.phpunit.de/en/12.5/fixtures.html", "https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit: preparar e limpar com métodos de ciclo

## Em uma frase
Os métodos de preparação e limpeza são executados antes e depois de cada teste, e há variantes no nível da classe para recursos compartilhados.

## Por que importa
A preparação isolada reduz dependência entre casos e deixa explícito o estado inicial de cada verificação.

## Como funciona
Prepare o estado mínimo no nível de teste, use o nível de classe apenas para recursos custosos e mantenha a limpeza correspondente na mesma camada.

## Exemplo
Um caso de persistência pode abrir transação antes do exercício e revertê-la depois, devolvendo o banco ao estado anterior.

## Limites e trade-offs
Recursos compartilhados no nível de classe sem limpeza contaminam a execução seguinte, e a preparação pesada em cada caso torna a suíte lenta.

## Como verificar
Rode a classe completa em ordem aleatória e confirme que cada teste continua independente dos demais.

## Conexões
- [[phpunit-data-providers]] — Veja também: PHPUnit: variar entradas com provedores de dados.
- [[phpunit-test-doubles]] — Veja também: PHPUnit: substituir dependências com dublês.

## Fontes
- [PHPUnit — Fixtures](https://docs.phpunit.de/en/12.5/fixtures.html) — preparação e limpeza por teste e por classe; consultado em 2026-10-03.
- [PHPUnit — Writing tests](https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html) — classes de teste, asserções, provedores de dados e exceções; consultado em 2026-10-03.
