---
id: software.seguranca.tranche13.001273
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/netblue30/firejail/master/README.md", "https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Isolamento Efêmero de Sistema de Arquivos no Firejail: **`--private`**, **`--private-dev`**, **`--private-etc`**, **`--private-bin`** e **`--private-tmp`**

## Em uma frase
Imagine que você precisa abrir um arquivo suspeito, testar uma ferramenta baixada da internet ou acessar um site desconhecido em um navegador totalmente descartável que **não enxergue absolutamente nenhum arquivo da sua pasta `/home`** e que **destrua 100% dos artefatos gravados na memória RAM no segundo em que você fechar a janela**.

## Por que importa
Sem isolamento de sistema de arquivos, qualquer processo executado pelo usuário pode enumerar documentos confidenciais e persistir backdoors em `~/.config` ou `~/.bashrc`.

## Como funciona
Para isso, o Firejail oferece a família de diretivas **`private`**, baseadas em montagens `tmpfs` (em memória RAM) e `bind mounts` dentro de um Mount Namespace isolado: **(1) `--private`** — monta um diretório `/home/usuario` e `/root` completamente novos e vazios em memória RAM (`tmpfs`), descartando tudo quando a sandbox termina (ou `--private=/caminho/pasta_dedicada` se quiser persistir apenas em uma pasta isolada!); **(2) `--private-tmp`** — monta um `/tmp` e `/var/tmp` exclusivos em `tmpfs`; **(3) `--private-dev`** — cria um `/dev` mínimo contendo apenas dispositivos seguros (`null`, `zero`, `full`, `random`, `urandom`, `tty`, `dri` GPU), ocultando discos brutos (`/dev/sda`, `/dev/nvme0n1`), webcam (`/dev/video0`) e USBs!; **(4) `--private-bin=lista`** — monta em `/bin` e `/usr/bin` **apenas os binários explicitamente listados** (removendo `sh`, `bash`, `curl`, `python`, `nc` para impedir que um exploit de RCE consiga invocar um shell!); e **(5) `--private-etc=lista`**!

## Exemplo
```bash
# Iniciar uma sessao descartavel do navegador Firefox com /home, /tmp e /dev 100% isolados em memoria RAM (tmpfs) e sem acesso a webcam
firejail --private --private-dev --private-tmp --novideo firefox --no-remote
```

## Limites e trade-offs
Olhe o poder da flag **`--private-bin`**: se você confinar um leitor de PDF (`evince`) com `private-bin evince`, mesmo que um invasor explore uma vulnerabilidade crítica de corrupção de memória no leitor de PDF e tente executar `system("/bin/sh -c 'curl ...'")`, a chamada falhará imediatamente com `ENOENT (No such file or directory)` porque **`/bin/sh` e `/usr/bin/curl` simplesmente não existem dentro do sistema de arquivos daquela sandbox**!

## Como verificar
Adicione **`--novideo`** (bloqueia webcam `/dev/video*`), **`--nosound`** (bloqueia microfone/áudio) e **`--no3d`** (desativa aceleração OpenGL/Vulkan se quiser reduzir a superfície de ataque de drivers de GPU) ao analisar artefatos não confiáveis.

## Conexões
- [[firejail-anatomia-perfis-profile-blacklist-whitelist-read-only-include]] — Veja também: Anatomia dos Perfis **`.profile`** e Customizações **`.local`** no Firejail: `blacklist`, `whitelist`, `read-only`, `noexec` e Herança `include`.
- [[firejail-filtragem-syscalls-seccomp-caps-drop-all-nonewprivs]] — Veja também: Redução de Superfície de Ataque do Kernel no Firejail: **`--seccomp`**, **`--caps.drop=all`**, **`--nonewprivs`** e **`--noroot` (User Namespace)**.
- [[firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities]] — Referência cruzada direta com firejail-arquitetura-sandbox-suid-namespaces-seccomp-capabilities.

## Fontes
- [Firejail Security Sandbox Official GitHub (`netblue30/firejail`)](https://raw.githubusercontent.com/netblue30/firejail/master/README.md) — repositório oficial do Firejail cobrindo arquitetura de isolamento por namespaces do Kernel Linux, `seccomp-bpf`, capabilities, cgroups e mais de 1.000 perfis `.profile`; consultado em 2026-10-03.
- [Firejail Official System Configuration Reference (`etc/firejail.config`)](https://raw.githubusercontent.com/netblue30/firejail/master/etc/firejail.config) — configuração oficial de políticas de hardening global do Firejail (`force-nonewprivs`, `disable-mnt`, `restricted-network`, `seccomp-error-action`, `x11`, `dbus`, `apparmor`); consultado em 2026-10-03.
