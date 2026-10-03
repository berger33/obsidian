---
id: software.testes.tranche15.000855
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
fontes: ["https://pytest-xdist.readthedocs.io/en/stable/how-it-works.html", "https://pytest-xdist.readthedocs.io/en/stable/distribution.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# pytest-xdist: manter a coleta idêntica em todos os workers

## Em uma frase
O controlador depende de uma coleção consistente: os workers coletam os itens e seus identificadores, e a coordenação pressupõe que a lista resultante corresponda entre processos.

## Por que importa
Gerar testes a partir de relógio, ordem não determinística de set, serviços externos ou estado local pode fazer workers discordarem sobre nomes ou ordem de casos.

## Como funciona
O problema aparece antes de uma asserção falhar, porque o controlador não consegue distribuir um inventário divergente com segurança.

## Exemplo
Ordene explicitamente os dados usados para criar casos parametrizados e carregue a mesma configuração em todos os workers. Se uma fonte variável for indispensável, materialize um snapshot controlado antes de começar a coleta.

## Limites e trade-offs
Fazer a suíte determinística não garante que os testes sejam independentes durante a execução; coleta igual e isolamento de estado são contratos separados.

## Como verificar
Repita `pytest --collect-only` em ambientes limpos e compare node IDs, depois execute com múltiplos workers e confirme que não há erro de divergência de coleção.

## Conexões
- [[pytest-xdist-grupos-de-testes-com-estado-compartilhado]] — Veja também: pytest-xdist: manter testes relacionados no mesmo worker com loadgroup.
- [[pytest-xdist-limite-de-reinicios-de-worker]] — Veja também: pytest-xdist: tratar reinício de worker como recuperação limitada.

## Fontes
- [pytest-xdist — How it works](https://pytest-xdist.readthedocs.io/en/stable/how-it-works.html) — arquitetura de controlador/workers, coleta e protocolo de execução; consultado em 2026-10-02.
- [pytest-xdist — Distribution](https://pytest-xdist.readthedocs.io/en/stable/distribution.html) — algoritmos load, loadscope, loadfile, loadgroup e worksteal, identidade de workers e afinidade; consultado em 2026-10-02.
