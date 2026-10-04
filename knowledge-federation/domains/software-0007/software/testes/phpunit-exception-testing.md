---
id: software.testes.tranche18.001203
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
fontes: ["https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html", "https://docs.phpunit.de/en/12.5/test-doubles.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit: verificar caminhos de exceção

## Em uma frase
As asserções de exceção confirmam a classe lançada e permitem inspecionar a mensagem, com cuidados sobre o trecho realmente coberto pela verificação.

## Por que importa
Caminhos de erro são parte do contrato e, sem verificação, regressões passam a devolver falhas genéricas em produção.

## Como funciona
Verifique a classe da exceção, limite a verificação ao trecho que deve lançá-la e confira a mensagem apenas quando ela for parte do contrato.

## Exemplo
Uma validação de entrada pode ser exercitada com valor inválido para confirmar a exceção de domínio correspondente.

## Limites e trade-offs
Envolver código demais na verificação faz outra exceção passar pelo mesmo teste, e a checagem apenas de mensagem aceita classes erradas.

## Como verificar
Faça o trecho lançar outro tipo de exceção e confirme que a verificação correspondente falha.

## Conexões
- [[phpunit-coverage]] — Veja também: PHPUnit: medir e interpretar cobertura.
- [[phpunit-groups-and-filtering]] — Veja também: PHPUnit: organizar e selecionar execuções.

## Fontes
- [PHPUnit — Writing tests](https://docs.phpunit.de/en/12.5/writing-tests-for-phpunit.html) — classes de teste, asserções, provedores de dados e exceções; consultado em 2026-10-03.
- [PHPUnit — Test doubles](https://docs.phpunit.de/en/12.5/test-doubles.html) — dublês de tipos, configuração de retornos e verificação de chamadas; consultado em 2026-10-03.
