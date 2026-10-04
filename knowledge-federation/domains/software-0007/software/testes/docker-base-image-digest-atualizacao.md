---
id: software.testes.tranche08.000242
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

# Docker: controlar base image e processo de atualização

## Em uma frase
Registre de forma deliberada a referência da imagem base e mantenha rotina para incorporar correções de segurança.

## Por que importa
Tag pode apontar para conteúdo atualizado em momento diferente, enquanto pin absoluto sem manutenção mantém vulnerabilidade conhecida.

## Como funciona
Escolha tag ou digest segundo política de reprodutibilidade, automatize descoberta de atualização e teste rebuild antes de promover imagem nova.

## Exemplo
Pull request atualiza digest, executa build e testes de runtime, e mostra diferença de versão ao revisor.

## Limites e trade-offs
Digest fixa bytes, não garante que eles sejam seguros; scanners também têm cobertura, atraso e falsos positivos.

## Como verificar
Rebuild em ambiente limpo, compare referência resolvida e leia avisos de build; confirme que pipeline tem mecanismo de atualização.

## Conexões
- [[docker-image-sbom-provenance-release]] — Veja também: Docker: associar imagem publicada a versão e proveniência.
- [[terraform-provider-lockfile-reprodutibilidade]] — Veja também: Terraform: validar reprodutibilidade de providers.

## Fontes
- [Docker — Building best practices](https://docs.docker.com/build/building/best-practices/) — multi-stage, pinning, cache e testes de imagens; consultado em 2026-10-02.
- [Docker — Build checks](https://docs.docker.com/build/checks/) — checks estáticos de Dockerfile durante build; consultado em 2026-10-02.
