---
id: software.devops.tranche07.000700
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

# Containers crun: execução de processos adicionais (crun exec) com isolamento de sub-cgroup, capabilities, AppArmor e SELinux

## Em uma frase
O subcomando `crun exec` inicia um novo processo dentro de um container em execução permitindo customizar perfil AppArmor (`--apparmor`), rótulo SELinux (`--process-label`), capabilities (`--cap`), `--no-new-privs`, usuário (`--user`) e alocação em um `--cgroup` interno específico.

## Por que importa
Quando um engenheiro de plataforma ou um agente de diagnóstico executa um comando dentro de um container ativo (`exec`), muitas vezes é necessário que esse processo auxiliar rode com privilégios diferentes do processo principal da aplicação (por exemplo, sem adquirir novos privilégios, sob um perfil LSM mais restrito ou dentro de um sub-cgroup separado para que um comando de diagnóstico não consuma a cota de memória principal nem altere a contabilidade do serviço). A página de manual `crun.1.md` especifica todas as flags de `crun exec`.

## Como funciona
Ao invocar `crun [global options] exec [options] CONTAINER CMD`, o runtime entra nos namespaces do container ativo e lança o comando solicitado aplicando as restrições passadas por linha de comando ou por um arquivo JSON completo de processo (`--process=FILE`). As opções incluem `--cwd=PATH` (diretório de trabalho), `--env=ENV` (variáveis de ambiente), `-u / --user=UID[:GID]`, `-t / --tty` e `--console-socket=SOCKET`, `--detach` e `--pid-file=PATH`. Na camada de segurança e recursos, `--cap=CAP` adiciona capabilities específicas, `--no-new-privs` ativa o bit `no_new_privs` do kernel, `--apparmor=PROFILE` e `--process-label=VALUE` aplicam contextos de AppArmor e SELinux ao novo processo, e `--cgroup=PATH` posiciona o processo em um sub-cgroup específico que já exista dentro do cgroup do container.

## Exemplo
```bash
# Executar um processo de diagnóstico dentro de um container ativo com usuário não-root e no-new-privs
sudo crun exec --user 1000:1000 --no-new-privs --cwd /tmp meu-container-id id
```

## Limites e trade-offs
Conforme documentado em `crun.1.md` para a flag `--cgroup=PATH` do subcomando `exec`, o caminho do sub-cgroup informado já deve existir previamente dentro do cgroup do container antes da chamada `crun exec`, caso contrário a movimentação do novo processo para o sub-cgroup falhará.

## Como verificar
Com um container em execução sob o `crun`, execute `crun exec --no-new-privs <container-id> grep NoNewPrivs /proc/self/status` e confirme que a saída reporta `NoNewPrivs: 1`.

## Conexões
- [[crun-builds-estaticos-reprodutiveis-nix-verificacao-gpg]] — Veja também: Containers crun: builds estáticos reprodutíveis com Nix, automação Ansible e verificação GPG com crun.keyring.
- [[crun-runtime-oci-linguagem-c-baixo-consumo-memoria]] — Referência cruzada direta com crun-runtime-oci-linguagem-c-baixo-consumo-memoria.
- [[crun-comandos-cli-estado-mounts-dinamicos-update]] — Referência cruzada direta com crun-comandos-cli-estado-mounts-dinamicos-update.
- [[crun-gerenciamento-cgroups-v2-systemd-subgroup-delegation]] — Referência cruzada direta com crun-gerenciamento-cgroups-v2-systemd-subgroup-delegation.

## Fontes
- [Containers crun GitHub — README.md (C Architecture, Memory Footprint, Shared libcrun & Nix Static Build)](https://raw.githubusercontent.com/containers/crun/main/README.md) — README oficial do crun demonstrando benchmarks de velocidade e memória (512 KB) frente ao runc, compilação Autotools com libocispec, libcrun compartilhada, builds estáticos Nix e verificação GPG; consultado em 2026-10-03.
- [Containers crun Manual Page — crun.1.md (Commands, Cgroup v2 Delegation, CRIU & OCI Annotations)](https://raw.githubusercontent.com/containers/crun/main/crun.1.md) — Página de manual oficial crun.1.md especificando comandos CLI, opções globais de log, delegação em cgroup v2, checkpoint/restore com pre-dump CRIU e anotações run.oci.* (incluindo wasm e krun); consultado em 2026-10-03.
- [Containers crun — Official GitHub Repository](https://github.com/containers/crun) — Repositório oficial do runtime OCI crun na organização containers; consultado em 2026-10-03.
