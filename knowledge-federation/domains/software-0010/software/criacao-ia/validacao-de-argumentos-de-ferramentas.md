---
id: software.criacao_ia.tranche01.000026
tipo: tecnica
dominio: software
subdominio: criacao-ia
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-01.md"
fontes: ["https://platform.openai.com/docs/guides/function-calling", "https://platform.openai.com/docs/guides/structured-outputs"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Validação de argumentos de ferramentas

## Em uma frase

Argumentos do modelo continuam sendo dados não confiáveis, mesmo que tenham sido produzidos em formato JSON ou por schema.

## Por que importa

Validação no servidor impede valores fora de faixa, campos extras e identificadores que não pertencem ao usuário atual.

## Como funciona

Faça parse tipado, aplique limites e autorização contextual, rejeite propriedades desconhecidas e retorne erro controlado ao fluxo.

## Exemplo

Para mover um personagem, o servidor restringe o nome de destino a locais desbloqueados na sessão autenticada.

## Limites e trade-offs

Schema sintático não substitui checagem de propriedade, estado atual, rate limit ou regra de negócio.

## Como verificar

Envie campo ausente, enum inválido, número extremo e ID de outro usuário; confirme rejeição sem efeito lateral.

## Conexões
- [[function-calling-lidar-com-zero-ou-varias-chamadas]] — Function calling: lidar com zero ou várias chamadas.
- [[ferramentas-restringir-acoes-de-gameplay]] — Ferramentas: restringir ações de gameplay.

## Fontes
- [OpenAI API — Function calling](https://platform.openai.com/docs/guides/function-calling) — Define o ciclo de chamada de ferramenta entre modelo, aplicativo e resultado de ferramenta. Consulta: 2026-10-04.
- [OpenAI API — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — Documenta respostas compatíveis com esquemas JSON e suas limitações. Consulta: 2026-10-04.
