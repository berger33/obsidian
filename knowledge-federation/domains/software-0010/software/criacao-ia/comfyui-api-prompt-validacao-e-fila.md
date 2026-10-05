---
id: software.criacao_ia.tranche05.000412
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
fontes: ["https://docs.comfy.org/development/comfyui-server/comms_routes.md", "https://docs.comfy.org/development/comfyui-server/comms_messages.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ComfyUI: interpretar POST prompt como validação e enfileiramento, não como resultado

## Em uma frase
`POST /prompt` valida e enfileira um workflow; sua resposta informa o identificador da execução ou os erros de validação, não a imagem final.

## Por que importa
Uma integração que trata aceitação do payload como conclusão pode exibir sucesso antes de qualquer nó terminar ou esconder erros de dependência.

## Como funciona
Envie o prompt no formato API e leia `prompt_id` e `number` quando aceito; em falha, examine `error` e `node_errors`. Guarde o identificador para correlacionar as notificações e recuperar o histórico.

## Exemplo
Um serviço cria uma tarefa interna apenas depois de receber `prompt_id`, expõe estado `queued` e passa o mesmo identificador aos leitores de WebSocket e history.

## Limites e trade-offs
A validação de entrada não garante que a execução termine; erros de runtime, interrupções e disponibilidade de modelos precisam de estados separados na aplicação.

## Como verificar
Teste um workflow válido e um payload com nó inválido; confirme as chaves de retorno de cada caso e que nenhum resultado é marcado como pronto somente por receber `prompt_id`.

## Conexões
- [[comfyui-api-exportar-workflow-formato-api]] — ComfyUI: exportar o grafo no formato API em vez de reutilizar o arquivo visual.
- [[comfyui-api-websocket-client-id-correlacao]] — ComfyUI: abrir o WebSocket com client_id e correlacionar por prompt_id.

## Fontes
- [ComfyUI Server — Routes](https://docs.comfy.org/development/comfyui-server/comms_routes.md) — Especifica `POST /prompt`, validação, enfileiramento e respostas de sucesso ou erro. Consulta: 2026-10-04.
- [ComfyUI Server — Messages](https://docs.comfy.org/development/comfyui-server/comms_messages.md) — Descreve eventos de execução associados ao `prompt_id` enfileirado. Consulta: 2026-10-04.
