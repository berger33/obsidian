---
id: software.testes.tranche15.000907
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://kotest.io/docs/framework/concurrency6.html", "https://kotest.io/docs/framework/project-setup.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Kotest 6.2: evitar aplicar expectativa JVM a todas as plataformas

## Em uma frase
Os modos de concorrência descritos na documentação do Kotest têm suporte dependente da plataforma; os destinos que não oferecem esses modos continuam executando testes sequencialmente.

## Por que importa
Um projeto multiplataforma pode compilar a mesma Spec para JVM, JS ou Native, mas engine e capacidades de execução não são idênticos.

## Como funciona
Tratar um teste que depende de simultaneidade como portátil sem verificar destino cria falsa cobertura da matriz.

## Exemplo
Separe testes que validam uma propriedade de concorrência JVM de expectativas funcionais compartilhadas, e configure concurrency apenas nos targets onde a implementação oferece esse comportamento.

## Limites e trade-offs
Uma passagem sequencial em outro target não prova ausência de race condition em JVM, assim como a configuração JVM não acelera automaticamente o Native.

## Como verificar
Execute os mesmos casos em cada target suportado e registre qual semântica de concorrência o engine aplicou, incluindo testes próprios para coordenação paralela.

## Conexões
- [[kotest-prepare-spec-e-instancias-recriadas]] — Veja também: Kotest 6.2: escolher listener de setup conforme o número de instâncias.
- [[kotest-filter-por-tags-sem-perder-casos]] — Veja também: Kotest 6.2: usar tags como classificação sem transformar filtro em suíte completa.

## Fontes
- [Kotest 6.2 — Concurrency](https://kotest.io/docs/framework/concurrency6.html) — concorrência de specs/testes, dispatcher e escopo por plataforma; consultado em 2026-10-02.
- [Kotest 6.2 — Setup](https://kotest.io/docs/framework/project-setup.html) — diferenças de engine e targets multiplataforma; consultado em 2026-10-02.
