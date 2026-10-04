---
id: software.testes.tranche13.000666
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
fontes: ["https://jasmine.github.io/api/7.0/global", "https://jasmine.github.io/tutorials/async"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jasmine: limitar estado compartilhado em beforeAll

## Em uma frase
`beforeAll` prepara uma vez os specs de seu grupo, enquanto `beforeEach` roda antes de cada spec.

## Por que importa
Compartilhar inicialização reduz custo, mas também pode fazer um teste passar por alterações deixadas por outro teste.

## Como funciona
Mantenha em `beforeAll` apenas recursos imutáveis ou de leitura compartilhada e recrie estado mutável em `beforeEach`; associe cleanup ao escopo que criou o recurso.

## Exemplo
Uma conexão somente-leitura pode ser aberta uma vez para uma suíte, enquanto cada exemplo constrói um carrinho novo com itens próprios.

## Limites e trade-offs
A documentação alerta que setup compartilhado facilita vazamento de estado; não use execução ordenada como correção para isolamento ausente.

## Como verificar
Execute os exemplos em ordem aleatória e confirme que nenhum altera dados que mudam o resultado de outro spec.

## Conexões
- [[jasmine-spy-call-history]] — Veja também: Jasmine: inspecionar histórico de chamadas de spy.
- [[jasmine-focused-spec-cleanup]] — Veja também: Jasmine: remover fit e fdescribe antes da CI.

## Fontes
- [Jasmine 7 — Global API](https://jasmine.github.io/api/7.0/global) — specs, suites, focus, hooks and async timeout; consultado em 2026-10-02.
- [Jasmine — Testing Async Code](https://jasmine.github.io/tutorials/async) — async/await, promises, callbacks and failure propagation; consultado em 2026-10-02.
