---
id: software.criacao_ia.tranche05.000414
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
fontes: ["https://docs.comfy.org/development/comfyui-server/comms_messages.md", "https://docs.comfy.org/development/comfyui-server/api-examples.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ComfyUI: distinguir atualização `executed` do fim e do sucesso da execução

## Em uma frase
`executed` só é enviado quando um nó retorna atualização de UI; `executing` com `node: null` marca o fim do acompanhamento, enquanto `execution_success` identifica sucesso explícito.

## Por que importa
Uma integração que trata cada atualização de UI como conclusão pode encerrar cedo, e outra que interpreta o marcador de fim como sucesso pode ocultar erro ou interrupção.

## Como funciona
Associe eventos ao `prompt_id`. Use `executing` com `node: null` como marcador de fim no padrão de acompanhamento documentado, mas só marque sucesso ao receber `execution_success`; trate `execution_error` e `execution_interrupted` separadamente. Processe `executed` como atualização opcional de saída do nó.

## Exemplo
O monitor atualiza previews quando chegam mensagens `executed`, deixa de esperar ao receber `executing` com `node: null` para o prompt ativo e só mostra estado de sucesso após `execution_success`.

## Limites e trade-offs
`executed` não é emitido por todo nó, pois depende de retorno de UI. O cliente deve lidar também com erros, interrupções e reconexões; o marcador de fim, isoladamente, não comprova saída bem-sucedida.

## Como verificar
Use workflows com nó que retorna UI e nó sem UI, além de execução com erro e interrupção; confira que o acompanhamento termina, que só o evento de sucesso marca sucesso e que eventos de outro prompt são ignorados.

## Conexões
- [[comfyui-api-websocket-client-id-correlacao]] — ComfyUI: abrir o WebSocket com client_id e correlacionar por prompt_id.
- [[comfyui-api-history-resultado-por-prompt-id]] — ComfyUI: recuperar o histórico da execução usando o prompt_id.

## Fontes
- [ComfyUI Server — Messages](https://docs.comfy.org/development/comfyui-server/comms_messages.md) — Define `executed`, `executing` com nó nulo, `execution_success`, `execution_error` e `execution_interrupted`. Consulta: 2026-10-04.
- [ComfyUI Server — API Examples](https://docs.comfy.org/development/comfyui-server/api-examples.md) — Demonstra o marcador `executing` com `node is None` para encerrar a espera e consultar `/history`. Consulta: 2026-10-04.
