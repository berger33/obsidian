---
id: software.testes.tranche13.000667
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
fontes: ["https://jasmine.github.io/api/7.0/global", "https://jasmine.github.io/api/7.0/Configuration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Jasmine: remover fit e fdescribe antes da CI

## Em uma frase
`fit` e `fdescribe` focam uma spec ou suite e fazem com que apenas testes focados sejam executados.

## Por que importa
Foco é útil durante investigação, mas um modificador esquecido pode deixar o pipeline verde sem executar regressões vizinhas.

## Como funciona
Use a forma focada somente temporariamente, mantenha um comando de CI que execute a suíte completa e procure `fit`/`fdescribe` no diff antes do commit.

## Exemplo
Enquanto ajusta uma assertion, `fit` pode executar um único caso; depois de corrigido, restaure `it` para recuperar a execução integral.

## Limites e trade-offs
O modo focado não valida specs excluídos nem representa um relatório completo; não o confunda com filtro planejado de um job dedicado.

## Como verificar
Adicione deliberadamente um spec focado e confirme que o comando local sinaliza a redução; a verificação de CI deve revelar a configuração que o mantém.

## Conexões
- [[jasmine-beforeall-state-boundary]] — Veja também: Jasmine: limitar estado compartilhado em beforeAll.
- [[jasmine-pending-spec-intent]] — Veja também: Jasmine: registrar pending sem confundir com cobertura.

## Fontes
- [Jasmine 7 — Global API](https://jasmine.github.io/api/7.0/global) — specs, suites, focus, hooks and async timeout; consultado em 2026-10-02.
- [Jasmine 7 — Configuration](https://jasmine.github.io/api/7.0/Configuration) — random execution, spec discovery and environment configuration; consultado em 2026-10-02.
