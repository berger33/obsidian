---
id: software.criacao_ia.tranche04.000333
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.entities@1.4/api/Unity.Entities.IJobEntity.html", "https://docs.unity3d.com/Packages/com.unity.entities@1.0/api/Unity.Entities.IJobEntity.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Entities: IJobEntity gera código por assinatura — e pode virar main thread sem aviso de sintaxe

## Em uma frase
Tipos que implementam IJobEntity com Execute() geram um IJobChunk na compilação; se a query usa SharedComponent ou ManagedComponent, o job gerado exige o EntityManager e só roda na main thread.

## Por que importa
IJobEntity é o equilíbrio produtivo do DOTS: menos boilerplate que IJobChunk para computação por entidade. O contrapeso documentado é a restrição de thread quando a query toca tipos que quebram o modelo chunk-contíguo — descobrir isso na review do plano de jobs, não no profile de um build de produção travando.

## Como funciona
A referência formaliza: 'qualquer tipo que implemente a interface e tenha Execute() (com qualquer número de parâmetros) dispara a geração de código de um IJobChunk correspondente'. Os parâmetros compõem a query e a assinatura de acesso (in/refRO/refRW/out); SharedComponent/ManagedComponent na lista implica main thread. Para trabalho pesado concorrente, o caminho é tirar esses tipos da assinatura (copiar para componente usual) e aceitar o boilerplate de IJobChunk quando o controle fino do chunk importa — o próprio manual pondera que IJobChunk tem overhead menor e mais flexibilidade.

## Exemplo
O 'culling por distância' precisa do material compartilhado: em vez de passar SharedComponent por parâmetro (que força a main thread), um sistema pré-calcula um componente de flag por chunk e o IJobEntity passa a rodar com a Job Safety intacta em paralelo.

## Limites e trade-offs
A frase do manual é comparativa: IJobEntity 'pode expressar a mesma operação com muito menos boilerplate' para computação simples por entidade — a decisão é por caso, não por gosto. Os parâmetros do Execute definem query e filtro, e gerar a query errada não é erro de compilação, é custo silencioso. Jobs que alternam enabled-state de habilitáveis também completam antes da leitura do estado.

## Como verificar
Adicione um SharedComponent à assinatura de um fixture e confirme no Profiler que o job migrou para o worker da main thread; remova e veja o paralelo voltar. O teste de compilação do Gerador (erro de assinatura malformada) valida que o pipeline está ativo no CI. Compare IJobChunk vs. IJobEntity no mesmo workload para calibrar a escolha declarada no manual.

## Conexões
- [[unity-ecb-bufferfromentity-replay]] — Unity Entities: a EntityCommandBuffer é replay, não fila mágica.
- [[unity-safety-system-corrida-exception]] — Unity Jobs: o safety system é a sua revisão de concorrência em tempo de execução.

## Fontes
- [Unity Entities @1.4 — IJobEntity (API)](https://docs.unity3d.com/Packages/com.unity.entities@1.4/api/Unity.Entities.IJobEntity.html) — define a geração por fonte e a comparação de overhead com IJobChunk Consulta: 2026-10-04.
- [Unity Entities @1.0 — IJobEntity (API)](https://docs.unity3d.com/Packages/com.unity.entities@1.0/api/Unity.Entities.IJobEntity.html) — documenta a restrição do EntityManager/main thread para Shared e Managed Components Consulta: 2026-10-04.
