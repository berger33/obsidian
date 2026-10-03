---
id: software.devops.tranche01.000037
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-25.md"
fontes: ["https://raw.githubusercontent.com/opentofu/opentofu/main/README.md", "https://github.com/opentofu/opentofu"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Políticas formais de reporte de vulnerabilidades de segurança e questões de copyright

## Em uma frase
As seções Reporting security vulnerabilities e Reporting possible copyright issues do README oficial estabelecem dois canais formais de governança e conformidade: vulnerabilidades reais ou potenciais devem seguir a Security Policy em `https://github.com/opentofu/opentofu/security/policy` (com envio de e-mail de confirmação de recebimento e um segundo e-mail quando o problema for identificado positiva ou negativamente), enquanto possíveis questões de copyright ou propriedade intelectual devem ser reportadas diretamente para `liaison@opentofu.org`.

## Por que importa
Em um projeto de infraestrutura como código nascido como fork comunitário sob governança aberta, manter tanto um fluxo estruturado de divulgação coordenada de vulnerabilidades quanto um canal dedicado de propriedade intelectual (`liaison@opentofu.org`) dá segurança jurídica e operacional a empresas adotantes.

## Como funciona
Nunca abra uma issue pública para relatar uma vulnerabilidade de segurança no OpenTofu; siga o procedimento privado em `github.com/opentofu/opentofu/security/policy`, e utilize `liaison@opentofu.org` para qualquer comunicação relativa a direitos autorais ou propriedade intelectual.

## Exemplo
Em ambos os fluxos, o README compromete-se explicitamente com o envio de um e-mail inicial confirmando o recebimento do relato.

## Limites e trade-offs
Issues comuns de bugs funcionais e dúvidas de uso que não envolvam segurança nem copyright continuam nos canais públicos (GitHub Issues e GitHub Discussions).

## Como verificar
Conferi as seções Reporting security vulnerabilities e Reporting possible copyright issues no README oficial.

## Conexões
- [[opentofu-nightly-builds-and-latest-json]] — Veja também: Builds noturnos (`nightlies.opentofu.org`), retenção de 30 dias e automação via `latest.json`.
- [[opentofu-registry-access-and-inclusion-policy]] — Veja também: Acesso ao OpenTofu Registry e transparência da Registry Inclusion Policy.

## Fontes
- [OpenTofu — README oficial](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md) — README oficial do OpenTofu com definição OSS, quatro Key features (IaC, Execution Plans, Resource Graph e Change Automation), Nightly Builds (30 dias e latest.json), Security Policy, liaison@opentofu.org, Registry Policy, reuniões e licença MPL-2.0.; consultado em 2026-10-03.
- [Repositório oficial opentofu/opentofu](https://github.com/opentofu/opentofu) — Repositório oficial do OpenTofu no GitHub com código-fonte, RELEASE.md, CONTRIBUTING.md e LICENSE (MPL-2.0).; consultado em 2026-10-03.
