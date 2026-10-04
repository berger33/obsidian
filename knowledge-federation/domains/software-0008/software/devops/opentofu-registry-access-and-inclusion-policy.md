---
id: software.devops.tranche01.000038
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/opentofu/opentofu/main/README.md", "https://opentofu.org/docs/intro/install"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Acesso ao OpenTofu Registry e transparência da Registry Inclusion Policy

## Em uma frase
A seção Registry Access do README oficial informa que, para cumprir sanções aplicáveis, o projeto bloqueia o acesso a partir de países de origem específicos, remetendo os detalhes completos para a política pública `Registry Inclusion Policy` em `https://github.com/opentofu/registry/blob/main/POLICY.md`.

## Por que importa
Como a inicialização de projetos OpenTofu baixa provedores e módulos do registro público por padrão, operadores de redes corporativas globais, mirrors internos e equipes de conformidade precisam conhecer as regras do registro oficial e onde a política está versionada (`opentofu/registry`).

## Como funciona
Consulte `https://github.com/opentofu/registry/blob/main/POLICY.md` ao publicar provedores/módulos no registro oficial ou ao planejar espelhos (mirrors) de provedores para ambientes desconectados (air-gapped) e redes sujeitas a restrições regionais.

## Exemplo
O próprio registro do OpenTofu mantém sua política de inclusão e operação versionada em um repositório Git público (`github.com/opentofu/registry`).

## Limites e trade-offs
Em ambientes sem acesso direto à internet pública ou sujeitos a bloqueios de rede, configure caches ou espelhos locais de provedores conforme a documentação oficial em `opentofu.org/docs`.

## Como verificar
Conferi a seção Registry Access no README oficial de `opentofu/opentofu`.

## Conexões
- [[opentofu-security-policy-and-copyright-liaison]] — Veja também: Políticas formais de reporte de vulnerabilidades de segurança e questões de copyright.
- [[opentofu-tsc-and-community-meetings]] — Veja também: Governança aberta: reuniões semanais da comunidade e quinzenais do Technical Steering Committee (TSC).

## Fontes
- [OpenTofu — README oficial](https://raw.githubusercontent.com/opentofu/opentofu/main/README.md) — README oficial do OpenTofu com definição OSS, quatro Key features (IaC, Execution Plans, Resource Graph e Change Automation), Nightly Builds (30 dias e latest.json), Security Policy, liaison@opentofu.org, Registry Policy, reuniões e licença MPL-2.0.; consultado em 2026-10-03.
- [OpenTofu — Installing OpenTofu (documentação oficial)](https://opentofu.org/docs/intro/install) — Guia oficial de introdução e instalação do OpenTofu na documentação oficial opentofu.org.; consultado em 2026-10-03.
