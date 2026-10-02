---
id: software.testes.tranche13.000703
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
fontes: ["https://onsi.github.io/ginkgo/#spec-parallelization", "https://pkg.go.dev/github.com/onsi/ginkgo/v2"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Ginkgo: isolar recursos ao executar specs com -p

## Em uma frase
CLI `ginkgo -p` executa specs usando processos paralelos e acelera suites que não compartilham recurso mutável.

## Por que importa
Paralelismo por processo muda fronteiras de memória e pode expor colisões em bancos, diretórios temporários e portas.

## Como funciona
Escolha número de nós compatível com infraestrutura, identifique recursos por spec ou worker e sincronize apenas a inicialização realmente comum.

## Exemplo
Cada partição pode criar seu próprio schema ou prefixo para que duas specs de integração escrevam sem sobrescrever fixture uma da outra.

## Limites e trade-offs
Um spec serializado não cobre race em código compartilhado de produção; reservar processos não garante isolamento de serviço externo automaticamente.

## Como verificar
Execute a mesma suite serial e paralela com isolamento de recurso ativo e compare falhas, tempo e limpeza final.

## Conexões
- [[ginkgo-suite-synchronized-setup]] — Veja também: Ginkgo: sincronizar recurso compartilhado na suite paralela.
- [[ginkgo-random-order-seed]] — Veja também: Ginkgo: reproduzir falha de ordem com seed.

## Fontes
- [Ginkgo v2 — Spec Parallelization](https://onsi.github.io/ginkgo/#spec-parallelization) — parallel workers and suite-level synchronization; consultado em 2026-10-02.
- [Ginkgo v2 — API Reference](https://pkg.go.dev/github.com/onsi/ginkgo/v2) — spec nodes, decorators and reports; consultado em 2026-10-02.
