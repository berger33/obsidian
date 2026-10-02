---
id: software.testes.tranche08.000154
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

# Playwright: mocks de API alinhados ao contrato

## Em uma frase
Mocke somente a fronteira que o teste precisa controlar e mantenha a resposta coerente com o contrato consumido pela interface.

## Por que importa
Mocks determinísticos ajudam a cobrir erro, latência e dados raros, mas respostas inventadas podem validar um cliente incompatível com o serviço real.

## Como funciona
Intercepte rota específica, filtre método e caminho, valide a requisição relevante e retorne payload representativo. Combine cenários simulados com testes separados que exercitem a API real.

## Exemplo
Para verificar estado vazio, o teste intercepta apenas GET /items e responde com lista vazia; uma assertion confirma a mensagem acessível, não detalhes do componente.

## Limites e trade-offs
Um mock não verifica autenticação real, serialização do servidor ou consistência do contrato publicado. Atualize fixtures quando o schema mudar.

## Como verificar
Compare payload do mock com schema ou exemplo versionado; execute um teste de integração sem interceptação e confirme que status, campos e erros são compatíveis.

## Conexões
- [[playwright-har-replay-cobertura-rede]] — Veja também: Playwright: replay de HAR para cenários de rede.
- [[playwright-status-http-vs-falha-transporte]] — Veja também: Playwright: distinguir erro HTTP de falha de transporte.

## Fontes
- [Playwright — Mock APIs](https://playwright.dev/docs/mock) — mock, resposta modificada e replay de HAR; consultado em 2026-10-02.
- [Playwright — Network](https://playwright.dev/docs/network) — interceptação, observação e alteração controlada de tráfego; consultado em 2026-10-02.
