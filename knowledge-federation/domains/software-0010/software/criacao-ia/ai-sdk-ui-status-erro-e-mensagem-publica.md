---
id: software.criacao_ia.tranche05.000460
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: avancado
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-05.md"
fontes: ["https://ai-sdk.dev/docs/ai-sdk-ui/chatbot", "https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# AI SDK UI: conduzir controles por status e mostrar erro genérico ao usuário

## Em uma frase
O `status` separa envio, streaming, pronto e erro, enquanto a interface pública deve evitar revelar detalhes internos da falha do servidor.

## Por que importa
Estados distintos ajudam a bloquear duplicidade e oferecer retry, e mensagens de erro genéricas reduzem vazamento de informação operacional.

## Como funciona
Use `submitted` e `streaming` para spinner ou botão de parada, `ready` para aceitar novo envio e `error` para estado recuperável; mantenha detalhes técnicos em logs protegidos e permita `regenerate` quando apropriado.

## Exemplo
Uma tela mostra spinner antes do primeiro chunk, desabilita enviar durante streaming, oferece tentar novamente após falha e apresenta “Algo deu errado” ao usuário.

## Limites e trade-offs
A mensagem genérica não substitui telemetria nem tratamento de causas específicas; diferencie abort, disconnect e erro de execução no servidor quando a aplicação precisar persistir estado.

## Como verificar
Simule resposta lenta, sucesso, falha HTTP e erro durante stream; confirme estados visuais, retry e ausência de stack trace ou segredo no texto exibido.

## Conexões
- [[ai-sdk-ui-escolher-text-stream-ou-data-stream]] — AI SDK UI: escolher text stream ou data stream conforme a forma do evento.

## Fontes
- [AI SDK UI — Chatbot](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot) — Define estados submetido, streaming, ready e error, com controles e erro genérico. Consulta: 2026-10-04.
- [AI SDK UI — useChat reference](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat) — Lista status, error, regenerate e metadados de conclusão e desconexão. Consulta: 2026-10-04.
