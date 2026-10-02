---
id: software.testes.tranche15.000859
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
fontes: ["https://pptr.dev/api/puppeteer.page", "https://pptr.dev/api/puppeteer.launchoptions"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Puppeteer: isolar estado com contexto de navegador

## Em uma frase
Cada contexto de navegador mantém cookies, cache e armazenamento próprios, funcionando como um perfil isolado dentro da mesma instância de navegador.

## Por que importa
Compartilhar um único contexto entre casos faz sessão e storage vazarem de um teste para outro e cria dependência de ordem que só aparece na suíte completa.

## Como funciona
Crie um contexto por cenário e feche-o ao final, usando páginas do mesmo contexto apenas quando o compartilhamento de sessão for parte deliberada do fluxo testado.

## Exemplo
`const contexto = await browser.createBrowserContext(); const page = await contexto.newPage();` seguido de `await contexto.close()` no encerramento do caso.

## Limites e trade-offs
Contextos são mais baratos que instâncias novas, mas não isolam tudo: serviços externos, arquivos baixados e estado do servidor continuam compartilhados entre eles.

## Como verificar
Autentique-se em um contexto, confirme que o segundo permanece deslogado e que fechar o primeiro não interfere nas páginas restantes.

## Conexões
- [[puppeteer-screenshots-artifacts]] — Veja também: Puppeteer: capturar evidências com screenshot.

## Fontes
- [Puppeteer — Page API](https://pptr.dev/api/puppeteer.page) — navegação, seleção de elementos, avaliação na página e eventos; consultado em 2026-10-02.
- [Puppeteer — Launch options](https://pptr.dev/api/puppeteer.launchoptions) — opções de lançamento, headless, protocolo, produto e argumentos; consultado em 2026-10-02.
