---
id: software.seguranca.tranche07.000688
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

# Bubblewrap (`bwrap`): Sincronização e Observabilidade Programática (`--info-fd`, `--json-status-fd`, `--block-fd`, `--sync-fd` e `--args FD`)

## Em uma frase
Quando o `bwrap` é integrado dentro de um serviço maior (como um executor de jobs de CI, um motor de avaliação de código ou o próprio Flatpak), o orquestrador precisa saber o `PID` real do sandbox no host, sincronizar a configuração de rede/cgroups antes do processo iniciar e receber o código de saída exato em JSON.

## Por que importa
As flags de descritores de arquivo de controle do `bwrap` (`bwrap.xml`) resolvem isso sem condições de corrida: **`--info-fd <FD>`** e **`--json-status-fd <FD>`** escrevem um documento JSON contendo o `child-pid` (e ao final o `exit-code`), **`--block-fd <FD>`** faz o `bwrap` pausar após criar os namespaces mas antes de iniciar o comando até que o orquestrador feche o FD, e **`--args <FD>`** lê argumentos separados por byte nulo (`\0`) de um descritor de arquivo.

## Como funciona
Usar **`--args <FD>`** evita expor linhas de comando gigantescas com centenas de `--ro-bind` na tabela pública de processos (`ps aux` / `/proc/<pid>/cmdline`) do host.

## Exemplo
```python
import json, os, subprocess

# Ler o PID real e o exit-code final do processo confinado via --json-status-fd em Python
r_fd, w_fd = os.pipe()
proc = subprocess.Popen(
    [
        "bwrap", "--unshare-all", "--ro-bind", "/usr", "/usr",
        "--symlink", "usr/lib", "/lib", "--symlink", "usr/lib64", "/lib64",
        "--proc", "/proc", "--dev", "/dev", "--new-session", "--die-with-parent",
        "--json-status-fd", str(w_fd), "/usr/bin/true"
    ],
    pass_fds=(w_fd,)
)
os.close(w_fd)
with os.fdopen(r_fd) as f:
    for line in f:
        print("Evento JSON bwrap:", json.loads(line))
proc.wait()
```

## Limites e trade-offs
Sempre feche a ponta de escrita do pipe (`os.close(w_fd)`) no processo pai imediatamente após o `subprocess.Popen(..., pass_fds=(w_fd,))`, para que a leitura em `r_fd` detecte `EOF` assim que o `bwrap` encerrar.

## Como verificar
Execute o script Python acima e confirme o recebimento dos dois objetos JSON: o primeiro com `{"child-pid": ...}` e o segundo com `{"exit-code": 0}`.

## Conexões
- [[bubblewrap-prevencao-escape-sockets-dbus-x11-wayland-xdg-dbus-proxy]] — Veja também: Bubblewrap (`bwrap`): Prevenção de Escape de Sandbox via Sockets do Host (**D-Bus**, **X11**, Docker Socket, `ssh-agent`) e Uso do **`xdg-dbus-proxy`**.
- [[bubblewrap-injecao-arquivos-memoria-file-bind-data-ro-bind-data]] — Veja também: Bubblewrap (`bwrap`): Injeção Efêmera de Configurações e Segredos em Memória via Descritores de Arquivo (`--ro-bind-data FD DEST`, `--bind-data` e `--perms`).
- [[bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces]] — Referência cruzada direta com bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces.
- [[bubblewrap-isolamento-namespaces-unshare-all-pid1-rede-loopback]] — Referência cruzada direta com bubblewrap-isolamento-namespaces-unshare-all-pid1-rede-loopback.
- [[bubblewrap-confinamento-workers-conversao-arquivos-limites-cgroups-systemd]] — Referência cruzada direta com bubblewrap-confinamento-workers-conversao-arquivos-limites-cgroups-systemd.

## Fontes
- [Bubblewrap Official GitHub — Unprivileged Sandboxing Architecture & Security Limitations](https://raw.githubusercontent.com/containers/bubblewrap/main/README.md) — documentação oficial do Bubblewrap cobrindo User Namespaces, PR_SET_NO_NEW_PRIVS, tmpfs raiz, CVE-2017-5226 (TIOCSTI) e isolamento de D-Bus; consultado em 2026-10-03.
- [Bubblewrap Official Reference Manual — bwrap(1) DocBook Specification](https://raw.githubusercontent.com/containers/bubblewrap/main/bwrap.xml) — manual oficial bwrap(1) cobrindo --unshare-all, --disable-userns, --ro-bind, --seccomp, --clearenv, --new-session, --die-with-parent e --json-status-fd; consultado em 2026-10-03.
- [Containers Bubblewrap Official Repository](https://github.com/containers/bubblewrap) — repositório oficial da ferramenta de sandboxing Bubblewrap; consultado em 2026-10-03.
