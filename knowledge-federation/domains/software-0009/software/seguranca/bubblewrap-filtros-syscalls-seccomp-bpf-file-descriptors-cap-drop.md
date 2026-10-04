---
id: software.seguranca.tranche07.000685
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

# Bubblewrap (`bwrap`): Restrição de Syscalls do Kernel via **`--seccomp FD`** (`--add-seccomp-fd`) e Remoção de Capabilities (`--cap-drop ALL`)

## Em uma frase
Como todos os processos dentro de um sandbox ainda compartilham o mesmo kernel Linux do host, reduzir a superfície de chamadas de sistema (syscalls) expostas ao processo confinado é essencial; o `bwrap` aplica programas **Seccomp-BPF** compilados através das flags **`--seccomp <FD>`** e **`--add-seccomp-fd <FD>`**, além de gerenciar *Linux Capabilities* no user namespace com **`--cap-drop ALL`** / `--cap-add`.

## Por que importa
Syscalls exóticos ou legados do kernel Linux (como `keyctl`, `add_key`, `request_key`, `ptrace`, `userfaultfd`, `perf_event_open`, `bpf`, `io_uring_setup`, `kexec_load`, `acct`, `lookup_dcookie`) são historicamente responsáveis pela maioria das vulnerabilidades de escalação de privilégio de kernel.

## Como funciona
O programa pai compila a política Seccomp (usando `libseccomp` em C, Python `seccomp` ou gerando o bytecode BPF com `bpfc` / `flatpak`), abre um descritor de arquivo contendo o bytecode BPF e passa o número do descritor para `bwrap --seccomp 3 3< filtro.bpf`, que o carrega no kernel imediatamente antes do `execve` final.

## Exemplo
```python
# Gerar um filtro Seccomp-BPF binario com libseccomp bloqueando syscalls perigosos para uso com bwrap --seccomp
import subprocess, os

# Exemplo: invocar bwrap garantindo queda de todas as capabilities no namespace (--cap-drop ALL)
cmd = [
    "bwrap", "--unshare-all", "--cap-drop", "ALL",
    "--ro-bind", "/usr", "/usr", "--symlink", "usr/lib", "/lib",
    "--symlink", "usr/lib64", "/lib64", "--proc", "/proc", "--dev", "/dev",
    "--new-session", "--die-with-parent", "/usr/bin/id"
]
subprocess.run(cmd, check=True)
```

## Limites e trade-offs
Conforme alerta o `README.md` oficial do Bubblewrap, se o aplicativo confinado dentro do `bwrap` for um navegador web (como Chromium ou Firefox) que cria seus próprios sub-sandboxes internos via `seccomp`, o seu filtro `--seccomp` externo não deve bloquear a própria syscall `seccomp` / `prctl`, para permitir que o navegador aplique camadas ainda mais restritivas aos seus processos de renderização.

## Como verificar
Verifique em `/proc/<PID>/status` do processo dentro do sandbox os campos `Seccomp: 2` (modo filtro BPF ativo) e `CapEff: 0000000000000000`.

## Conexões
- [[bubblewrap-isolamento-terminal-new-session-tiocsti-die-with-parent]] — Veja também: Bubblewrap (`bwrap`): Proteção contra Injeção de Comandos no Terminal (**`CVE-2017-5226` / `TIOCSTI`** via **`--new-session`**) e **`--die-with-parent`**.
- [[bubblewrap-higienizacao-variaveis-ambiente-clearenv-setenv-unsetenv]] — Veja também: Bubblewrap (`bwrap`): Higienização de Variáveis de Ambiente (`--clearenv`, `--setenv`, `--unsetenv`), `--chdir` e Controle de `argv[0]`.
- [[bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces]] — Referência cruzada direta com bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces.

## Fontes
- [Bubblewrap Official GitHub — Unprivileged Sandboxing Architecture & Security Limitations](https://raw.githubusercontent.com/containers/bubblewrap/main/README.md) — documentação oficial do Bubblewrap cobrindo User Namespaces, PR_SET_NO_NEW_PRIVS, tmpfs raiz, CVE-2017-5226 (TIOCSTI) e isolamento de D-Bus; consultado em 2026-10-03.
- [Bubblewrap Official Reference Manual — bwrap(1) DocBook Specification](https://raw.githubusercontent.com/containers/bubblewrap/main/bwrap.xml) — manual oficial bwrap(1) cobrindo --unshare-all, --disable-userns, --ro-bind, --seccomp, --clearenv, --new-session, --die-with-parent e --json-status-fd; consultado em 2026-10-03.
- [Containers Bubblewrap Official Repository](https://github.com/containers/bubblewrap) — repositório oficial da ferramenta de sandboxing Bubblewrap; consultado em 2026-10-03.
