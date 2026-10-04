---
id: software.seguranca.tranche04.000319
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md", "https://docs.clamav.net/manual/Usage.html", "https://docs.clamav.net/manual/Signatures.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ClamAV: Monitoramento Operacional com `clamdtop`, Pool de Memória e Dimensionamento em Containers

## Em uma frase
O utilitário `clamdtop` e os comandos de controle `STATS`/`VERSION` do socket do `clamd` expõem em tempo real o uso das filas de varredura, a ocupação das threads (`MaxThreads`), a latência das requisições e o consumo de memória dos bancos.

## Por que importa
O banco de assinaturas do ClamAV consome mais de `1,2 GiB` de RAM base e, durante recargas concorrentes de banco (`ConcurrentDatabaseReload yes`), o pico de memória dobra temporariamente (`~2,4 GiB`), causando mortes por `OOMKilled` em pods Kubernetes subdimensionados.

## Como funciona
O comando `clamdtop` conecta-se ao socket Unix ou TCP do `clamd` e exibe quais arquivos estão sendo processados por cada thread ativa e o estado dos *mempools* internos. Em containers com menos de `2,5 GiB` de limite de memória, desabilitar `ConcurrentDatabaseReload no` evita que duas cópias completas do banco coexistam na RAM durante atualizações do `freshclam`, ao custo de pausar novas varreduras por alguns segundos durante o reload.

## Exemplo
```bash
# Consultar estatísticas de threads, filas e memória diretamente no socket do clamd
printf "nSTATS\n" | socat - UNIX-CONNECT:/run/clamav/clamd.ctl

# Monitorar interativamente o daemon clamd no terminal
clamdtop /run/clamav/clamd.ctl
```

## Limites e trade-offs
Definir `limits.memory` abaixo de `2Gi` em um Deployment Kubernetes do ClamAV com `ConcurrentDatabaseReload yes` padrão derrubará o pod toda vez que o `freshclam` atualizar o banco `daily.cld`.

## Como verificar
Verifique a saída de `printf "nSTATS\n" | socat - UNIX-CONNECT:/run/clamav/clamd.ctl` e confirme `QUEUE: 0 items` e a ausência de eventos `OOMKilled` após um comando `RELOAD`.

## Conexões
- [[clamav-integracao-pipelines-upload-api-milter-icap-s3]] — Veja também: ClamAV: Integração em Gateways de E-mail (`clamav-milter`), Servidores ICAP e Eventos S3/API.
- [[clamav-gerenciamento-falsos-positivos-ign2-fp-clamsubmit]] — Veja também: ClamAV: Supressão Auditável de Falsos Positivos (`.ign2` e `.fp`) e Submissão com `clamsubmit`.
- [[clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites]] — Referência cruzada direta com clamav-daemon-clamd-conf-unix-socket-tcp-instream-limites.
- [[clamav-atualizacao-freshclam-cvd-cld-private-local-mirrors]] — Referência cruzada direta com clamav-atualizacao-freshclam-cvd-cld-private-local-mirrors.
- [[clamav-arquitetura-libclamav-clamd-clamscan-freshclam]] — Referência cruzada direta com clamav-arquitetura-libclamav-clamd-clamscan-freshclam.

## Fontes
- [Cisco ClamAV Official Documentation — Usage Manual (libclamav Architecture, clamd, clamdscan, clamonacc, freshclam, sigtool & clambc)](https://raw.githubusercontent.com/Cisco-Talos/clamav/main/README.md) — Manual oficial de uso do ClamAV detalhando o fluxo de varredura cliente/servidor do clamd, utilitários de banco e configuração; consultado em 2026-10-03.
- [Cisco ClamAV GitHub — README.md (Open-Source Antivirus Engine Overview, Signatures, Packaging & Licensing)](https://docs.clamav.net/manual/Usage.html) — README oficial do Cisco-Talos/clamav descrevendo a arquitetura da engine, suporte multiplataforma e documentação de assinaturas; consultado em 2026-10-03.
- [Cisco ClamAV Official Documentation — Signature Writing Manual](https://docs.clamav.net/manual/Signatures.html) — Manual oficial de criação de assinaturas customizadas, lógicas, bytecode e YARA no ClamAV; consultado em 2026-10-03.
