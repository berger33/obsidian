---
id: software.seguranca.tranche07.000686
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

# Bubblewrap (`bwrap`): Higienização de Variáveis de Ambiente (`--clearenv`, `--setenv`, `--unsetenv`), `--chdir` e Controle de `argv[0]`

## Em uma frase
Por padrão, um processo iniciado pelo `bwrap` herda todas as variáveis de ambiente do processo pai no host — o que pode vazar tokens de sessão da nuvem (`AWS_SECRET_ACCESS_KEY`, `GITHUB_TOKEN`, `KUBECONFIG`, `SSH_AUTH_SOCK`, `DBUS_SESSION_BUS_ADDRESS`) para dentro do código não-confiável; a flag **`--clearenv`** zera 100% do ambiente herdado!

## Por que importa
Após limpar todas as variáveis com `--clearenv`, você define explicitamente apenas as variáveis estritamente necessárias com **`--setenv VAR VALOR`** (ex.: `--setenv PATH /usr/bin:/bin`, `--setenv HOME /tmp`, `--setenv LANG C.UTF-8`).

## Como funciona
A ordem das flags na linha de comando do `bwrap` importa: sempre coloque **`--clearenv` antes** das flags `--setenv`, pois o `bwrap` processa as alterações de ambiente sequencialmente da esquerda para a direita.

## Exemplo
```bash
# Limpar todas as variaveis de ambiente do host (--clearenv) para evitar vazamento de tokens AWS/GitHub/SSH para o sandbox
bwrap \
  --unshare-all \
  --clearenv \
  --setenv PATH "/usr/bin:/bin" \
  --setenv HOME "/tmp" \
  --setenv LANG "C.UTF-8" \
  --ro-bind /usr /usr \
  --symlink usr/lib /lib \
  --symlink usr/lib64 /lib64 \
  --proc /proc --dev /dev --tmpfs /tmp \
  --chdir /tmp \
  --new-session --die-with-parent \
  /usr/bin/env
```

## Limites e trade-offs
Mesmo que você não monte o diretório `/run/user/1000` dentro do sandbox, esquecer de usar `--clearenv` expõe os valores literais de variáveis de ambiente contendo chaves de API que estavam exportadas no shell ou no worker que chamou o `bwrap`.

## Como verificar
Execute o comando acima em um terminal onde você tenha exportado `SECRET_TOKEN=teste` e confirme que `/usr/bin/env` dentro do sandbox imprime exclusivamente `PATH`, `HOME` e `LANG`.

## Conexões
- [[bubblewrap-filtros-syscalls-seccomp-bpf-file-descriptors-cap-drop]] — Veja também: Bubblewrap (`bwrap`): Restrição de Syscalls do Kernel via **`--seccomp FD`** (`--add-seccomp-fd`) e Remoção de Capabilities (`--cap-drop ALL`).
- [[bubblewrap-prevencao-escape-sockets-dbus-x11-wayland-xdg-dbus-proxy]] — Veja também: Bubblewrap (`bwrap`): Prevenção de Escape de Sandbox via Sockets do Host (**D-Bus**, **X11**, Docker Socket, `ssh-agent`) e Uso do **`xdg-dbus-proxy`**.
- [[bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces]] — Referência cruzada direta com bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces.
- [[bubblewrap-construcao-filesystem-ro-bind-tmpfs-dev-proc-nodev]] — Referência cruzada direta com bubblewrap-construcao-filesystem-ro-bind-tmpfs-dev-proc-nodev.
- [[sudo-higienizacao-ambiente-env-reset-secure-path-use-pty-timestamp]] — Referência cruzada direta com sudo-higienizacao-ambiente-env-reset-secure-path-use-pty-timestamp.

## Fontes
- [Bubblewrap Official GitHub — Unprivileged Sandboxing Architecture & Security Limitations](https://raw.githubusercontent.com/containers/bubblewrap/main/README.md) — documentação oficial do Bubblewrap cobrindo User Namespaces, PR_SET_NO_NEW_PRIVS, tmpfs raiz, CVE-2017-5226 (TIOCSTI) e isolamento de D-Bus; consultado em 2026-10-03.
- [Bubblewrap Official Reference Manual — bwrap(1) DocBook Specification](https://raw.githubusercontent.com/containers/bubblewrap/main/bwrap.xml) — manual oficial bwrap(1) cobrindo --unshare-all, --disable-userns, --ro-bind, --seccomp, --clearenv, --new-session, --die-with-parent e --json-status-fd; consultado em 2026-10-03.
- [Containers Bubblewrap Official Repository](https://github.com/containers/bubblewrap) — repositório oficial da ferramenta de sandboxing Bubblewrap; consultado em 2026-10-03.
