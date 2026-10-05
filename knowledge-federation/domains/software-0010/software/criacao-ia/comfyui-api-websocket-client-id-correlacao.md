---
id: software.criacao_ia.tranche05.000413
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
fontes: ["https://docs.comfy.org/development/comfyui-server/comms_overview.md", "https://docs.comfy.org/development/comfyui-server/api-examples.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ComfyUI: abrir o WebSocket com client_id e correlacionar por prompt_id

## Em uma frase
O cliente WebSocket deve fornecer ou controlar seu `client_id` e associar eventos ao `prompt_id` da submissão correspondente.

## Por que importa
Um socket pode receber notificações de execução que não pertencem à tarefa visualizada; correlação evita misturar progresso de usuários ou trabalhos concorrentes.

## Como funciona
Conecte-se à rota WebSocket com um identificador de cliente, mantenha o prompt_id retornado pela fila e filtre notificações segundo o protocolo documentado. Registre os listeners antes da submissão quando a sequência da aplicação exigir captura desde o início.

## Exemplo
Uma aba cria um UUID para `client_id`, abre `/ws?clientId=...`, envia o workflow e só atualiza a barra de progresso quando a mensagem contém o `prompt_id` ativo.

## Limites e trade-offs
`client_id` é identificador de sessão de eventos, não mecanismo de autenticação. Não exponha o servidor local a origens não confiáveis apenas por tornar o identificador imprevisível.

## Como verificar
Execute dois prompts próximos em clientes distintos e confira que os consumidores ignoram eventos alheios; teste reconexão sem atribuir eventos antigos à nova tarefa.

## Conexões
- [[comfyui-api-prompt-validacao-e-fila]] — ComfyUI: interpretar POST prompt como validação e enfileiramento, não como resultado.
- [[comfyui-api-evento-final-e-executed]] — ComfyUI: distinguir atualização `executed` do fim e do sucesso da execução.

## Fontes
- [ComfyUI Server — Communication Overview](https://docs.comfy.org/development/comfyui-server/comms_overview.md) — Descreve a conexão WebSocket e os identificadores de cliente para comunicação do servidor. Consulta: 2026-10-04.
- [ComfyUI Server — API Examples](https://docs.comfy.org/development/comfyui-server/api-examples.md) — Mostra a sequência de submissão e acompanhamento de execuções por identificador. Consulta: 2026-10-04.
