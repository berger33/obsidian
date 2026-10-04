---
id: software.testes.tranche22.001650
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://gcovr.com/en/stable/index.html", "https://pypi.org/project/gcovr/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# gcovr: o gcov resumido em texto e XML

## Em uma frase
O gcovr é um utilitário para gerenciar o uso do GNU gcov e gerar sumários de cobertura de código resumidos, com inspiração declarada no coverage.py do Python — um comando de linha alternativo ao lcov que roda o gcov e produz relatórios.

## Por que importa
gcov sozinho cospe um arquivo anotado por unidade de compilação; times C/C++ precisam de um número por commit e de um XML que o portal de qualidade entenda, e é essa lacuna que a ferramenta declara cobrir ("text summaries and XML reports").

## Como funciona
O pacote é Python: instale do PyPI com pip install gcovr e invoque sobre um build instrumentado; os selos oficiais apontam GitHub, issue tracker e Stack Overflow com tag própria.

## Exemplo
A tabela de opções da página inicial mostra um formato por flag — de --txt (default) a --sonarqube —, e é essa matriz que define onde a ferramenta para e onde o lcov começa.

## Limites e trade-offs
Desenvolvimento do projeto foi motivado por formatos que faltavam no lcov da época; quem precisa exatamente do HTML do lcov pode não ganhar nada trocando.

## Como verificar
Rode pipx run gcovr --version ou instale o pacote e confirme que o help lista as flags da tabela oficial.

## Conexões
- [[gcovr-getting-started]] — Veja também: gcovr: três passos do build ao relatório.

## Fontes
- [gcovr — documentação inicial (8.6)](https://gcovr.com/en/stable/index.html) — definição, matriz de formatos de saída e índice da doc; consultado em 2026-10-03.
- [gcovr — página no PyPI](https://pypi.org/project/gcovr/) — instalação oficial via pip; consultado em 2026-10-03.
