---
id: software.testes.tranche08.000249
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
fontes: ["https://docs.docker.com/build/building/best-practices/", "https://docs.docker.com/build/checks/"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Docker: associar imagem publicada a versão e proveniência

## Em uma frase
Registre referência imutável da imagem publicada e evidências de build para ligar produção ao código e processo de origem.

## Por que importa
Tag mutável e artifact sem proveniência dificultam identificar qual conteúdo foi testado ou reverter versão com confiança.

## Como funciona
Capture digest após build, associe commit e workflow e publique metadados de proveniência segundo a plataforma disponível.

## Exemplo
Release anota digest e commit; deploy consome digest ensaiado no smoke test em vez de resolver novamente uma tag móvel.

## Limites e trade-offs
Metadados de proveniência não provam que o código é seguro nem substituem assinatura verificada e política de supply chain.

## Como verificar
Compare digest testado e implantado, valide assinatura/attestation quando adotada e confirme caminho reprodutível entre source, build e artifact.

## Conexões
- [[gha-artifact-retention-provenance]] — Veja também: GitHub Actions: reter artifacts sem perder proveniência.
- [[docker-base-image-digest-atualizacao]] — Veja também: Docker: controlar base image e processo de atualização.

## Fontes
- [Docker — Building best practices](https://docs.docker.com/build/building/best-practices/) — multi-stage, pinning, cache e testes de imagens; consultado em 2026-10-02.
- [Docker — Build checks](https://docs.docker.com/build/checks/) — checks estáticos de Dockerfile durante build; consultado em 2026-10-02.
