---
id: software.testes.tranche16.000993
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-16.md"
fontes: ["https://coverage.readthedocs.io/en/6.5.0/branch.html", "https://coverage.readthedocs.io/en/6.5.0/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: habilitar cobertura de ramos

## Em uma frase
Com cobertura de ramos ativa, a medição registra quais desfechos de decisões foram executados, inclusive caminhos parciais de expressões lógicas.

## Por que importa
Existe linha coberta por um único desfecho, e somente a leitura de ramos revela a condição que nunca foi exercitada.

## Como funciona
Ative a opção no arquivo de configuração para que toda a equipe use o mesmo modo e interprete as linhas parciais como comportamento não verificado.

## Exemplo
Uma função de validação com caminho de aceitação testado e caminho de recusa intocado aparece com ramo parcial apesar de a linha constar como executada.

## Limites e trade-offs
Nem todo ramo é significativo, e decisões defensivas geradas por ferramentas podem inflar a lista; a triagem deve focar caminhos de negócio.

## Como verificar
Compare o relatório com e sem a opção e explique quais linhas mudaram de estado para confirmar que a medição de ramos está ativa.

## Conexões
- [[coveragepy-run-basics]] — Veja também: coverage.py: medir a execução de um programa.
- [[coveragepy-config-files]] — Veja também: coverage.py: centralizar regras na configuração.

## Fontes
- [coverage.py — Branch coverage](https://coverage.readthedocs.io/en/6.5.0/branch.html) — medição de ramos, ramos parciais e ajuste de exclusões; consultado em 2026-10-03.
- [coverage.py — Configuration](https://coverage.readthedocs.io/en/6.5.0/config.html) — arquivos de configuração, fontes, omissões, exclusões e limites; consultado em 2026-10-03.
