---
id: software.testes.tranche15.000856
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
fontes: ["https://pytest-xdist.readthedocs.io/en/stable/crash.html", "https://pytest-xdist.readthedocs.io/en/stable/distribution.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest-xdist: tratar reinício de worker como recuperação limitada

## Em uma frase
Quando um processo worker quebra, pytest-xdist pode reiniciá-lo e registrar a falha associada ao teste; `--max-worker-restart` limita essa recuperação ou a desativa com zero.

## Por que importa
Reinício ajuda a concluir a sessão após falha de processo, mas não torna confiável um teste que corrompe estado externo, trava repetidamente ou depende do conteúdo volátil do worker perdido.

## Como funciona
O limite deve servir de contenção operacional, enquanto a causa da queda continua sendo investigada.

## Exemplo
Use um valor explícito de `--max-worker-restart` no job que tenha histórico de falhas transitórias e preserve o log completo do worker para diagnóstico; num job de depuração, `--max-worker-restart=0` expõe a primeira queda sem repetição.

## Limites e trade-offs
Reexecutar processo pode ocultar um defeito intermitente se o pipeline considerar somente o resultado final; registre reinícios como sinal separado de saúde da suíte.

## Como verificar
Provoque um worker que encerra abruptamente em um teste de laboratório, observe o limite configurado e confirme que o relatório mantém visível qual caso estava ativo quando ocorreu a queda.

## Conexões
- [[pytest-xdist-coleta-deterministica-entre-workers]] — Veja também: pytest-xdist: manter a coleta idêntica em todos os workers.
- [[pytest-xdist-captura-de-saida-nao-e-stdout-direto]] — Veja também: pytest-xdist: planejar diagnósticos sem depender de -s.

## Fontes
- [pytest-xdist — When tests crash](https://pytest-xdist.readthedocs.io/en/stable/crash.html) — reinício de workers e limite de processos que podem ser reiniciados; consultado em 2026-10-02.
- [pytest-xdist — Distribution](https://pytest-xdist.readthedocs.io/en/stable/distribution.html) — algoritmos load, loadscope, loadfile, loadgroup e worksteal, identidade de workers e afinidade; consultado em 2026-10-02.
