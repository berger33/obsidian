---
id: software.criacao_ia.tranche05.000456
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
fontes: ["https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-resume-streams", "https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# AI SDK UI: implementar retomada de stream com persistência e endpoint GET

## Em uma frase
Retomar uma geração após desconexão exige estado persistido para mensagens e stream ativo, além de rotas POST e GET coordenadas pelo chat ID.

## Por que importa
`resume` no hook não armazena por si só o stream em execução; sem referência recuperável, uma página recarregada não sabe a qual saída se reconectar.

## Como funciona
Guarde no backend a relação chat–activeStreamId e dados de stream, crie POST que persiste/produz e GET que retoma ou retorna 204 quando não há stream ativo. Ative `resume` no cliente com ID estável.

## Exemplo
Um serviço armazena eventos em Redis, persiste `activeStreamId` no registro do chat e permite que `useChat` reabra GET após refresh para continuar recebendo a resposta.

## Limites e trade-offs
O SDK oferece opções e callbacks, mas não provisiona Redis, persistência ou política de retenção automaticamente; o chat ID ainda precisa ser validado no servidor.

## Como verificar
Comece geração longa, recarregue a página, confira reconexão e depois teste ausência de stream, stream concluído e chat pertencente a outro usuário.

## Conexões
- [[ai-sdk-ui-tools-execution-and-output]] — AI SDK UI: separar execução de tools server-side e client-side com addToolOutput.
- [[ai-sdk-ui-stop-nao-cancela-geracao-retomavel]] — AI SDK UI: em streams retomáveis, distinguir stop local de cancelamento server-side.

## Fontes
- [AI SDK UI — Chatbot Resume Streams](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-resume-streams) — Especifica storage, activeStreamId e os endpoints de criação e retomada. Consulta: 2026-10-04.
- [AI SDK UI — useChat reference](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat) — Documenta opção `resume` e configuração do endpoint de reconexão no transport. Consulta: 2026-10-04.
