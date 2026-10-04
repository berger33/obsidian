---
id: software.seguranca.tranche12.001142
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/aide/aide/master/README", "https://aide.github.io/doc/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Anatomia de Regras e Atributos no **`aide.conf`**: Combinando **`sha256+sha512`**, **`acl`**, **`xattrs`**, **`selinux`** e **`e2fsattrs`**

## Em uma frase
No arquivo de configuração **`/etc/aide/aide.conf`** (ou `/etc/aide.conf` no RHEL), você define grupos de verificação customizados combinando atributos atômicos com os operadores `+` (adicionar atributo) e `-` (remover atributo de uma regra base)!

## Por que importa
Os atributos fundamentais de metadados incluem: **`p`** (permissões/modo), **`ftype`** (tipo de arquivo: regular, diretório, symlink, dispositivo), **`i`** (número do inode), **`n`** (número de hard links), **`l`** (alvo de link simbólico), **`u`** (usuário UID), **`g`** (grupo GID), **`s`** (tamanho exato), **`S`** (*check for growing size* — ideal para arquivos de log que só crescem!), **`m`** (`mtime`), **`c`** (`ctime`) e **`I`** (*ignore changed filename* — acompanha o arquivo pelo inode mesmo se renomeado)!

## Como funciona
Nos atributos de segurança avançada do kernel Linux, o AIDE verifica nativamente: **`acl`** (POSIX Access Control Lists `getfacl`), **`selinux`** (contexto SELinux `user:role:type:level`), **`xattrs`** (Extended Attributes — onde residem as **Linux Capabilities `security.capability`**, como `cap_setuid+ep`!) e **`e2fsattrs`** (atributos `ext2/ext3/ext4` manipulados por `chattr`, como imutável `i` ou append-only `a`)!

## Exemplo
```ini
# Definicao de regras de alta seguranca no /etc/aide/aide.conf combinando SHA-256 + SHA-512 + Capabilities (xattrs) + SELinux + ACLs
database_in=file:/var/lib/aide/aide.db.gz
database_out=file:/var/lib/aide/aide.db.new.gz
gzip_dbout=yes

FIPSR = p+ftype+i+l+n+u+g+s+m+c+acl+selinux+xattrs+e2fsattrs+sha256+sha512
LOGGROW = p+ftype+l+u+g+i+n+S+acl+selinux+xattrs+e2fsattrs
DIRONLY = p+ftype+i+n+u+g+acl+selinux+xattrs+e2fsattrs
```

## Limites e trade-offs
Por que incluir obrigatoriamente **`xattrs`** na regra de verificação de `/bin`, `/sbin` e `/usr`? Porque um atacante moderno em Linux frequentemente evita criar binários `SUID root` (facilmente detectados por `find / -perm -4000`) e, em vez disso, injeta a capability **`cap_setuid+ep`** em uma cópia do `/usr/bin/python3` via `setcap` — uma backdoor invisível ao `ls -l` tradicional, mas detectada instantaneamente pelo atributo **`xattrs`** do AIDE!

## Como verificar
Nunca utilize apenas `md5` ou `sha1` em políticas modernas do AIDE: padronize `sha256+sha512` em todas as regras de binários e bibliotecas.

## Conexões
- [[aide-arquitetura-monitoramento-integridade-arquivos-fim-linux]] — Veja também: Arquitetura do **AIDE (`aide/aide` — Advanced Intrusion Detection Environment)**: Monitoramento de Integridade de Arquivos (**FIM**) e Detecção de Rootkits em Linux/Unix.
- [[aide-selecao-arquivos-regex-inclusao-negativa-restrita-macros]] — Veja também: Regras de Seleção e Expressões Regulares PCRE2 no **`aide.conf`**: Seleções Regulares (`/caminho`), Restritas (`=/caminho`), Negativas (`!/caminho`) e Macros.
- [[aide-ciclo-operacional-init-check-update-codigos-retorno]] — Referência cruzada direta com aide-ciclo-operacional-init-check-update-codigos-retorno.

## Fontes
- [AIDE Official Repository README — Advanced Intrusion Detection Environment (v0.19)](https://raw.githubusercontent.com/aide/aide/master/README) — documentação oficial do código-fonte do AIDE cobrindo arquitetura, verificação criptográfica GPG, PCRE2 e bibliotecas `libnettle`/`libgcrypt`; consultado em 2026-10-03.
- [The Official AIDE Manual (`aide.github.io/doc`)](https://aide.github.io/doc/) — manual técnico oficial do AIDE detalhando regras de atributos (`p`, `i`, `n`, `u`, `g`, `s`, `m`, `c`, `S`, `acl`, `selinux`, `xattrs`, `e2fsattrs`, `sha256`, `sha512`), seleções regex e assinatura de banco de dados; consultado em 2026-10-03.
