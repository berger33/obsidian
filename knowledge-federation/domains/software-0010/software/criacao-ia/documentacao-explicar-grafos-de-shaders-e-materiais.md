---
id: software.criacao_ia.tranche02.000197
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

# Documentação de Arte: detalhar entradas e nós matemáticos de shader graphs

## Em uma frase
Documentar grafos de shaders explicando nós matemáticos e entradas expostas facilita o reuso de materiais por artistas técnicos.

## Por que importa
Grafos visuais densos sem documentação de nós e propriedades tornam-se caixas-pretas impossíveis de customizar com segurança.

## Como funciona
Catalogue todas as propriedades expostas no material (ex.: `NormalStrength`, `RoughnessMultiplier`), detalhando a faixa válida de valores e exibindo capturas dos subgrafos matemáticos com descrições de função.

## Exemplo
```markdown
# Documentacao de Shader: PBR Dissolve Shader

## Propriedades Expostas

## Limites e trade-offs
Nome

## Como verificar
Tipo

## Conexões
- [[documentacao-incorporar-sandboxes-e-demos-interativos]] — Veja também: Documentação Interativa: incorporar sandboxes de código executável em tutoriais.
- [[documentacao-manter-guias-de-migracao-e-breaking-changes]] — Veja também: Manutenção de Software: documentar breaking changes e guias de migração.

## Fontes
- [Diátaxis Documentation Framework — Explanation](https://diataxis.fr/explanation/) — Especificação formal do quadrante de explicação, arquitetura conceitual e análise de trade-offs. Consulta: 2026-10-04.
- [Diátaxis Documentation Framework — How-to Guides](https://diataxis.fr/how-to-guides/) — Guia para redação de passos orientados a problemas práticos de produção e trabalho diário. Consulta: 2026-10-04.
