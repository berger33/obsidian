---
id: software.testes.tranche12.000596
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
data_revisao_ia: 2026-10-02
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-12.md"
fontes: ["https://pitest.org/quickstart/incremental_analysis/", "https://pitest.org/quickstart/maven/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# PIT: tratar histórico incremental como otimização

## Em uma frase
A análise incremental conserva resultados anteriores e evita recomputar mutações que PIT considera inferíveis a partir de código e testes não alterados.

## Por que importa
Histórico pode tornar ciclos sucessivos mais rápidos, mas as inferências dependem de pressupostos sobre mudanças e não substituem validação completa após alterações relevantes.

## Como funciona
Habilite `withHistory` ou configure os arquivos de entrada e saída de histórico para um fluxo controlado; invalide ou renove os dados quando a estrutura da análise mudar.

## Exemplo
Um desenvolvedor pode usar histórico local para comparar commits próximos e reservar uma execução limpa para confirmar uma release.

## Limites e trade-offs
A documentação descreve como não provada a suposição de que mudanças em dependências raramente alteram o estado de mutantes analisados.

## Como verificar
Compare uma execução incremental com uma completa em amostra representativa e registre diferenças antes de tornar histórico parte de um gate.

## Conexões
- [[pit-timeouts-mutantes-hang]] — Veja também: PIT: distinguir timeout de mutante sobrevivente.
- [[pit-maven-dry-run-setup]] — Veja também: PIT: usar dry run ao configurar a análise.

## Fontes
- [PIT — Incremental Analysis](https://pitest.org/quickstart/incremental_analysis/) — histórico incremental e pressupostos usados para inferir resultados anteriores; consultado em 2026-10-02.
- [PIT — Maven Quick Start](https://pitest.org/quickstart/maven/) — goal mutationCoverage, filtros e modo dry run documentado desde 1.17.3; consultado em 2026-10-02.
