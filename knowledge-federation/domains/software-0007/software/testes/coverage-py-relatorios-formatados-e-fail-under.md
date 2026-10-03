---
id: software.testes.tranche15.000878
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
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://coverage.readthedocs.io/en/latest/commands/cmd_report.html", "https://coverage.readthedocs.io/en/latest/config.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: escolher formato de relatório e aplicar limite de cobertura

## Em uma frase
O mesmo conjunto de dados de execução pode ser exibido em saídas distintas; `fail_under` transforma o percentual total em condição de saída do comando de relatório.

## Por que importa
O formato texto é adequado a logs, HTML ajuda a inspecionar linhas e XML, JSON ou LCOV alimentam integrações.

## Como funciona
A cobertura de branches pode compor o total reportado, e a precisão configurada influencia a interpretação de limites fracionários.

## Exemplo
Gere HTML para investigação local e XML ou LCOV para ferramentas externas; configure `[report] fail_under` ou a opção equivalente no comando usado pelo job de CI.

## Limites e trade-offs
Um limite agrega uma métrica escolhida e não verifica exclusões, teste relevante ou diff; formatadores e parsers de CI podem mostrar arredondamentos diferentes.

## Como verificar
Force temporariamente um limite acima da cobertura atual e confirme que o relatório termina com o status esperado, depois valide que o formato armazenado continua sendo consumido pelo dashboard.

## Conexões
- [[coverage-py-contexto-de-cobertura-nao-e-assertividade]] — Veja também: coverage.py: não interpretar linha executada como comportamento validado.
- [[coverage-py-caminhos-equivalentes-entre-runners]] — Veja também: coverage.py: mapear caminhos de checkout ao combinar workers.

## Fontes
- [Coverage.py 7.16.2 — coverage report](https://coverage.readthedocs.io/en/latest/commands/cmd_report.html) — resumo, contexts, fail-under, formatos e colunas de branch; consultado em 2026-10-02.
- [Coverage.py 7.16.2 — Configuration reference](https://coverage.readthedocs.io/en/latest/config.html) — opções run/report, arquivos paralelos, paths, exclusões e limites; consultado em 2026-10-02.
