---
id: software.testes.tranche13.000704
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-13.md"
fontes: ["https://onsi.github.io/ginkgo/#spec-randomization", "https://onsi.github.io/ginkgo/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Ginkgo: reproduzir falha de ordem com seed

## Em uma frase
Randomização muda ordem de execução dos specs e seed permite repetir a sequência que revelou dependência entre casos.

## Por que importa
Dependência de ordem é uma fonte de flakiness que um run sempre ordenado pode esconder por muito tempo.

## Como funciona
Habilite randomização no runner ou CLI, registre o seed em log de CI e reproduza localmente antes de alterar setup compartilhado.

## Exemplo
Uma suite intermitente passa com um seed e falha com outro; o seed reportado transforma a ordem problemática em investigação repetível.

## Limites e trade-offs
Repetir seed reproduz ordem, mas não garante reproduzir scheduling de goroutines, latência ou estado de serviço remoto.

## Como verificar
Rode mais de um seed em janela controlada e, ao encontrar falha, registre também ambiente e logs das fixtures.

## Conexões
- [[ginkgo-process-parallel-isolation]] — Veja também: Ginkgo: isolar recursos ao executar specs com -p.
- [[ginkgo-label-filter]] — Veja também: Ginkgo: selecionar specs por labels declarados.

## Fontes
- [Ginkgo v2 — Spec Randomization](https://onsi.github.io/ginkgo/#spec-randomization) — randomized order and seed-based reproduction; consultado em 2026-10-02.
- [Ginkgo v2 — Documentation](https://onsi.github.io/ginkgo/) — spec construction, setup, filtering and execution; consultado em 2026-10-02.
