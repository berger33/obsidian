---
id: software.criacao_ia.tranche02.000194
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-criacao-ia-2000-0004-tranche-02.md"
fontes: ["https://diataxis.fr/explanation/", "https://diataxis.fr/how-to-guides/"]
tags: [dominio/software, subdominio/criacao-ia, qualidade/candidata]
lote: software-criacao-ia-2000-0004
---

# Diátaxis Referência: catalogar APIs e parâmetros com precisão e sem narrativa

## Em uma frase
Páginas de referência técnica catalogam assinaturas de métodos, tipos de dados, parâmetros e retornos de forma neutra e austera.

## Por que importa
A referência técnica deve ser informativa e direta, funcionando como um mapa formal e confiável para consulta rápida durante a programação.

## Como funciona
Organize as entradas alfabeticamente ou por módulo, descrevendo o tipo de cada parâmetro, valores padrão, possíveis códigos de erro e exceções lançadas, sem digressões narrativas.

## Exemplo
```markdown
# Referencia: StateTreeComponent.StartLogic()

## Assinatura
`bool StartLogic()`

## Retorno
- `true`: A arvore de estados foi inicializada e comecou a avaliacao.
- `false`: Falha na inicializacao (asset StateTree nulo ou configuracao invalida).

## Excecoes
- Emite aviso no log de gameplay se chamado com o ator inativo.
```

## Limites e trade-offs
Incluir tutoriais ou discussões teóricas longas dentro da referência dificulta a localização rápida das propriedades desejadas.

## Como verificar
Confira se todos os parâmetros aceitos pela função constam na tabela com seus tipos estáticos devidamente documentados.

## Conexões
- [[diataxis-redigir-guias-how-to-para-tarefas-de-producao]] — Veja também: Diátaxis How-To: redigir passos objetivos para tarefas práticas de produção.
- [[diataxis-elaborar-artigos-de-explicacao-e-design]] — Veja também: Diátaxis Explicação: aprofundar decisões arquiteturais e modelos conceituais.
- [[diataxis-aplicar-os-quatro-quadrantes-de-documentacao]] — Conexão temática direta com diataxis-aplicar-os-quatro-quadrantes-de-documentacao.
- [[referencia-descrever-campos-com-precisao]] — Conexão temática direta com referencia-descrever-campos-com-precisao.
- [[documentacao-automatizar-validacao-de-links-e-snippets-em-ci]] — Conexão temática direta com documentacao-automatizar-validacao-de-links-e-snippets-em-ci.

## Fontes
- [Diátaxis Documentation Framework — Explanation](https://diataxis.fr/explanation/) — Especificação formal do quadrante de explicação, arquitetura conceitual e análise de trade-offs. Consulta: 2026-10-04.
- [Diátaxis Documentation Framework — How-to Guides](https://diataxis.fr/how-to-guides/) — Guia para redação de passos orientados a problemas práticos de produção e trabalho diário. Consulta: 2026-10-04.
