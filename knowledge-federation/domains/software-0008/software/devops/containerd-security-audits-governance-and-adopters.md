---
id: software.devops.tranche01.000080
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
fontes: ["https://raw.githubusercontent.com/containerd/containerd/main/README.md", "https://pkg.go.dev/github.com/containerd/containerd/v2"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Auditorias de segurança públicas (`containerd.io/security`), repositório `containerd/project` e `ADOPTERS.md`

## Em uma frase
As seções finais do README oficial (Security audit, Reporting security issues, Project details, Adoption e Now Recruiting) documentam a governança e a segurança da organização: auditorias independentes de segurança estão publicadas em `https://containerd.io/security/`, vulnerabilidades devem ser reportadas seguindo `containerd/project/blob/main/SECURITY.md#reporting-a-vulnerability`, e toda a governança (`GOVERNANCE.md`, incluindo o convite aberto a novos `security advisors`), lista de mantenedores (`MAINTAINERS`) e diretrizes de contribuição (`CONTRIBUTING.md`) ficam centralizadas no repositório `https://github.com/containerd/project`, enquanto adotantes públicos constam de `ADOPTERS.md`.

## Por que importa
Centralizar `GOVERNANCE.md`, `MAINTAINERS`, `SECURITY.md` e `CONTRIBUTING.md` no repositório `containerd/project` garante regras uniformes para o containerd principal e para todos os subprojetos da organização no GitHub, enquanto a publicação aberta das auditorias em `containerd.io/security/` apoia processos de compliance.

## Como funciona
Consulte `https://containerd.io/security/` para baixar relatórios de auditoria de segurança do runtime, siga `containerd/project/blob/main/SECURITY.md` para reporte responsável de vulnerabilidades e procure issues com a label `exp/beginner` se quiser iniciar contribuições técnicas no projeto.

## Exemplo
Na seção Now Recruiting, o projeto destaca que busca ajuda não apenas em código (issues `exp/beginner` e novos subprojetos), mas também em documentação, alcance comunitário e novos `security advisors`.

## Limites e trade-offs
A comunicação síncrona ocorre nos canais `#containerd` e `#containerd-dev` do Slack da CNCF e nas reuniões no Zoom listadas no calendário da CNCF.

## Como verificar
Conferi as seções Announcements, Communication, Security audit, Reporting security issues, Project details e Adoption no README oficial.

## Conexões
- [[containerd-nightly-builds-and-production-warning]] — Veja também: Builds noturnos para Linux e Windows via GitHub Actions e restrição estrita contra uso em produção.

## Fontes
- [containerd — README oficial](https://raw.githubusercontent.com/containerd/containerd/main/README.md) — README oficial do containerd com arquitetura para Linux/Windows, guias ops/namespaces/client-opts, requisitos runc/hcsshim e kernel 4.x vs 3.18 btrfs, criu, OCI Distribution e hosts.md, autocompletar ctr, plugin CRI GA com critest/crictl e licenças.; consultado em 2026-10-03.
- [Pacote containerd v2 no pkg.go.dev](https://pkg.go.dev/github.com/containerd/containerd/v2) — Referência oficial da biblioteca Go github.com/containerd/containerd/v2 no pkg.go.dev.; consultado em 2026-10-03.
