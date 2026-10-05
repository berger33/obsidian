---
id: software.criacao_ia.tranche05.000415
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
fontes: ["https://docs.comfy.org/development/comfyui-server/comms_routes.md", "https://docs.comfy.org/development/comfyui-server/api-examples.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# ComfyUI: recuperar o histórico da execução usando o prompt_id

## Em uma frase
Depois do acompanhamento em tempo real, `/history` permite consultar resultados persistidos para o `prompt_id` e recuperar metadados de saída.

## Por que importa
WebSocket é útil para progresso ao vivo, mas uma interface também precisa recuperar o resultado após reconexão, navegação ou atraso de processamento.

## Como funciona
Use a rota de histórico documentada com o identificador da tarefa; extraia as referências de output do registro correspondente e mantenha o status da chamada de API separado do ciclo de execução.

## Exemplo
Após o sinal terminal, um worker consulta `/history/{prompt_id}`, lê as imagens registradas na saída e persiste referências com o ID de execução para permitir reabrir o resultado.

## Limites e trade-offs
O histórico é uma consulta do servidor e não substitui autorização da aplicação. Não suponha que todo nó produza imagem ou que a resposta tenha o mesmo shape para cada workflow.

## Como verificar
Conclua um workflow com imagem e outro sem imagem; consulte o histórico de ambos, valide o prompt_id selecionado e trate registro ausente ou saída vazia de forma explícita.

## Conexões
- [[comfyui-api-evento-final-e-executed]] — ComfyUI: distinguir atualização `executed` do fim e do sucesso da execução.
- [[comfyui-api-view-parametros-de-arquivo]] — ComfyUI: recuperar arquivos de saída pela rota view e seus parâmetros.

## Fontes
- [ComfyUI Server — Routes](https://docs.comfy.org/development/comfyui-server/comms_routes.md) — Lista `/history` e sua função na consulta dos resultados de uma execução. Consulta: 2026-10-04.
- [ComfyUI Server — API Examples](https://docs.comfy.org/development/comfyui-server/api-examples.md) — Demonstra busca posterior do histórico após o acompanhamento de uma execução. Consulta: 2026-10-04.
