---
id: software.criacao_ia.tranche05.000418
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

# ComfyUI: separar controle da fila de interrupção da execução ativa

## Em uma frase
A API oferece operações distintas para consultar ou alterar a fila e para interromper a execução corrente; a interface deve escolher a ação conforme o estado.

## Por que importa
Remover trabalhos pendentes e interromper um workflow já em andamento têm efeitos diferentes sobre o usuário e não devem compartilhar um botão ambíguo.

## Como funciona
Consulte `/queue` para observar o estado da fila e use a rota de interrupção documentada para sinalizar o cancelamento da tarefa em execução. Mantenha o prompt_id ativo no cliente para reconciliar a resposta com a notificação final.

## Exemplo
O painel oferece “Remover pendentes” para limpar tarefas ainda enfileiradas e um botão “Interromper execução atual” separado, com confirmação quando há trabalho ativo.

## Limites e trade-offs
Uma interrupção não equivale a desfazer efeitos já persistidos nem a garantir que todo recurso de um nó customizado foi revertido; estados terminais devem ser conferidos após a ação.

## Como verificar
Crie uma fila com duas tarefas, remova apenas pendentes e depois interrompa uma execução de teste; verifique qual prompt deixou a fila e qual evento final foi emitido.

## Conexões
- [[comfyui-api-object-info-nos-instalados]] — ComfyUI: consultar object_info para descobrir o esquema dos nós disponíveis.
- [[comfyui-api-upload-image-referencia]] — ComfyUI: usar a referência devolvida por upload/image em vez de caminho local.

## Fontes
- [ComfyUI Server — Routes](https://docs.comfy.org/development/comfyui-server/comms_routes.md) — Separa endpoints de estado/controle da fila e o endpoint de interrupção de execução. Consulta: 2026-10-04.
- [ComfyUI Server — Messages](https://docs.comfy.org/development/comfyui-server/comms_messages.md) — Documenta eventos de execução que ajudam a atualizar o estado após interrupção. Consulta: 2026-10-04.
