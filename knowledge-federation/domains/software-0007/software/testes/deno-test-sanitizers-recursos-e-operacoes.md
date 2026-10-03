---
id: software.testes.tranche15.000893
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
fontes: ["https://docs.deno.com/runtime/test/sanitizers/", "https://docs.deno.com/runtime/test/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Deno test: reativar sanitizers para detectar recursos e operações vazados

## Em uma frase
Os sanitizers podem apontar operações assíncronas pendentes e recursos não fechados, problemas que assertions de valor não capturam; em Deno 2.8, op e resource sanitizers são opt-in por padrão segundo a documentação atual.

## Por que importa
O sanitizer de saída continua com default próprio, e os demais podem ser configurados por teste, módulo, CLI, ambiente ou deno.json com precedência.

## Como funciona
Uma suíte migrada de versão precisa confirmar os defaults reais em vez de assumir que toda detecção está ativa.

## Exemplo
Configure `sanitizeOps: true` e `sanitizeResources: true` para testes de concorrência ou I/O e use as opções no escopo adequado quando a suíte exigir esses diagnósticos de forma sistemática.

## Limites e trade-offs
Desabilitar sanitizers para silenciar falha pode esconder handles abertos que contaminam casos seguintes; se um caso específico for exceção, registre a razão e restaure o comportamento mais estrito nos demais.

## Como verificar
Abra uma conexão ou timer sem fechar num teste de laboratório, confirme que o sanitizer ativo relata o vazamento e verifique a configuração efetiva depois de uma atualização do Deno.

## Conexões
- [[deno-test-steps-com-subcasos-hierarquicos]] — Veja também: Deno test: usar steps para estruturar uma operação com fases.
- [[deno-test-timeout-cobre-loop-sincrono-e-promise]] — Veja também: Deno test: colocar deadline em testes que podem pendurar.

## Fontes
- [Deno Runtime — Test sanitizers](https://docs.deno.com/runtime/test/sanitizers/) — sanitizers de ops, resources e exit com níveis de precedência; consultado em 2026-10-02.
- [Deno Runtime — Testing](https://docs.deno.com/runtime/test/) — steps, timeouts, affected tests, permissões, snapshots, sanitizers e reporters; consultado em 2026-10-02.
