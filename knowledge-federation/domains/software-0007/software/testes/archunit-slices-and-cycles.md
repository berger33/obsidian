---
id: software.testes.tranche19.001340
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://www.archunit.org/userguide/html/000_Index.html", "https://github.com/TNG/ArchUnit-Examples"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# ArchUnit: detectar dependências cíclicas

## Em uma frase
Regras de fatias dividem os pacotes segundo um padrão com grupos de captura e verificam se as fatias resultantes estão livres de ciclos.

## Por que importa
Ciclos entre módulos impedem refatoração e testes isolados, e a verificação os expõe antes de virarem estrutura consolidada.

## Como funciona
Defina o padrão que nomeia as fatias, ative a verificação de ausência de ciclos e trate cada ciclo como problema de desenho.

## Exemplo
Um projeto pode agrupar os pacotes por área do domínio e verificar que nenhuma área depende de outra de forma circular.

## Limites e trade-offs
Padrões mal escritos juntam fatias distintas em uma só, escondendo o ciclo, e a correção exige repensar a responsabilidade do módulo.

## Como verificar
Anote um ciclo conhecido e confirme que a verificação falha listando as fatias envolvidas na dependência circular.

## Conexões
- [[archunit-layered-architecture]] — Veja também: ArchUnit: verificar arquitetura em camadas.
- [[archunit-dependency-rules]] — Veja também: ArchUnit: controlar dependências entre classes e pacotes.

## Fontes
- [ArchUnit — User Guide](https://www.archunit.org/userguide/html/000_Index.html) — regras, camadas, fatias, congelamento e verificação por diagrama; consultado em 2026-10-03.
- [ArchUnit — Exemplos oficiais](https://github.com/TNG/ArchUnit-Examples) — exemplos de regras e do uso de congelamento; consultado em 2026-10-03.
