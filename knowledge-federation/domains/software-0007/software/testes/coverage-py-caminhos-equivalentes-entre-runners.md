---
id: software.testes.tranche15.000879
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
fontes: ["https://coverage.readthedocs.io/en/latest/config.html", "https://coverage.readthedocs.io/en/latest/commands/cmd_report.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: mapear caminhos de checkout ao combinar workers

## Em uma frase
Builds em diretórios diferentes podem registrar o mesmo arquivo-fonte com caminhos absolutos distintos, fragmentando a cobertura combinada sem uma regra de equivalência.

## Por que importa
A seção `[paths]` declara conjuntos de prefixos que representam a mesma árvore de fontes em runners locais, containers ou sistemas operacionais diferentes.

## Como funciona
Na combinação, coverage.py pode remapear um arquivo para o primeiro caminho correspondente que exista no ambiente de relatório.

## Exemplo
Liste `src/` como caminho canônico e acrescente padrões específicos dos workers sob a mesma entrada; teste a regra com dados gravados em paths de build separados antes de habilitar em todos os jobs.

## Limites e trade-offs
Um padrão amplo pode unir módulos diferentes com o mesmo sufixo e dados combinados de revisões distintas continuam semanticamente incompatíveis mesmo se os caminhos coincidirem.

## Como verificar
Combine dois artefatos conhecidos da mesma revisão, verifique o número de arquivos mapeados e investigue avisos de caminhos que ficaram sem correspondência.

## Conexões
- [[coverage-py-relatorios-formatados-e-fail-under]] — Veja também: coverage.py: escolher formato de relatório e aplicar limite de cobertura.

## Fontes
- [Coverage.py 7.16.2 — Configuration reference](https://coverage.readthedocs.io/en/latest/config.html) — opções run/report, arquivos paralelos, paths, exclusões e limites; consultado em 2026-10-02.
- [Coverage.py 7.16.2 — coverage report](https://coverage.readthedocs.io/en/latest/commands/cmd_report.html) — resumo, contexts, fail-under, formatos e colunas de branch; consultado em 2026-10-02.
