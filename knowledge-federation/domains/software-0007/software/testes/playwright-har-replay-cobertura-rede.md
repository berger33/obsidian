---
id: software.testes.tranche08.000155
tipo: tecnica
dominio: software
subdominio: testes
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://playwright.dev/docs/mock", "https://playwright.dev/docs/network"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Playwright: replay de HAR para cenários de rede

## Em uma frase
Use HAR replay para reproduzir tráfego conhecido e confira se o arquivo cobre as requisições que o cenário realmente emite.

## Por que importa
Uma captura versionada facilita reproduzir sequências de rede, mas entradas incompletas podem deixar tráfego escapar para serviços externos ou produzir falso sucesso.

## Como funciona
Registre o fluxo representativo, reduza dados sensíveis, limite correspondência por URL/método e trate explicitamente requisições sem entrada. Mantenha o HAR revisável junto da mudança de contrato.

## Exemplo
Um teste de página de catálogo replaya respostas de pesquisa e detalhes, enquanto uma busca não gravada falha de forma visível em vez de atingir a internet.

## Limites e trade-offs
HAR reproduz respostas capturadas; não simula todos os estados temporais, autorização, concorrência ou comportamento de um serviço mutável.

## Como verificar
Execute sem conectividade externa, confirme que todas as rotas esperadas foram atendidas e revise o artefato para tokens, cookies e dados pessoais antes do commit.

## Conexões
- [[playwright-mock-api-contrato-resposta]] — Veja também: Playwright: mocks de API alinhados ao contrato.
- [[playwright-status-http-vs-falha-transporte]] — Veja também: Playwright: distinguir erro HTTP de falha de transporte.

## Fontes
- [Playwright — Mock APIs](https://playwright.dev/docs/mock) — mock, resposta modificada e replay de HAR; consultado em 2026-10-02.
- [Playwright — Network](https://playwright.dev/docs/network) — interceptação, observação e alteração controlada de tráfego; consultado em 2026-10-02.
