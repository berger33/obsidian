---
id: software.testes.tranche15.000872
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
fontes: ["https://coverage.readthedocs.io/en/latest/config.html", "https://coverage.readthedocs.io/en/latest/commands/cmd_combine.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: combinar arquivos paralelos antes de interpretar a cobertura

## Em uma frase
Com execuções paralelas, cada processo pode gravar seu próprio arquivo de dados; a combinação agrega essas medições para produzir uma visão coerente do conjunto.

## Por que importa
A opção `parallel` incorpora máquina, PID e um sufixo aleatório no arquivo de dados, evitando que processos sobrescrevam a mesma base.

## Como funciona
`coverage combine` reúne os arquivos compatíveis; versões atuais também automatizam parte dessa combinação durante operações de relatório quando detectam arquivos paralelos.

## Exemplo
Configure `[run] parallel = true`, execute os processos e confira os arquivos gerados; use `coverage combine` explicitamente quando o pipeline precisa de uma etapa de agregação auditável antes dos relatórios.

## Limites e trade-offs
Dados antigos, workers de outro commit ou caminhos distintos podem contaminar ou fragmentar a combinação; mantenha artifacts isolados por revisão e use `[paths]` apenas para aliases equivalentes.

## Como verificar
Gere dados em dois processos com caminhos controlados, combine-os e compare a soma de contextos/linhas com relatórios individuais e com uma execução serial de referência.

## Conexões
- [[coverage-py-contextos-estaticos-para-fases]] — Veja também: coverage.py: marcar fases de execução com contextos estáticos.
- [[coverage-py-subprocessos-e-instrumentacao]] — Veja também: coverage.py: propagar medição a subprocessos de forma configurada.

## Fontes
- [Coverage.py 7.16.2 — Configuration reference](https://coverage.readthedocs.io/en/latest/config.html) — opções run/report, arquivos paralelos, paths, exclusões e limites; consultado em 2026-10-02.
- [Coverage.py 7.16.2 — Combining data files](https://coverage.readthedocs.io/en/latest/commands/cmd_combine.html) — arquivos paralelos, combinação, remoção de entradas antigas e remapeamento de caminhos; consultado em 2026-10-02.
