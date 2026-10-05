---
id: software.criacao_ia.tranche05.000437
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/get-the-output.html", "https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/manage-memory.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Sentis 2.5: escolher entre PeekOutput emprestado e CopyOutput próprio

## Em uma frase
`PeekOutput` devolve uma referência cujo armazenamento pertence ao worker, enquanto `CopyOutput` cria ou preenche um tensor cuja vida útil a aplicação administra.

## Por que importa
Usar a referência emprestada depois de outra inferência pode expor conteúdo sobrescrito; não descartar uma cópia própria pode manter memória ocupada.

## Como funciona
Leia `PeekOutput` antes de agendar novamente se só precisa do resultado corrente. Use `CopyOutput` quando precisa de uma cópia independente, respeite sua capacidade e chame `Dispose` no tensor gerenciado pela aplicação.

## Exemplo
A UI copia uma classificação que precisa permanecer disponível após o próximo `Schedule`; um consumidor transitório lê `PeekOutput` e termina antes de o worker reutilizar a memória.

## Limites e trade-offs
A referência de `PeekOutput` não deve ser descartada pela aplicação e será liberada com o worker; a cópia não é atualizada automaticamente ao executar o worker de novo.

## Como verificar
Agende duas entradas diferentes, compare a referência emprestada e a cópia após cada execução, e valide que o tensor de cópia é descartado no encerramento do componente.

## Conexões
- [[unity-sentis-compatibilidade-operadores-backend]] — Unity Sentis 2.5: validar operadores e tipos antes de fixar backend.
- [[unity-sentis-evitar-readback-sincrono-na-main-thread]] — Unity Sentis 2.5: evitar leitura síncrona que bloqueia a main thread.

## Fontes
- [Unity Sentis 2.5 — Get output from a model](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/get-the-output.html) — Define propriedade, reutilização e atualização de PeekOutput versus CopyOutput. Consulta: 2026-10-04.
- [Unity Sentis 2.5 — Manage memory](https://docs.unity3d.com/Packages/com.unity.ai.inference@2.5/manual/manage-memory.html) — Exige Dispose em workers e tensores instanciados pela aplicação. Consulta: 2026-10-04.
