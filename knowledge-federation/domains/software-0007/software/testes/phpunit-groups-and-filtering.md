---
id: software.testes.tranche18.001204
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
fontes: ["https://docs.phpunit.de/en/12.5/attributes.html", "https://github.com/sebastianbergmann/phpunit"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PHPUnit: organizar e selecionar execuções

## Em uma frase
Grupos e filtros permitem incluir ou excluir conjuntos de testes, e a configuração do projeto pode declarar suítes separadas por tipo.

## Por que importa
Recortes por natureza do teste mantêm execuções rápidas na revisão e a suíte completa nas etapas mais custosas.

## Como funciona
Declare suítes por diretório ou grupo, mantenha a convenção estável e execute filtros apenas de forma temporária.

## Exemplo
Uma suíte de integração pode ficar separada da suíte de unidade, permitindo decidir quando cada uma roda no pipeline.

## Limites e trade-offs
Filtros de linha de comando repetidos viram prática informal que ninguém documenta, e grupos inconsistentes deixam testes fora da execução.

## Como verificar
Liste os testes de cada suíte declarada e confirme que o conjunto corresponde ao esperado antes de fixar a configuração.

## Conexões
- [[phpunit-exception-testing]] — Veja também: PHPUnit: verificar caminhos de exceção.
- [[phpunit-ci-and-reports]] — Veja também: PHPUnit: integrar ao pipeline com evidências.

## Fontes
- [PHPUnit — Attributes](https://docs.phpunit.de/en/12.5/attributes.html) — atributos de teste, provedores, grupos e configuração de dublês; consultado em 2026-10-03.
- [PHPUnit — repositório oficial](https://github.com/sebastianbergmann/phpunit) — código-fonte, exemplos e documentação do projeto; consultado em 2026-10-03.
