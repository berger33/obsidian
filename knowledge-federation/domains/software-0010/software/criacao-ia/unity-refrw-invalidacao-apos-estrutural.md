---
id: software.criacao_ia.tranche04.000337
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
fontes: ["https://docs.unity3d.com/Packages/com.unity.entities@1.0/manual/concepts-safety.html", "https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/programming-entities.html"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Unity Entities: RefRW/RefRO são handles com verificação, não ponteiros para sempre

## Em uma frase
Os tipos de referência RefRW/RefRO dão acesso por-entidade a um componente com checagens de validade — e uma mudança estrutural pode invalidar o alvo que a referência aponta.

## Por que importa
O modelo por referência ('ref access' via SystemAPI) é a cara do ECS moderno e é fácil de escrever demais: segurar um RefRW através de um ponto de mudança estrutural significa ler/escrever memória que o runtime pode ter movido. O manual de segurança nomeia exatamente essa armadilha e o que a proteção faz por você no Editor.

## Como funciona
A página oficial: 'esses tipos de referência têm checagens para garantir que o tipo contido ainda é válido quando as checagens de segurança estão ativas'. A regra de operação é curta: obter o handle, usar, descartar antes do ponto de mutação estrutural; para atravessar o ponto, reobter. Com as checagens ativas, o erro vira exceção com contexto; em runtime builds, o que fica é o undefined que o manual não promete capturar — o mesmo contraste geral da proteção do Entities.

## Exemplo
Um sistema coleta 'var tf = pm.GetRefRW<LocalTransform>(e)', chama um helper que desabilita um componente (estrutural) e depois usa o 'tf' — no Editor a exceção pega na hora; removendo a reobtenção, a regressão entra no release silenciosamente.

## Limites e trade-offs
RefRW/RefRO resolvem por entidade (o custo por acesso é o do lookup, não o do loop por chunk — para varredura ampla, o IJobChunk continua sendo o grão certo). Habilitar/desabilitar habilitáveis não é estrutural, mas a página lista as esperas de jobs igualmente. E as checagens ativas têm custo; o perfil com/sem é parte do ciclo, não luxo.

## Como verificar
Num teste de Editor, reproduza a invalidação (ref antes de remoção estrutural de componente) e confirme a exceção de validade. O mesmo código com Safety Checks desligado: documente o que ocorre na sua máquina — a lição é que a checagem é seu detector, não seu seguro. Um roslyn-analyzer caseiro nas chamadas pode forçar re-obtenção após pontos estruturais.

## Conexões
- [[unity-chunks-arquetipos-leitura-lote]] — Unity Entities: iterar por chunk é o grão de leitura da arquitetura.
- [[unity-blob-assets-imutavel-compacto]] — Unity Entities: Blob assets são o lado imutável do dado, não JSON serializado.

## Fontes
- [Unity Entities @1.0 — Safety in Entities](https://docs.unity3d.com/Packages/com.unity.entities@1.0/manual/concepts-safety.html) — define a checagem de validade dos RefRW/RefRO e o contraste Editor vs. runtime build Consulta: 2026-10-04.
- [Unity Entities @1.4 — Programming in Entities](https://docs.unity3d.com/Packages/com.unity.entities@1.4/manual/programming-entities.html) — panorama oficial das formas de acesso e de organização de dados em entidades Consulta: 2026-10-04.
