---
id: software.testes.tranche18.001199
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
fontes: ["https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html", "https://docs.phpunit.de/en/12.5/attributes.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit: variar entradas com provedores de dados

## Em uma frase
Os provedores fornecem conjuntos de argumentos, e cada conjunto aparece como teste separado no relatório quando identificado por nome.

## Por que importa
A cobertura de variações fica declarativa e cada conjunto tem resultado próprio, evitando que a primeira falha esconda as demais.

## Como funciona
Declare o provedor como método estático, nomeie os conjuntos e mantenha os dados simples, sem criar objetos complexos nem dublês.

## Exemplo
Um provedor pode listar pares de entrada e resultado esperado para a regra de formatação de valores monetários.

## Limites e trade-offs
Provedores que dependem do estado do caso não funcionam, porque são executados antes da preparação, e dados grandes dificultam a leitura.

## Como verificar
Acrescente um conjunto nomeado e confirme que ele aparece como caso independente no relatório.

## Conexões
- [[phpunit-assertions]] — Veja também: PHPUnit: usar asserções específicas.
- [[phpunit-fixtures]] — Veja também: PHPUnit: preparar e limpar com métodos de ciclo.

## Fontes
- [PHPUnit — Writing tests](https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html) — classes de teste, asserções, provedores de dados e exceções; consultado em 2026-10-03.
- [PHPUnit — Attributes](https://docs.phpunit.de/en/12.5/attributes.html) — atributos de teste, provedores, grupos e configuração de dublês; consultado em 2026-10-03.
