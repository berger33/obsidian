---
id: software.seguranca.tranche07.000687
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

# Bubblewrap (`bwrap`): Prevenção de Escape de Sandbox via Sockets do Host (**D-Bus**, **X11**, Docker Socket, `ssh-agent`) e Uso do **`xdg-dbus-proxy`**

## Em uma frase
Como enfatiza a seção *Limitations* do `README.md` oficial do Bubblewrap: *"Everything mounted into the sandbox can potentially be used to escalate privileges. For example, if you bind a D-Bus socket into the sandbox, it can be used to execute commands via systemd."*

## Por que importa
**Jamais monte diretamente dentro de um sandbox `bwrap` o socket do barramento de sessão D-Bus (`/run/user/$UID/bus`), o socket do sistema D-Bus (`/run/dbus/system_bus_socket`), o socket do X11 (`/tmp/.X11-unix/X0`), o `SSH_AUTH_SOCK` ou `/var/run/docker.sock`**!

## Como funciona
Qualquer processo com acesso irrestrito ao D-Bus de sessão pode invocar `org.freedesktop.systemd1.Manager.StartTransientUnit` (executando qualquer comando fora do sandbox!) ou ler senhas do `org.freedesktop.secrets`; e qualquer processo com acesso ao socket **X11** pode capturar todas as teclas digitadas em todas as janelas da área de trabalho (`xinput`) ou injetar eventos de teclado em um terminal aberto fora do sandbox. Se um aplicativo desktop confinado precisar de D-Bus ou interface gráfica, use **Wayland** (que isola janelas por cliente) e filtre o D-Bus com o daemon **`xdg-dbus-proxy`** (`flatpak/xdg-dbus-proxy`).

## Exemplo
```bash
# Verificar de dentro de um sandbox que nem o socket D-Bus nem o socket X11 do host estao acessiveis
bwrap \
  --unshare-all --clearenv \
  --setenv PATH "/usr/bin:/bin" \
  --ro-bind /usr /usr --symlink usr/bin /bin --symlink usr/lib64 /lib64 \
  --proc /proc --dev /dev --tmpfs /tmp --tmpfs /run \
  --new-session --die-with-parent \
  /usr/bin/ls -la /run /tmp
```

## Limites e trade-offs
Ao confinar ferramentas de linha de comando ou agentes de IA/automação locais no computador do desenvolvedor, nunca monte `~/.ssh`, `~/.aws`, `~/.kube`, `~/.gnupg` ou `~/.config` sem filtro: monte apenas a pasta do repositório de projeto específico onde o agente deve trabalhar.

## Como verificar
Audite scripts de wrapper `bwrap` procurando por `--bind /run/user` ou `--bind /tmp/.X11-unix` e substitua-os por isolamento total ou `xdg-dbus-proxy`.

## Conexões
- [[bubblewrap-higienizacao-variaveis-ambiente-clearenv-setenv-unsetenv]] — Veja também: Bubblewrap (`bwrap`): Higienização de Variáveis de Ambiente (`--clearenv`, `--setenv`, `--unsetenv`), `--chdir` e Controle de `argv[0]`.
- [[bubblewrap-monitoramento-ciclo-vida-info-fd-json-status-fd-block-fd]] — Veja também: Bubblewrap (`bwrap`): Sincronização e Observabilidade Programática (`--info-fd`, `--json-status-fd`, `--block-fd`, `--sync-fd` e `--args FD`).
- [[bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces]] — Referência cruzada direta com bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces.
- [[bubblewrap-construcao-filesystem-ro-bind-tmpfs-dev-proc-nodev]] — Referência cruzada direta com bubblewrap-construcao-filesystem-ro-bind-tmpfs-dev-proc-nodev.

## Fontes
- [Bubblewrap Official GitHub — Unprivileged Sandboxing Architecture & Security Limitations](https://raw.githubusercontent.com/containers/bubblewrap/main/README.md) — documentação oficial do Bubblewrap cobrindo User Namespaces, PR_SET_NO_NEW_PRIVS, tmpfs raiz, CVE-2017-5226 (TIOCSTI) e isolamento de D-Bus; consultado em 2026-10-03.
- [Bubblewrap Official Reference Manual — bwrap(1) DocBook Specification](https://raw.githubusercontent.com/containers/bubblewrap/main/bwrap.xml) — manual oficial bwrap(1) cobrindo --unshare-all, --disable-userns, --ro-bind, --seccomp, --clearenv, --new-session, --die-with-parent e --json-status-fd; consultado em 2026-10-03.
- [Containers Bubblewrap Official Repository](https://github.com/containers/bubblewrap) — repositório oficial da ferramenta de sandboxing Bubblewrap; consultado em 2026-10-03.
