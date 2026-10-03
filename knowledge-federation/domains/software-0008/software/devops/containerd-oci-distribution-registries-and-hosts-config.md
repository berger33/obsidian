---
id: software.devops.tranche01.000075
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

# Suporte a qualquer registry compatível com a OCI Distribution Specification e configuração em `docs/hosts.md`

## Em uma frase
A seção Supported Registries do README oficial declara que qualquer registro de imagens compatível com a **OCI Distribution Specification** (`github.com/opencontainers/distribution-spec`) é suportado pelo containerd, apontando a documentação de configuração de hosts de registro em `docs/hosts.md`.

## Por que importa
Padronizar a transferência de imagens sobre a especificação aberta OCI Distribution garante que o containerd puxe e empurre imagens de qualquer registry público, corporativo ou espelho local sem lock-in, enquanto a configuração por host em `docs/hosts.md` permite definir mirrors, certificados TLS privados e endpoints customizados.

## Como funciona
Configure espelhos de registro (mirrors), autoridades certificadoras internas e políticas de resolução de hosts seguindo o guia oficial `docs/hosts.md` do repositório.

## Exemplo
Em ambientes corporativos com cache local de imagens ou registros privados com CA própria, toda a personalização de transporte de registro do containerd é regida pelo modelo descrito em `docs/hosts.md`.

## Limites e trade-offs
Certifique-se de que qualquer registro ou proxy de artefatos intermediário adotado na infraestrutura implemente fielmente a OCI Distribution Specification.

## Como verificar
Conferi a seção Supported Registries no README oficial de `containerd/containerd`.

## Conexões
- [[containerd-checkpoint-restore-with-criu]] — Veja também: Checkpoint e Restore de contêineres em Linux com o requisito do `criu`.
- [[containerd-releases-stability-and-ctr-autocompletion]] — Veja também: Estabilidade de API (`RELEASES.md`, `FEATURES.MD`) e autocompletar de shell para o cliente `ctr`.

## Fontes
- [containerd — README oficial](https://raw.githubusercontent.com/containerd/containerd/main/README.md) — README oficial do containerd com arquitetura para Linux/Windows, guias ops/namespaces/client-opts, requisitos runc/hcsshim e kernel 4.x vs 3.18 btrfs, criu, OCI Distribution e hosts.md, autocompletar ctr, plugin CRI GA com critest/crictl e licenças.; consultado em 2026-10-03.
- [Repositório oficial containerd/containerd](https://github.com/containerd/containerd) — Repositório oficial do containerd no GitHub com docs/, RELEASES.md, BUILDING.md e ADOPTERS.md.; consultado em 2026-10-03.
