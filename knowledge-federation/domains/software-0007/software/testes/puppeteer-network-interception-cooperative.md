---
id: software.testes.tranche15.000853
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://pptr.dev/guides/network-interception", "https://pptr.dev/api/puppeteer.page"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Puppeteer: resolver interceptação de rede de forma cooperativa

## Em uma frase
Com a interceptação ativa, mais de uma callback pode opinar sobre a mesma requisição, e a resolução cooperativa decide o resultado pela prioridade informada em cada voto.

## Por que importa
No modo legado a primeira chamada decide imediatamente e as demais observam um estado já resolvido, o que produz lógica inalcançável e depuração enganosa em páginas com várias camadas de interceptação.

## Como funciona
Consulte `isInterceptResolutionHandled()` antes de agir e, quando camadas distintas participarem da decisão, declare prioridades explícitas nas chamadas de `abort`, `continue` ou `respond`.

## Exemplo
Bloquear imagens e liberar o restante pode ser escrito como `r.resourceType() === 'image' ? r.abort('blockedbyclient', 0) : r.continue({}, 0)` dentro do evento de requisição.

## Limites e trade-offs
Prioridades maiores vencem apenas entre votos cooperativos; misturar chamadas legadas com cooperativas torna a decisão final difícil de prever e de testar.

## Como verificar
Registre `interceptResolutionState()` em duas callbacks concorrentes, confirme qual ação prevaleceu e inclua uma requisição que nenhuma callback resolva.

## Conexões
- [[puppeteer-selector-syntax-beyond-css]] — Veja também: Puppeteer: usar seletores além do CSS.
- [[puppeteer-request-abort-and-continue]] — Veja também: Puppeteer: concluir toda requisição interceptada.

## Fontes
- [Puppeteer — Network interception](https://pptr.dev/guides/network-interception) — interceptação de requisições, resolução cooperativa e prioridades; consultado em 2026-10-02.
- [Puppeteer — Page API](https://pptr.dev/api/puppeteer.page) — navegação, seleção de elementos, avaliação na página e eventos; consultado em 2026-10-02.
