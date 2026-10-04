---
id: software.seguranca.tranche12.001141
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

# Arquitetura do **AIDE (`aide/aide` — Advanced Intrusion Detection Environment)**: Monitoramento de Integridade de Arquivos (**FIM**) e Detecção de Rootkits em Linux/Unix

## Em uma frase
Quando um invasor conquista privilégio `root` em um servidor Linux e instala um **rootkit de userland** — substituindo binários como `/bin/ls`, `/bin/ps`, `/usr/bin/ss`, `/usr/sbin/sshd` ou bibliotecas compartilhadas em `/lib/x86_64-linux-gnu/` para ocultar processos e conexões de rede —, como o administrador ou perito forense comprova quais binários do sistema foram adulterados?

## Por que importa
Escrito em C (GPLv2, mantido por Hannes von Haugwitz) como uma alternativa livre e avançada ao Tripwire clássico, o **AIDE (*Advanced Intrusion Detection Environment*)** é o motor padrão de **File Integrity Monitoring (FIM)** nas principais distribuições Linux corporativas (RHEL, Debian, Ubuntu, SUSE, AlmaLinux, Rocky Linux) e requisito direto de conformidade **PCI-DSS Requisito 11.5**, **CIS Benchmarks**, **NIST SP 800-53 (`SI-7`)** e **DISA STIG**!

## Como funciona
O AIDE constrói um banco de dados criptográfico de referência (`aide.db.gz`) contendo **múltiplos hashes criptográficos simultâneos (`sha256`, `sha512`, `stribog`, `whirlpool`, `gost`)** combinados com metadados completos de cada inode (`permissions`, `ftype`, `inode`, `nlinks`, `uid`, `gid`, `size`, `mtime`, `ctime`, `ACL`, `SELinux context`, `xattrs` e atributos `e2fsattrs`/`chattr`)!

## Exemplo
```bash
# Instalar o AIDE em Debian/Ubuntu ou RHEL, verificar a versao e listar os recursos compilados (libgcrypt/nettle, ACL, xattr, SELinux, e2fsattrs)
aide --version
```

## Limites e trade-offs
Por que o AIDE calcula e armazena **mais de um hash criptográfico e todos os atributos de inode** para cada arquivo monitorado? Porque embora um atacante com `root` possa falsificar facilmente o tamanho do arquivo e o `mtime` (*timestomping* via `touch -r`), alterar o conteúdo de um binário mantendo simultaneamente o mesmo `SHA-256`, `SHA-512` e atributos estendidos é criptograficamente inviável!

## Como verificar
Para máxima segurança contra adulteração pós-comprometimento, copie sempre o banco de dados inicial (`aide.db.gz`) e o binário do AIDE para um armazenamento externo somente-leitura ou servidor central de auditoria.

## Conexões
- [[aide-regras-atributos-hashes-acl-xattrs-selinux-e2fsattrs-aide-conf]] — Veja também: Anatomia de Regras e Atributos no **`aide.conf`**: Combinando **`sha256+sha512`**, **`acl`**, **`xattrs`**, **`selinux`** e **`e2fsattrs`**.
- [[aide-selecao-arquivos-regex-inclusao-negativa-restrita-macros]] — Referência cruzada direta com aide-selecao-arquivos-regex-inclusao-negativa-restrita-macros.
- [[atomicredteam-testes-linux-macos-containers-bash-sh-validacao-edr]] — Referência cruzada direta com atomicredteam-testes-linux-macos-containers-bash-sh-validacao-edr.

## Fontes
- [AIDE Official Repository README — Advanced Intrusion Detection Environment (v0.19)](https://raw.githubusercontent.com/aide/aide/master/README) — documentação oficial do código-fonte do AIDE cobrindo arquitetura, verificação criptográfica GPG, PCRE2 e bibliotecas `libnettle`/`libgcrypt`; consultado em 2026-10-03.
- [The Official AIDE Manual (`aide.github.io/doc`)](https://aide.github.io/doc/) — manual técnico oficial do AIDE detalhando regras de atributos (`p`, `i`, `n`, `u`, `g`, `s`, `m`, `c`, `S`, `acl`, `selinux`, `xattrs`, `e2fsattrs`, `sha256`, `sha512`), seleções regex e assinatura de banco de dados; consultado em 2026-10-03.
