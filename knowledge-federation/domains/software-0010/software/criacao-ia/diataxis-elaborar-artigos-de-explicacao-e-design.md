---
id: software.criacao_ia.tranche02.000195
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

# Diátaxis Explicação: aprofundar decisões arquiteturais e modelos conceituais

## Em uma frase
Artigos de explicação discutem o contexto histórico, decisões de arquitetura e alternativas técnicas de um sistema de software.

## Por que importa
Entender por que uma tecnologia foi escolhida e quais seus limites fundamentais ajuda os engenheiros a projetarem sistemas mais robustos.

## Como funciona
Aborde o tema sob uma perspectiva abrangente, comparando diferentes abordagens (ex.: ECS vs Programação Orientada a Objetos em IA de jogos) e justificando as razões que motivaram o design atual.

## Exemplo
```markdown
# Explicacao: Por que adotamos Utility AI em vez de Behavior Trees

Behavior Trees sao excelentes para comportamentos com sequencias hierarquicas rigidas.
No entanto, quando os NPCs precisam ponderar dezenas de fatores continuos (saude, distancia, municao),
as arvores sofrem de explosao de ramos condicionais. O modelo Utility AI substitui esses ramos
por curvas de resposta matematicas continuas...
```

## Limites e trade-offs
Artigos de explicação não devem conter listas de passos práticos de execução; foque exclusivamente na teoria, arquitetura e conceitos.

## Como verificar
Revise se o texto apresenta uma visão equilibrada mencionando tanto os pontos fortes quanto os limites da abordagem escolhida.

## Conexões
- [[diataxis-organizar-referencias-tecnicas-sem-narrativa]] — Veja também: Diátaxis Referência: catalogar APIs e parâmetros com precisão e sem narrativa.
- [[documentacao-incorporar-sandboxes-e-demos-interativos]] — Veja também: Documentação Interativa: incorporar sandboxes de código executável em tutoriais.
- [[diataxis-aplicar-os-quatro-quadrantes-de-documentacao]] — Conexão temática direta com diataxis-aplicar-os-quatro-quadrantes-de-documentacao.
- [[unity-utility-ai-avaliar-decisoes-com-curvas]] — Conexão temática direta com unity-utility-ai-avaliar-decisoes-com-curvas.
- [[unreal-statetree-estruturar-hierarquia-de-estados]] — Conexão temática direta com unreal-statetree-estruturar-hierarquia-de-estados.

## Fontes
- [Diátaxis Documentation Framework — Explanation](https://diataxis.fr/explanation/) — Especificação formal do quadrante de explicação, arquitetura conceitual e análise de trade-offs. Consulta: 2026-10-04.
- [Diátaxis Documentation Framework — How-to Guides](https://diataxis.fr/how-to-guides/) — Guia para redação de passos orientados a problemas práticos de produção e trabalho diário. Consulta: 2026-10-04.
