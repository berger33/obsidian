---
id: software.criacao_ia.tranche04.000335
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
fontes: ["https://github.com/Unity-Technologies/EntityComponentSystemSamples/blob/master/EntitiesSamples/Docs/jobs.md", "https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/programming-entities.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Jobs: em IJobParallelFor você escreve no seu índice e lê fora com intenção declarada

## Em uma frase
A doc de jobs do repositório ECS Samples é um exemplo vivo da regra: 'Nums[0]' dentro de um Execute(int index) dispara exceção de safety, mesmo sendo leitura — acesso fora do índice próprio precisa de atributo.

## Por que importa
IJobParallelFor distribui índices entre threads; o safety system protege o modelo assumindo que cada invocação toca apenas seu fatiamento. Leituras de um elemento compartilhado (o 'scaler' global no array) são seguras em essência, mas o runtime não sabe — e o contrato fica explícito justamente para forçar você a dizer que sabe.

## Como funciona
Caminhos oficiais pelo mesmo documento: ler via um container separado marcado [ReadOnly] (a exceção de mão única da main thread aplica análogo), copiar o valor para o struct do job antes do schedule (quando é escalar, é a solução mais limpa), ou dividir o acesso com [NativeDisableParallelForRestriction] quando você gerencia os índices escritos (strided/overlap seu, não do scheduler). Parâmetro 'batch' de Schedule(chunksize) ajusta o grão da fenda — não a regra de acesso.

## Exemplo
Um job de física lê 'dt' de um array de config no index 0: a versão correta é um campo float copiado do array antes do Schedule, não um 'config[0]' dentro do Execute — sem atributo e sem corrida possível.

## Limites e trade-offs
Fatiamento manual (paralelo com writes multi-índice) reabilita a corrida se os índices se sobrepõem — o atributo não adiciona segurança, remove o detector. 'batch size' não conserta regra de acesso, só amortiza overhead de dispatch. E o comportamento sem as checagens (build) é o mesmo código com a mesma corrida: o crash é que muda de exceção para corrupção.

## Como verificar
Rode o exemplo da doc (Nums[0] em paralelo) e confirme a exceção apontando o índice fora do próprio. Refatore para campo escalado e confirme o verde — o teste é a lição. Um unit test que roda o job com checagens ativas e valida resultado é barato e pega regressões de refactor.

## Conexões
- [[unity-safety-system-corrida-exception]] — Unity Jobs: o safety system é a sua revisão de concorrência em tempo de execução.
- [[unity-chunks-arquetipos-leitura-lote]] — Unity Entities: iterar por chunk é o grão de leitura da arquitetura.

## Fontes
- [Unity ECS Samples — jobs.md](https://github.com/Unity-Technologies/EntityComponentSystemSamples/blob/master/EntitiesSamples/Docs/jobs.md) — o caso Nums[0] e as opções [ReadOnly]/disable/stride estão documentados neste arquivo Consulta: 2026-10-04.
- [Unity Entities @1.4 — Programming in Entities](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/programming-entities.html) — panorama oficial de jobs e contêineres na stack Entities Consulta: 2026-10-04.
