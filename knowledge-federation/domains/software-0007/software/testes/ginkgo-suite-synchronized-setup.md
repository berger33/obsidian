---
id: software.testes.tranche13.000702
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
fontes: ["https://onsi.github.io/ginkgo/#spec-parallelization", "https://onsi.github.io/ginkgo/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Ginkgo: sincronizar recurso compartilhado na suite paralela

## Em uma frase
Suite-level setup e teardown têm nós próprios; em execução paralela, recurso compartilhado exige coordenação entre processos.

## Por que importa
Criar um banco de teste por processo ou coordenar preparo uma vez evita que workers iniciem migrações concorrentes sobre o mesmo serviço.

## Como funciona
Use `SynchronizedBeforeSuite` e o par de callbacks correspondente quando a inicialização precisa produzir estado global e distribuir dados para nós; encerre o serviço na finalização coordenada.

## Exemplo
Um job inicia container uma única vez e entrega endereço às partições, enquanto cada spec usa nome de registro próprio.

## Limites e trade-offs
Setup sincronizado amplia escopo do estado e cleanup precisa funcionar mesmo quando uma partição falha; não coloque cenário individual nessa fixture.

## Como verificar
Rode com dois processos, registre quem inicia o serviço e quem recebe configuração e confirme limpeza da infraestrutura após a suite.

## Conexões
- [[ginkgo-before-after-nesting]] — Veja também: Ginkgo: ordenar setup e cleanup em containers aninhados.
- [[ginkgo-process-parallel-isolation]] — Veja também: Ginkgo: isolar recursos ao executar specs com -p.

## Fontes
- [Ginkgo v2 — Spec Parallelization](https://onsi.github.io/ginkgo/#spec-parallelization) — parallel workers and suite-level synchronization; consultado em 2026-10-02.
- [Ginkgo v2 — Documentation](https://onsi.github.io/ginkgo/) — spec construction, setup, filtering and execution; consultado em 2026-10-02.
