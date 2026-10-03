---
id: software.testes.tranche15.000920
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
fontes: ["https://mswjs.io/guides/integrations/node", "https://mswjs.io/api/setup-server/listen"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# MSW em Node.js: entender o que setupServer realmente intercepta

## Em uma frase
Apesar do nome, `setupServer` não inicia um socket HTTP de aplicação; em Node, o MSW intercepta requests feitos por APIs compatíveis no processo.

## Por que importa
Essa camada permite reutilizar handlers sem alterar o código do cliente para apontar a um mock específico, mantendo a chamada de rede na fronteira habitual.

## Como funciona
O adapter Node é importado de `msw/node`, enquanto handlers são definidos pela API compartilhada do pacote.

## Exemplo
Crie `setupServer(...handlers)` num módulo de teste e inicie a interceptação no hook global do runner, deixando o cliente chamar a URL normal do endpoint.

## Limites e trade-offs
Um request emitido por outra ferramenta, processo ou API não interceptada pode escapar; configure comportamento explícito para solicitações sem handler e controle tráfego externo no ambiente.

## Como verificar
Faça um teste com request compatível e outro processo filho de propósito, observando quais são interceptados e confirmando que nenhum servidor externo foi aberto pelo setupServer.

## Conexões
- [[msw-listen-onunhandledframe-com-politica-explicita]] — Veja também: MSW: falhar ou avisar para frames de rede sem handler.

## Fontes
- [MSW — Node.js integration](https://mswjs.io/guides/integrations/node) — setupServer e ciclo listen/reset/close em testes; consultado em 2026-10-02.
- [MSW — listen()](https://mswjs.io/api/setup-server/listen) — início da interceptação e estratégias para frames sem handler; consultado em 2026-10-02.
