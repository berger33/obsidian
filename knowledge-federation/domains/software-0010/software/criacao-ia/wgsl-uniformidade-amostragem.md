---
id: software.criacao_ia.tranche04.000319
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
fontes: ["https://www.w3.org/TR/WGSL/", "https://www.w3.org/TR/webgpu/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# WGSL: fluxo divergente e operações uniformes — uma análise, não uma sugestão

## Em uma frase
A especificação WGSL faz análise de uniformidade: certas operações (barrier, sampling com derivadas implícitas) só são válidas onde o compilador pode provar que threads concordam.

## Por que importa
Um barrier dentro de um ramo que metade do workgroup pode pular é deadlock na teoria e undefined na prática; um textureSample em fluxo não uniforme usa derivadas mistas entre pixels vizinhos e produz artefatos de mip aleatórios. A regra existe porque o hardware é SIMT — fingir o contrário é como portar código CUDA direto e estragar a festa.

## Como funciona
A análise marca valores como uniformes (idênticos entre threads do workgroup) e não-uniformes; operações 'uniform-only' (workgroupUniformLoad, barrier, gradientes implícitos) precisam de inputs uniformes em fluxo uniforme. Para sampling em condição ramificada, use textureSampleLevel com mip calculado manualmente; para sincronização parcial, reconstrua o algoritmo em fases com barriers entre elas, não dentro de ramos.

## Exemplo
Um tile de 'only red pixels' que chama barrier() dentro do if por pixel é rejeitado; a mesma lógica com um mask lido uniformemente do workgroup, barrier fora do if e seleção por máscara dentro, compila e preserva a semântica.

## Limites e trade-offs
A análise é conservadora: há casos corretos que ela rejeita — a especificação fornece 'nonuniform' escape para casos controlados de sampling, mas o abuso anula a proteção. Uniformidade de derivada é regra de fragment; em compute o que importa é o contrato do workgroup (barrier atinge threads do mesmo workgroup e ponto final).

## Como verificar
Injete um barrier num ramo dependente de input por-thread e confirme o erro de compilação com mensagem de fluxo não-uniforme. Substitua o sample divergente por sampleLevel manual e valide a ausência de artefatos de mip num caso extremo de zoom. Rode o mesmo shader em dois drivers para ver a variação de diagnóstico (não de resultado).

## Conexões
- [[wgsl-builtins-estagios-corte]] — WGSL: cada estágio expõe apenas os embutidos que fazem sentido para ele.
- [[wgsl-sem-conversao-implicita]] — WGSL: sem coerções implícitas — o construtor é obrigatório e o erro é cedo.

## Fontes
- [W3C — WGSL (especificação)](https://www.w3.org/TR/WGSL/) — define a análise de uniformidade e as operações uniform-only Consulta: 2026-10-04.
- [W3C — WebGPU](https://www.w3.org/TR/webgpu/) — descreve o modelo de execução compute por workgroups no qual a análise se apoia Consulta: 2026-10-04.
