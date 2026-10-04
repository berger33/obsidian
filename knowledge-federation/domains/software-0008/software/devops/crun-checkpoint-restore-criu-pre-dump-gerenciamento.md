---
id: software.devops.tranche07.000695
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

# Containers crun: Checkpoint e Restore de containers com CRIU, pre-dumps incrementais e restauração LSM

## Em uma frase
Os subcomandos `crun checkpoint` e `crun restore` integram o CRIU para congelar e restaurar containers (incluindo conexões TCP ativas e UNIX sockets), suportando cópias incrementais de memória sem parar o container (`--pre-dump` / `--parent-path`) e reconfiguração de contexto SELinux/AppArmor na restauração.

## Por que importa
Realizar o checkpoint completo de um container que utiliza vários gigabytes de memória RAM pausa a aplicação durante todo o tempo necessário para gravar as páginas de memória em disco. De acordo com a página de manual `crun.1.md`, o suporte do `crun` a `--pre-dump` permite copiar a memória em segundo plano enquanto o container continua rodando, reduzindo o tempo de congelamento no checkpoint final para uma fração de segundo.

## Como funciona
O comando `crun checkpoint` aceita opções como `--image-path=DIR`, `--work-path=DIR`, `--leave-running`, `--tcp-established`, `--ext-unix-sk`, `--shell-job` e `--manage-cgroups-mode=MODE` (`soft` por padrão, `ignore`, `full` ou `strict`). Quando `--pre-dump` é utilizado, o `crun` faz o dump apenas da memória sem parar o container; como não é possível restaurar diretamente de um pre-dump, executam-se quantos pre-dumps forem necessários e um checkpoint final apontando para o pre-dump anterior via `--parent-path=DIR` (que deve obrigatoriamente ser um caminho relativo a partir do diretório `--image-path`, falhando se for usado caminho absoluto). Na restauração (`crun restore`), opções como `--lsm-profile=TYPE:NAME` (`apparmor` ou `selinux`) e `--lsm-mount-context=VALUE` permitem restaurar o container em um novo Pod Kubernetes onde os rótulos SELinux mudaram, e a anotação `org.criu.config=FILE` (requer CRIU >= 4.2) permite customizar a configuração RPC do CRIU (`/etc/criu/crun.conf` ou `/etc/criu/runc.conf`).

## Exemplo
```bash
# Realizar um pre-dump de memória sem parar o container seguido do checkpoint final com caminho relativo
mkdir -p /tmp/ckpt/predump1 /tmp/ckpt/final
sudo crun checkpoint --pre-dump --image-path=/tmp/ckpt/predump1 meu-container
sudo crun checkpoint --parent-path=../predump1 --image-path=/tmp/ckpt/final meu-container

# Restaurar o container a partir do checkpoint final em modo detached
sudo crun restore --detach --image-path=/tmp/ckpt/final --bundle=/caminho/bundle meu-container-restaurado
```

## Limites e trade-offs
Conforme enfatizado na documentação de `--parent-path` em `crun.1.md`, passar um caminho absoluto em `--parent-path` (como `/tmp/ckpt/predump1`) fará com que o `crun` e o CRIU falhem; é obrigatório usar um caminho relativo a partir do diretório especificado em `--image-path` (como `../predump1`).

## Como verificar
Após executar `crun checkpoint` e `crun restore --detach`, execute `crun list` e `crun ps <id>` para confirmar que o processo restaurado retomou a execução a partir do estado salvo.

## Conexões
- [[crun-gerenciamento-cgroups-v2-systemd-subgroup-delegation]] — Veja também: Containers crun: gerenciamento de cgroups (cgroupfs, systemd) e anotações de subgrupo e delegação em cgroup v2.
- [[crun-extensoes-oci-seccomp-annotations-handlers-wasm-krun]] — Veja também: Containers crun: extensões de anotações OCI para seccomp avançado, pidfd e handlers nativos para WebAssembly (wasm) e libkrun (krun).
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Referência cruzada direta com crun-runtime-oci-linguagem-c-baixo-consumo-memoria.
- [[crun-comandos-cli-estado-mounts-dinamicos-update]] — Referência cruzada direta com crun-comandos-cli-estado-mounts-dinamicos-update.
- [[runc-supervisores-systemd-cgroup-v2-checkpoint-criu]] — Referência cruzada direta com runc-supervisores-systemd-cgroup-v2-checkpoint-criu.

## Fontes
- [Containers crun GitHub — README.md (C Architecture, Memory Footprint, Shared libcrun & Nix Static Build)](https://raw.githubusercontent.com/containers/crun/main/README.md) — README oficial do crun demonstrando benchmarks de velocidade e memória (512 KB) frente ao runc, compilação Autotools com libocispec, libcrun compartilhada, builds estáticos Nix e verificação GPG; consultado em 2026-10-03.
- [Containers crun Manual Page — crun.1.md (Commands, Cgroup v2 Delegation, CRIU & OCI Annotations)](https://raw.githubusercontent.com/containers/crun/main/crun.1.md) — Página de manual oficial crun.1.md especificando comandos CLI, opções globais de log, delegação em cgroup v2, checkpoint/restore com pre-dump CRIU e anotações run.oci.* (incluindo wasm e krun); consultado em 2026-10-03.
- [Containers crun — Official GitHub Repository](https://github.com/containers/crun) — Repositório oficial do runtime OCI crun na organização containers; consultado em 2026-10-03.
