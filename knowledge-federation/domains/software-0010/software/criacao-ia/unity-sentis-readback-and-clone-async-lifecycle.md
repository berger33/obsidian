---
id: software.criacao_ia.tranche05.000439
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/read-output-async.html", "https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/manage-memory.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Sentis 2.5: usar ReadbackAndCloneAsync com sincronização e descarte explícitos

## Em uma frase
`ReadbackAndCloneAsync` fornece uma cópia de CPU sem bloquear a chamada enquanto o readback termina, e a cópia retornada deve ser descartada.

## Por que importa
A interface consegue processar resultado apenas quando disponível sem transformar uma consulta ao tensor GPU em espera síncrona no frame atual.

## Como funciona
Agende o modelo, obtenha a saída com `PeekOutput`, aguarde `ReadbackAndCloneAsync` e só leia os valores da cópia quando a operação completar. Gerencie cancelamento e ciclo de vida do componente ao redor da tarefa.

## Exemplo
Um detector executa o worker, aguarda o clone assíncrono em um método de Unity e chama `Dispose` na cópia após mapear índices para rótulos.

## Limites e trade-offs
O tensor retornado é uma cópia de CPU e usa memória própria; reagendar o worker enquanto ainda se depende da saída emprestada exige controlar a ordem das operações.

## Como verificar
Simule componente desativado durante a espera, teste uma saída normal e confirme que o clone só é lido após a conclusão e sempre é liberado.

## Conexões
- [[unity-sentis-evitar-readback-sincrono-na-main-thread]] — Unity Sentis 2.5: evitar leitura síncrona que bloqueia a main thread.
- [[unity-sentis-schedule-iterable-frames]] — Unity Sentis 2.5: distribuir camadas de inferência entre frames com ScheduleIterable.

## Fontes
- [Unity Sentis 2.5 — Read output asynchronously](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/read-output-async.html) — Apresenta `ReadbackAndCloneAsync` como caminho awaitable não bloqueante e descarta o clone. Consulta: 2026-10-04.
- [Unity Sentis 2.5 — Manage memory](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/manage-memory.html) — Requer liberar o tensor clonado de readback para soltar recursos. Consulta: 2026-10-04.
