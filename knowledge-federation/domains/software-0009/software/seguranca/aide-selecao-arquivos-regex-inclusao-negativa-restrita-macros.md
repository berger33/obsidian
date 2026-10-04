---
id: software.seguranca.tranche12.001143
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

# Regras de Seleção e Expressões Regulares PCRE2 no **`aide.conf`**: Seleções Regulares (`/caminho`), Restritas (`=/caminho`), Negativas (`!/caminho`) e Macros

## Em uma frase
Um erro clássico ao escrever regras de seleção no **`aide.conf`** é não compreender como o motor de árvore do AIDE avalia expressões regulares PCRE2 (`libpcre2-8`), causando ou falsos positivos intermináveis em diretórios voláteis (`/proc`, `/sys`, `/run`, `/var/lib/docker`) ou exclusões amplas demais que deixam subdiretórios inteiros desprotegidos!

## Por que importa
O AIDE possui **três prefixos de linha de seleção**: **(1) Seleção Regular (`/caminho REGRA`)** — aplica a regra recursivamente a `/caminho` e a todos os seus arquivos e subdiretórios filhos; **(2) Seleção Negativa (`!/caminho_regex`)** — exclui completamente do banco de dados qualquer arquivo ou diretório que case com a regex PCRE2 (não coloque nome de regra após uma linha `!`); e **(3) Seleção Restrita (`=/caminho REGRA`)** — aplica a regra apenas ao diretório exato sem descer recursivamente em toda a subárvore por padrão!

## Como funciona
Além disso, o `aide.conf` suporta **Macros e Variáveis** (`@@define VAR valor`, `@@{VAR}`, `@@ifdef`, `@@ifhost <hostname>`), permitindo manter um único arquivo `aide.conf` corporativo parametrizado por função de servidor!

## Exemplo
```ini
# Exemplo de selecoes recursivas, restritas (=) e exclusoes negativas (!) com PCRE2 no /etc/aide/aide.conf
@@define BIN_RULE FIPSR

/boot   @@{BIN_RULE}
/bin    @@{BIN_RULE}
/sbin   @@{BIN_RULE}
/lib    @@{BIN_RULE}
/lib64  @@{BIN_RULE}
/usr    @@{BIN_RULE}
/etc    @@{BIN_RULE}

# Excluir pseudo-filesystems do kernel, sockets de runtime e arquivos de estado temporario
!/proc
!/sys
!/dev
!/run
!/var/lib/docker
!/etc/mtab$
```

## Limites e trade-offs
Sempre ancore o final das suas expressões regulares de exclusão com **`$`** quando quiser excluir um arquivo específico (por exemplo, `!/etc/mtab$` em vez de `!/etc/mtab`), pois sem o `$` um invasor poderia criar um diretório malicioso chamado `/etc/mtab_backdoor/` e ele seria ignorado pela regra `!`!

## Como verificar
Use `aide --config-check` (`-D`) sempre que editar o `aide.conf` para validar a sintaxe das regras e expressões PCRE2 antes de regenerar o banco.

## Conexões
- [[aide-regras-atributos-hashes-acl-xattrs-selinux-e2fsattrs-aide-conf]] — Veja também: Anatomia de Regras e Atributos no **`aide.conf`**: Combinando **`sha256+sha512`**, **`acl`**, **`xattrs`**, **`selinux`** e **`e2fsattrs`**.
- [[aide-ciclo-operacional-init-check-update-codigos-retorno]] — Veja também: Ciclo Operacional do AIDE: **`--init`**, **`--check`**, **`--update`**, **`--compare`** e Interpretação dos **Códigos de Retorno (`1` a `7`)** em Scripts.
- [[aide-arquitetura-monitoramento-integridade-arquivos-fim-linux]] — Referência cruzada direta com aide-arquitetura-monitoramento-integridade-arquivos-fim-linux.

## Fontes
- [AIDE Official Repository README — Advanced Intrusion Detection Environment (v0.19)](https://raw.githubusercontent.com/aide/aide/master/README) — documentação oficial do código-fonte do AIDE cobrindo arquitetura, verificação criptográfica GPG, PCRE2 e bibliotecas `libnettle`/`libgcrypt`; consultado em 2026-10-03.
- [The Official AIDE Manual (`aide.github.io/doc`)](https://aide.github.io/doc/) — manual técnico oficial do AIDE detalhando regras de atributos (`p`, `i`, `n`, `u`, `g`, `s`, `m`, `c`, `S`, `acl`, `selinux`, `xattrs`, `e2fsattrs`, `sha256`, `sha512`), seleções regex e assinatura de banco de dados; consultado em 2026-10-03.
