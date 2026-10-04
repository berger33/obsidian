---
id: software.seguranca.tranche12.001146
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

# Blindagem Anti-Tampering do Próprio AIDE: Verificação Remota via **SSH/SFTP**, Mídia Read-Only e Assinatura Criptográfica **GnuPG**

## Em uma frase
Existe uma limitação fundamental em qualquer ferramenta de File Integrity Monitoring (FIM) baseada em host que o próprio manual oficial do AIDE destaca em negrito: **se o binário `/usr/bin/aide`, o arquivo `/etc/aide/aide.conf` e o banco `/var/lib/aide/aide.db.gz` ficam gravados no disco local com permissão de escrita para `root`, um invasor que escale privilégio para `root` pode simplesmente rodar `aide --update` para regerar o banco incluindo seu rootkit ou substituir o binário do `/usr/bin/aide` por um script que sempre imprime `"All files match AIDE database"`!**

## Por que importa
Como eliminar esse ponto único de falha em servidores críticos? A arquitetura de alta segurança recomendada pelo manual do AIDE consiste em **desacoplar o verificador e o banco de dados do host monitorado**!

## Como funciona
Você pode: **(1)** Armazenar o `aide.db.gz`, o `aide.conf` e o binário compilado estaticamente (`./configure --enable-static`) em um **servidor central de segurança dedicado**, que monta o sistema de arquivos do host alvo em modo somente-leitura via SSHFS / snapshot LVM / snapshot EBS (ou copia o banco de referência para o host apenas no momento da checagem e valida o hash SHA-256 do binário `/usr/bin/aide` antes de invocá-lo); e **(2)** Assinar digitalmente o banco `aide.db.gz` e o `aide.conf` com **GnuPG (`gpg --detach-sign`)**, mantendo a chave privada GPG fora do servidor monitorado!

## Exemplo
```bash
# Assinar criptograficamente o banco de dados de referencia do AIDE com GnuPG e verificar a assinatura antes de executar o --check
gpg --armor --detach-sign /var/lib/aide/aide.db.gz
gpg --verify /var/lib/aide/aide.db.gz.asc /var/lib/aide/aide.db.gz && \
  sudo aide --config=/etc/aide/aide.conf --check
```

## Limites e trade-offs
Em ambientes AWS, GCP ou Azure, uma técnica moderna e extremamente eficaz é montar um snapshot diário do disco da instância de produção em uma instância isolada de auditoria de segurança e rodar o `aide --check --before="root_prefix=/mnt/snapshot_prod"` contra o disco montado em modo `ro` (*read-only*) — tornando impossível para qualquer rootkit de kernel no host de produção esconder seus arquivos!

## Como verificar
A diretiva **`root_prefix=/mnt/snapshot_prod`** no AIDE permite verificar uma árvore de arquivos inteira montada em um subdiretório usando exatamente o mesmo `aide.conf` e `aide.db.gz` da raiz original.

## Conexões
- [[aide-monitoramento-logs-crescentes-growing-size-rotacao-logrotate]] — Veja também: Monitoramento de Integridade de **Arquivos de Log (`S` / `ANF` / `ARF`)** no AIDE: Como Detectar Truncamento de Logs sem Falsos Positivos no `logrotate`.
- [[aide-configuracao-modular-debian-ubuntu-aide-conf-d-update-aide-conf]] — Veja também: Arquitetura Modular no Debian/Ubuntu (**`/etc/aide/aide.conf.d/`**): **`update-aide.conf`**, **`aideinit`** e Integração com Pacotes `.deb`.
- [[aide-arquitetura-monitoramento-integridade-arquivos-fim-linux]] — Referência cruzada direta com aide-arquitetura-monitoramento-integridade-arquivos-fim-linux.
- [[aide-ciclo-operacional-init-check-update-codigos-retorno]] — Referência cruzada direta com aide-ciclo-operacional-init-check-update-codigos-retorno.
- [[pacu-pos-exploracao-ec2-userdata-ssm-ebs-snapshots-exfiltracao]] — Referência cruzada direta com pacu-pos-exploracao-ec2-userdata-ssm-ebs-snapshots-exfiltracao.

## Fontes
- [AIDE Official Repository README — Advanced Intrusion Detection Environment (v0.19)](https://raw.githubusercontent.com/aide/aide/master/README) — documentação oficial do código-fonte do AIDE cobrindo arquitetura, verificação criptográfica GPG, PCRE2 e bibliotecas `libnettle`/`libgcrypt`; consultado em 2026-10-03.
- [The Official AIDE Manual (`aide.github.io/doc`)](https://aide.github.io/doc/) — manual técnico oficial do AIDE detalhando regras de atributos (`p`, `i`, `n`, `u`, `g`, `s`, `m`, `c`, `S`, `acl`, `selinux`, `xattrs`, `e2fsattrs`, `sha256`, `sha512`), seleções regex e assinatura de banco de dados; consultado em 2026-10-03.
