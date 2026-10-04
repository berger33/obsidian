---
id: software.seguranca.tranche12.001145
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

# Monitoramento de Integridade de **Arquivos de Log (`S` / `ANF` / `ARF`)** no AIDE: Como Detectar Truncamento de Logs sem Falsos Positivos no `logrotate`

## Em uma frase
Como monitorar `/var/log/auth.log`, `/var/log/syslog` ou `/var/log/audit/audit.log` com o AIDE para detectar se um invasor editou ou truncou linhas de log para esconder seu IP, **sem que o AIDE gere falso positivo a cada segundo porque o arquivo de log cresceu de tamanho ou porque o `logrotate` rotacionou o arquivo de madrugada**?

## Por que importa
O AIDE possui três atributos especializados exatamente para o ciclo de vida de arquivos de log: **(1) Atributo `S` (*Check for growing size*)** — verifica que o tamanho atual do arquivo é maior ou igual ao tamanho registrado no banco (alertando imediatamente se o arquivo encolheu/foi truncado!); **(2) Atributo `ANF` (*Allow New Files*)** — permite que um novo arquivo recém-rotacionado (ex.: `auth.log.1`) apareça sem disparar alerta de adição; e **(3) Atributo `ARF` (*Allow Removed Files*)** — permite que o arquivo mais antigo da rotação (ex.: `auth.log.4.gz`) seja removido pelo `logrotate` sem disparar alerta de exclusão!

## Como funciona
Combinando `>` (regra de log em crescimento `p+ftype+l+u+g+i+n+S`), `ANF` para o primeiro arquivo rotacionado e `ARF` para o último arquivo da fila do `logrotate`, você monitora a integridade da cadeia de logs com zero ruído operacional!

## Exemplo
```ini
# Regras no /etc/aide/aide.conf para monitorar logs ativos em crescimento e arquivos rotacionados pelo logrotate
ActLog   = p+ftype+l+u+g+i+n+S+acl+selinux+xattrs
RotLogNew = p+ftype+l+u+g+s+m+c+sha256+ANF+I
RotLogOld = p+ftype+l+u+g+s+m+c+sha256+ARF

/var/log/auth\.log$        ActLog
/var/log/auth\.log\.1$     RotLogNew
/var/log/auth\.log\.4\.gz$ RotLogOld
```

## Limites e trade-offs
Para proteger os logs locais do servidor contra truncamento mesmo por um atacante com `root` antes de o AIDE rodar, combine o monitoramento do AIDE com o atributo de sistema de arquivos **`append-only` (`chattr +a /var/log/auth.log`)** e encaminhe todos os eventos em tempo real via TLS para um servidor SIEM remoto!

## Como verificar
Como a regra `ActLog` inclui `e2fsattrs`, o AIDE também alertará caso alguém remova a flag `+a` do arquivo de log.

## Conexões
- [[aide-ciclo-operacional-init-check-update-codigos-retorno]] — Veja também: Ciclo Operacional do AIDE: **`--init`**, **`--check`**, **`--update`**, **`--compare`** e Interpretação dos **Códigos de Retorno (`1` a `7`)** em Scripts.
- [[aide-protecao-banco-dados-assinatura-gpg-armazenamento-remoto-ssh]] — Veja também: Blindagem Anti-Tampering do Próprio AIDE: Verificação Remota via **SSH/SFTP**, Mídia Read-Only e Assinatura Criptográfica **GnuPG**.
- [[aide-arquitetura-monitoramento-integridade-arquivos-fim-linux]] — Referência cruzada direta com aide-arquitetura-monitoramento-integridade-arquivos-fim-linux.
- [[aide-regras-atributos-hashes-acl-xattrs-selinux-e2fsattrs-aide-conf]] — Referência cruzada direta com aide-regras-atributos-hashes-acl-xattrs-selinux-e2fsattrs-aide-conf.
- [[aide-selecao-arquivos-regex-inclusao-negativa-restrita-macros]] — Referência cruzada direta com aide-selecao-arquivos-regex-inclusao-negativa-restrita-macros.

## Fontes
- [AIDE Official Repository README — Advanced Intrusion Detection Environment (v0.19)](https://raw.githubusercontent.com/aide/aide/master/README) — documentação oficial do código-fonte do AIDE cobrindo arquitetura, verificação criptográfica GPG, PCRE2 e bibliotecas `libnettle`/`libgcrypt`; consultado em 2026-10-03.
- [The Official AIDE Manual (`aide.github.io/doc`)](https://aide.github.io/doc/) — manual técnico oficial do AIDE detalhando regras de atributos (`p`, `i`, `n`, `u`, `g`, `s`, `m`, `c`, `S`, `acl`, `selinux`, `xattrs`, `e2fsattrs`, `sha256`, `sha512`), seleções regex e assinatura de banco de dados; consultado em 2026-10-03.
