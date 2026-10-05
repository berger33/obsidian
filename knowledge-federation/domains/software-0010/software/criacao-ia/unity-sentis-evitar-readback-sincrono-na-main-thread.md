---
id: software.criacao_ia.tranche05.000438
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/read-output-async.html", "https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/get-the-output.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Sentis 2.5: evitar leitura síncrona que bloqueia a main thread

## Em uma frase
Ler dados de saída que ainda estão sendo calculados ou residem na GPU pode bloquear a thread principal enquanto ocorre sincronização ou readback.

## Por que importa
A pausa aparece como hitch de frame, mesmo quando o agendamento da rede foi encaminhado de forma assíncrona pelo backend.

## Como funciona
Mantenha saída na GPU quando possível e use `ReadbackAndCloneAsync` ou solicitação de readback com polling ao transferir dados para CPU; descarte o tensor clonado depois do uso.

## Exemplo
Um HUD solicita cópia assíncrona do tensor após inferência, atualiza o placar ao completar e mantém o frame loop livre enquanto o readback está pendente.

## Limites e trade-offs
O readback assíncrono não torna instantânea a inferência nem elimina custo de cópia; sequências de agendamento e leitura precisam respeitar a vida útil do tensor.

## Como verificar
Meça frame time com saída lida sincronamente e com readback assíncrono em dispositivo real; confira que a resposta chega antes de ser exibida e que clones são descartados.

## Conexões
- [[unity-sentis-peekoutput-copyoutput-propriedade]] — Unity Sentis 2.5: escolher entre PeekOutput emprestado e CopyOutput próprio.
- [[unity-sentis-readback-and-clone-async-lifecycle]] — Unity Sentis 2.5: usar ReadbackAndCloneAsync com sincronização e descarte explícitos.

## Fontes
- [Unity Sentis 2.5 — Read output asynchronously](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/read-output-async.html) — Explica as causas do bloqueio e mostra métodos de readback assíncrono. Consulta: 2026-10-04.
- [Unity Sentis 2.5 — Get output from a model](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/get-the-output.html) — Alerta para espera bloqueante ao transferir saída do backend para CPU. Consulta: 2026-10-04.
