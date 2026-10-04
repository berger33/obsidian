---
id: software.seguranca.tranche12.001149
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

# Otimização de Performance e Controle de Impacto de I/O do AIDE em Produção: **Multithreading (`num_workers`)**, `ionice` e `nice`

## Em uma frase
Em servidores de banco de dados ou storage com milhões de arquivos e dezenas de gigabytes em `/usr` e `/opt`, rodar um cálculo criptográfico `SHA-256 + SHA-512` em thread única ou sem controle de prioridade de disco pode demorar longo tempo ou competir por IOPS com a aplicação de produção.

## Por que importa
A partir do **AIDE v0.18+**, o motor de cálculo de hashes e verificação foi reescrito com suporte a **processamento paralelo multithread** controlado pela diretiva **`num_workers`** no `aide.conf` (ou flag `--workers`), que aceita um número inteiro de threads ou uma porcentagem dos núcleos de CPU disponíveis (por exemplo, **`num_workers=50%`** ou **`num_workers=4`**)!

## Como funciona
Para garantir que a varredura periódica do AIDE nunca degrade a latência de I/O ou CPU dos serviços de produção, combine `num_workers` moderado no `aide.conf` com o escalonador de I/O *Idle/Best-Effort* do kernel Linux (**`ionice -c 3`**) e prioridade de CPU reduzida (**`nice -n 19`**) na unidade `systemd` (`dailyaidecheck.service`)!

## Exemplo
```bash
# Executar o aide --check com baixa prioridade de CPU (nice 19) e I/O de disco em classe Idle (ionice -c 3) para zero impacto em producao
sudo ionice -c 3 nice -n 19 aide --config=/etc/aide/aide.conf --check
```

## Limites e trade-offs
Na configuração de uma unidade `systemd` customizada para o AIDE, você pode declarar nativamente `Nice=19`, `IOSchedulingClass=idle` e `CPUQuota=50%` na seção `[Service]` — garantindo por cgroups v2 do kernel que o AIDE nunca consuma mais da metade de um core nem dispute leitura de disco com o PostgreSQL ou Nginx!

## Como verificar
Evite incluir diretórios de dados de bancos de dados (`/var/lib/postgresql`, `/var/lib/mysql`) ou diretórios de cache nas regras de hash do AIDE.

## Conexões
- [[aide-integracao-siem-syslog-json-auditoria-pci-dss-cis-benchmark]] — Veja também: Integração do AIDE com **SIEM e Conformidade (`PCI-DSS 11.5` / `CIS Benchmarks`)**: Parseando Relatórios de Alteração e Alertando sobre Drift.
- [[aide-resposta-incidentes-forense-linux-rootkits-ld-so-preload-pam]] — Veja também: Caça a Backdoors e Persistência Linux com o AIDE: Detectando Adulteração em **`/etc/ld.so.preload`**, Módulos **PAM (`/lib/security/`)**, `sshd` e `systemd`.
- [[aide-arquitetura-monitoramento-integridade-arquivos-fim-linux]] — Referência cruzada direta com aide-arquitetura-monitoramento-integridade-arquivos-fim-linux.
- [[aide-selecao-arquivos-regex-inclusao-negativa-restrita-macros]] — Referência cruzada direta com aide-selecao-arquivos-regex-inclusao-negativa-restrita-macros.
- [[aide-configuracao-modular-debian-ubuntu-aide-conf-d-update-aide-conf]] — Referência cruzada direta com aide-configuracao-modular-debian-ubuntu-aide-conf-d-update-aide-conf.

## Fontes
- [AIDE Official Repository README — Advanced Intrusion Detection Environment (v0.19)](https://raw.githubusercontent.com/aide/aide/master/README) — documentação oficial do código-fonte do AIDE cobrindo arquitetura, verificação criptográfica GPG, PCRE2 e bibliotecas `libnettle`/`libgcrypt`; consultado em 2026-10-03.
- [The Official AIDE Manual (`aide.github.io/doc`)](https://aide.github.io/doc/) — manual técnico oficial do AIDE detalhando regras de atributos (`p`, `i`, `n`, `u`, `g`, `s`, `m`, `c`, `S`, `acl`, `selinux`, `xattrs`, `e2fsattrs`, `sha256`, `sha512`), seleções regex e assinatura de banco de dados; consultado em 2026-10-03.
