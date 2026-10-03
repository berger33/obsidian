---
id: software.devops.tranche03.000230
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/kyverno/kyverno/main/README.md", "https://github.com/kyverno/kyverno"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# SBOM em formato CycloneDX (ghcr.io/kyverno/sbom), SLSA 3 e política de uso de IA em contribuições

## Em uma frase
Os badges de topo e as seções Contributing e Software Bill of Materials do README destacam que o Kyverno possui selo **SLSA 3**, que todas as imagens do Kyverno incluem uma Software Bill of Materials (SBOM) no formato **CycloneDX** (`cyclonedx.org`) publicada em `ghcr.io/kyverno/sbom`, e que o guia de contribuição inclui, além de `CONTRIBUTING.md` e `DEVELOPMENT.md`, a política formal de uso de IA da comunidade (`AI_USAGE_POLICY.md` em `kyverno/community`).

## Por que importa
Enquanto o Cilium publica SBOMs em formato SPDX, o Kyverno publica SBOMs em formato CycloneDX em `ghcr.io/kyverno/sbom` aliado a garantias SLSA 3; conhecer ambos os padrões (SPDX e CycloneDX) permite automatizar a ingestão de inventários de dependências nas ferramentas de segurança da empresa.

## Como funciona
Incorpore a leitura dos pacotes em `ghcr.io/kyverno/sbom` (formato CycloneDX) na sua auditoria de cadeia de suprimentos e siga `CONTRIBUTING.md`, `DEVELOPMENT.md` e `AI_USAGE_POLICY.md` ao contribuir com o projeto.

## Exemplo
A equipe de segurança consome o SBOM CycloneDX publicado em `ghcr.io/kyverno/sbom` antes de promover uma nova versão do Kyverno para o registro interno Harbor.

## Limites e trade-offs
Verifique a assinatura e a proveniência SLSA 3 dos artefatos do Kyverno junto com a análise do SBOM CycloneDX durante atualizações de versão.

## Como verificar
Conferi os badges de topo e as seções Contributing e Software Bill of Materials no README oficial de kyverno/kyverno.

## Conexões
- [[kyverno-policy-library-and-interactive-playground]] — Veja também: Biblioteca oficial de políticas prontas para produção e Kyverno Playground.

## Fontes
- [Kyverno — GitHub README](https://raw.githubusercontent.com/kyverno/kyverno/main/README.md) — Visão geral do Kyverno (motor de políticas nativo para Kubernetes, validação/mutação/geração/limpeza e verificação de imagens, Non-Goals, projetos Chainsaw/Policy Reporter/Kyverno JSON/Envoy Plugin, casos de uso e SBOM CycloneDX).; consultado em 2026-10-03.
- [Kyverno — Repositório Oficial no GitHub](https://github.com/kyverno/kyverno) — Repositório oficial do Kyverno na CNCF com código-fonte, CONTRIBUTING.md, DEVELOPMENT.md e pacotes SBOM.; consultado em 2026-10-03.
