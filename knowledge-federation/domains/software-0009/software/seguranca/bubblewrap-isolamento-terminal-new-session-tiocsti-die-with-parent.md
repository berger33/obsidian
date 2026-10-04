---
id: software.seguranca.tranche07.000684
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

# Bubblewrap (`bwrap`): Proteção contra Injeção de Comandos no Terminal (**`CVE-2017-5226` / `TIOCSTI`** via **`--new-session`**) e **`--die-with-parent`**

## Em uma frase
A seção *Limitations* do `README.md` oficial do Bubblewrap destaca uma vulnerabilidade crítica que ocorre quando se executa um processo não-confiável a partir de um terminal interativo sem isolar a sessão de controle do terminal: a injeção **`ioctl(fd, TIOCSTI, &char)` (`CVE-2017-5226`)**.

## Por que importa
Em sistemas Linux onde o `ioctl` `TIOCSTI` (*Terminal I/O Control Simulate Terminal Input*) ainda é permitido, se um processo dentro do sandbox herdar o descritor de arquivo do terminal controlador da sua sessão shell externa, ele pode chamar `ioctl(0, TIOCSTI, "rm -rf ~\n")`: esses caracteres são empurrados para a fila de entrada do terminal do host e serão executados pelo seu shell assim que o `bwrap` terminar!

## Como funciona
Para bloquear completamente o `CVE-2017-5226`, passe **sempre** a flag **`--new-session`** (que chama `setsid(2)` desvinculando o processo do terminal controlador da sessão pai) e combine-a com **`--die-with-parent`** (que usa `prctl(PR_SET_PDEATHSIG, SIGKILL)` no kernel para matar instantaneamente todos os processos do sandbox caso o processo pai que chamou o `bwrap` morra).

## Exemplo
```bash
# Padrao obrigatorio para execucao segura: --new-session (contra TIOCSTI CVE-2017-5226) + --die-with-parent
bwrap \
  --unshare-all \
  --ro-bind /usr /usr \
  --symlink usr/lib /lib \
  --symlink usr/lib64 /lib64 \
  --proc /proc --dev /dev \
  --new-session \
  --die-with-parent \
  /usr/bin/python3 -c "import fcntl, termios; fcntl.ioctl(0, termios.TIOCSTI, b'id\n')"
```

## Limites e trade-offs
Ao usar `--new-session`, o controle de trabalho do shell (`Ctrl+Z` / `SIGTSTP`) não é encaminhado pelo terminal controlador; em alternativa (ou em adição), filtre o syscall `ioctl` com argumento `TIOCSTI` usando um filtro **Seccomp BPF (`--seccomp FD`)** (e em kernels Linux 6.2+, configure `sysctl dev.tty.legacy_tiocsti=0`).

## Como verificar
Execute o teste acima e confirme que a chamada `fcntl.ioctl(0, termios.TIOCSTI, ...)` falha imediatamente com `PermissionError: [Errno 1] Operation not permitted` (`EPERM`).

## Conexões
- [[bubblewrap-isolamento-namespaces-unshare-all-pid1-rede-loopback]] — Veja também: Bubblewrap (`bwrap`): Isolamento de Namespaces (`--unshare-all`, `--unshare-net`, `--unshare-pid`), *Reaping* de Zumbis (**PID 1**) e `--disable-userns`.
- [[bubblewrap-filtros-syscalls-seccomp-bpf-file-descriptors-cap-drop]] — Veja também: Bubblewrap (`bwrap`): Restrição de Syscalls do Kernel via **`--seccomp FD`** (`--add-seccomp-fd`) e Remoção de Capabilities (`--cap-drop ALL`).
- [[bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces]] — Referência cruzada direta com bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces.
- [[sudo-higienizacao-ambiente-env-reset-secure-path-use-pty-timestamp]] — Referência cruzada direta com sudo-higienizacao-ambiente-env-reset-secure-path-use-pty-timestamp.

## Fontes
- [Bubblewrap Official GitHub — Unprivileged Sandboxing Architecture & Security Limitations](https://raw.githubusercontent.com/containers/bubblewrap/main/README.md) — documentação oficial do Bubblewrap cobrindo User Namespaces, PR_SET_NO_NEW_PRIVS, tmpfs raiz, CVE-2017-5226 (TIOCSTI) e isolamento de D-Bus; consultado em 2026-10-03.
- [Bubblewrap Official Reference Manual — bwrap(1) DocBook Specification](https://raw.githubusercontent.com/containers/bubblewrap/main/bwrap.xml) — manual oficial bwrap(1) cobrindo --unshare-all, --disable-userns, --ro-bind, --seccomp, --clearenv, --new-session, --die-with-parent e --json-status-fd; consultado em 2026-10-03.
- [Containers Bubblewrap Official Repository](https://github.com/containers/bubblewrap) — repositório oficial da ferramenta de sandboxing Bubblewrap; consultado em 2026-10-03.
