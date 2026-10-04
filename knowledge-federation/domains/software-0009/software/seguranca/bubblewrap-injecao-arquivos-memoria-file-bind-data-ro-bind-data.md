---
id: software.seguranca.tranche07.000689
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

# Bubblewrap (`bwrap`): Injeção Efêmera de Configurações e Segredos em Memória via Descritores de Arquivo (`--ro-bind-data FD DEST`, `--bind-data` e `--perms`)

## Em uma frase
Muitas vezes o processo confinado dentro do sandbox precisa ler um arquivo `/etc/resolv.conf` customizado, um `/etc/passwd` sintético mínimo ou um arquivo de configuração gerado dinamicamente para aquela execução, **sem que o orquestrador queira gravar arquivos temporários no disco físico do host**.

## Por que importa
As opções **`--ro-bind-data <FD> <DEST>`**, **`--bind-data <FD> <DEST>`** e **`--file <FD> <DEST>`** (combinadas com **`--perms <OCTAL>`**, ex.: `--perms 0400`) leem o conteúdo de um descritor de arquivo aberto pelo orquestrador (como um `memfd_create` ou pipe anônimo em memória) e o expõem como um arquivo somente-leitura no caminho `<DEST>` dentro do `tmpfs` do sandbox!

## Como funciona
Assim que o sandbox termina, o `tmpfs` desaparece da memória RAM sem jamais ter tocado o sistema de arquivos do host.

## Exemplo
```bash
# Injetar um /etc/passwd sintetico minimo em somente-leitura (--ro-bind-data) a partir de um file descriptor
exec 4<<< "sandbox:x:1000:1000:Sandbox User:/tmp:/sbin/nologin"
bwrap \
  --unshare-all --uid 1000 --gid 1000 \
  --ro-bind /usr /usr --symlink usr/lib /lib --symlink usr/lib64 /lib64 \
  --proc /proc --dev /dev --tmpfs /tmp --dir /etc \
  --perms 0444 --ro-bind-data 4 /etc/passwd \
  --new-session --die-with-parent \
  /usr/bin/id
exec 4<&-
```

## Limites e trade-offs
A flag **`--perms <OCTAL>`** afeta apenas a próxima operação `--file`, `--bind-data`, `--ro-bind-data` ou `--dir` imediatamente subsequente na linha de comando, voltando ao padrão nas operações seguintes.

## Como verificar
Verifique na saída do comando acima que o binário `/usr/bin/id` resolve `uid=1000(sandbox) gid=1000` lendo o `/etc/passwd` injetado via FD `4`.

## Conexões
- [[bubblewrap-monitoramento-ciclo-vida-info-fd-json-status-fd-block-fd]] — Veja também: Bubblewrap (`bwrap`): Sincronização e Observabilidade Programática (`--info-fd`, `--json-status-fd`, `--block-fd`, `--sync-fd` e `--args FD`).
- [[bubblewrap-confinamento-workers-conversao-arquivos-limites-cgroups-systemd]] — Veja também: Bubblewrap (`bwrap`) + `systemd-run`: Defesa contra Negação de Serviço (Fork Bombs / Exaustão de RAM) com **cgroups v2** e `AppArmor` para `bwrap`.
- [[bubblewrap-construcao-filesystem-ro-bind-tmpfs-dev-proc-nodev]] — Referência cruzada direta com bubblewrap-construcao-filesystem-ro-bind-tmpfs-dev-proc-nodev.

## Fontes
- [Bubblewrap Official GitHub — Unprivileged Sandboxing Architecture & Security Limitations](https://raw.githubusercontent.com/containers/bubblewrap/main/README.md) — documentação oficial do Bubblewrap cobrindo User Namespaces, PR_SET_NO_NEW_PRIVS, tmpfs raiz, CVE-2017-5226 (TIOCSTI) e isolamento de D-Bus; consultado em 2026-10-03.
- [Bubblewrap Official Reference Manual — bwrap(1) DocBook Specification](https://raw.githubusercontent.com/containers/bubblewrap/main/bwrap.xml) — manual oficial bwrap(1) cobrindo --unshare-all, --disable-userns, --ro-bind, --seccomp, --clearenv, --new-session, --die-with-parent e --json-status-fd; consultado em 2026-10-03.
- [Containers Bubblewrap Official Repository](https://github.com/containers/bubblewrap) — repositório oficial da ferramenta de sandboxing Bubblewrap; consultado em 2026-10-03.
