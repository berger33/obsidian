---
id: software.seguranca.tranche07.000690
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://raw.githubusercontent.com/containers/bubblewrap/main/README.md", "https://raw.githubusercontent.com/containers/bubblewrap/main/bwrap.xml", "https://github.com/containers/bubblewrap"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Bubblewrap (`bwrap`) + `systemd-run`: Defesa contra Negação de Serviço (Fork Bombs / Exaustão de RAM) com **cgroups v2** e `AppArmor` para `bwrap`

## Em uma frase
Como alerta explicitamente a seção *System security* do `README.md` oficial do Bubblewrap: embora o `bwrap` impeça escalação de privilégio, um processo malicioso dentro do sandbox ainda pode tentar realizar ataques de **Negação de Serviço (DoS)** contra o host (como uma *fork bomb*, alocação de toda a memória RAM ou saturação de CPU) se não houver limites de recursos (**cgroups v2**) aplicados.

## Por que importa
Enquanto o `bwrap` cuida do isolamento de namespaces, sistema de arquivos e syscalls, o controle de cotas de recursos físicos (`MemoryMax`, `TasksMax`, `CPUQuota`, `IOWeight`) deve ser aplicado envolvendo a chamada do `bwrap` em um escopo transitório de **cgroups v2** via **`systemd-run --user --scope`** (ou `setrlimit` / slice do serviço).

## Como funciona
Além disso, no Ubuntu 24.04+ e Debian modernos (onde `kernel.apparmor_restrict_unprivileged_userns = 1` restringe a criação de user namespaces não-privilegiados a binários que possuam um perfil AppArmor com a permissão `userns,`), o pacote oficial do `bubblewrap` já inclui o perfil `/etc/apparmor.d/bwrap` autorizando `userns`.

## Exemplo
```bash
# Executar o sandbox Bubblewrap dentro de um escopo cgroups v2 estrito (maximo 256 MiB de RAM e 32 processos/threads)
systemd-run --user --scope \
  -p MemoryMax=256M -p MemorySwapMax=0 \
  -p TasksMax=32 -p CPUQuota=50% \
  bwrap --unshare-all --ro-bind /usr /usr --symlink usr/lib /lib --symlink usr/lib64 /lib64 \
    --proc /proc --dev /dev --tmpfs /tmp --new-session --die-with-parent \
    /usr/bin/sha256sum /usr/bin/bwrap
```

## Limites e trade-offs
Sempre defina **`TasksMax=32`** (ou outro teto baixo compatível com o worker) e **`MemorySwapMax=0`** no escopo cgroups v2 que envolve o `bwrap` ao processar entradas de usuários externos: isso neutraliza instantaneamente qualquer *fork bomb* ou bomba de descompressão (*zip/pdf bomb*) sem afetar o restante do servidor.

## Como verificar
Verifique com `systemctl --user status` durante a execução que o escopo transitório aplica os limites `Tasks:` e `Memory:` do cgroup v2.

## Conexões
- [[bubblewrap-injecao-arquivos-memoria-file-bind-data-ro-bind-data]] — Veja também: Bubblewrap (`bwrap`): Injeção Efêmera de Configurações e Segredos em Memória via Descritores de Arquivo (`--ro-bind-data FD DEST`, `--bind-data` e `--perms`).
- [[bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces]] — Referência cruzada direta com bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces.
- [[bubblewrap-filtros-syscalls-seccomp-bpf-file-descriptors-cap-drop]] — Referência cruzada direta com bubblewrap-filtros-syscalls-seccomp-bpf-file-descriptors-cap-drop.

## Fontes
- [Bubblewrap Official GitHub — Unprivileged Sandboxing Architecture & Security Limitations](https://raw.githubusercontent.com/containers/bubblewrap/main/README.md) — documentação oficial do Bubblewrap cobrindo User Namespaces, PR_SET_NO_NEW_PRIVS, tmpfs raiz, CVE-2017-5226 (TIOCSTI) e isolamento de D-Bus; consultado em 2026-10-03.
- [Bubblewrap Official Reference Manual — bwrap(1) DocBook Specification](https://raw.githubusercontent.com/containers/bubblewrap/main/bwrap.xml) — manual oficial bwrap(1) cobrindo --unshare-all, --disable-userns, --ro-bind, --seccomp, --clearenv, --new-session, --die-with-parent e --json-status-fd; consultado em 2026-10-03.
- [Containers Bubblewrap Official Repository](https://github.com/containers/bubblewrap) — repositório oficial da ferramenta de sandboxing Bubblewrap; consultado em 2026-10-03.
