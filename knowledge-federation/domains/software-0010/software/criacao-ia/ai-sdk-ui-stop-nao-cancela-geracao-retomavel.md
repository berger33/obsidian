---
id: software.criacao_ia.tranche05.000457
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

# AI SDK UI: em streams retomáveis, distinguir stop local de cancelamento server-side

## Em uma frase
Em uma configuração retomável, `stop()` fecha a conexão do cliente e não cancela automaticamente o trabalho de geração no servidor.

## Por que importa
Reutilizar o botão local como se fosse cancelamento pode deixar modelo, job ou writer consumindo recursos e ainda permitir reconexão ao stream ativo.

## Como funciona
Implemente endpoint explícito de stop que persiste resposta parcial, cancela o produtor e remove o registro de stream ativo com proteção contra corrida; depois chame `chat.stop()` para parar a leitura local.

## Exemplo
Ao pressionar Stop, o cliente envia o chat e activeStreamId ao endpoint de cancelamento, recebe confirmação do servidor e encerra também a conexão local.

## Limites e trade-offs
Navegar, fechar aba e refresh são desconexões, não intenção de cancelamento. O servidor precisa evitar que requisição de stop antiga encerre uma geração mais nova.

## Como verificar
Teste separadamente refresh e botão stop; depois da desconexão, confirme que o stream pode ser retomado, e depois da ação explícita confirme que o produtor parou.

## Conexões
- [[ai-sdk-ui-retomar-streams-com-storage]] — AI SDK UI: implementar retomada de stream com persistência e endpoint GET.
- [[ai-sdk-ui-data-parts-persistentes-transient]] — AI SDK UI: separar data parts persistentes de eventos transient de interface.

## Fontes
- [AI SDK UI — Chatbot Resume Streams](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot-resume-streams) — Afirma que stop em configuração retomável é desconexão e propõe endpoint dedicado de cancelamento. Consulta: 2026-10-04.
- [AI SDK UI — useChat reference](https://ai-sdk.dev/docs/reference/ai-sdk-ui/use-chat) — Define `stop` como interrupção da requisição de streaming no cliente. Consulta: 2026-10-04.
