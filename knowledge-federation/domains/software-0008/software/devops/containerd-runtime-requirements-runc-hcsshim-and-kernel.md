---
id: software.devops.tranche01.000073
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
fontes: ["https://raw.githubusercontent.com/containerd/containerd/main/README.md", "https://github.com/containerd/containerd"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Requisitos de runtime: `runc` no Linux, `hcsshim` no Windows e versões mínimas de kernel para snapshotters

## Em uma frase
A seção Runtime Requirements do README oficial explica que a maioria das interações com recursos de contêineres do Linux e do Windows é delegada ao `runc` (`github.com/opencontainers/runc`, cuja versão exigida é descrita em `docs/RUNC.md`) e/ou a bibliotecas específicas do sistema operacional (como `hcsshim` da Microsoft para Windows); no Linux, um ponto de partida razoável de versão mínima de kernel é a série **4.x**, pois o snapshotter de sistema de arquivos `overlay` (usado por padrão) utiliza recursos finalizados na série 4.x do kernel.

## Por que importa
Escolher o snapshotter de armazenamento certo para cada distribuição Linux exige conhecer o suporte do kernel: enquanto o snapshotter padrão `overlay` pede recursos consolidados no kernel 4.x, o README observa que o uso de `btrfs` oferece maior flexibilidade de versão de kernel (mínimo recomendado **3.18**), mas exige o módulo de kernel `btrfs` e as ferramentas `btrfs` instaladas na distribuição.

## Como funciona
Verifique a versão exata recomendada do `runc` em `docs/RUNC.md` ao atualizar o containerd em hosts Linux, use kernels 4.x+ com o snapshotter padrão `overlay` e instale o módulo/ferramentas `btrfs` caso opte pelo snapshotter `btrfs`.

## Exemplo
Separar o daemon de ciclo de vida (`containerd`) do runtime OCI de baixo nível (`runc`, documentado em `docs/RUNC.md`) permite atualizar e auditar cada componente com clareza.

## Limites e trade-offs
Como lembra o próprio README, números de versão de kernel em distribuições corporativas podem conter backports específicos da distro, mas a série 4.x permanece a referência base para o snapshotter padrão `overlay`.

## Como verificar
Conferi a seção Runtime Requirements no README oficial de `containerd/containerd`.

## Conexões
- [[containerd-ops-namespaces-and-client-opts-guides]] — Veja também: Documentação operacional central: `docs/ops.md`, isolamento em `docs/namespaces.md` e `docs/client-opts.md`.
- [[containerd-checkpoint-restore-with-criu]] — Veja também: Checkpoint e Restore de contêineres em Linux com o requisito do `criu`.

## Fontes
- [containerd — README oficial](https://raw.githubusercontent.com/containerd/containerd/main/README.md) — README oficial do containerd com arquitetura para Linux/Windows, guias ops/namespaces/client-opts, requisitos runc/hcsshim e kernel 4.x vs 3.18 btrfs, criu, OCI Distribution e hosts.md, autocompletar ctr, plugin CRI GA com critest/crictl e licenças.; consultado em 2026-10-03.
- [Repositório oficial containerd/containerd](https://github.com/containerd/containerd) — Repositório oficial do containerd no GitHub com docs/, RELEASES.md, BUILDING.md e ADOPTERS.md.; consultado em 2026-10-03.
