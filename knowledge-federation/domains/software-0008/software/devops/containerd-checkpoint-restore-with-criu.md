---
id: software.devops.tranche01.000074
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

# Checkpoint e Restore de contêineres em Linux com o requisito do `criu`

## Em uma frase
Ainda na seção Runtime Requirements do README oficial, a documentação especifica que, para utilizar os recursos de **checkpoint and restore** no Linux, é necessário ter o `criu` (Checkpoint/Restore In Userspace) instalado no sistema.

## Por que importa
Capacidades de congelar o estado em memória de um contêiner em execução (checkpoint) e restaurá-lo posteriormente ou em outro nó (restore) dependem de suporte externo no espaço de usuário do Linux; como a maioria dos nós padrão só executa partida a frio de imagens, o containerd mantém seus requisitos mínimos enxutos e só exige o `criu` quando essa funcionalidade é acionada.

## Como funciona
Instale o pacote `criu` nos hosts Linux onde você planeja executar operações de checkpoint e restore de contêineres via containerd; em nós que não utilizam checkpoint/restore, o `criu` não é necessário para a operação normal do daemon.

## Exemplo
Manter o `criu` como dependência condicional preserva a diretriz central da seção Runtime Requirements ("Runtime requirements for containerd are very minimal").

## Limites e trade-offs
Verifique a compatibilidade do kernel e das políticas de segurança do host com o `criu` antes de habilitar fluxos de migração ou snapshot de memória em produção.

## Como verificar
Conferi o parágrafo sobre `criu` e Checkpoint and Restore na seção Runtime Requirements do README oficial.

## Conexões
- [[containerd-runtime-requirements-runc-hcsshim-and-kernel]] — Veja também: Requisitos de runtime: `runc` no Linux, `hcsshim` no Windows e versões mínimas de kernel para snapshotters.
- [[containerd-oci-distribution-registries-and-hosts-config]] — Veja também: Suporte a qualquer registry compatível com a OCI Distribution Specification e configuração em `docs/hosts.md`.

## Fontes
- [containerd — README oficial](https://raw.githubusercontent.com/containerd/containerd/main/README.md) — README oficial do containerd com arquitetura para Linux/Windows, guias ops/namespaces/client-opts, requisitos runc/hcsshim e kernel 4.x vs 3.18 btrfs, criu, OCI Distribution e hosts.md, autocompletar ctr, plugin CRI GA com critest/crictl e licenças.; consultado em 2026-10-03.
- [Repositório oficial containerd/containerd](https://github.com/containerd/containerd) — Repositório oficial do containerd no GitHub com docs/, RELEASES.md, BUILDING.md e ADOPTERS.md.; consultado em 2026-10-03.
