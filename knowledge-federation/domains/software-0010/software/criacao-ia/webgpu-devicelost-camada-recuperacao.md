---
id: software.criacao_ia.tranche04.000302
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-04.md"
fontes: ["https://developer.mozilla.org/en-US/docs/Web/API/GPUDevice/lost", "https://www.w3.org/TR/webgpu/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WebGPU: tratar device lost como fronteira de recuperação

## Em uma frase
Todo objeto de uma WebGPU device se torna inutilizável quando ela é perdida, e device.lost é a única notificação confiável para reconstruir o estado.

## Por que importa
Drivers reiniciam, GPUs dedicadas são recuperadas pelo sistema e a própria aplicação pode destruir o dispositivo. Ignorar device.lost produz erros em cascata por todo o código que ainda referencia pipelines, buffers e bind groups mortos, com diagnóstico confuso longe da causa real.

## Como funciona
Após criar o dispositivo, aguarde a promise device.lost, que resolve com um objeto de razão ('device-lost' quando o driver falha, 'destroyed-by-application' após chamar destroy()). Marque a camada de render como suja e reconstrua a partir do registro de configuração original: o adaptador e o dispositivo novo não herdam objetos do anterior. Erros não capturados também podem culminar em perda do dispositivo, por isso a recuperação deve ser idempotente.

## Exemplo
Um jogo web guarda a lista declarativa de recursos criados (buffers, texturas, layouts) num construtor de cena. Quando device.lost resolve com 'device-lost', o jogo mostra uma pausa automática, recria adaptador e dispositivo e repassa o mesmo construtor.

## Limites e trade-offs
Não existe API para retomar o dispositivo antigo: reconstruir é a única rota. Reconstruir no mesmo frame da perda custa tempo e causa um hitch visível; amortecer com um pequeno atraso é decisão da aplicação. O comportamento em caso de falha do navegador varia por plataforma.

## Como verificar
Chame device.destroy() e confirme que await device.lost resolve com a razão esperada. Simule falha de driver quando o sistema permitir e observe se a aplicação recria os recursos sem travar. Verifique que chamadas póstumas aos objetos antigos geram erro claro e são interceptadas pela sua camada.

## Conexões
- [[webgpu-requestadapter-por-criterios]] — WebGPU: filtrar adaptador por potência e modo de compatibilidade.
- [[webgpu-requiredlimits-calcular-custo]] — WebGPU: pedir limites maiores e calcular antes do limite suportado.

## Fontes
- [MDN — GPUDevice: lost](https://developer.mozilla.org/en-US/docs/Web/API/GPUDevice/lost) — descreve a promise e as razões de perda do dispositivo Consulta: 2026-10-04.
- [W3C — WebGPU (especificação)](https://www.w3.org/TR/webgpu/) — define a semântica de perda de dispositivo e invalidação de objetos dependentes Consulta: 2026-10-04.
