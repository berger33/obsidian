---
id: software.seguranca.tranche12.001150
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

# Caça a Backdoors e Persistência Linux com o AIDE: Detectando Adulteração em **`/etc/ld.so.preload`**, Módulos **PAM (`/lib/security/`)**, `sshd` e `systemd`

## Em uma frase
Quais são os alvos favoritos de persistência furtiva em servidores Linux que passam despercebidos por uma inspeção superficial de processos, mas que o **AIDE** denuncia com precisão cirúrgica no segundo em que são tocados?

## Por que importa
Primeiro, **`/etc/ld.so.preload`** e **`/etc/ld.so.conf.d/`**: rootkits de userland (como *Symbiote*, *BPFDoor* loaders ou *Azazel/Jynx*) injetam uma biblioteca `.so` maliciosa em `/etc/ld.so.preload` para sequestrar chamadas `libc` (`readdir`, `fopen`, `accept`) de todos os binários dinâmicos do sistema; segundo, **Módulos PAM (`/lib/x86_64-linux-gnu/security/pam_unix.so`)**: um invasor substitui o `pam_unix.so` por uma versão trojanizada que aceita uma "senha mestra" secreta para qualquer usuário e grava senhas legítimas digitadas no SSH; e terceiro, **Units do `systemd` (`/lib/systemd/system/` e `/etc/systemd/system/`)** e **Hooks do `apt`/`dpkg` (`/etc/apt/apt.conf.d/`)**!

## Como funciona
Quando o AIDE verifica esses diretórios (especialmente a partir de uma imagem limpa ou com `root_prefix` em um snapshot), ele exibe linha por linha os atributos exatos que divergiram (`f < ... : /lib/x86_64-linux-gnu/security/pam_unix.so`, mostrando o `Size`, `Mtime`, `Ctime` e `SHA256` antigo versus novo)!

## Exemplo
```bash
# Inspecionar no relatorio do AIDE qualquer adicao (+) ou modificacao (f) em bibliotecas PAM, ld.so.preload, systemd ou binarios SSH
sudo aide -c /etc/aide/aide.conf --check | \
  grep -E "(ld\.so|pam_|systemd|sshd|sudo)"
```

## Limites e trade-offs
Se o AIDE acusar modificação de hash (`SHA-256` / `SHA-512`) em um binário crítico como `/usr/sbin/sshd` ou `/lib/x86_64-linux-gnu/security/pam_unix.so` fora de uma janela de atualização de pacotes, **isole imediatamente o host na rede** e preserve uma cópia forense do arquivo adulterado antes de reinstalar o pacote ou reconstruir a máquina!

## Como verificar
Cruze o timestamp `ctime` (change time do inode, que não pode ser falsificado via `touch` sem alterar o relógio do kernel) reportado pelo AIDE com os logs de autenticação SSH e `auditd` para identificar a sessão exata do invasor.

## Conexões
- [[aide-otimizacao-performance-workers-multithread-limites-io-producao]] — Veja também: Otimização de Performance e Controle de Impacto de I/O do AIDE em Produção: **Multithreading (`num_workers`)**, `ionice` e `nice`.
- [[aide-arquitetura-monitoramento-integridade-arquivos-fim-linux]] — Referência cruzada direta com aide-arquitetura-monitoramento-integridade-arquivos-fim-linux.
- [[aide-protecao-banco-dados-assinatura-gpg-armazenamento-remoto-ssh]] — Referência cruzada direta com aide-protecao-banco-dados-assinatura-gpg-armazenamento-remoto-ssh.
- [[openssh-hardening-sshd-config-criptografia-autenticacao-restricoes]] — Referência cruzada direta com openssh-hardening-sshd-config-criptografia-autenticacao-restricoes.

## Fontes
- [AIDE Official Repository README — Advanced Intrusion Detection Environment (v0.19)](https://raw.githubusercontent.com/aide/aide/master/README) — documentação oficial do código-fonte do AIDE cobrindo arquitetura, verificação criptográfica GPG, PCRE2 e bibliotecas `libnettle`/`libgcrypt`; consultado em 2026-10-03.
- [The Official AIDE Manual (`aide.github.io/doc`)](https://aide.github.io/doc/) — manual técnico oficial do AIDE detalhando regras de atributos (`p`, `i`, `n`, `u`, `g`, `s`, `m`, `c`, `S`, `acl`, `selinux`, `xattrs`, `e2fsattrs`, `sha256`, `sha512`), seleções regex e assinatura de banco de dados; consultado em 2026-10-03.
