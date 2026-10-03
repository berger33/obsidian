---
id: software.testes.tranche15.000887
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
fontes: ["https://pestphp.com/docs/browser-testing", "https://pestphp.com/docs/continuous-integration"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Pest 5: reservar browser tests para fluxos que exigem navegador real

## Em uma frase
O plugin de browser permite visitar páginas e interagir com elementos por texto, seletor CSS ou atributo de teste, cobrindo comportamento que um teste de controller não observa.

## Por que importa
O exemplo do Pest combina navegação, formulários, assertions do navegador e integrações da aplicação, enquanto a instalação requer o plugin de browser e Playwright.

## Como funciona
Esse teste mede a experiência integrada; não precisa substituir testes unitários rápidos para cada regra simples.

## Exemplo
Instale `pestphp/pest-plugin-browser`, instale Playwright e abra a rota com `visit('/')`; preencha formulário, clique no botão e valide o conteúdo final que o usuário vê.

## Limites e trade-offs
O browser e seus binários elevam custo de setup e podem tornar a execução mais lenta; screenshots e traces gerados precisam ficar fora do versionamento salvo quando forem artefatos intencionais.

## Como verificar
Execute o fluxo em modo headless no CI e abra os artefatos de diagnóstico de uma falha, confirmando que o navegador, servidor e dados de teste foram inicializados corretamente.

## Conexões
- [[pest-tia-elegibilidade-e-cobertura-dos-casos-reproduzidos]] — Veja também: Pest 5: interpretar a cobertura preservada por Tia como trilha reproduzível.
- [[pest-browser-espera-timeout-e-flakiness]] — Veja também: Pest 5: calibrar o timeout e entender o auto-wait do Playwright.

## Fontes
- [Pest 5 — Browser Testing](https://pestphp.com/docs/browser-testing) — Playwright, navegação, seletores, browsers, timeout e diagnóstico; consultado em 2026-10-02.
- [Pest 5 — Continuous Integration](https://pestphp.com/docs/continuous-integration) — execução integral em CI, browser plugin, parallel e artifacts; consultado em 2026-10-02.
