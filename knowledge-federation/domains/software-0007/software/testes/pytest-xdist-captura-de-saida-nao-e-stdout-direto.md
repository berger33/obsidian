---
id: software.testes.tranche15.000857
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
fontes: ["https://pytest-xdist.readthedocs.io/en/stable/", "https://pytest-xdist.readthedocs.io/en/stable/how-to.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest-xdist: planejar diagnósticos sem depender de -s

## Em uma frase
A opção tradicional `-s` ou `--capture=no` não funciona com pytest-xdist, porque os testes acontecem em processos workers e a saída precisa ser controlada pelo protocolo do plugin.

## Por que importa
Um teste que parece depender de `print()` ao vivo pode ficar sem o fluxo de diagnóstico esperado quando passa de uma execução serial para a paralela.

## Como funciona
Logs por worker ou relatórios estruturados oferecem associação melhor entre mensagem, processo e caso.

## Exemplo
Configure cada worker para escrever em um arquivo que incorpore `worker_id`, ou use os mecanismos de logging e captura do pytest e recolha as saídas após a falha.

## Limites e trade-offs
Desativar captura não corrige corrida de escrita e vários workers não compartilham uma única ordem temporal de saída; não use a sequência dos logs como prova de ordem de execução.

## Como verificar
Compare o diagnóstico serial e paralelo em um teste que falha, confirme que a saída é recuperável e que nomes de arquivos impedem sobrescritas entre workers.

## Conexões
- [[pytest-xdist-limite-de-reinicios-de-worker]] — Veja também: pytest-xdist: tratar reinício de worker como recuperação limitada.
- [[pytest-xdist-ordem-global-nao-garantida]] — Veja também: pytest-xdist: remover dependência de ordem na distribuição load.

## Fontes
- [pytest-xdist — Documentation](https://pytest-xdist.readthedocs.io/en/stable/) — visão geral, execução paralela, recursos suportados e limitações de captura; consultado em 2026-10-02.
- [pytest-xdist — How-tos](https://pytest-xdist.readthedocs.io/en/stable/how-to.html) — fixtures worker_id/testrun_uid, variáveis de ambiente e coordenação de fixtures de sessão; consultado em 2026-10-02.
