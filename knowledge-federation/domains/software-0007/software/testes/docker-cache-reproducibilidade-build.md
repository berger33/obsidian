---
id: software.testes.tranche08.000248
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-08.md"
fontes: ["https://docs.docker.com/build/building/best-practices/", "https://docs.docker.com/build/building/context/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Docker: testar cache sem depender dele para correção

## Em uma frase
Confirme que build correto pode ser reproduzido sem cache e que o cache apenas acelera, sem fornecer entrada oculta.

## Por que importa
Cache invalidado incorretamente pode reutilizar artefato antigo e mascarar dependência de arquivo que não foi declarada.

## Como funciona
Construa com cache limpo em CI periódico e mantenha ordem de instruções que torne dependências explícitas. Compare outputs relevantes entre execução fria e quente.

## Exemplo
Build com alteração em lockfile invalida etapa de instalação; build limpo e incremental produzem o mesmo binário versionado.

## Limites e trade-offs
Build não determinístico pode diferir por timestamp, rede ou ferramenta; igualdade binária requer configuração adicional além de limpar cache.

## Como verificar
Execute build frio e quente em ambiente controlado, inspecione entradas copiadas e confirme atualização após mudança de dependência.

## Conexões
- [[docker-base-image-digest-atualizacao]] — Veja também: Docker: controlar base image e processo de atualização.
- [[ml-reproducibilidade-seed-ambiente-artefatos]] — Veja também: ML: tornar experimentos e artefatos reproduzíveis.

## Fontes
- [Docker — Building best practices](https://docs.docker.com/build/building/best-practices/) — multi-stage, pinning, cache e testes de imagens; consultado em 2026-10-02.
- [Docker — Build context](https://docs.docker.com/build/building/context/) — arquivos incluídos/excluídos do contexto de build; consultado em 2026-10-02.
