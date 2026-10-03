---
id: software.devops.tranche01.000079
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
fontes: ["https://raw.githubusercontent.com/containerd/containerd/main/README.md", "https://github.com/containerd/containerd"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Builds noturnos para Linux e Windows via GitHub Actions e restrição estrita contra uso em produção

## Em uma frase
A seção Nightly builds do README oficial informa que binários noturnos são gerados todas as noites a partir da branch `main` para `Linux` e `Windows` no workflow `Nightly` do GitHub Actions (`github.com/containerd/containerd/actions?query=workflow%3ANightly`), trazendo um aviso enfático: "Please be aware: nightly builds might have critical bugs, it's not recommended for use in production and no support provided."

## Por que importa
Testar contra binários noturnos de `main` permite que desenvolvedores de plugins, integradores de sistemas operacionais e suítes de CI detectem incompatibilidades cedo tanto em Linux quanto em Windows, mas colocá-los em nós de produção exporia o cluster a bugs críticos sem suporte da comunidade.

## Como funciona
Consuma os artefatos do workflow `Nightly` apenas em ambientes de laboratório e pipelines de integração contínua para testar mudanças recentes da branch `main` em Linux ou Windows; em produção, utilize exclusivamente releases oficiais listadas em `github.com/containerd/containerd/releases` ou pacotes estáveis da distribuição.

## Exemplo
O aviso explícito de que não há suporte para builds noturnos ("no support provided") reforça a importância de verificar `containerd --version` antes de abrir chamados operacionais.

## Limites e trade-offs
Para acompanhar a saúde das branches de release em comparação à `main`, consulte também os painéis periódicos do Kubernetes em `testgrid.k8s.io/containerd`.

## Como verificar
Conferi a seção Nightly builds no README oficial de `containerd/containerd`.

## Conexões
- [[containerd-cri-validation-critest-and-crictl-debugging]] — Veja também: Validação e depuração de setups CRI com `cri-tools`: `critest` e `crictl`.
- [[containerd-security-audits-governance-and-adopters]] — Veja também: Auditorias de segurança públicas (`containerd.io/security`), repositório `containerd/project` e `ADOPTERS.md`.

## Fontes
- [containerd — README oficial](https://raw.githubusercontent.com/containerd/containerd/main/README.md) — README oficial do containerd com arquitetura para Linux/Windows, guias ops/namespaces/client-opts, requisitos runc/hcsshim e kernel 4.x vs 3.18 btrfs, criu, OCI Distribution e hosts.md, autocompletar ctr, plugin CRI GA com critest/crictl e licenças.; consultado em 2026-10-03.
- [Repositório oficial containerd/containerd](https://github.com/containerd/containerd) — Repositório oficial do containerd no GitHub com docs/, RELEASES.md, BUILDING.md e ADOPTERS.md.; consultado em 2026-10-03.
