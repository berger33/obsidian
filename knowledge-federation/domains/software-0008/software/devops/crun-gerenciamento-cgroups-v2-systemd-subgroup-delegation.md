---
id: software.devops.tranche07.000694
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/containers/crun/main/README.md", "https://raw.githubusercontent.com/containers/crun/main/crun.1.md", "https://github.com/containers/crun"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Containers crun: gerenciamento de cgroups (cgroupfs, systemd) e anotações de subgrupo e delegação em cgroup v2

## Em uma frase
O `crun` gerencia cgroups via `--cgroup-manager` (`cgroupfs`, `systemd` ou `disabled`) e fornece anotações OCI avançadas (`run.oci.systemd.subgroup`, `run.oci.delegate-cgroup` e `run.oci.systemd.force_cgroup_v1`) para controle fino de hierarquia e delegação segura em cgroup v2.

## Por que importa
Na hierarquia unificada do Linux `cgroup v2`, a regra de "sem processos internos" (no internal processes rule) exige que os processos de um container fiquem em um subgrupo folha separado dos nós intermediários que distribuem controladores; além disso, containers que executam o próprio systemd ou gerenciadores internos precisam receber um sub-cgroup delegado sem escapar dos limites impostos pelo runtime no host. A documentação `crun.1.md` detalha como o `crun` resolve esses dois desafios.

## Como funciona
Por meio de `--cgroup-manager=MANAGER` (ou `--systemd-cgroup`), o `crun` configura os limites de recursos diretamente via `cgroupfs` ou via `systemd`. Quando gerenciado pelo systemd em `cgroup v2`, a anotação `run.oci.systemd.subgroup=SUBGROUP` controla o sub-cgroup criado sob o escopo do systemd (`/sys/fs/cgroup/$PATH/$SUBGROUP`, cujo padrão é `container` em cgroup v2 e `""` em cgroup v1). Se além dela a anotação `run.oci.delegate-cgroup=DELEGATED-CGROUP` for especificada (suportada exclusivamente em cgroup v2, pois a delegação em cgroup v1 não é segura), o `crun` cria mais um nível `/sys/fs/cgroup/$PATH/$SUBGROUP/$DELEGATED-CGROUP` e move o processo do container para lá: o runtime aplica os limites apenas em `$PATH/$SUBGROUP`, permitindo que o payload do container gerencie livremente `$DELEGATED-CGROUP` sem jamais exceder o teto do pai. Já `run.oci.systemd.force_cgroup_v1=/PATH` permite rodar containers com versões legadas do systemd dentro de um host cgroup v2.

## Exemplo
```bash
# Executar crun especificando explicitamente o gerenciador systemd para cgroups v2
crun --cgroup-manager=systemd list
```

## Limites e trade-offs
Conforme adverte a documentação oficial em `crun.1.md`, a anotação `run.oci.delegate-cgroup` só funciona em sistemas `cgroup v2` e exige que `run.oci.systemd.subgroup` esteja ativo; já o uso de `run.oci.systemd.force_cgroup_v1=/PATH` requer que o host já possua a montagem manual `none,name=systemd` preparada em `/sys/fs/cgroup/systemd` com permissões adequadas.

## Como verificar
Inspecione `/proc/<pid-do-container>/cgroup` em um host Linux com `cgroup v2` e `crun --cgroup-manager=systemd` para confirmar que o processo do container reside no subgrupo `/container` (ou no subgrupo delegado configurado).

## Conexões
- [[crun-logging-global-options-journald-syslog-json]] — Veja também: Containers crun: opções globais de diagnóstico, backends de log (file, journald, syslog) e formatos text/json.
- [[crun-checkpoint-restore-criu-pre-dump-gerenciamento]] — Veja também: Containers crun: Checkpoint e Restore de containers com CRIU, pre-dumps incrementais e restauração LSM.
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Referência cruzada direta com crun-runtime-oci-linguagem-c-baixo-consumo-memoria.
- [[crun-comandos-cli-estado-mounts-dinamicos-update]] — Referência cruzada direta com crun-comandos-cli-estado-mounts-dinamicos-update.
- [[runc-supervisores-systemd-cgroup-v2-checkpoint-criu]] — Referência cruzada direta com runc-supervisores-systemd-cgroup-v2-checkpoint-criu.

## Fontes
- [Containers crun GitHub — README.md (C Architecture, Memory Footprint, Shared libcrun & Nix Static Build)](https://raw.githubusercontent.com/containers/crun/main/README.md) — README oficial do crun demonstrando benchmarks de velocidade e memória (512 KB) frente ao runc, compilação Autotools com libocispec, libcrun compartilhada, builds estáticos Nix e verificação GPG; consultado em 2026-10-03.
- [Containers crun Manual Page — crun.1.md (Commands, Cgroup v2 Delegation, CRIU & OCI Annotations)](https://raw.githubusercontent.com/containers/crun/main/crun.1.md) — Página de manual oficial crun.1.md especificando comandos CLI, opções globais de log, delegação em cgroup v2, checkpoint/restore com pre-dump CRIU e anotações run.oci.* (incluindo wasm e krun); consultado em 2026-10-03.
- [Containers crun — Official GitHub Repository](https://github.com/containers/crun) — Repositório oficial do runtime OCI crun na organização containers; consultado em 2026-10-03.
