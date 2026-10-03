---
id: software.seguranca.tranche07.000683
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

# Bubblewrap (`bwrap`): Isolamento de Namespaces (`--unshare-all`, `--unshare-net`, `--unshare-pid`), *Reaping* de Zumbis (**PID 1**) e `--disable-userns`

## Em uma frase
A flag **`--unshare-all`** do `bwrap` ativa simultaneamente o isolamento de todos os namespaces de kernel disponíveis: `--unshare-user-try`, `--unshare-ipc`, `--unshare-pid`, `--unshare-net`, `--unshare-uts` e `--unshare-cgroup-try`.

## Por que importa
Dois desses isolamentos merecem destaque arquitetural: **(1) `--unshare-net`** cria uma pilha de rede completamente desconectada do mundo externo (contendo apenas a interface de loopback `lo` isolada), garantindo que um parser de PDF/imagem ou script de build malicioso **jamais consiga abrir conexões para a internet, para a LAN interna ou para o endpoint de metadados da nuvem (`169.254.169.254`)**; e **(2) `--unshare-pid`** oculta todos os outros processos do host e faz o próprio `bwrap` rodar um **processo `PID 1` mínimo** dentro do sandbox para adotar e recolher (*reap*) processos filhos órfãos/zumbis.

## Como funciona
Além disso, conforme documentado em `bwrap.xml`, a flag **`--disable-userns`** (combinada com `--unshare-user`) impede que o processo dentro do sandbox crie *novos* user namespaces aninhados ou chame `mount`/`pivot_root` novamente para tentar rearranjar sua árvore de diretórios!

## Exemplo
```bash
# Isolar todos os namespaces (incluindo rede offline --unshare-net) e bloquear criacao de userns aninhados (--disable-userns)
bwrap \
  --unshare-all \
  --disable-userns \
  --hostname sandbox-worker \
  --ro-bind /usr /usr \
  --symlink usr/lib /lib \
  --symlink usr/lib64 /lib64 \
  --proc /proc \
  --dev /dev \
  --new-session --die-with-parent \
  /usr/bin/ip addr show
```

## Limites e trade-offs
Se um processo específico dentro do sandbox precisar de acesso à rede mas você ainda quiser todos os demais namespaces isolados, passe **`--unshare-all --share-net`** (como a última flag vence no `bwrap`, `--share-net` reabilita apenas o namespace de rede mantendo `user`, `pid`, `ipc`, `uts` e `cgroup` isolados).

## Como verificar
Verifique na saída do comando acima que a única interface de rede existente dentro do sandbox é `1: lo: <LOOPBACK,UP,LOWER_UP>` e que `ps aux` dentro do sandbox mostra apenas o `PID 1` (`bwrap`) e o `PID 2` (seu comando).

## Conexões
- [[bubblewrap-construcao-filesystem-ro-bind-tmpfs-dev-proc-nodev]] — Veja também: Bubblewrap (`bwrap`): Construção Zero-Trust do Sistema de Arquivos (`--ro-bind`, `--bind`, `--tmpfs`, `--proc`, `--dev`, `--dir` e `--file`).
- [[bubblewrap-isolamento-terminal-new-session-tiocsti-die-with-parent]] — Veja também: Bubblewrap (`bwrap`): Proteção contra Injeção de Comandos no Terminal (**`CVE-2017-5226` / `TIOCSTI`** via **`--new-session`**) e **`--die-with-parent`**.
- [[bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces]] — Referência cruzada direta com bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces.
- [[bubblewrap-filtros-syscalls-seccomp-bpf-file-descriptors-cap-drop]] — Referência cruzada direta com bubblewrap-filtros-syscalls-seccomp-bpf-file-descriptors-cap-drop.

## Fontes
- [Bubblewrap Official GitHub — Unprivileged Sandboxing Architecture & Security Limitations](https://raw.githubusercontent.com/containers/bubblewrap/main/README.md) — documentação oficial do Bubblewrap cobrindo User Namespaces, PR_SET_NO_NEW_PRIVS, tmpfs raiz, CVE-2017-5226 (TIOCSTI) e isolamento de D-Bus; consultado em 2026-10-03.
- [Bubblewrap Official Reference Manual — bwrap(1) DocBook Specification](https://raw.githubusercontent.com/containers/bubblewrap/main/bwrap.xml) — manual oficial bwrap(1) cobrindo --unshare-all, --disable-userns, --ro-bind, --seccomp, --clearenv, --new-session, --die-with-parent e --json-status-fd; consultado em 2026-10-03.
- [Containers Bubblewrap Official Repository](https://github.com/containers/bubblewrap) — repositório oficial da ferramenta de sandboxing Bubblewrap; consultado em 2026-10-03.
