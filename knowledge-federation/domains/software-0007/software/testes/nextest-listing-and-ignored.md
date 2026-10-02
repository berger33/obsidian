---
id: software.testes.tranche15.000949
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://nexte.st/docs/running/", "https://nexte.st/docs/partitioning/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# nextest: listar e reexecutar testes ignorados

## Em uma frase
O comando de listagem mostra o conjunto descoberto sem executar, e a opção de execução de ignorados permite rodar casos marcados como pendentes.

## Por que importa
Listar antes de executar valida filtros e partições, enquanto ignorados esquecidos escondem cobertura que a equipe julga existente.

## Como funciona
Use a listagem para conferir a seleção, execute ignorados quando a verificação for intencional e trate os casos pendentes como dívida visível.

## Exemplo
`cargo nextest list` apresenta os testes descobertos, e a execução de ignorados pode ser solicitada explicitamente para verificar trabalho incompleto.

## Limites e trade-offs
Ignorados não entram no resultado padrão e podem permanecer nesse estado por tempo indeterminado; a listagem mostra o que existe, não o que está coberto de verdade.

## Como verificar
Compare a lista completa com a lista filtrada de um shard e execute os ignorados para observar quais casos ainda falham antes de decidir mantê-los.

## Conexões
- [[nextest-doctests-boundary]] — Veja também: nextest: reconhecer o limite dos doctests.

## Fontes
- [nextest — Running tests](https://nexte.st/docs/running/) — execução, filtros, saída, listagem e testes ignorados; consultado em 2026-10-02.
- [nextest — Partitioning](https://nexte.st/docs/partitioning/) — particionamento por fatias e por hash para shards de CI; consultado em 2026-10-02.
