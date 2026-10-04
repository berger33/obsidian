---
id: software.criacao_ia.tranche04.000334
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.entities@1.0/manual/concepts-safety.html", "https://github.com/Unity-Technologies/EntityComponentSystemSamples/blob/master/EntitiesSamples/Docs/jobs.md"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Jobs: o safety system é a sua revisão de concorrência em tempo de execução

## Em uma frase
Com as checagens ativas, Schedule() lança exceção ao detectar corrida potencial entre jobs sobre os mesmos dados — o que a maioria dos runtimes de paralelismo deixa para o azar.

## Por que importa
O ecossistema Burst/jobs opera em memória nativa com unsafe; a documentação oficial das amostras de ECS é explícita ao dizer que duas jobs sobre a mesma NativeArray sem dependência declarada são exatamente a condição de corrida. O safety system transforma essa classe de bug em exceção determinística — desativá-lo 'para performance' desliga o detector, não a corrida.

## Como funciona
O mecanismo marca cada NativeArray em uso por job com seu tipo de acesso (ReadOnly/Write); um segundo acesso concorrente conflituante lança exceção ao schedulear. Leituras concorrentes são permitidas. Exceções ao controle vêm de atributos: [ReadOnly] declara intenção, [NativeDisableParallelForRestriction] libera acesso multi-índicio, [NativeDisableContainerSafetyRestriction] desliga as checagens do container para o caso em que você provou segurança manual (documentado, mas 'certifique-se de que não está criando corrida'). O Editor e o runtime têm políticas distintas: no build, o runtime não garante o throw — garante, isso sim, crash/corrupção.

## Exemplo
Dois jobs que escrevem na mesma NativeArray (o exemplo canônico da doc de jobs) disparam exceção na chamada Schedule, apontando o par conflito. O refactor declarado pela própria doc: encadear dependência, fatiar por sub-intervalo, ou declarar o motivo do disable.

## Limites e trade-offs
Desabilitar checagens é poder com preço: o manual de segurança do Entities adverte que em builds não há garantias de erro limpo fora do Editor. Main thread lendo um container em uso por job é exceção também — o caminho de mão única é [ReadOnly] no job. E o safety cobre containers e jobs; não substitui análise de aliasing de ponteiros crus (unsafe/native) — as ferramentas são complementares.

## Como verificar
Reproduza o par de jobs conflitante num teste e observe a exceção nomeando o acesso; é o contrato em ação. Rode o mesmo código no Editor com Safety Checks desligado (Jobs > Burst > Safety Checks) para ver a mudança sumir do radar e o resultado flutuar — e conclua o motivo da configuração padrão. Adicione um teste PlayMode que falha se o log contiver exceção de safety.

## Conexões
- [[unity-ijobentity-fonte-gerada-main-thread]] — Unity Entities: IJobEntity gera código por assinatura — e pode virar main thread sem aviso de sintaxe.
- [[unity-parallelfor-indexo-proprio]] — Unity Jobs: em IJobParallelFor você escreve no seu índice e lê fora com intenção declarada.

## Fontes
- [Unity Entities @1.0 — Safety in Entities](https://docs.unity3d.com/Packages/com.unity.entities@1.0/manual/concepts-safety.html) — descreve as checagens de segurança, a configuração do Editor e o comportamento distinto em runtime builds Consulta: 2026-10-04.
- [Unity ECS Samples — jobs.md](https://github.com/Unity-Technologies/EntityComponentSystemSamples/blob/master/EntitiesSamples/Docs/jobs.md) — documentação oficial de jobs do repositório de amostras: exceções de corrida, ReadOnly e os atributos de disable Consulta: 2026-10-04.
