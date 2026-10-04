---
id: software.seguranca.tranche07.000682
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

# Bubblewrap (`bwrap`): Construção Zero-Trust do Sistema de Arquivos (`--ro-bind`, `--bind`, `--tmpfs`, `--proc`, `--dev`, `--dir` e `--file`)

## Em uma frase
Diferente de abordagens de *blocklist* (que herdam o sistema de arquivos inteiro do host e tentam esconder apenas `/etc/shadow` ou `~/.ssh`), o `bwrap` parte de uma raiz `/` **100% vazia**: qualquer diretório do host que você não passar explicitamente em `--ro-bind` ou `--bind` simplesmente não existe dentro do sandbox.

## Por que importa
Para confinar conversores de arquivos perigosos (como Ghostscript, ImageMagick, `ffmpeg`, LibreOffice headless, parsers de PDF ou descompactadores que processam uploads de usuários na web), você monta `/usr`, `/lib` e `/etc/ld.so.cache` em **somente-leitura (`--ro-bind`)**, cria um `/tmp` efêmero em memória (`--tmpfs /tmp`) e monta em escrita (`--bind`) exclusivamente o diretório de trabalho daquele job específico.

## Como funciona
Conforme documentado no `README.md` e em `bwrap.xml`, todas as montagens `--bind` e `--ro-bind` têm a flag **`nodev` aplicada por padrão** (impedindo acesso a nós de dispositivos de bloco/caractere em diretórios normais), enquanto **`--dev /dev`** cria um `/dev` mínimo seguro contendo apenas `/dev/null`, `/dev/zero`, `/dev/full`, `/dev/random`, `/dev/urandom` e `/dev/tty`.

## Exemplo
```bash
# Confinar a conversao de um PDF enviado por usuario externo usando Ghostscript em um filesystem estritamente restrito
bwrap \
  --unshare-all \
  --ro-bind /usr /usr \
  --ro-bind /lib /lib \
  --ro-bind /lib64 /lib64 \
  --ro-bind /etc/ld.so.cache /etc/ld.so.cache \
  --proc /proc \
  --dev /dev \
  --tmpfs /tmp \
  --ro-bind /var/spool/uploads/job_991/input.pdf /tmp/input.pdf \
  --bind /var/spool/uploads/job_991/out /tmp/out \
  --chdir /tmp \
  --new-session --die-with-parent \
  /usr/bin/gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=png16m -sOutputFile=/tmp/out/page-%d.png /tmp/input.pdf
```

## Limites e trade-offs
Nunca use `--dev-bind /dev /dev` (que expõe todos os dispositivos reais do host como `/dev/sda`, `/dev/mem` ou `/dev/dri`) a menos que o processo precise estritamente de aceleração de GPU específica (caso em que se usa `--dev /dev` seguido de `--dev-bind /dev/dri /dev/dri`).

## Como verificar
Teste tentar ler `/etc/passwd` ou `/var/spool/uploads/` fora de `job_991` de dentro do sandbox acima e confirme que os arquivos não existem no namespace de montagem.

## Conexões
- [[bubblewrap-arquitetura-sandboxing-unprivileged-user-namespaces]] — Veja também: Bubblewrap (`bwrap`): Arquitetura de Sandboxing sem Privilégios no Linux, **User Namespaces (`CLONE_NEWUSER`)** e **`PR_SET_NO_NEW_PRIVS`**.
- [[bubblewrap-isolamento-namespaces-unshare-all-pid1-rede-loopback]] — Veja também: Bubblewrap (`bwrap`): Isolamento de Namespaces (`--unshare-all`, `--unshare-net`, `--unshare-pid`), *Reaping* de Zumbis (**PID 1**) e `--disable-userns`.

## Fontes
- [Bubblewrap Official GitHub — Unprivileged Sandboxing Architecture & Security Limitations](https://raw.githubusercontent.com/containers/bubblewrap/main/README.md) — documentação oficial do Bubblewrap cobrindo User Namespaces, PR_SET_NO_NEW_PRIVS, tmpfs raiz, CVE-2017-5226 (TIOCSTI) e isolamento de D-Bus; consultado em 2026-10-03.
- [Bubblewrap Official Reference Manual — bwrap(1) DocBook Specification](https://raw.githubusercontent.com/containers/bubblewrap/main/bwrap.xml) — manual oficial bwrap(1) cobrindo --unshare-all, --disable-userns, --ro-bind, --seccomp, --clearenv, --new-session, --die-with-parent e --json-status-fd; consultado em 2026-10-03.
- [Containers Bubblewrap Official Repository](https://github.com/containers/bubblewrap) — repositório oficial da ferramenta de sandboxing Bubblewrap; consultado em 2026-10-03.
