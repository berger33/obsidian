---
id: software.testes.tranche08.000244
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

# Docker: não inserir secrets em ARG, ENV ou layers

## Em uma frase
Evite embutir credenciais em build arguments ou variáveis persistentes na imagem; use mecanismo próprio de secret para build.

## Por que importa
Valores podem aparecer em metadados, history, cache ou camada mesmo quando arquivo é removido em instrução posterior.

## Como funciona
Passe credencial pelo mecanismo de secret do builder durante a instrução que precisa dela e não copie material para estágio final.

## Exemplo
Build baixa dependência privada usando secret montado temporariamente; teste inspeciona history e filesystem para provar ausência do token.

## Limites e trade-offs
Secret mount não protege contra processo malicioso ou comando que imprime valor; logs, cache e contexto também precisam de controle.

## Como verificar
Use token canário, examine image history, layers, build logs e artefatos cacheados; revogue segredo de teste depois da validação.

## Conexões
- [[docker-build-context-dockerignore-audit]] — Veja também: Docker: auditar build context e .dockerignore.
- [[gha-artifact-retention-provenance]] — Veja também: GitHub Actions: reter artifacts sem perder proveniência.

## Fontes
- [Docker — Building best practices](https://docs.docker.com/build/building/best-practices/) — multi-stage, pinning, cache e testes de imagens; consultado em 2026-10-02.
- [Docker — Build context](https://docs.docker.com/build/building/context/) — arquivos incluídos/excluídos do contexto de build; consultado em 2026-10-02.
