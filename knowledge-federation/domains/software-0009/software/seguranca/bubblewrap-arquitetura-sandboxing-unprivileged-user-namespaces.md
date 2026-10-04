---
id: software.seguranca.tranche07.000681
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

# Bubblewrap (`bwrap`): Arquitetura de Sandboxing sem Privilégios no Linux, **User Namespaces (`CLONE_NEWUSER`)** e **`PR_SET_NO_NEW_PRIVS`**

## Em uma frase
**Bubblewrap (`bwrap`)** (`containers/bubblewrap`, LGPLv2+, usado como motor de isolamento do Flatpak, `rpm-ostree` e `libgnome-desktop`) é o utilitário de baixo nível para construção de sandboxes de processos no Linux projetado para ser executado por **usuários comuns sem privilégios**.

## Por que importa
Conforme destaca o `README.md` oficial do Bubblewrap, runtimes de infraestrutura como o Docker tradicional não podem ser delegados diretamente a usuários não-confiáveis porque permitem escalar para `root` no host; já o `bwrap` utiliza **User Namespaces não-privilegiados (`CLONE_NEWUSER`)** e ativa obrigatoriamente o bit **`PR_SET_NO_NEW_PRIVS`** no kernel.

## Como funciona
Ao iniciar, o `bwrap` cria um novo **Mount Namespace (`CLONE_NEWNS`)** cuja raiz (`/`) é um sistema de arquivos **`tmpfs` completamente vazio e invisível a partir do host**, que é destruído automaticamente pelo kernel assim que o último processo do sandbox termina; cabe aos argumentos da linha de comando do `bwrap` montar explicitamente apenas os diretórios necessários.

## Exemplo
```bash
# Executar um comando dentro de um sandbox Bubblewrap com todos os namespaces isolados e /usr montado somente-leitura
bwrap \
  --unshare-all \
  --ro-bind /usr /usr \
  --symlink usr/lib /lib \
  --symlink usr/lib64 /lib64 \
  --symlink usr/bin /bin \
  --proc /proc \
  --dev /dev \
  --tmpfs /tmp \
  --new-session \
  --die-with-parent \
  /usr/bin/id
```

## Limites e trade-offs
O `bwrap` moderno removeu o modo `setuid` legado e exige `PR_SET_NO_NEW_PRIVS`, garantindo que nenhum binário `setuid` dentro do sandbox possa conceder privilégios adicionais no host.

## Como verificar
Execute o comando acima como usuário comum e verifique que `ls /home` dentro do sandbox não existe (pois `/home` nunca foi montado no `tmpfs` raiz).

## Conexões
- [[bubblewrap-construcao-filesystem-ro-bind-tmpfs-dev-proc-nodev]] — Veja também: Bubblewrap (`bwrap`): Construção Zero-Trust do Sistema de Arquivos (`--ro-bind`, `--bind`, `--tmpfs`, `--proc`, `--dev`, `--dir` e `--file`).
- [[bubblewrap-isolamento-namespaces-unshare-all-pid1-rede-loopback]] — Referência cruzada direta com bubblewrap-isolamento-namespaces-unshare-all-pid1-rede-loopback.
- [[sudo-auditoria-superficie-ataque-cve-2021-3156-cve-2023-22809-alternativas]] — Referência cruzada direta com sudo-auditoria-superficie-ataque-cve-2021-3156-cve-2023-22809-alternativas.

## Fontes
- [Bubblewrap Official GitHub — Unprivileged Sandboxing Architecture & Security Limitations](https://raw.githubusercontent.com/containers/bubblewrap/main/README.md) — documentação oficial do Bubblewrap cobrindo User Namespaces, PR_SET_NO_NEW_PRIVS, tmpfs raiz, CVE-2017-5226 (TIOCSTI) e isolamento de D-Bus; consultado em 2026-10-03.
- [Bubblewrap Official Reference Manual — bwrap(1) DocBook Specification](https://raw.githubusercontent.com/containers/bubblewrap/main/bwrap.xml) — manual oficial bwrap(1) cobrindo --unshare-all, --disable-userns, --ro-bind, --seccomp, --clearenv, --new-session, --die-with-parent e --json-status-fd; consultado em 2026-10-03.
- [Containers Bubblewrap Official Repository](https://github.com/containers/bubblewrap) — repositório oficial da ferramenta de sandboxing Bubblewrap; consultado em 2026-10-03.
